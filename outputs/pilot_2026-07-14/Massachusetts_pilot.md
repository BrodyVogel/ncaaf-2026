# Massachusetts — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-25.80** (rank 138/138 in hybrid field)  band ±6.80

## 1. Unit grades (LLM real | shadow proxy)
- QB    22 | proxy —
- RB    10 | proxy —
- WRTE  14 | proxy —
- OL    12 | proxy 2
- DL    12 | proxy —
- LB    30 | proxy 33
- DB    16 | proxy 0
- ST    20 | proxy 10

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.075 RB:+0.094 WRTE:+0.040 OL:+0.073  (R²=0.54)
- def: DL:-0.088 LB:-0.059 DB:-0.090  (R²=0.62)
- grade-implied off +16.02 vs anchor off +9.94
- grade-implied def +32.79 vs anchor def +39.76  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+13.06**
- resid decomposition (diagnostic): level +16.13 (=-0.541x anchor margin - the calibrated fade) + shape -3.08 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -30.9 → -30.9 → -30.9
- FEI      -1.54 → -32.93 → -32.93
- Massey   5.9 → -32.26 → -32.26
- FPI      -18.8 → -22.39 → -26.58  [WINSORIZED]
- TR       -28.5 → -27.76 → -27.76
- blend -30.22  (dispersion 10.55, FLAGGED

## 4. Assembly
- anchor -30.22  class +0.00  k×resid +4.57 (k=0.35, cap ±6.0)  ST -0.60  → recentered (-0.45) → **-25.80**
- band: 6.0 × coach(1.0) × dispersion(1.10) × conf(1+0.03×1) = ±6.80

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (b94b9c4)