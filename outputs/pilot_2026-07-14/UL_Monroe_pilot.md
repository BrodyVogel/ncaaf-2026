# UL Monroe — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-16.18** (rank 132/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    42 | proxy —
- RB    40 | proxy —
- WRTE  40 | proxy —
- OL    38 | proxy —
- DL    40 | proxy —
- LB    44 | proxy —
- DB    40 | proxy —
- ST    40 | proxy 27

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.091 WRTE:+0.037 OL:+0.083  (R²=0.55)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.63)
- grade-implied off +23.26 vs anchor off +15.24
- grade-implied def +27.35 vs anchor def +36.96  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+17.63**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +11.75 (=-0.541x anchor margin) + shape +5.88 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -24.3 → -24.3 → -24.3
- FEI      -1.02 → -21.72 → -21.72
- Massey   6.46 → -21.76 → -21.76
- FPI      -19.3 → -22.97 → -22.97
- TR       -19.8 → -19.44 → -19.44
- blend -22.41  (dispersion 4.86)

## 4. Assembly
- anchor -22.41  class +0.00  k×resid +6.00 (k=0.35, cap ±6.0)  ST -0.20  → recentered (-0.43) → **-16.18**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T16:52:00Z (UL Monroe)