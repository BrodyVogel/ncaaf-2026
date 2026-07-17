# Fresno State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-2.31** (rank 75/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    30 | proxy —
- RB    46 | proxy 24
- WRTE  38 | proxy 0
- OL    40 | proxy 11
- DL    44 | proxy 33
- LB    40 | proxy 27
- DB    44 | proxy 75
- ST    48 | proxy 79

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.038 OL:+0.083  (R²=0.54)
- def: DL:-0.084 LB:-0.061 DB:-0.094  (R²=0.62)
- grade-implied off +22.94 vs anchor off +20.71
- grade-implied def +26.98 vs anchor def +22.79  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-1.96**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +1.13 (=-0.541x anchor margin) + shape -3.09 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.3 → -2.3 → -2.3
- FEI      -0.14 → -2.75 → -2.75
- Massey   7.45 → -3.19 → -3.19
- FPI      -2.5 → -3.4 → -3.4
- TR       2.0 → 1.43 → 1.43
- blend -2.08  (dispersion 4.83)

## 4. Assembly
- anchor -2.08  class +0.00  k×resid -0.69 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.50) → **-2.31**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (13cba26)