# Florida International — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-10.72** (rank 111/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy 36
- RB    42 | proxy 2
- WRTE  46 | proxy 7
- OL    40 | proxy 12
- DL    46 | proxy 0
- LB    44 | proxy 25
- DB    44 | proxy 29
- ST    44 | proxy 47

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.095 WRTE:+0.038 OL:+0.083  (R²=0.54)
- def: DL:-0.082 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +23.96 vs anchor off +20.60
- grade-implied def +26.53 vs anchor def +35.90  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+12.73**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +8.28 (=-0.541x anchor margin) + shape +4.45 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.7 → -13.7 → -13.7
- FEI      -0.83 → -17.62 → -17.62
- Massey   6.66 → -18.01 → -18.01
- FPI      -12.6 → -15.16 → -15.16
- TR       -15.0 → -14.84 → -14.84
- blend -15.51  (dispersion 4.31)

## 4. Assembly
- anchor -15.51  class +0.00  k×resid +4.46 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.46) → **-10.72**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T17:48:00Z (Florida International)