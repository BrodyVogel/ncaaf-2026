# Ohio — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-11.50** (rank 114/138 in hybrid field)  band ±6.98

## 1. Unit grades (LLM real | shadow proxy)
- QB    22 | proxy —
- RB    20 | proxy —
- WRTE  16 | proxy —
- OL    12 | proxy —
- DL    18 | proxy —
- LB    40 | proxy 47
- DB    22 | proxy 12
- ST    24 | proxy 23

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.091 WRTE:+0.037 OL:+0.083  (R²=0.55)
- def: DL:-0.082 LB:-0.058 DB:-0.099  (R²=0.62)
- grade-implied off +16.95 vs anchor off +15.32
- grade-implied def +31.29 vs anchor def +24.18  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-5.48**
- resid decomposition (diagnostic): level +4.79 (=-0.541x anchor margin - the calibrated fade) + shape -10.27 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.6 → -13.6 → -12.78  [WINSORIZED]
- FEI      -0.28 → -5.77 → -5.77
- Massey   7.34 → -5.26 → -5.36  [WINSORIZED]
- FPI      -8.0 → -9.8 → -9.8
- TR       -10.9 → -10.92 → -10.92
- blend -9.57  (dispersion 8.34)

## 4. Assembly
- anchor -9.57  class +0.00  k×resid -1.92 (k=0.35, cap ±6.0)  ST -0.52  → recentered (-0.50) → **-11.50**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×1) = ±6.98

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (8fb97ff)