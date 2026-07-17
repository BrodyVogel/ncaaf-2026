# Wake Forest — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+2.98** (rank 54/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    54 | proxy 58
- RB    46 | proxy —
- WRTE  46 | proxy 26
- OL    44 | proxy 53
- DL    58 | proxy 57
- LB    48 | proxy 25
- DB    50 | proxy 46
- ST    54 | proxy 93

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.036 OL:+0.083  (R²=0.54)
- def: DL:-0.081 LB:-0.063 DB:-0.096  (R²=0.62)
- grade-implied off +25.32 vs anchor off +24.07
- grade-implied def +24.82 vs anchor def +20.83  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-2.73**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -1.75 (=-0.541x anchor margin) + shape -0.98 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.6 → 3.6 → 3.6
- FEI      0.19 → 4.37 → 4.37
- Massey   7.78 → 2.99 → 2.99
- FPI      3.4 → 3.48 → 3.48
- TR       2.4 → 1.81 → 1.81
- PickSix  53 → 3.59 → 3.59
- blend 3.35  (dispersion 2.56)

## 4. Assembly
- anchor +3.35  class -0.00  k×resid -0.96 (k=0.35, cap ±6.0)  ST +0.08  → recentered (-0.50) → **+2.98**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (f4e0779)