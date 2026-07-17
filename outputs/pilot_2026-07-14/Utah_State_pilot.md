# Utah State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-6.51** (rank 93/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    32 | proxy —
- RB    40 | proxy —
- WRTE  34 | proxy 14
- OL    36 | proxy 12
- DL    36 | proxy 16
- LB    36 | proxy 26
- DB    36 | proxy 19
- ST    38 | proxy 10

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.091 WRTE:+0.038 OL:+0.083  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +22.05 vs anchor off +24.27
- grade-implied def +28.65 vs anchor def +30.33  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-0.54**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +3.28 (=-0.541x anchor margin) + shape -3.82 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.7 → -7.7 → -7.7
- FEI      -0.28 → -5.77 → -5.77
- Massey   7.31 → -5.82 → -5.82
- FPI      -6.7 → -8.29 → -8.29
- TR       -3.8 → -4.12 → -4.12
- blend -6.57  (dispersion 4.17)

## 4. Assembly
- anchor -6.57  class +0.00  k×resid -0.19 (k=0.35, cap ±6.0)  ST -0.24  → recentered (-0.49) → **-6.51**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (726aed5)