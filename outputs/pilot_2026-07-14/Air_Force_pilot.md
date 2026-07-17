# Air Force — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-8.83** (rank 102/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    32 | proxy 54
- RB    22 | proxy 13
- WRTE  14 | proxy —
- OL    26 | proxy 32
- DL    14 | proxy 41
- LB    20 | proxy 27
- DB    18 | proxy 5
- ST    12 | proxy 59

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.094 WRTE:+0.036 OL:+0.082  (R²=0.54)
- def: DL:-0.082 LB:-0.059 DB:-0.097  (R²=0.62)
- grade-implied off +18.81 vs anchor off +23.76
- grade-implied def +33.17 vs anchor def +29.24  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-8.87**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +2.96 (=-0.541x anchor margin) + shape -11.84 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.4 → -2.4 → -2.44  [WINSORIZED]
- FEI      -0.23 → -4.69 → -4.69
- Massey   7.23 → -7.32 → -7.32
- FPI      -6.8 → -8.41 → -8.41
- TR       -7.4 → -7.57 → -7.57
- blend -5.48  (dispersion 6.01)

## 4. Assembly
- anchor -5.48  class +0.00  k×resid -3.11 (k=0.35, cap ±6.0)  ST -0.76  → recentered (-0.52) → **-8.83**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (e925048)