#!/usr/bin/env python3
"""FINAL PASS — the full-138 real-grade conversion refit + consistent board rebuild.

This is the production step every pilot readout promised ("Conversion weights are
proxy-fitted; real-grade refit happens at full 138") and the GRADING_BIAS_DIAG
(2026-07-16) deferred to this checkpoint. Owner approval: 2026-07-18 session.

WHAT IT REPLACES (and why the pilot-era finals were provisional):
  1. Each team's at-grading-time final used conversion weights fitted on the 137-team
     SHADOW-PROXY field (documented inflated at the bottom, diag Finding 2) and was
     applied out-of-sample. Here the grade->points conversion is refitted by OLS on
     ALL 138 teams' REAL grades against the anchor off/def splits.
  2. Each pilot final was recentered against a DIFFERENT hybrid (proxy+real) field
     as the season's grading progressed, so the recenter shift drifted team to team.
     Here every team is recentered once, against the same full real field.
  Nothing else changes: K, CAP, band formula, class term, the grades themselves and
  the anchor blends are all frozen inputs.

FROZEN CONSTANTS (do not change without owner approval):
  K=0.35 (residual weight), CAP=6.0 (residual clip), SIGMA=6.0 (base band),
  coach band x1.13, dispersion band x1.10, conf band 1+0.03*min(L,5),
  ST term = (ST-50)/50 (max +/-1 pt), class_per_side from the anchor run (0.0).

REPEAT LOOP (after any grade edit):
  1. edit snapshots/<Team>/grades.json  (and keep the dossier PLANNED line or
     _meta.planned_vs_final_deviations consistent, else grades_check fails)
  2. python3 pipeline/grades_check.py <Team_Dir>     # per-team gate
  3. python3 pipeline/final_pass.py                  # refit + rebuild everything
  Outputs regenerate deterministically; the refit re-estimates on the edited grades.

RESIDUAL MODE — DECISION RECORD (owner: Brody, 2026-07-19):
  DEFAULT (OFFICIAL) = CONFERENCE-DEMEANED residual. Each conference's mean residual
  is subtracted before the k*clip step, so ONLY within-conference roster shape (the
  validated signal, diag Finding 3, Spearman 0.94) enters the final. The cross-
  conference level component is removed per owner policy: "no conference biases
  unless quantitatively verified" — it is unverifiable directly (no historical
  grades), the churn rationale was backtest-refuted (Finding 5), it is unstable
  across fit regimes (Finding 2), and the P4/G5 class effect measured nil
  (+0.15 pts, t=0.3, anchor-run class test 2026-07-15).
  PSEUDO-POOLS for the 2 Independents (no real conference): Notre Dame demeans
  against the ALL-P4 pool mean, UConn against the ALL-G5 pool mean (anchor p4 flag).
  --frozen-resid runs the pre-decision formula (full residual, no demeaning) for
  comparison; it writes ONLY to outputs/final_pass/*_frozen.* — never the official
  boards. (--demean-conf-resid is accepted as a no-op for back-compatibility.)

OUTPUTS:
  outputs/final_pass/ASSEMBLY.csv        per-team: anchor, implied O/D, resid, adj,
                                         st, recentered final, band (full audit)
  outputs/final_pass/REFIT_DIAG.md       weights before/after, R2, level-slope,
                                         conference resid table, movers, cap census
  outputs/FINAL_BOARD_2026.csv / .md     the official deliverable boards (refit)
"""
import csv, glob, json, os, subprocess, datetime, sys
import numpy as np

OFF, DEF = ["QB", "RB", "WRTE", "OL"], ["DL", "LB", "DB"]
K, CAP, SIGMA = 0.35, 6.0, 6.0
ANCHOR = "outputs/anchor_runs/anchor_run_2026-07-14_class0.json"
# Proxy-fit reference weights (from the pilot regime) for the before/after table only.
PROXY_REF = {"off": {"QB": 0.072, "RB": 0.092, "WRTE": 0.037, "OL": 0.082, "R2": 0.54},
             "def": {"DL": -0.083, "LB": -0.059, "DB": -0.096, "R2": 0.61}}


