# North Carolina — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+1.84** (rank 58/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy —
- RB    50 | proxy 42
- WRTE  48 | proxy 80
- OL    44 | proxy —
- DL    54 | proxy 80
- LB    40 | proxy —
- DB    54 | proxy 65
- ST    46 | proxy 47

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.091 WRTE:+0.038 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +25.34 vs anchor off +23.53
- grade-implied def +25.15 vs anchor def +22.07  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-1.27**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -0.79 (=-0.541x anchor margin) + shape -0.48 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.8 → 3.8 → 3.8
- FEI      -0.23 → -4.69 → -2.66  [WINSORIZED]
- Massey   7.57 → -0.94 → -0.94
- FPI      4.9 → 5.22 → 5.22
- TR       2.1 → 1.53 → 1.53
- PickSix  57 → 2.34 → 2.34
- blend 1.87  (dispersion 9.91)

## 4. Assembly
- anchor +1.87  class -0.00  k×resid -0.45 (k=0.35, cap ±6.0)  ST -0.08  → recentered (-0.49) → **+1.84**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (2c6d867)