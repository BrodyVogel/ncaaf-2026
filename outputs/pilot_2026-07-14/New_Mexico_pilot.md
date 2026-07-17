# New Mexico — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-6.60** (rank 92/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    34 | proxy 35
- RB    16 | proxy —
- WRTE  22 | proxy 2
- OL    24 | proxy 17
- DL    22 | proxy 53
- LB    44 | proxy 74
- DB    26 | proxy 36
- ST    18 | proxy 56

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.091 WRTE:+0.039 OL:+0.083  (R²=0.54)
- def: DL:-0.083 LB:-0.061 DB:-0.095  (R²=0.62)
- grade-implied off +18.53 vs anchor off +23.55
- grade-implied def +30.23 vs anchor def +28.15  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-7.10**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +2.49 (=-0.541x anchor margin) + shape -9.59 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -0.5 → -0.5 → -0.94  [WINSORIZED]
- FEI      -0.37 → -7.71 → -7.71
- Massey   7.23 → -7.32 → -7.32
- FPI      -3.5 → -4.56 → -4.56
- TR       -2.1 → -2.49 → -2.49
- blend -3.99  (dispersion 7.21)

## 4. Assembly
- anchor -3.99  class +0.00  k×resid -2.49 (k=0.35, cap ±6.0)  ST -0.64  → recentered (-0.51) → **-6.60**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (9e22a3d)