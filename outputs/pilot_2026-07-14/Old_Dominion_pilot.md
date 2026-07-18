# Old Dominion — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-3.12** (rank 82/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    44 | proxy 57
- RB    46 | proxy 30
- WRTE  40 | proxy —
- OL    40 | proxy —
- DL    42 | proxy 9
- LB    48 | proxy —
- DB    54 | proxy 66
- ST    42 | proxy 25

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.090 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.085 LB:-0.059 DB:-0.095  (R²=0.62)
- grade-implied off +24.07 vs anchor off +21.09
- grade-implied def +25.73 vs anchor def +24.41  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+1.66**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +1.80 (=-0.541x anchor margin) + shape -0.13 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.8 → -5.8 → -5.8
- FEI      -0.03 → -0.38 → -0.38
- Massey   7.53 → -1.69 → -1.69
- FPI      -4.4 → -5.61 → -5.61
- TR       -4.6 → -4.89 → -4.89
- blend -4.03  (dispersion 5.42)

## 4. Assembly
- anchor -4.03  class +0.00  k×resid +0.58 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.48) → **-3.12**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T16:05:00Z (Old Dominion)