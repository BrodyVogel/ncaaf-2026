# Central Michigan — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-12.81** (rank 117/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    38 | proxy —
- RB    28 | proxy —
- WRTE  28 | proxy —
- OL    28 | proxy 4
- DL    24 | proxy 0
- LB    14 | proxy —
- DB    22 | proxy 15
- ST    26 | proxy 7

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.093 WRTE:+0.038 OL:+0.078  (R²=0.54)
- def: DL:-0.085 LB:-0.057 DB:-0.097  (R²=0.62)
- grade-implied off +20.57 vs anchor off +16.95
- grade-implied def +32.29 vs anchor def +30.05  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+1.39**
- resid decomposition (diagnostic): level +7.09 (=-0.541x anchor margin - the calibrated fade) + shape -5.70 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -12.4 → -12.4 → -12.4
- FEI      -0.64 → -13.53 → -13.53
- Massey   6.9 → -13.51 → -13.51
- FPI      -12.8 → -15.4 → -15.4
- TR       -12.6 → -12.54 → -12.54
- blend -13.3  (dispersion 3.0)

## 4. Assembly
- anchor -13.30  class +0.00  k×resid +0.49 (k=0.35, cap ±6.0)  ST -0.48  → recentered (-0.49) → **-12.81**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (b9b71a2)