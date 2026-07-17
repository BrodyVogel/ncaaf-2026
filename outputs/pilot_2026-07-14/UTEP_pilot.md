# UTEP — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-20.09** (rank 136/138 in hybrid field)  band ±6.72

## 1. Unit grades (LLM real | shadow proxy)
- QB    16 | proxy —
- RB    12 | proxy —
- WRTE  12 | proxy —
- OL     8 | proxy —
- DL    10 | proxy 9
- LB    14 | proxy 39
- DB    14 | proxy 11
- ST    14 | proxy 27

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.091 WRTE:+0.037 OL:+0.083  (R²=0.55)
- def: DL:-0.083 LB:-0.060 DB:-0.096  (R²=0.61)
- grade-implied off +15.32 vs anchor off +14.89
- grade-implied def +34.17 vs anchor def +34.51  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+0.76**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +10.61 (=-0.541x anchor margin) + shape -9.85 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -20.5 → -20.5 → -20.5
- FEI      -0.89 → -18.92 → -18.92
- Massey   6.53 → -20.44 → -20.44
- FPI      -16.6 → -19.82 → -19.82
- TR       -21.0 → -20.58 → -20.58
- blend -20.13  (dispersion 1.67)

## 4. Assembly
- anchor -20.13  class +0.00  k×resid +0.27 (k=0.35, cap ±6.0)  ST -0.72  → recentered (-0.49) → **-20.09**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×4) = ±6.72

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (c045330)