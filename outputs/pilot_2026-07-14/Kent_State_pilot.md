# Kent State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-19.77** (rank 136/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    32 | proxy 9
- RB    10 | proxy —
- WRTE  26 | proxy —
- OL    12 | proxy 2
- DL    22 | proxy 9
- LB    14 | proxy 23
- DB    18 | proxy 1
- ST    26 | proxy 13

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.069 RB:+0.093 WRTE:+0.038 OL:+0.080  (R²=0.53)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +17.11 vs anchor off +15.11
- grade-implied def +32.79 vs anchor def +36.29  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+5.50**
- resid decomposition (diagnostic): level +11.46 (=-0.541x anchor margin - the calibrated fade) + shape -5.96 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -20.1 → -20.1 → -20.1
- FEI      -1.06 → -22.58 → -22.58
- Massey   6.32 → -24.38 → -24.38
- FPI      -17.9 → -21.34 → -21.34
- TR       -22.1 → -21.64 → -21.64
- blend -21.69  (dispersion 4.28)

## 4. Assembly
- anchor -21.69  class +0.00  k×resid +1.93 (k=0.35, cap ±6.0)  ST -0.48  → recentered (-0.48) → **-19.77**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (e7b5480)