# SMU — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+9.39** (rank 30/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    62 | proxy 74
- RB    54 | proxy 2
- WRTE  52 | proxy 59
- OL    62 | proxy 85
- DL    52 | proxy 63
- LB    56 | proxy 52
- DB    52 | proxy 47
- ST    50 | proxy 54

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.100 WRTE:+0.036 OL:+0.077  (R²=0.54)
- def: DL:-0.082 LB:-0.059 DB:-0.097  (R²=0.62)
- grade-implied off +28.17 vs anchor off +32.41
- grade-implied def +24.61 vs anchor def +20.19  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-8.66**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -6.61 (=-0.541x anchor margin) + shape -2.05 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      10.9 → 10.9 → 10.9
- FEI      0.44 → 9.76 → 9.76
- Massey   8.26 → 11.99 → 11.99
- FPI      11.1 → 12.45 → 12.45
- TR       14.4 → 13.3 → 13.3
- PickSix  21 → 14.1 → 14.1
- blend 11.91  (dispersion 4.34)

## 4. Assembly
- anchor +11.91  class -0.00  k×resid -3.03 (k=0.35, cap ±6.0)  ST +0.00  → recentered (-0.51) → **+9.39**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (647ccd9)