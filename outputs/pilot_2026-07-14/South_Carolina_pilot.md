# South Carolina — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+8.47** (rank 32/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    56 | proxy 75
- RB    48 | proxy —
- WRTE  52 | proxy 25
- OL    44 | proxy 47
- DL    56 | proxy 82
- LB    48 | proxy 78
- DB    52 | proxy 85
- ST    48 | proxy 36

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.092 WRTE:+0.038 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +25.82 vs anchor off +29.53
- grade-implied def +24.70 vs anchor def +18.77  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-9.64**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -5.82 (=-0.541x anchor margin) + shape -3.82 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      12.1 → 12.1 → 12.1
- FEI      0.43 → 9.54 → 9.54
- Massey   8.16 → 10.12 → 10.12
- FPI      11.7 → 13.15 → 13.15
- TR       12.2 → 11.19 → 11.19
- PickSix  28 → 11.37 → 11.37
- blend 11.37  (dispersion 3.6)

## 4. Assembly
- anchor +11.37  class -0.00  k×resid -3.37 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.51) → **+8.47**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T04:46:58Z (bd6d1a0)