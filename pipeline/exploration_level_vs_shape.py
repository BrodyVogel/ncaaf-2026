#!/usr/bin/env python3
"""DIAGNOSTIC (2026-07-15, user-prompted): is the residual's LEVEL component predictive,
or is the bottoms-up grading mechanism broken?

Context: production resid = grade-implied margin - anchor margin. On the 2026 real-graded
teams, resid regresses on anchor margin with slope -0.541 (the "level fade"): grade-implied
spreads run at ~46% of anchor spreads. k x resid therefore implicitly fades every anchor
deviation by ~k x 0.541 ~ 0.19. The user's challenge (TT-ISU): raw resids imply an 11.5-pt
spread vs the anchors' 20.7 - if the level component is artifact, we are over-compressing;
if it is calibrated regression-to-the-mean, the final 17.75 spread is the defensible number.

Test on the SAME panel as the ratified k calibration (step4b: conference-adjusted grades,
LOYO offsets, 2022-2025, n~530): decompose resid_total into
    level = s x dev        (s = within-panel slope of resid on preseason dev)
    shape = resid - level
and regress miss (actual-minus-preseason margin change) on the components:
    (A) miss ~ resid_total                       [reproduces gamma ~ +0.32..0.39]
    (B) miss ~ dev + resid_total                 [does dev carry signal beyond resid?]
    (C) miss ~ level + shape                     [separate coefficients]
    (D) same, P4-only and G5-only
    (E) miss ~ dev alone                         [is regression-to-mean real at all?]
Interpretation guide:
    coef(dev) in (E) < 0  => preseason anchors overstate deviations (fade is real)
    coef(level) ~ coef(shape) in (C) => current single-k formula is correctly specified
    coef(level) ~ 0, coef(shape) > 0 => level fade is artifact; k should hit shape only
READ-ONLY: changes nothing; feeds a propose->approve decision.
"""
import csv, json
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step4b_calibration_conf_adjusted import (fit_offsets, unit_grades_adjusted, fin,
                                              confs, ols)
from pff_common import UNITS, OFF_UNITS, DEF_UNITS, build_team_lookup

D = "data/cfbd/2026-07-12"
POWER5 = {"SEC", "Big Ten", "Big 12", "ACC", "Pac-12"}


