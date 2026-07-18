# Ole Miss — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+15.40** (rank 16/138 in hybrid field)  band ±6.78

## 1. Unit grades (LLM real | shadow proxy)
- QB    70 | proxy —
- RB    68 | proxy 95
- WRTE  56 | proxy 43
- OL    54 | proxy 81
- DL    60 | proxy 85
- LB    58 | proxy 43
- DB    56 | proxy 67
- ST    62 | proxy 87

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.089 WRTE:+0.039 OL:+0.080  (R²=0.53)
- def: DL:-0.081 LB:-0.061 DB:-0.096  (R²=0.61)
- grade-implied off +29.61 vs anchor off +36.48
- grade-implied def +23.45 vs anchor def +18.22  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-12.10**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -9.88 (=-0.541x anchor margin) + shape -2.22 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      15.9 → 15.9 → 15.9
- FEI      0.93 → 20.32 → 20.32
- Massey   8.74 → 20.99 → 20.99
- FPI      16.0 → 18.16 → 18.16
- TR       22.3 → 20.86 → 20.86
- PickSix  10 → 19.93 → 19.93
- blend 18.87  (dispersion 5.09)

## 4. Assembly
- anchor +18.87  class -0.00  k×resid -4.24 (k=0.35, cap ±6.0)  ST +0.24  → recentered (-0.52) → **+15.40**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×0) = ±6.78

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T04:37:20Z (5e5111f)