# New Mexico State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-13.08** (rank 120/138 in hybrid field)  band ±6.72

## 1. Unit grades (LLM real | shadow proxy)
- QB    40 | proxy 10
- RB    38 | proxy —
- WRTE  42 | proxy 6
- OL    34 | proxy 15
- DL    40 | proxy 6
- LB    38 | proxy 26
- DB    44 | proxy 12
- ST    46 | proxy 84

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.093 WRTE:+0.036 OL:+0.082  (R²=0.53)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +22.62 vs anchor off +16.13
- grade-implied def +27.40 vs anchor def +34.27  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+13.36**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +9.81 (=-0.541x anchor margin) + shape +3.55 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -16.4 → -16.4 → -16.4
- FEI      -0.89 → -18.92 → -18.92
- Massey   6.54 → -20.26 → -20.26
- FPI      -15.7 → -18.77 → -18.77
- TR       -18.4 → -18.1 → -18.1
- blend -18.14  (dispersion 3.86)

## 4. Assembly
- anchor -18.14  class +0.00  k×resid +4.68 (k=0.35, cap ±6.0)  ST -0.08  → recentered (-0.46) → **-13.08**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×4) = ±6.72

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T20:20:00Z (New Mexico State)