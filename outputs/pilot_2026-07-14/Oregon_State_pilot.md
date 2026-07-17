# Oregon State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-7.37** (rank 94/138 in hybrid field)  band ±7.19

## 1. Unit grades (LLM real | shadow proxy)
- QB    34 | proxy 36
- RB    32 | proxy —
- WRTE  26 | proxy 4
- OL    24 | proxy 33
- DL    42 | proxy 60
- LB    44 | proxy 93
- DB    42 | proxy 22
- ST    38 | proxy 0

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.036 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.062 DB:-0.094  (R²=0.62)
- grade-implied off +20.23 vs anchor off +20.21
- grade-implied def +27.06 vs anchor def +27.19  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+0.15**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +3.78 (=-0.541x anchor margin) + shape -3.62 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -6.3 → -6.3 → -6.3
- FEI      -0.37 → -7.71 → -7.71
- Massey   7.31 → -5.82 → -5.82
- FPI      -8.1 → -9.92 → -9.92
- TR       -10.0 → -10.06 → -10.06
- blend -7.68  (dispersion 4.24)

## 4. Assembly
- anchor -7.68  class +0.00  k×resid +0.05 (k=0.35, cap ±6.0)  ST -0.24  → recentered (-0.49) → **-7.37**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×2) = ±7.19

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (7ac7d37)