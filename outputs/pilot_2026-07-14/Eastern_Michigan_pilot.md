# Eastern Michigan — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-15.27** (rank 126/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    40 | proxy —
- RB    14 | proxy —
- WRTE  34 | proxy 6
- OL    18 | proxy 14
- DL    18 | proxy 5
- LB    16 | proxy —
- DB    28 | proxy 3
- ST    24 | proxy 3

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.093 WRTE:+0.035 OL:+0.081  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +18.82 vs anchor off +17.14
- grade-implied def +32.07 vs anchor def +33.46  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+3.07**
- resid decomposition (diagnostic): level +8.83 (=-0.541x anchor margin - the calibrated fade) + shape -5.76 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -15.0 → -15.0 → -15.0
- FEI      -0.8 → -16.98 → -16.98
- Massey   6.68 → -17.63 → -17.63
- FPI      -16.3 → -19.47 → -19.47
- TR       -13.9 → -13.79 → -13.79
- blend -16.31  (dispersion 5.68)

## 4. Assembly
- anchor -16.31  class +0.00  k×resid +1.07 (k=0.35, cap ±6.0)  ST -0.52  → recentered (-0.48) → **-15.27**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (6cbb74f)