def ols(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    return b, y - X @ b


def match_spread(x, target, mask=None):
    """Rescale x to the standard deviation of `target`, preserving x's mean. OLS fitted values
    are shrunk toward the mean by ~sqrt(R^2); this un-shrinks the grade signal onto the anchor's
    scale before it is blended. Mean-preserving — changes spread, never the field's center.
    AUDIT D2 (2026-08-02): scale statistics computed on `mask` rows (reliable teams) only."""
    xm = x if mask is None else x[mask]
    tm = target if mask is None else target[mask]
    mx = float(xm.mean()); sx = float(xm.std())
    return x.copy() if sx < 1e-9 else mx + (x - mx) * (float(tm.std()) / sx)


def load_field():
    run = json.load(open(ANCHOR))
    A, cps = run["teams"], run["_meta"]["class_per_side"]
    rows, misses = [], []
    for p in sorted(glob.glob("snapshots/*/grades.json")):
        tdir = p.split("/")[1]
        g = json.load(open(p))
        meta = json.load(open(f"snapshots/{tdir}/META.json"))
        name = meta["team"]
        if name not in A:
            misses.append(name); continue
        units = g["units"]
        rows.append(dict(
            dir=tdir, name=name, conf=meta.get("conference", "?"),
            g={u: units[u]["grade"] for u in units},
            L=sum(1 for u in units if units[u]["confidence"] == "L"),
            coach=bool(meta.get("coach_change")),
            off=A[name]["off"], dfn=A[name]["dfn"], blend=A[name]["blend"],
            p4=A[name]["p4"], disp=A[name]["dispersion_flag"]))
    # Hard validation: this script must never run on a partial or mis-joined field.
    assert not misses, f"snapshot teams missing from anchor run: {misses}"
    assert len(rows) == len(A) == 138, f"expected 138 teams, joined {len(rows)} of {len(A)}"
    for r in rows:
        missing = [u for u in OFF + DEF + ["ST"] if u not in r["g"]]
        assert not missing, f"{r['name']} missing units {missing}"
    return rows, cps


def main():
    demean = "--frozen-resid" not in sys.argv   # DEFAULT = demeaned (owner decision 2026-07-19)
    rows, cps = load_field()
    n = len(rows); ones = np.ones(n)

    # AUDIT D2 (2026-08-02, owner-approved): teams on the manual-override list carry
    # grades we declared unreliable; they are excluded from EVERY fit (conversion OLS,
    # un-shrink scale, strip regression, recenter mean) — they still receive predictions
    # and their finals are overridden downstream. Mirrors the 07-23 demeaning-pool fix.
    _ovr_fit = set()
    if "--no-overrides" not in sys.argv and os.path.exists("data/manual_overrides_2026.csv"):
        _ovr_fit = {orow["team"] for orow in csv.DictReader(open("data/manual_overrides_2026.csv"))}
    vote = np.array([r["name"] not in _ovr_fit for r in rows])

    # ---- 1. REFIT the conversion on the 133 reliable real grades (OLS with intercept) ----
    Xo = np.column_stack([ones] + [np.array([r["g"][u] for r in rows]) for u in OFF])
    Xd = np.column_stack([ones] + [np.array([r["g"][u] for r in rows]) for u in DEF])
    yo = np.array([r["off"] for r in rows]); yd = np.array([r["dfn"] for r in rows])
    bo, ro = ols(Xo[vote], yo[vote]); bd, rd = ols(Xd[vote], yd[vote])
    r2o = 1 - ro.var() / yo[vote].var(); r2d = 1 - rd.var() / yd[vote].var()
    implied_off = Xo @ bo; implied_def = Xd @ bd

    # ---- 1b. De-compress the grade signal, step 1: un-shrink the OLS fit ----
    # OLS fitted values are shrunk toward the mean by ~sqrt(R^2) (off R2~0.67 -> ~82% of anchor
    # spread, def R2~0.49 -> ~70%). Inflate each fitted side back onto the anchor's (fair) scale.
    decompress = "--no-decompress" not in sys.argv   # de-compress the grade signal (2026-07-19)
    if decompress:
        implied_off = match_spread(implied_off, yo, mask=vote)   # AUDIT D2: scale fit on reliable rows
        implied_def = match_spread(implied_def, yd, mask=vote)

    # ---- 2. Residual, adjustment, assembly (frozen formula) ----
    resid = (implied_off - yo) - (implied_def - yd)          # + = grades warmer than anchor
    # Demeaning-pool fix (2026-07-23, owner-approved): teams on the manual-override list have
    # grades we explicitly declared unreliable (e.g. NDSU's -27 no-data artifact, raw resid -23).
    # Before this fix their junk residuals still voted in the conference means, spuriously
    # boosting innocent pool-mates (+0.33 MW, +0.54 Pac-12, +0.25 CUSA). Exclude them from every
    # demeaning pool; their own finals are overridden downstream anyway.
    _ovr_names = _ovr_fit

    def pool_refs(vec):
        """Within-pool means (override teams excluded from pools; Independents pseudo-pooled)."""
        cm = {}
        for r, rs in zip(rows, vec):
            if r["name"] in _ovr_names:
                continue
            cm.setdefault(r["conf"], []).append(float(rs))
        cm = {c: float(np.mean(v)) for c, v in cm.items()}
        p4m = float(np.mean([rs for r, rs in zip(rows, vec) if r["p4"] and r["name"] not in _ovr_names]))
        g5m = float(np.mean([rs for r, rs in zip(rows, vec) if not r["p4"] and r["name"] not in _ovr_names]))
        out = []
        for r in rows:
            if r["conf"] == "FBS Independents":
                out.append(p4m if r["p4"] else g5m)
            else:
                out.append(cm[r["conf"]])
        return np.array(out), cm, p4m, g5m
    refs, conf_mean, p4_mean, g5_mean = pool_refs(resid)
    if demean and not decompress:  # single demean (comparison modes)
        resid = resid - refs
    if decompress:
        # De-compress step 2: remove the part of the grade residual that is linear in team
        # strength. Even after un-shrinking (1b), the residual comes out negatively correlated
        # with the anchor level (grades disagree more negatively for stronger teams) — that
        # correlation IS the compression, and blending it at K=0.35 dragged every extreme toward
        # the middle (top teams under, bottom over, even for top teams that never play a bottom-
        # feeder). Strip the level-linear component; what remains is level-orthogonal, team-
        # specific signal that never pulls extremes inward. 1b+2 together cut edge~line R^2
        # 0.32->0.14 and restore the fair spread (SD ~13, matching KFord + market), Spearman 1.00
        # vs the pre-fix ordering. --no-decompress reproduces the pre-fix (compressed) formula.
        ancv = np.array([r["blend"] for r in rows])
        Aq = np.column_stack([np.ones(n), ancv])
        if demean:
            # AUDIT D1 (2026-08-02, owner-approved): sequential demean-then-strip re-inserted
            # conference means through the level fit (verified +0.56 SEC / -0.50 CUSA tilt xK).
            # Alternate the two projections to their JOINT fixed point: the shipped residual is
            # orthogonal to the demeaning pools AND the anchor level simultaneously.
            for _ in range(20):
                prev = resid.copy()
                rf, conf_mean, p4_mean, g5_mean = pool_refs(resid)
                resid = resid - rf
                cq, _ = ols(Aq[vote], resid[vote])      # AUDIT D2: strip fit on reliable rows
                resid = resid - Aq @ cq
                if float(np.abs(resid - prev).max()) < 1e-9:
                    break
        else:
            cq, _ = ols(Aq[vote], resid[vote])
            resid = resid - Aq @ cq
    adj = np.clip(K * resid, -CAP, CAP)
    cls = np.array([-cps if r["p4"] else cps for r in rows])  # 0.0 in this run
    stv = np.array([(r["g"]["ST"] - 50) / 50 * 1.0 for r in rows])
    if demean:
        # AUDIT D3 (2026-08-02, owner-approved): ST was the one channel bypassing demeaning
        # (conference ST-grade means span ~16..54 => a hidden +0.29 P4-G5 level term).
        st_refs, _, _, _ = pool_refs(stv)
        stv = stv - st_refs
    final_raw = np.array([r["blend"] for r in rows]) + cls + adj + stv

    # ---- 3. One consistent recenter over the full real field ----
    shift = float(final_raw[vote].mean())   # AUDIT D2: recenter on reliable rows
    final = final_raw - shift

    # ---- 3b. Manual overrides for grade-unreliable teams (owner decision 2026-07-20) ----
    # A few realignment / recent FCS-reclass teams have no reliable FBS roster grades (e.g. NDSU
    # was graded ~-27, a pure no-data artifact), leaving their final well below SP+ AND the market
    # and generating false win-total edges. Replace those with researched values (SP+ + targeted
    # web research), logged in data/manual_overrides_2026.csv. Applied post-recenter so the
    # researched number appears exactly; the ~0.15-pt field-mean drift from a handful of teams is
    # immaterial. --no-overrides skips this (reproduces the pure-model ratings).
    ovr = {}
    if "--no-overrides" not in sys.argv and os.path.exists("data/manual_overrides_2026.csv"):
        for orow in csv.DictReader(open("data/manual_overrides_2026.csv")):
            ovr[orow["team"]] = orow
    override_names = []
    for i, r in enumerate(rows):
        o = ovr.get(r["name"])
        if o:
            final[i] = float(o["rating"]); override_names.append(r["name"])

    # ---- 4. Bands (same frozen formula, recomputed from source data) ----
    band = np.array([SIGMA * (1.13 if r["coach"] else 1.0) * (1.10 if r["disp"] else 1.0)
                     * (1 + 0.03 * min(r["L"], 5)) for r in rows])
    for i, r in enumerate(rows):                      # optional wider band for override teams
        o = ovr.get(r["name"])
        if o and o.get("band"):
            band[i] = float(o["band"])

    # ---- 5. Diagnostics ----
    # level slope, re-measured at 138 (diagnostic ONLY — never enters the final)
    margin = yo - yd
    bl, rl = ols(np.column_stack([ones, margin]), resid)
    lvl_slope = float(bl[1]); lvl_r2 = 1 - rl.var() / resid.var()
    capped = [r["name"] for r, a in zip(rows, adj) if abs(abs(a) - CAP) < 1e-9]
    # movers vs the pilot-era board (if present)
    old = {}
    if os.path.exists("outputs/grade_board.csv"):
        for rr in csv.DictReader(open("outputs/grade_board.csv")):
            try: old[rr["team"]] = float(rr["final"])
            except (ValueError, KeyError): pass
    deltas = [(r["name"], f, f - old[r["name"]]) for r, f in zip(rows, final) if r["name"] in old]

    # rank stability vs the pilot-era ordering (Spearman)
    spearman = None
    if len(old) > 100:
        both = [(old[r["name"]], f) for r, f in zip(rows, final) if r["name"] in old]
        a = np.argsort(np.argsort([x[0] for x in both]))
        b = np.argsort(np.argsort([x[1] for x in both]))
        spearman = float(np.corrcoef(a, b)[0, 1])

    order = np.argsort(-final)
    git_rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True).stdout.strip()
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    os.makedirs("outputs/final_pass", exist_ok=True)
    tag = "" if demean else "_frozen"
    board_csv = "outputs/FINAL_BOARD_2026.csv" if demean else f"outputs/final_pass/FINAL_BOARD{tag}.csv"
    board_md = "outputs/FINAL_BOARD_2026.md" if demean else f"outputs/final_pass/FINAL_BOARD{tag}.md"

    # ---- ASSEMBLY.csv (full audit trail) ----
    with open(f"outputs/final_pass/ASSEMBLY{tag}.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "team", "conference", "anchor_blend", "implied_off", "anchor_off",
                    "implied_def", "anchor_def", "residual", "k_x_resid_clipped", "class",
                    "st_term", "recenter_shift", "final", "band", "L_count", "new_HC", "capped"])
        for rk, i in enumerate(order, 1):
            r = rows[i]
            w.writerow([rk, r["name"], r["conf"], f"{r['blend']:.2f}", f"{implied_off[i]:.2f}",
                        f"{yo[i]:.2f}", f"{implied_def[i]:.2f}", f"{yd[i]:.2f}",
                        f"{resid[i]:+.2f}", f"{adj[i]:+.2f}", f"{cls[i]:+.2f}", f"{stv[i]:+.2f}",
                        f"{-shift:+.2f}", f"{final[i]:.2f}", f"{band[i]:.2f}", r["L"],
                        "Y" if r["coach"] else "", "Y" if r["name"] in capped else ""])

    # ---- Boards (official by default; alt paths under --demean-conf-resid) ----
    with open(board_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "team", "conference", "power_rating", "band_±", "grade_sum", "new_HC"])
        for rk, i in enumerate(order, 1):
            r = rows[i]
            w.writerow([rk, r["name"], r["conf"], f"{final[i]:.2f}", f"{band[i]:.2f}",
                        sum(r["g"][u] for u in OFF + DEF + ["ST"]), "Y" if r["coach"] else ""])
    variant_note = ("" if demean else
                    " — FROZEN-RESID VARIANT (pre-decision formula; NOT the official board)")
    mode_line = ("residual mode: CONFERENCE-DEMEANED (official; Independents pseudo-pooled ND->P4, UConn->G5)"
                 if demean else "residual mode: frozen (full residual; comparison only)")
    L = [f"# 2026 Preseason FBS Power Ratings — Final Board (full-138 REFIT){variant_note}", "",
         f"Produced by pipeline/final_pass.py @ {git_rev} on {stamp}. Conversion refit on all 138",
         "real grades (R² off %.2f / def %.2f); one consistent recenter (%+.2f). power_rating =" % (r2o, r2d, -shift),
         "projected neutral-field margin vs an average FBS team (points); band = the +/- uncertainty.",
         mode_line, "",
         "| # | Team | Conf | Rating | Band | New HC |", "|--:|------|------|-------:|-----:|:--:|"]
    for rk, i in enumerate(order, 1):
        r = rows[i]
        L.append(f"| {rk} | {r['name']} | {r['conf']} | {final[i]:+.2f} | ±{band[i]:.1f} | "
                 f"{'Y' if r['coach'] else ''} |")
    open(board_md, "w").write("\n".join(L) + "\n")

    # ---- REFIT_DIAG.md ----
    byc = {}
    for r, rs in zip(rows, resid):
        byc.setdefault(r["conf"], []).append(float(rs))
    deltas_sorted = sorted(deltas, key=lambda x: -abs(x[2]))
    D = [f"# Final-pass refit diagnostic — {stamp} @ {git_rev}", "",
         "## Conversion weights (proxy-fit regime -> full-138 real-grade refit)",
         "| side | unit | proxy-fit | refit-138 |", "|---|---|---:|---:|"]
    for i, u in enumerate(OFF):
        D.append(f"| off | {u} | {PROXY_REF['off'][u]:+.3f} | {bo[1+i]:+.3f} |")
    for i, u in enumerate(DEF):
        D.append(f"| def | {u} | {PROXY_REF['def'][u]:+.3f} | {bd[1+i]:+.3f} |")
    D += [f"| off | R² | {PROXY_REF['off']['R2']:.2f} | {r2o:.2f} |",
          f"| def | R² | {PROXY_REF['def']['R2']:.2f} | {r2d:.2f} |", "",
          f"intercepts: off {bo[0]:+.2f}, def {bd[0]:+.2f}", "",
          "## Level slope (diagnostic only; NEVER enters the final)",
          f"- resid ~ a + b*(anchor margin) at n=138: slope **{lvl_slope:+.3f}** "
          f"(R² {lvl_r2:.2f}); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).", "",
          f"## Residual census — post-mode residual (mean {resid.mean():+.3f}; in official mode each"
          " conference mean is ≈0 by construction)",
          f"- capped at ±{CAP}: **{len(capped)}** teams: {', '.join(capped) if capped else '(none)'}",
          f"- |resid| p50 {np.percentile(abs(resid),50):.2f} / p90 {np.percentile(abs(resid),90):.2f} / max {abs(resid).max():.2f}", "",
          "## Mean residual by conference (grades-vs-anchor, refit regime)",
          "| conference | n | mean resid | min | max |", "|---|--:|---:|---:|---:|"]
    for c in sorted(byc, key=lambda c: np.mean(byc[c])):
        v = byc[c]
        D.append(f"| {c} | {len(v)} | {np.mean(v):+.2f} | {min(v):+.1f} | {max(v):+.1f} |")
    ups = [d for d in deltas_sorted if d[2] > 0][:10]
    downs = sorted([d for d in deltas_sorted if d[2] < 0], key=lambda x: x[2])[:10]
    D += ["", f"## Movers vs the pilot-era board (mean |Δ| {np.mean([abs(d[2]) for d in deltas]):.2f}, "
          f"max {max(abs(d[2]) for d in deltas):.2f}"
          + (f"; rank Spearman vs pilot-era {spearman:.3f}" if spearman else "") + ")",
          "| biggest UP | Δ | | biggest DOWN | Δ |", "|---|---:|---|---|---:|"]
    for i in range(max(len(ups), len(downs))):
        u = f"{ups[i][0]} | {ups[i][2]:+.2f}" if i < len(ups) else " | "
        d_ = f"{downs[i][0]} | {downs[i][2]:+.2f}" if i < len(downs) else " | "
        D.append(f"| {u} | | {d_} |")
    # the demean decision: what is (or would be) removed, per pool
    verb = "REMOVED (official mode)" if demean else "would be removed (frozen comparison run)"
    D += ["", f"## Conference-level component {verb} — owner decision 2026-07-19",
          "The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference",
          "mean resid) on top of its within-conference shape. Demeaning drops that shared component.",
          f"Independents pseudo-pooled: ND -> all-P4 mean ({p4_mean:+.2f}), UConn -> all-G5 mean ({g5_mean:+.2f}).",
          "| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |", "|---|---:|---:|"]
    for c in sorted(conf_mean, key=lambda c: conf_mean[c]):
        D.append(f"| {c} | {conf_mean[c]:+.2f} | {K * conf_mean[c]:+.2f} |")
    D.append(f"| (all-P4 pool / ND ref) | {p4_mean:+.2f} | {K * p4_mean:+.2f} |")
    D.append(f"| (all-G5 pool / UConn ref) | {g5_mean:+.2f} | {K * g5_mean:+.2f} |")
    D += ["", "## Provenance",
          f"- anchor run: {ANCHOR} (frozen); class_per_side {cps}; teams 138/138 joined",
          f"- constants: K={K} CAP={CAP} SIGMA={SIGMA}; recenter shift {-shift:+.3f}; "
          f"mode {'OFFICIAL (conference-demeaned; IND pseudo-pooled)' if demean else 'FROZEN-RESID comparison variant'}",
          "- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail."]
    open(f"outputs/final_pass/REFIT_DIAG{tag}.md", "w").write("\n".join(D) + "\n")

    print(f"FINAL PASS complete ({'OFFICIAL conference-demeaned' if demean else 'FROZEN-RESID variant'}): 138 teams | "
          f"R2 off {r2o:.2f} def {r2d:.2f} | level slope {lvl_slope:+.3f} | capped {len(capped)} | "
          f"recenter {-shift:+.2f} | mean |dFinal| vs pilot-era {np.mean([abs(d[2]) for d in deltas]):.2f}")
    print(f"wrote outputs/final_pass/ASSEMBLY{tag}.csv, outputs/final_pass/REFIT_DIAG{tag}.md, "
          f"{board_csv}, {board_md}")


if __name__ == "__main__":
    main()
