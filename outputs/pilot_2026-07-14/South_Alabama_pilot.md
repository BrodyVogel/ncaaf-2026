# South Alabama — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-8.63** (rank 102/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy 34
- RB    52 | proxy 66
- WRTE  42 | proxy 26
- OL    38 | proxy —
- DL    38 | proxy 23
- LB    42 | proxy 17
- DB    44 | proxy 63
- ST    42 | proxy 32

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.093 WRTE:+0.036 OL:+0.083  (R²=0.54)
- def: DL:-0.081 LB:-0.055 DB:-0.100  (R²=0.62)
- grade-implied off +24.66 vs anchor off +23.34
- grade-implied def +27.26 vs anchor def +34.76  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+8.82**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +6.18 (=-0.541x anchor margin) + shape +2.64 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.3 → -13.3 → -13.3
- FEI      -0.52 → -10.94 → -10.94
- Massey   7.03 → -11.07 → -11.07
- FPI      -10.5 → -12.72 → -12.72
- TR       -10.8 → -10.82 → -10.82
- blend -12.02  (dispersion 2.48)

## 4. Assembly
- anchor -12.02  class +0.00  k×resid +3.09 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.47) → **-8.63**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T16:18:00Z (South Alabama)