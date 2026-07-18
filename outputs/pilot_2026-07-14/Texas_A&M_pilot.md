# Texas A&M — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+14.56** (rank 18/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    58 | proxy 61
- RB    54 | proxy 88
- WRTE  58 | proxy 75
- OL    52 | proxy 84
- DL    56 | proxy 70
- LB    52 | proxy 90
- DB    58 | proxy 75
- ST    56 | proxy 88

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.091 WRTE:+0.037 OL:+0.081  (R²=0.53)
- def: DL:-0.083 LB:-0.058 DB:-0.096  (R²=0.61)
- grade-implied off +27.40 vs anchor off +36.98
- grade-implied def +23.92 vs anchor def +17.02  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-16.48**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -10.80 (=-0.541x anchor margin) + shape -5.68 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      20.3 → 20.3 → 20.3
- FEI      0.85 → 18.6 → 18.6
- Massey   8.49 → 16.3 → 16.3
- FPI      20.0 → 22.81 → 22.81
- TR       22.7 → 21.24 → 21.24
- PickSix  13 → 18.1 → 18.1
- blend 19.67  (dispersion 6.51)

## 4. Assembly
- anchor +19.67  class -0.00  k×resid -5.77 (k=0.35, cap ±6.0)  ST +0.12  → recentered (-0.54) → **+14.56**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T05:34:00Z (Texas A&M)