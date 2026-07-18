# NC State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+3.50** (rank 53/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    54 | proxy 30
- RB    56 | proxy 68
- WRTE  42 | proxy 38
- OL    46 | proxy 47
- DL    40 | proxy 27
- LB    42 | proxy —
- DB    46 | proxy 22
- ST    48 | proxy 39

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.074 RB:+0.090 WRTE:+0.038 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.057 DB:-0.098  (R²=0.62)
- grade-implied off +26.20 vs anchor off +30.94
- grade-implied def +27.01 vs anchor def +25.06  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-6.69**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -3.18 (=-0.541x anchor margin) + shape -3.51 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      4.9 → 4.9 → 4.9
- FEI      0.33 → 7.39 → 7.39
- Massey   7.92 → 5.62 → 5.62
- FPI      3.7 → 3.83 → 3.83
- TR       6.2 → 5.45 → 5.45
- PickSix  41 → 5.57 → 5.57
- blend 5.38  (dispersion 3.56)

## 4. Assembly
- anchor +5.38  class -0.00  k×resid -2.34 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.51) → **+3.50**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (3e24366)