# Missouri — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+10.45** (rank 28/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    50 | proxy 13
- RB    72 | proxy 98
- WRTE  52 | proxy 79
- OL    58 | proxy 98
- DL    48 | proxy 48
- LB    54 | proxy 98
- DB    50 | proxy 51
- ST    56 | proxy 93

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.093 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.085 LB:-0.054 DB:-0.098  (R²=0.61)
- grade-implied off +28.82 vs anchor off +31.53
- grade-implied def +25.28 vs anchor def +17.57  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-10.42**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -7.55 (=-0.541x anchor margin) + shape -2.87 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      14.8 → 14.8 → 14.8
- FEI      0.56 → 12.35 → 12.35
- Massey   8.3 → 12.74 → 12.74
- FPI      12.2 → 13.73 → 13.73
- TR       15.4 → 14.26 → 14.26
- PickSix  27 → 11.5 → 11.5
- blend 13.45  (dispersion 3.3)

## 4. Assembly
- anchor +13.45  class -0.00  k×resid -3.65 (k=0.35, cap ±6.0)  ST +0.12  → recentered (-0.52) → **+10.45**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T04:19:08Z (6f14031)