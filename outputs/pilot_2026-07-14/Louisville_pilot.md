# Louisville — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+9.41** (rank 29/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy —
- RB    72 | proxy —
- WRTE  48 | proxy 75
- OL    50 | proxy 54
- DL    62 | proxy 90
- LB    50 | proxy —
- DB    52 | proxy 63
- ST    44 | proxy 47

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.093 WRTE:+0.035 OL:+0.082  (R²=0.54)
- def: DL:-0.082 LB:-0.060 DB:-0.096  (R²=0.61)
- grade-implied off +27.68 vs anchor off +31.06
- grade-implied def +24.13 vs anchor def +19.24  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-8.27**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -6.39 (=-0.541x anchor margin) + shape -1.87 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      11.0 → 11.0 → 11.0
- FEI      0.5 → 11.05 → 11.05
- Massey   8.3 → 12.74 → 12.74
- FPI      9.5 → 10.58 → 10.58
- TR       13.7 → 12.63 → 12.63
- PickSix  19 → 14.36 → 14.36
- blend 11.91  (dispersion 3.78)

## 4. Assembly
- anchor +11.91  class -0.00  k×resid -2.89 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.51) → **+9.41**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (7ef9e64)