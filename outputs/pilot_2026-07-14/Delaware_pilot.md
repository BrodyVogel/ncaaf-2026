# Delaware — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-9.02** (rank 103/138 in hybrid field)  band ±6.60

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 21
- RB    48 | proxy 7
- WRTE  50 | proxy 51
- OL    48 | proxy 31
- DL    44 | proxy 48
- LB    46 | proxy 18
- DB    46 | proxy 21
- ST    42 | proxy 39

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.095 WRTE:+0.035 OL:+0.082  (R²=0.54)
- def: DL:-0.086 LB:-0.056 DB:-0.095  (R²=0.61)
- grade-implied off +25.78 vs anchor off +22.27
- grade-implied def +26.36 vs anchor def +35.83  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+12.98**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +7.34 (=-0.541x anchor margin) + shape +5.65 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.0 → -13.0 → -13.0
- FEI      -0.8 → -16.98 → -16.98
- Massey   6.56 → -19.88 → -17.72  [WINSORIZED]
- FPI      -6.6 → -8.17 → -9.99  [WINSORIZED]
- TR       -12.5 → -12.45 → -12.45
- blend -13.86  (dispersion 11.71, FLAGGED

## 4. Assembly
- anchor -13.86  class +0.00  k×resid +4.54 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.46) → **-9.02**
- band: 6.0 × coach(1.0) × dispersion(1.10) × conf(1+0.03×0) = ±6.60

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T17:38:00Z (Delaware)