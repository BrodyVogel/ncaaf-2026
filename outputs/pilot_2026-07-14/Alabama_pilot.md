# Alabama — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+14.63** (rank 18/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy 92
- RB    48 | proxy —
- WRTE  54 | proxy 69
- OL    46 | proxy 98
- DL    46 | proxy 72
- LB    48 | proxy —
- DB    76 | proxy 100
- ST    48 | proxy 81

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.091 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.082 LB:-0.063 DB:-0.091  (R²=0.61)
- grade-implied off +25.53 vs anchor off +32.27
- grade-implied def +23.44 vs anchor def +11.63  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-18.55**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -11.17 (=-0.541x anchor margin) + shape -7.38 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      18.2 → 18.2 → 18.2
- FEI      1.07 → 23.34 → 23.34
- Massey   8.74 → 20.99 → 20.99
- FPI      20.1 → 22.93 → 22.93
- TR       21.6 → 20.19 → 20.19
- PickSix  16 → 17.06 → 17.06
- blend 20.13  (dispersion 6.28)

## 4. Assembly
- anchor +20.13  class -0.00  k×resid -6.00 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.54) → **+14.63**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T02:24:39Z