# Miami (OH) — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-7.41** (rank 95/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    30 | proxy 6
- RB    26 | proxy —
- WRTE  24 | proxy 6
- OL    30 | proxy 3
- DL    28 | proxy 9
- LB    38 | proxy 16
- DB    26 | proxy 3
- ST    40 | proxy 56

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.53)
- def: DL:-0.085 LB:-0.060 DB:-0.099  (R²=0.63)
- grade-implied off +19.78 vs anchor off +17.71
- grade-implied def +30.31 vs anchor def +24.69  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-3.55**
- resid decomposition (diagnostic): level +3.78 (=-0.541x anchor margin - the calibrated fade) + shape -7.33 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.9 → -2.9 → -2.9
- FEI      -0.32 → -6.63 → -6.63
- Massey   7.24 → -7.13 → -7.13
- FPI      -7.0 → -8.64 → -8.64
- TR       -10.6 → -10.63 → -10.63
- blend -6.47  (dispersion 7.73)

## 4. Assembly
- anchor -6.47  class +0.00  k×resid -1.24 (k=0.35, cap ±6.0)  ST -0.20  → recentered (-0.50) → **-7.41**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (a4426e7)