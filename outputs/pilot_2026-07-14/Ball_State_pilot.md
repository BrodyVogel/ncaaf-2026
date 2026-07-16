# Ball State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-21.84** (rank 137/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    18 | proxy —
- RB     8 | proxy —
- WRTE  12 | proxy —
- OL    12 | proxy 2
- DL     8 | proxy —
- LB     8 | proxy —
- DB    14 | proxy —
- ST    10 | proxy 12

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.074 RB:+0.094 WRTE:+0.039 OL:+0.076  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.62)
- grade-implied off +15.42 vs anchor off +13.62
- grade-implied def +34.67 vs anchor def +35.28  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+2.41**
- resid decomposition (diagnostic): level +11.72 (=-0.541x anchor margin - the calibrated fade) + shape -9.30 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -25.2 → -25.2 → -25.2
- FEI      -0.95 → -20.21 → -20.21
- Massey   6.53 → -20.44 → -20.44
- FPI      -17.3 → -20.64 → -20.64
- TR       -23.0 → -22.5 → -22.5
- blend -22.37  (dispersion 4.99)

## 4. Assembly
- anchor -22.37  class +0.00  k×resid +0.84 (k=0.35, cap ±6.0)  ST -0.80  → recentered (-0.48) → **-21.84**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (cd6d519)