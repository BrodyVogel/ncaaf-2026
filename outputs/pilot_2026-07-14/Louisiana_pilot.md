# Louisiana — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-6.62** (rank 94/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy 33
- RB    42 | proxy —
- WRTE  44 | proxy 29
- OL    48 | proxy 32
- DL    44 | proxy 0
- LB    40 | proxy —
- DB    54 | proxy 76
- ST    48 | proxy 51

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.075 LB:-0.060 DB:-0.102  (R²=0.62)
- grade-implied off +24.75 vs anchor off +24.75
- grade-implied def +25.90 vs anchor def +34.35  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+8.44**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +5.19 (=-0.541x anchor margin) + shape +3.25 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -9.1 → -9.1 → -9.1
- FEI      -0.46 → -9.65 → -9.65
- Massey   7.0 → -11.63 → -11.63
- FPI      -8.3 → -10.15 → -10.15
- TR       -10.3 → -10.34 → -10.34
- blend -10.0  (dispersion 2.53)

## 4. Assembly
- anchor -10.00  class +0.00  k×resid +2.96 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.47) → **-6.62**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T15:20:00Z (Louisiana)