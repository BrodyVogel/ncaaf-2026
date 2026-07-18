# Marshall — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-5.70** (rank 91/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    50 | proxy 53
- RB    40 | proxy —
- WRTE  46 | proxy 35
- OL    44 | proxy 43
- DL    40 | proxy —
- LB    42 | proxy 22
- DB    42 | proxy 12
- ST    36 | proxy 24

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.038 OL:+0.082  (R²=0.54)
- def: DL:-0.086 LB:-0.057 DB:-0.094  (R²=0.61)
- grade-implied off +24.44 vs anchor off +27.85
- grade-implied def +27.31 vs anchor def +35.85  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+5.13**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +4.33 (=-0.541x anchor margin) + shape +0.80 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -6.4 → -6.4 → -6.4
- FEI      -0.3 → -6.2 → -6.2
- Massey   7.22 → -7.51 → -7.51
- FPI      -8.8 → -10.74 → -10.74
- TR       -8.8 → -8.91 → -8.91
- blend -7.69  (dispersion 4.54)

## 4. Assembly
- anchor -7.69  class +0.00  k×resid +1.80 (k=0.35, cap ±6.0)  ST -0.28  → recentered (-0.48) → **-5.70**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T15:52:00Z (Marshall)