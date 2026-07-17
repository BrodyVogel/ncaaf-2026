# Boston College — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-2.15** (rank 75/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    40 | proxy —
- RB    50 | proxy 45
- WRTE  42 | proxy 13
- OL    46 | proxy 44
- DL    40 | proxy 33
- LB    42 | proxy 58
- DB    48 | proxy 19
- ST    52 | proxy 70

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +24.68 vs anchor off +24.52
- grade-implied def +26.79 vs anchor def +28.28  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+1.65**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +2.03 (=-0.541x anchor margin) + shape -0.39 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.5 → -1.5 → -1.5
- FEI      -0.22 → -4.47 → -4.47
- Massey   7.51 → -2.07 → -2.07
- FPI      -2.7 → -3.63 → -3.63
- TR       -6.2 → -6.42 → -6.42
- PickSix  67 → -3.26 → -3.26
- blend -3.26  (dispersion 4.92)

## 4. Assembly
- anchor -3.26  class -0.00  k×resid +0.58 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.49) → **-2.15**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (e5b9dbc)