def main():
    n2c, lookup = build_team_lookup()

    def pre(y):
        return {n2c[r["norm_key"]]: (float(r["sp_plus_off"]), float(r["sp_plus_def"]))
                for r in csv.DictReader(open(f"data/backtest/sp_preseason/SP+_{y}_preseason.csv"))}

    panel = []
    for y in (2022, 2023, 2024, 2025):
        offsets = fit_offsets(exclude_year=y, lookup=lookup)
        ug = unit_grades_adjusted(y, lookup, offsets, 1.0)
        P, F, C = pre(y), fin(y), confs(y)
        teams = [t for t in P if t in F]
        umean = {u: np.mean([ug[(t, u)][0] for t in teams if (t, u) in ug]) for u in UNITS}
        rows = []
        for t in teams:
            g = {u: (ug[(t, u)][0] if (t, u) in ug else umean[u]) for u in UNITS}
            rows.append((t, g))
        Xo = np.column_stack([np.ones(len(rows))] + [[g[u] for _, g in rows] for u in OFF_UNITS])
        Xd = np.column_stack([np.ones(len(rows))] + [[g[u] for _, g in rows] for u in DEF_UNITS])
        yo = np.array([P[t][0] for t, _ in rows]); yd = np.array([P[t][1] for t, _ in rows])
        bo, ro, _ = ols(Xo, yo); bd, rd, _ = ols(Xd, yd)
        devs = np.array([(P[t][0] - P[t][1]) for t, _ in rows])
        devs = devs - devs.mean()  # center within year
        for i, (t, g) in enumerate(rows):
            pw = 1 if (C.get(t) in POWER5 or t == "Notre Dame") else 0
            panel.append(dict(year=y, team=t, power=pw, dev=float(devs[i]),
                              resid=float((-ro[i]) - (-rd[i])),
                              miss=(F[t][0] - P[t][0]) - (F[t][1] - P[t][1])))

    dev = np.array([r["dev"] for r in panel])
    resid = np.array([r["resid"] for r in panel])
    miss = np.array([r["miss"] for r in panel])
    pw = np.array([r["power"] for r in panel], float)
    n = len(panel)
    print(f"panel n={n} (2022-2025, conference-adjusted grades, LOYO)")

    # slope of resid on dev in the backtest world (the proxy-world level slope)
    b, _, t = ols(np.column_stack([np.ones(n), dev]), resid)
    s = b[1]
    print(f"\n[slope] resid ~ dev: {s:+.3f} (t={t[1]:+.1f})   [real-graded 2026 pilots: -0.541]")
    level = s * dev
    shape = resid - level

    print("\n(A) miss ~ resid            ", end="")
    b, _, t = ols(np.column_stack([np.ones(n), resid]), miss)
    print(f"gamma={b[1]:+.3f} (t={t[1]:+.1f})")

    print("(E) miss ~ dev              ", end="")
    b, _, t = ols(np.column_stack([np.ones(n), dev]), miss)
    print(f"beta={b[1]:+.3f} (t={t[1]:+.1f})   <- regression-to-mean check")

    print("(B) miss ~ dev + resid      ", end="")
    b, _, t = ols(np.column_stack([np.ones(n), dev, resid]), miss)
    print(f"beta={b[1]:+.3f} (t={t[1]:+.1f}), gamma={b[2]:+.3f} (t={t[2]:+.1f})")

    print("(C) miss ~ level + shape    ", end="")
    b, _, t = ols(np.column_stack([np.ones(n), level, shape]), miss)
    print(f"k_level={b[1]:+.3f} (t={t[1]:+.1f}), k_shape={b[2]:+.3f} (t={t[2]:+.1f})")

    for lab, mask in [("P4", pw == 1), ("G5", pw == 0)]:
        nn = int(mask.sum())
        b, _, t = ols(np.column_stack([np.ones(nn), level[mask], shape[mask]]), miss[mask])
        print(f"(D) {lab}-only (n={nn})       k_level={b[1]:+.3f} (t={t[1]:+.1f}), "
              f"k_shape={b[2]:+.3f} (t={t[2]:+.1f})")
        b, _, t = ols(np.column_stack([np.ones(nn), dev[mask]]), miss[mask])
        print(f"    {lab} miss ~ dev alone:   beta={b[1]:+.3f} (t={t[1]:+.1f})")

    # what the fits imply for the 2026 TT-ISU spread (dev on the 2026 anchor scale)
    print("\n[2026 implication] anchors: TT +21.67, ISU +0.99 (spread 20.68)")
    for lab, (kl, ks) in [("current formula (k=0.35 both)", (0.35, 0.35))]:
        pass
    b, _, _ = ols(np.column_stack([np.ones(n), dev, resid]), miss)
    beta, gamma = b[1], b[2]
    # 2026 production numbers: TT resid -13.57 (level -11.62, shape -1.95); ISU resid -4.38
    # (level -0.26 hmm production uses -0.541 slope; ISU level = -0.541*0.99*... see sheet)
    tt_fit = 21.67 + beta * 21.67 + gamma * (-13.57)
    isu_fit = 0.99 + beta * 0.99 + gamma * (-4.38)
    print(f"  fitted (B) model:  TT {tt_fit:+.2f}, ISU {isu_fit:+.2f}, spread {tt_fit-isu_fit:.2f}")
    print(f"  current formula:   TT +17.75, ISU -0.00, spread 17.75")
    print(f"  anchors alone:     spread 20.68")


if __name__ == "__main__":
    main()
