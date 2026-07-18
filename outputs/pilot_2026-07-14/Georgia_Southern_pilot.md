# Georgia Southern — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-7.95** (rank 98/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy —
- RB    42 | proxy 80
- WRTE  44 | proxy —
- OL    40 | proxy 27
- DL    42 | proxy 7
- LB    40 | proxy 7
- DB    42 | proxy 9
- ST    42 | proxy 13

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.095 WRTE:+0.037 OL:+0.080  (R²=0.54)
- def: DL:-0.084 LB:-0.060 DB:-0.096  (R²=0.61)
- grade-implied off +23.98 vs anchor off +22.21
- grade-implied def +27.34 vs anchor def +33.09  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+7.52**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +5.89 (=-0.541x anchor margin) + shape +1.63 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.9 → -8.9 → -8.9
- FEI      -0.6 → -12.67 → -12.67
- Massey   6.95 → -12.57 → -12.57
- FPI      -8.7 → -10.62 → -10.62
- TR       -11.7 → -11.68 → -11.68
- blend -10.89  (dispersion 3.77)

## 4. Assembly
- anchor -10.89  class +0.00  k×resid +2.63 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.47) → **-7.95**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T14:50:00Z (Georgia Southern)