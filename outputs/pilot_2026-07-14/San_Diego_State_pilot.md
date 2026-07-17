# San Diego State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-1.48** (rank 72/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    34 | proxy 16
- RB    52 | proxy 37
- WRTE  42 | proxy 48
- OL    40 | proxy 5
- DL    44 | proxy 39
- LB    42 | proxy —
- DB    34 | proxy 48
- ST    36 | proxy 58

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.092 WRTE:+0.035 OL:+0.084  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.62)
- grade-implied off +23.89 vs anchor off +23.34
- grade-implied def +27.81 vs anchor def +24.76  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-2.50**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +0.77 (=-0.541x anchor margin) + shape -3.27 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.3 → -1.3 → -1.3
- FEI      -0.06 → -1.02 → -1.02
- Massey   7.46 → -3.01 → -3.01
- FPI      1.4 → 1.15 → 1.15
- TR       1.1 → 0.57 → 0.57
- blend -0.82  (dispersion 4.15)

## 4. Assembly
- anchor -0.82  class +0.00  k×resid -0.88 (k=0.35, cap ±6.0)  ST -0.28  → recentered (-0.50) → **-1.48**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (df956b8)