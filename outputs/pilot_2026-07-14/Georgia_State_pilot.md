# Georgia State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-14.29** (rank 123/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy —
- RB    40 | proxy —
- WRTE  42 | proxy —
- OL    40 | proxy —
- DL    40 | proxy —
- LB    38 | proxy —
- DB    40 | proxy —
- ST    40 | proxy 30

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.63)
- grade-implied off +23.90 vs anchor off +19.57
- grade-implied def +27.69 vs anchor def +38.83  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+15.46**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +10.42 (=-0.541x anchor margin) + shape +5.04 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -25.1 → -25.1 → -23.47  [WINSORIZED]
- FEI      -0.79 → -16.76 → -16.76
- Massey   6.62 → -18.76 → -18.76
- FPI      -15.2 → -18.19 → -18.19
- TR       -19.4 → -19.05 → -19.05
- blend -19.95  (dispersion 8.34)

## 4. Assembly
- anchor -19.95  class +0.00  k×resid +5.41 (k=0.35, cap ±6.0)  ST -0.20  → recentered (-0.44) → **-14.29**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T15:00:00Z (Georgia State)