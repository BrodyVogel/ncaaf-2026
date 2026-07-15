#!/usr/bin/env python3
"""Residual-pattern diagnostic (2026-07-15, user sniff-test question on big AAC residuals).

Findings (run 2026-07-15, n=664 team-seasons 2021-25):
1. MEAN REVERSION IS REAL IN THE ANCHOR: miss = final - TRUE preseason SP+ regressed on
   preseason level (within-year): slope -0.193 (t=-8.6); every year negative (-0.11 to -0.24);
   within P4 -0.203, within G5 -0.181; bottom-decile preseason teams outperform +4.12 (SE .94),
   top-decile underperform -3.92 (SE .76). Preseason SP+ (~= market, miss corr .969) under-regresses.
2. GRADE COMPRESSION CONFIRMED: real LLM grades SD 14.9 vs shadow-proxy SD 25.9 on the same 15
   teams (per-unit: QB 8 vs 19, ST 9 vs 25, LB 10 vs 26...). Priors-for-unproven pulls to center.
3. NET EFFECT IS CALIBRATED, NOT ARTIFACT: resid~anchor slope = -0.578 (mine) vs -0.376 (proxy
   field). Applied level-fade = k x 0.578 = 0.202 per point of anchor deviation vs backtest-optimal
   0.193. The compressed grades + k=0.35 harvest the anchor's under-regression at ~the right size.
   (Proxy regime under-harvests: 0.35 x 0.376 = 0.132.)
4. DECOMPOSITION (level = proxy-slope x anchor_dev; shape = remainder): Iowa's -6.05 is ~all level
   (-7.4 level, +1.4 shape); Tulsa's +9.16 is ~all shape (+7.3); Charlotte/UAB/Rice ~half-half.
5. AAC 2021-25 mean miss +1.91 (n=64): mild real underpricing of the conference by preseason SP+.

Registered follow-up (full-138 compute): re-estimate component-specific loadings
(miss ~ level_component + shape_component) to test whether shape deserves k != 0.35.
"""
import csv, importlib.util
import numpy as np
spec = importlib.util.spec_from_file_location("s2", "pipeline/step2_backtest_v2.py")
s2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(s2)

def main():
    cfbd = "data/cfbd/2026-07-12"
    n2c = {r["norm_key"]: r["cfbd_school"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}
    xs, ys = [], []
    for y in range(2021, 2026):
        pre, fin = s2.load_pre("data/backtest/sp_preseason", y, n2c), s2.load_final(cfbd, y)
        px = np.array([pre[t]["overall"] for t in pre if t in fin])
        py = np.array([fin[t]["overall"] - pre[t]["overall"] for t in pre if t in fin])
        px -= px.mean(); py -= py.mean()
        xs.append(px); ys.append(py)
    x = np.concatenate(xs); yv = np.concatenate(ys)
    b = (x*yv).sum()/(x*x).sum()
    res = yv - b*x
    se = np.sqrt(res.var(ddof=1)/(x*x).sum())
    print(f"pooled within-year slope: {b:+.4f} (t={b/se:+.2f}, n={len(x)})")

if __name__ == "__main__":
    main()
