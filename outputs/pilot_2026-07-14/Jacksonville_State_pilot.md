# Jacksonville State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-6.52** (rank 93/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 20
- RB    42 | proxy —
- WRTE  46 | proxy 12
- OL    46 | proxy 27
- DL    42 | proxy 14
- LB    48 | proxy 8
- DB    50 | proxy 47
- ST    48 | proxy 21

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.091 WRTE:+0.038 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.058 DB:-0.097  (R²=0.61)
- grade-implied off +24.94 vs anchor off +23.73
- grade-implied def +26.05 vs anchor def +33.07  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+8.23**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +5.05 (=-0.541x anchor margin) + shape +3.18 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.7 → -7.7 → -7.7
- FEI      -0.49 → -10.29 → -10.29
- Massey   6.97 → -12.19 → -12.19
- FPI      -8.5 → -10.39 → -10.39
- TR       -10.7 → -10.73 → -10.73
- blend -9.83  (dispersion 4.49)

## 4. Assembly
- anchor -9.83  class +0.00  k×resid +2.88 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.47) → **-6.52**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T17:58:00Z (Jacksonville State)