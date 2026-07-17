# Georgia Tech — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+4.66** (rank 49/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy —
- RB    66 | proxy 66
- WRTE  38 | proxy 12
- OL    48 | proxy —
- DL    40 | proxy 33
- LB    50 | proxy —
- DB    48 | proxy 67
- ST    62 | proxy 85

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.091 WRTE:+0.039 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.095  (R²=0.61)
- grade-implied off +26.55 vs anchor off +28.59
- grade-implied def +26.33 vs anchor def +23.61  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-4.75**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -2.69 (=-0.541x anchor margin) + shape -2.06 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.0 → 6.0 → 6.0
- FEI      0.2 → 4.58 → 4.58
- Massey   8.01 → 7.31 → 7.31
- FPI      4.2 → 4.41 → 4.41
- TR       5.8 → 5.07 → 5.07
- PickSix  40 → 5.71 → 5.71
- blend 5.58  (dispersion 2.9)

## 4. Assembly
- anchor +5.58  class -0.00  k×resid -1.66 (k=0.35, cap ±6.0)  ST +0.24  → recentered (-0.51) → **+4.66**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (b5ffbfc)