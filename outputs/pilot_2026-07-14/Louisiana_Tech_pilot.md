# Louisiana Tech — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-6.98** (rank 94/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy —
- RB    38 | proxy —
- WRTE  44 | proxy —
- OL    44 | proxy —
- DL    42 | proxy —
- LB    46 | proxy —
- DB    44 | proxy —
- ST    40 | proxy 74

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.62)
- grade-implied off +24.10 vs anchor off +21.57
- grade-implied def +26.72 vs anchor def +31.33  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+7.14**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +5.28 (=-0.541x anchor margin) + shape +1.86 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.3 → -8.3 → -8.3
- FEI      -0.51 → -10.72 → -10.72
- Massey   7.04 → -10.88 → -10.88
- FPI      -9.6 → -11.67 → -11.67
- TR       -8.6 → -8.72 → -8.72
- blend -9.76  (dispersion 3.37)

## 4. Assembly
- anchor -9.76  class +0.00  k×resid +2.50 (k=0.35, cap ±6.0)  ST -0.20  → recentered (-0.48) → **-6.98**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T15:40:00Z (Louisiana Tech)