# California — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+1.27** (rank 60/138 in hybrid field)  band ±7.39

## 1. Unit grades (LLM real | shadow proxy)
- QB    58 | proxy 5
- RB    46 | proxy 41
- WRTE  54 | proxy 85
- OL    44 | proxy 60
- DL    42 | proxy 5
- LB    38 | proxy —
- DB    48 | proxy —
- ST    42 | proxy 10

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.076 RB:+0.094 WRTE:+0.034 OL:+0.080  (R²=0.54)
- def: DL:-0.086 LB:-0.058 DB:-0.095  (R²=0.62)
- grade-implied off +25.87 vs anchor off +28.43
- grade-implied def +26.88 vs anchor def +25.97  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-3.46**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -1.33 (=-0.541x anchor margin) + shape -2.13 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.7 → 3.7 → 3.7
- FEI      -0.07 → -1.24 → -1.24
- Massey   7.65 → 0.56 → 0.56
- FPI      0.9 → 0.56 → 0.56
- TR       4.0 → 3.34 → 3.34
- PickSix  50 → 4.44 → 4.44
- blend 2.15  (dispersion 5.68)

## 4. Assembly
- anchor +2.15  class -0.00  k×resid -1.21 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.49) → **+1.27**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×3) = ±7.39

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (7f3723b)