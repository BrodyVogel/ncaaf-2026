#!/usr/bin/env python3
"""Compute phase (build step 5): grades + anchor run -> final ratings + build sheets.

Per PARAMETERS.json (all ratified): fit anchor O/D on unit grades league-wide;
resid = grade-implied minus anchor; final = blend + class + clip(k*resid, cap) + st;
band = 6.0 x multipliers. AUDIT QA built in: shadow proxy column on every build sheet,
anchoring tripwire (fit R2 > 0.75 -> warning; proxy baseline 0.46-0.68), overrides
applied last + logged.

Usage: python3 compute_ratings.py <anchor_run.json> <grades_source> <outdir> [--proxy-as-grades]
  grades_source: dir of snapshots/*/grades.json, or the shadow JSON with --proxy-as-grades
    (dress-rehearsal mode: mechanical grades stand in; outputs labeled PROXY-PROVISIONAL)
"""
import csv, json, os, subprocess, sys, datetime
import numpy as np

OFF_UNITS, DEF_UNITS = ["QB", "RB", "WRTE", "OL"], ["DL", "LB", "DB"]
K, CAP, SIGMA = 0.35, 6.0, 6.0
R2_BASELINE = (0.46, 0.68)

def ols(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    return b, y - X @ b

def main(anchor_path, grades_src, outdir, proxy_mode=False):
    run = json.load(open(anchor_path))
    A = run["teams"]
    proxy = json.load(open("data/backtest/shadow_proxy_2026.json"))["grades"]

    grades, conf_flags, coach_flags = {}, {}, {}
    if proxy_mode:
        for t, g in json.load(open(grades_src))["grades"].items():
            grades[t] = {u: (g[u] if g[u] is not None else 50) for u in g}
            conf_flags[t] = sum(1 for u in g if g[u] is None)  # null units ~ low confidence
    else:
        for d in sorted(os.listdir(grades_src)):
            p = os.path.join(grades_src, d, "grades.json")
            if os.path.exists(p):
                gj = json.load(open(p))
                t = gj["team"]
                grades[t] = {u: gj["units"][u]["grade"] for u in gj["units"]}
                conf_flags[t] = sum(1 for u in gj["units"] if gj["units"][u]["confidence"] == "L")
                mp = os.path.join(grades_src, d, "META.json")
                if os.path.exists(mp):
                    coach_flags[t] = bool(json.load(open(mp)).get("coach_change"))

    teams = [t for t in grades if t in A]
    partial = len(teams) < len(A)
    ones = np.ones(len(teams))
    Xo = np.column_stack([ones] + [[grades[t][u] for t in teams] for u in OFF_UNITS])
    Xd = np.column_stack([ones] + [[grades[t][u] for t in teams] for u in DEF_UNITS])
    yo = np.array([A[t]["off"] for t in teams]); yd = np.array([A[t]["dfn"] for t in teams])
    bo, ro = ols(Xo, yo); bd, rd = ols(Xd, yd)
    r2o, r2d = 1 - ro.var() / yo.var(), 1 - rd.var() / yd.var()
    tripwire = r2o > 0.75 or r2d > 0.75

    rows = []
    for i, t in enumerate(teams):
        resid = float((-ro[i]) - (-rd[i]))
        adj = float(np.clip(K * resid, -CAP, CAP))
        cls = -run["_meta"]["class_per_side"] if A[t]["p4"] else run["_meta"]["class_per_side"]
        st = ((grades[t].get("ST") or 50) - 50) / 50 * 1.0
        final = A[t]["blend"] + cls + adj + st
        band = SIGMA * (1.13 if coach_flags.get(t) else 1.0) * (1.10 if A[t]["dispersion_flag"] else 1.0) \
               * (1 + 0.03 * min(conf_flags.get(t, 0), 5))  # coach_change x1.13 per PARAMETERS (wired 2026-07-14)
        rows.append(dict(team=t, final=final, anchor=A[t]["blend"], class_term=round(cls, 2),
                         resid=round(resid, 2), adj=round(adj, 2), st=round(st, 2),
                         band=round(band, 2), dispersion_flag=A[t]["dispersion_flag"],
                         low_conf_units=conf_flags.get(t, 0)))
    mean_shift = np.mean([r["final"] for r in rows])
    for r in rows:
        r["final"] = round(r["final"] - mean_shift, 2)
    rows.sort(key=lambda r: -r["final"])
    for i, r in enumerate(rows):
        r["rank"] = i + 1

    # flags: top-decile |resid| + dispersion flags
    resid_thresh = float(np.quantile([abs(r["resid"]) for r in rows], 0.9))
    for r in rows:
        r["resid_flag"] = bool(abs(r["resid"]) >= resid_thresh)

    # overrides (user-directed, applied LAST, logged)
    overrides = []
    if os.path.exists("outputs/overrides.csv"):
        for o in csv.DictReader(open("outputs/overrides.csv")):
            for r in rows:
                if r["team"] == o["team"] and o["field"] == "final":
                    overrides.append(dict(o, previous=r["final"]))
                    r["final"] = float(o["value"])

    os.makedirs(f"{outdir}/build_sheets", exist_ok=True)
    label = "PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)" if proxy_mode else \
            ("PROVISIONAL (partial league)" if partial else "FULL")
    with open(f"{outdir}/ratings.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    for r in rows:
        t = r["team"]
        src = A[t]["sources"]
        lines = [f"# {t} — build sheet [{label}]", "",
                 f"FINAL: **{r['final']:+.2f}** (rank {r['rank']}/{len(rows)})  band ±{r['band']}",
                 "",
                 "## 1. Unit grades (LLM | shadow proxy)"]
        for u in OFF_UNITS + DEF_UNITS + ["ST"]:
            g = grades[t].get(u); s = (proxy.get(t) or {}).get(u)
            lines.append(f"- {u:4s} {g if g is not None else '—':>3} | proxy {s if s is not None else '—'}")
        lines += ["", "## 2. Conversion (league-learned weights this run)",
                  f"- off: " + " ".join(f"{u}:{bo[1+i]:+.3f}" for i, u in enumerate(OFF_UNITS)) + f"  (R²={r2o:.2f})",
                  f"- def: " + " ".join(f"{u}:{bd[1+i]:+.3f}" for i, u in enumerate(DEF_UNITS)) + f"  (R²={r2d:.2f})",
                  f"- grade-implied vs anchor residual: **{r['resid']:+.2f}**",
                  "", "## 3. Anchor (per source: raw → normalized → used)"]
        for s, v in src.items():
            lines.append(f"- {s:8s} {v['raw']} → {v['normalized']} → {v['used']}"
                         + ("  [WINSORIZED]" if v["winsorized"] else ""))
        lines += [f"- blend {A[t]['blend']}  (dispersion {A[t]['dispersion']}"
                  + (", FLAGGED" if A[t]["dispersion_flag"] else "") + ")",
                  "", "## 4. Assembly",
                  f"- anchor {A[t]['blend']:+.2f}  class {r['class_term']:+.2f}  "
                  f"k×resid {r['adj']:+.2f} (k={K}, cap ±{CAP})  ST {r['st']:+.2f}  "
                  f"→ recentered → **{r['final']:+.2f}**",
                  f"- band: 6.0 × dispersion({'1.10' if r['dispersion_flag'] else '1.00'}) × "
                  f"conf(1+0.03×{min(r['low_conf_units'], 5)}) = ±{r['band']}",
                  f"- flags: resid_flag={r['resid_flag']}, dispersion_flag={r['dispersion_flag']}"]
        open(f"{outdir}/build_sheets/{t.replace(' ', '_')}.md", "w").write("\n".join(lines))

    git_rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    json.dump(dict(run_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   label=label, code_rev=git_rev, anchor_run=anchor_path, grades_source=grades_src,
                   k=K, cap=CAP, sigma=SIGMA, class_per_side=run["_meta"]["class_per_side"],
                   n_teams=len(rows), fit_r2=dict(off=round(r2o, 3), dfn=round(r2d, 3)),
                   tripwire_fired=bool(tripwire), tripwire_note=f"baseline {R2_BASELINE}; >0.75 = anchoring warning",
                   resid_flag_threshold=round(resid_thresh, 2),
                   n_overrides=len(overrides), overrides=overrides),
              open(f"{outdir}/run_log.json", "w"), indent=1)
    print(f"[{label}] {len(rows)} teams -> {outdir}")
    print(f"fit R²: off {r2o:.2f}, def {r2d:.2f} | tripwire {'FIRED' if tripwire else 'ok'} "
          f"(baseline {R2_BASELINE[0]}-{R2_BASELINE[1]})")
    print("top 10:", ", ".join(f"{r['team']} {r['final']:+.1f}" for r in rows[:10]))
    print("resid flags (top-decile |resid|):",
          ", ".join(f"{r['team']} {r['resid']:+.1f}" for r in rows if r["resid_flag"])[:400])

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main(args[0], args[1], args[2], proxy_mode="--proxy-as-grades" in sys.argv)
