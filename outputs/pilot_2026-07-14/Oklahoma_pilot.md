# Oklahoma — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+14.73** (rank 18/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    62 | proxy 49
- RB    52 | proxy 44
- WRTE  58 | proxy 76
- OL    54 | proxy 78
- DL    62 | proxy 84
- LB    56 | proxy 92
- DB    60 | proxy 94
- ST    62 | proxy 67

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.094 WRTE:+0.036 OL:+0.080  (R²=0.54)
- def: DL:-0.083 LB:-0.058 DB:-0.096  (R²=0.61)
- grade-implied off +27.65 vs anchor off +32.41
- grade-implied def +23.00 vs anchor def +13.89  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-13.87**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -10.02 (=-0.541x anchor margin) + shape -3.85 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      17.2 → 17.2 → 17.2
- FEI      0.8 → 17.52 → 17.52
- Massey   8.5 → 16.49 → 16.49
- FPI      17.8 → 20.25 → 20.25
- TR       22.0 → 20.57 → 20.57
- PickSix  6 → 24.07 → 22.52  [WINSORIZED]
- blend 18.82  (dispersion 7.58)

## 4. Assembly
- anchor +18.82  class -0.00  k×resid -4.86 (k=0.35, cap ±6.0)  ST +0.24  → recentered (-0.53) → **+14.73**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T04:27:58Z (087d8c0)