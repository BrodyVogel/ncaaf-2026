# Toledo — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-9.12** (rank 102/138 in hybrid field)  band ±7.91

## 1. Unit grades (LLM real | shadow proxy)
- QB    22 | proxy —
- RB    16 | proxy —
- WRTE  16 | proxy —
- OL    14 | proxy 5
- DL    18 | proxy 9
- LB    16 | proxy 14
- DB    16 | proxy 17
- ST    24 | proxy 90

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.081  (R²=0.54)
- def: DL:-0.085 LB:-0.062 DB:-0.096  (R²=0.63)
- grade-implied off +16.70 vs anchor off +20.00
- grade-implied def +33.43 vs anchor def +24.60  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-12.13**
- resid decomposition (diagnostic): level +2.49 (=-0.541x anchor margin - the calibrated fade) + shape -14.62 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -11.5 → -11.5 → -7.56  [WINSORIZED]
- FEI      0.07 → 1.78 → -1.35  [WINSORIZED]
- Massey   7.56 → -1.13 → -1.35  [WINSORIZED]
- FPI      -3.0 → -3.98 → -3.98
- TR       -8.6 → -8.72 → -7.56  [WINSORIZED]
- blend -4.89  (dispersion 13.28, FLAGGED

## 4. Assembly
- anchor -4.89  class +0.00  k×resid -4.25 (k=0.35, cap ±6.0)  ST -0.52  → recentered (-0.53) → **-9.12**
- band: 6.0 × coach(1.13) × dispersion(1.10) × conf(1+0.03×2) = ±7.91

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (cf02669)