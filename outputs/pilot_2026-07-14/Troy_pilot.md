# Troy — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-5.34** (rank 89/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy 34
- RB    42 | proxy —
- WRTE  42 | proxy —
- OL    40 | proxy 12
- DL    46 | proxy 30
- LB    42 | proxy 5
- DB    44 | proxy 6
- ST    48 | proxy 55

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.082 LB:-0.061 DB:-0.097  (R²=0.62)
- grade-implied off +23.88 vs anchor off +22.86
- grade-implied def +26.71 vs anchor def +30.54  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+4.85**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +4.15 (=-0.541x anchor margin) + shape +0.69 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -6.0 → -6.0 → -6.0
- FEI      -0.36 → -7.49 → -7.49
- Massey   7.17 → -8.44 → -8.44
- FPI      -7.4 → -9.1 → -9.1
- TR       -7.7 → -7.85 → -7.85
- blend -7.48  (dispersion 3.1)

## 4. Assembly
- anchor -7.48  class +0.00  k×resid +1.70 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.48) → **-5.34**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T16:42:00Z (Troy)