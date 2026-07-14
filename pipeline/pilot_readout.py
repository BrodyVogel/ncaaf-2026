#!/usr/bin/env python3
"""Pilot readout (two-team pilot, brief §9): one team's REAL grades against a
proxy-fitted conversion, out-of-sample.

Why this shape: conversion weights need league-wide grades; during the pilot only
N=1-2 teams have real grades. So weights are fitted on the OTHER 137 teams' shadow
proxy grades (dress-rehearsal fit) and the pilot team's grade-implied O/D is computed
OUT-OF-SAMPLE with its real grades. Weights get refitted on real grades once all 138
exist — labeled accordingly. Recentering uses the hybrid field (137 proxy + pilot real).

Usage: python3 pilot_readout.py <anchor_run.json> <Team> <snapshots_dir> <outdir>
"""
import json, os, subprocess, sys, datetime
import numpy as np

OFF_UNITS, DEF_UNITS = ["QB", "RB", "WRTE", "OL"], ["DL", "LB", "DB"]
K, CAP, SIGMA = 0.35, 6.0, 6.0

def ols(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    return b, y - X @ b

def main(anchor_path, team, snapdir, outdir):
    run = json.load(open(anchor_path)); A = run["teams"]
    proxy = json.load(open("data/backtest/shadow_proxy_2026.json"))["grades"]
    gj = json.load(open(os.path.join(snapdir, team.replace(" ", "_"), "grades.json")))
    real = {u: gj["units"][u]["grade"] for u in gj["units"]}
    low_conf = sum(1 for u in gj["units"] if gj["units"][u]["confidence"] == "L")

    # fit conversion on the proxy field EXCLUDING the pilot team (out-of-sample)
    others = [t for t in proxy if t in A and t != team]
    pg = {t: {u: (proxy[t][u] if proxy[t][u] is not None else 50) for u in proxy[t]} for t in others}
    ones = np.ones(len(others))
    Xo = np.column_stack([ones] + [[pg[t][u] for t in others] for u in OFF_UNITS])
    Xd = np.column_stack([ones] + [[pg[t][u] for t in others] for u in DEF_UNITS])
    yo = np.array([A[t]["off"] for t in others]); yd = np.array([A[t]["dfn"] for t in others])
    bo, ro = ols(Xo, yo); bd, rd = ols(Xd, yd)
    r2o, r2d = 1 - ro.var() / yo.var(), 1 - rd.var() / yd.var()

    # pilot team, out-of-sample
    xo = np.array([1.0] + [real[u] for u in OFF_UNITS])
    xd = np.array([1.0] + [real[u] for u in DEF_UNITS])
    implied_off, implied_def = float(xo @ bo), float(xd @ bd)
    resid = (implied_off - A[team]["off"]) - (implied_def - A[team]["dfn"])
    adj = float(np.clip(K * resid, -CAP, CAP))
    cls = -run["_meta"]["class_per_side"] if A[team]["p4"] else run["_meta"]["class_per_side"]
    st = (real["ST"] - 50) / 50 * 1.0
    final_raw = A[team]["blend"] + cls + adj + st

    # hybrid field for recentering + rank: others with proxy math, pilot with real
    finals = {}
    for t in others:
        r_t = float((-ro[others.index(t)]))  # off resid sign: y - Xb -> anchor - implied
        # replicate engine: resid = (implied-anchor)_off - (implied-anchor)_def = -ro - (-rd)
        resid_t = float((-ro[others.index(t)]) - (-rd[others.index(t)]))
        adj_t = float(np.clip(K * resid_t, -CAP, CAP))
        cls_t = -run["_meta"]["class_per_side"] if A[t]["p4"] else run["_meta"]["class_per_side"]
        st_t = ((pg[t].get("ST") or 50) - 50) / 50 * 1.0
        finals[t] = A[t]["blend"] + cls_t + adj_t + st_t
    finals[team] = final_raw
    mean_shift = float(np.mean(list(finals.values())))
    final = final_raw - mean_shift
    rank = 1 + sum(1 for t, v in finals.items() if v - mean_shift > final)

    band = SIGMA * (1.10 if A[team]["dispersion_flag"] else 1.0) * (1 + 0.03 * min(low_conf, 5))

    os.makedirs(outdir, exist_ok=True)
    src = A[team]["sources"]
    lines = [f"# {team} — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]", "",
             f"FINAL: **{final:+.2f}** (rank {rank}/138 in hybrid field)  band ±{band:.2f}", "",
             "## 1. Unit grades (LLM real | shadow proxy)"]
    for u in OFF_UNITS + DEF_UNITS + ["ST"]:
        s = (proxy.get(team) or {}).get(u)
        lines.append(f"- {u:4s} {real[u]:>3} | proxy {s if s is not None else '—'}")
    lines += ["", "## 2. Conversion (fitted on 137 proxy teams, applied OOS)",
              "- off: " + " ".join(f"{u}:{bo[1+i]:+.3f}" for i, u in enumerate(OFF_UNITS)) + f"  (R²={r2o:.2f})",
              "- def: " + " ".join(f"{u}:{bd[1+i]:+.3f}" for i, u in enumerate(DEF_UNITS)) + f"  (R²={r2d:.2f})",
              f"- grade-implied off {implied_off:+.2f} vs anchor off {A[team]['off']:+.2f}",
              f"- grade-implied def {implied_def:+.2f} vs anchor def {A[team]['dfn']:+.2f} (def: lower=better in SP+ space)"
              if False else
              f"- grade-implied def {implied_def:+.2f} vs anchor def {A[team]['dfn']:+.2f}",
              f"- residual (off-minus-def, grades-vs-anchor): **{resid:+.2f}**",
              "", "## 3. Anchor (per source: raw → normalized → used)"]
    for s, v in src.items():
        lines.append(f"- {s:8s} {v['raw']} → {v['normalized']} → {v['used']}"
                     + ("  [WINSORIZED]" if v["winsorized"] else ""))
    lines += [f"- blend {A[team]['blend']}  (dispersion {A[team]['dispersion']}"
              + (", FLAGGED" if A[team]["dispersion_flag"] else ")"),
              "", "## 4. Assembly",
              f"- anchor {A[team]['blend']:+.2f}  class {cls:+.2f}  k×resid {adj:+.2f} (k={K}, cap ±{CAP})  "
              f"ST {st:+.2f}  → recentered ({mean_shift:+.2f}) → **{final:+.2f}**",
              f"- band: {SIGMA} × dispersion({'1.10' if A[team]['dispersion_flag'] else '1.00'}) × "
              f"conf(1+0.03×{low_conf}) = ±{band:.2f}",
              "", "## 5. Pilot caveats",
              "- Conversion weights are proxy-fitted (real-grade refit happens at full 138).",
              "- Rank is vs a 137-proxy field — indicative only.",
              f"- grades snapshot rev: {gj['_meta']['snapshot_rev']}"]
    open(f"{outdir}/{team.replace(' ', '_')}_pilot.md", "w").write("\n".join(lines))

    git_rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True).stdout.strip()
    json.dump(dict(run_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   team=team, final=round(final, 2), rank=rank, band=round(band, 2),
                   resid=round(resid, 2), adj=round(adj, 2), class_term=round(cls, 2),
                   st=round(st, 2), anchor_blend=A[team]["blend"], implied_off=round(implied_off, 2),
                   implied_def=round(implied_def, 2), anchor_off=A[team]["off"], anchor_def=A[team]["dfn"],
                   fit_r2=dict(off=round(r2o, 3), dfn=round(r2d, 3)), low_conf_units=low_conf,
                   code_rev=git_rev, mode="PILOT-OOS"),
              open(f"{outdir}/{team.replace(' ', '_')}_pilot.json", "w"), indent=1)
    print(open(f"{outdir}/{team.replace(' ', '_')}_pilot.md").read())

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
