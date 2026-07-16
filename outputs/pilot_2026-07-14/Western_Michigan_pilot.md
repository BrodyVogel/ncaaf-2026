# Western Michigan — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-8.22** (rank 98/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy 64
- RB    28 | proxy 19
- WRTE  26 | proxy 17
- OL    28 | proxy 8
- DL    18 | proxy 82
- LB    16 | proxy —
- DB    30 | proxy 29
- ST    28 | proxy 74

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.095  (R²=0.61)
- grade-implied off +21.03 vs anchor off +19.25
- grade-implied def +31.88 vs anchor def +25.55  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-4.55**
- resid decomposition (diagnostic): level +3.41 (=-0.541x anchor margin - the calibrated fade) + shape -7.96 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.2 → -7.2 → -7.2
- FEI      -0.25 → -5.12 → -5.12
- Massey   7.24 → -7.13 → -7.13
- FPI      -4.0 → -5.14 → -5.14
- TR       -8.3 → -8.43 → -8.43
- blend -6.7  (dispersion 3.31)

## 4. Assembly
- anchor -6.70  class +0.00  k×resid -1.59 (k=0.35, cap ±6.0)  ST -0.44  → recentered (-0.51) → **-8.22**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (d01620e)