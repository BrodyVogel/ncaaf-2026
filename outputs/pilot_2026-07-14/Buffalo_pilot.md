# Buffalo — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-14.01** (rank 123/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    22 | proxy —
- RB    16 | proxy —
- WRTE  22 | proxy —
- OL    16 | proxy —
- DL    14 | proxy —
- LB    12 | proxy —
- DB    42 | proxy 45
- ST    22 | proxy 82

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.091 WRTE:+0.037 OL:+0.083  (R²=0.55)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.62)
- grade-implied off +17.15 vs anchor off +14.59
- grade-implied def +31.29 vs anchor def +29.21  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+0.48**
- resid decomposition (diagnostic): level +7.91 (=-0.541x anchor margin - the calibrated fade) + shape -7.43 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -11.9 → -11.9 → -11.9
- FEI      -0.72 → -15.25 → -15.25
- Massey   6.75 → -16.32 → -16.32
- FPI      -10.8 → -13.07 → -13.07
- TR       -16.5 → -16.28 → -16.28
- blend -14.12  (dispersion 4.42)

## 4. Assembly
- anchor -14.12  class +0.00  k×resid +0.17 (k=0.35, cap ±6.0)  ST -0.56  → recentered (-0.50) → **-14.01**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (6b0c2c1)