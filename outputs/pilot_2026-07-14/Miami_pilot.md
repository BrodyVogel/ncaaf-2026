# Miami — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+17.57** (rank 12/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    70 | proxy 84
- RB    70 | proxy 91
- WRTE  76 | proxy 97
- OL    52 | proxy 92
- DL    60 | proxy 89
- LB    46 | proxy —
- DB    60 | proxy 77
- ST    58 | proxy 62

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.093 WRTE:+0.038 OL:+0.083  (R²=0.53)
- def: DL:-0.079 LB:-0.062 DB:-0.095  (R²=0.61)
- grade-implied off +30.49 vs anchor off +35.03
- grade-implied def +23.87 vs anchor def +13.07  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-15.34**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -11.88 (=-0.541x anchor margin) + shape -3.46 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      21.0 → 21.0 → 21.0
- FEI      0.88 → 19.25 → 19.25
- Massey   8.68 → 19.87 → 19.87
- FPI      21.8 → 24.91 → 24.91
- TR       25.3 → 23.73 → 23.73
- PickSix  3 → 27.16 → 26.0  [WINSORIZED]
- blend 22.25  (dispersion 7.92)

## 4. Assembly
- anchor +22.25  class -0.00  k×resid -5.37 (k=0.35, cap ±6.0)  ST +0.16  → recentered (-0.53) → **+17.57**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (913011b)