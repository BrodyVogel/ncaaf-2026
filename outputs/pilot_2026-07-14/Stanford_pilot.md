# Stanford — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-1.91** (rank 73/138 in hybrid field)  band ±7.39

## 1. Unit grades (LLM real | shadow proxy)
- QB    42 | proxy —
- RB    56 | proxy 88
- WRTE  44 | proxy —
- OL    40 | proxy 31
- DL    44 | proxy 54
- LB    54 | proxy 61
- DB    50 | proxy 62
- ST    52 | proxy 74

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.097 WRTE:+0.036 OL:+0.080  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +25.04 vs anchor off +22.06
- grade-implied def +25.54 vs anchor def +24.64  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+2.08**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +1.40 (=-0.541x anchor margin) + shape +0.69 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.9 → -1.9 → -1.9
- FEI      -0.24 → -4.9 → -4.9
- Massey   7.43 → -3.57 → -3.57
- FPI      -3.3 → -4.33 → -4.33
- TR       -3.0 → -3.36 → -3.36
- PickSix  66 → -2.25 → -2.25
- blend -3.17  (dispersion 3.0)

## 4. Assembly
- anchor -3.17  class -0.00  k×resid +0.73 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.49) → **-1.91**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×3) = ±7.39

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (456ef48)