# LSU — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+14.77** (rank 18/138 in hybrid field)  band ±7.46

## 1. Unit grades (LLM real | shadow proxy)
- QB    60 | proxy 78
- RB    56 | proxy 34
- WRTE  60 | proxy 85
- OL    56 | proxy 69
- DL    62 | proxy 79
- LB    54 | proxy 68
- DB    62 | proxy 64
- ST    54 | proxy 52

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.094 WRTE:+0.036 OL:+0.082  (R²=0.54)
- def: DL:-0.080 LB:-0.059 DB:-0.097  (R²=0.61)
- grade-implied off +28.12 vs anchor off +31.86
- grade-implied def +23.00 vs anchor def +13.14  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-13.60**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -10.13 (=-0.541x anchor margin) + shape -3.47 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      20.2 → 20.2 → 20.2
- FEI      0.55 → 12.13 → 15.2  [WINSORIZED]
- Massey   8.29 → 12.56 → 15.2  [WINSORIZED]
- FPI      20.0 → 22.81 → 22.81
- TR       22.1 → 20.67 → 20.67
- PickSix  12 → 18.21 → 18.21
- blend 18.93  (dispersion 10.68, FLAGGED

## 4. Assembly
- anchor +18.93  class -0.00  k×resid -4.76 (k=0.35, cap ±6.0)  ST +0.08  → recentered (-0.52) → **+14.77**
- band: 6.0 × coach(1.13) × dispersion(1.10) × conf(1+0.03×0) = ±7.46

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T04:00:26Z (ea9e814)