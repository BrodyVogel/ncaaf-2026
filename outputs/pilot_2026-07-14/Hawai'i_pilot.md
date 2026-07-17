# Hawai'i — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-9.36** (rank 103/138 in hybrid field)  band ±6.72

## 1. Unit grades (LLM real | shadow proxy)
- QB    38 | proxy 42
- RB    14 | proxy —
- WRTE  18 | proxy 21
- OL    10 | proxy 3
- DL    16 | proxy 33
- LB    12 | proxy 16
- DB    18 | proxy 83
- ST    12 | proxy 67

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.091 WRTE:+0.038 OL:+0.084  (R²=0.54)
- def: DL:-0.082 LB:-0.054 DB:-0.101  (R²=0.62)
- grade-implied off +17.30 vs anchor off +24.39
- grade-implied def +33.33 vs anchor def +30.71  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-9.71**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +3.42 (=-0.541x anchor margin) + shape -13.13 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -3.9 → -3.9 → -3.9
- FEI      -0.37 → -7.71 → -7.71
- Massey   7.14 → -9.01 → -9.01
- FPI      -2.4 → -3.28 → -3.28
- TR       -6.3 → -6.51 → -6.51
- blend -5.72  (dispersion 5.73)

## 4. Assembly
- anchor -5.72  class +0.00  k×resid -3.40 (k=0.35, cap ±6.0)  ST -0.76  → recentered (-0.52) → **-9.36**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×4) = ±6.72

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (7b07c22)