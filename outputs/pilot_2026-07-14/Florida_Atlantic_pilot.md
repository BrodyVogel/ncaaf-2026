# Florida Atlantic — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-9.51** (rank 104/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    55 | proxy 57
- RB    40 | proxy —
- WRTE  50 | proxy 54
- OL    33 | proxy 44
- DL    28 | proxy 14
- LB    20 | proxy 5
- DB    15 | proxy 2
- ST    50 | proxy 45

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +24.08 vs anchor off +25.10
- grade-implied def +32.22 vs anchor def +37.00  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+3.76**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +6.44 (=-0.541x anchor margin) + shape -2.68 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.1 → -7.1 → -8.7  [WINSORIZED]
- FEI      -0.65 → -13.74 → -13.74
- Massey   6.86 → -14.26 → -14.26
- FPI      -11.3 → -13.65 → -13.65
- TR       -8.7 → -8.81 → -8.81
- blend -11.31  (dispersion 7.16)

## 4. Assembly
- anchor -11.31  class +0.00  k×resid +1.32 (k=0.35, cap ±6.0)  ST +0.00  → recentered (-0.48) → **-9.51**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15