# Akron — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-18.53** (rank 134/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    34 | proxy —
- RB    16 | proxy 3
- WRTE  28 | proxy 24
- OL    14 | proxy —
- DL    12 | proxy 14
- LB    12 | proxy —
- DB    22 | proxy 43
- ST    24 | proxy 25

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.085 WRTE:+0.035 OL:+0.086  (R²=0.54)
- def: DL:-0.081 LB:-0.060 DB:-0.096  (R²=0.61)
- grade-implied off +18.22 vs anchor off +12.77
- grade-implied def +33.35 vs anchor def +32.13  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+4.23**
- resid decomposition (diagnostic): level +10.47 (=-0.541x anchor margin - the calibrated fade) + shape -6.24 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -19.5 → -19.5 → -19.5
- FEI      -1.06 → -22.58 → -22.58
- Massey   6.53 → -20.44 → -20.44
- FPI      -16.9 → -20.17 → -20.17
- TR       -17.9 → -17.62 → -17.62
- blend -19.97  (dispersion 4.97)

## 4. Assembly
- anchor -19.97  class +0.00  k×resid +1.48 (k=0.35, cap ±6.0)  ST -0.52  → recentered (-0.48) → **-18.53**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (aadf7b3)