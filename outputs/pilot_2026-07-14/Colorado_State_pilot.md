# Colorado State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-12.36** (rank 115/138 in hybrid field)  band ±7.39

## 1. Unit grades (LLM real | shadow proxy)
- QB    24 | proxy 9
- RB    30 | proxy —
- WRTE  16 | proxy 2
- OL    16 | proxy —
- DL    26 | proxy 9
- LB    24 | proxy 19
- DB    22 | proxy 2
- ST    20 | proxy 3

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.069 RB:+0.093 WRTE:+0.034 OL:+0.084  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.098  (R²=0.62)
- grade-implied off +18.38 vs anchor off +17.12
- grade-implied def +31.63 vs anchor def +28.68  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-1.69**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +6.25 (=-0.541x anchor margin) + shape -7.94 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.3 → -8.3 → -8.57  [WINSORIZED]
- FEI      -0.61 → -12.88 → -12.88
- Massey   6.86 → -14.26 → -14.26
- FPI      -12.4 → -14.93 → -14.93
- TR       -10.7 → -10.73 → -10.73
- blend -11.66  (dispersion 6.63)

## 4. Assembly
- anchor -11.66  class +0.00  k×resid -0.59 (k=0.35, cap ±6.0)  ST -0.60  → recentered (-0.49) → **-12.36**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×3) = ±7.39

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (76bc976)