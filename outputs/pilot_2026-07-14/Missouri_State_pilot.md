# Missouri State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-11.55** (rank 115/138 in hybrid field)  band ±7.19

## 1. Unit grades (LLM real | shadow proxy)
- QB    42 | proxy 16
- RB    44 | proxy —
- WRTE  46 | proxy 30
- OL    36 | proxy —
- DL    42 | proxy 3
- LB    44 | proxy 19
- DB    42 | proxy 0
- ST    44 | proxy 1

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.069 RB:+0.092 WRTE:+0.036 OL:+0.084  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.097  (R²=0.61)
- grade-implied off +23.64 vs anchor off +17.98
- grade-implied def +27.10 vs anchor def +33.62  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+12.18**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +8.46 (=-0.541x anchor margin) + shape +3.72 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -18.7 → -18.7 → -18.7
- FEI      -0.6 → -12.67 → -12.67
- Massey   6.78 → -15.76 → -15.76
- FPI      -10.3 → -12.48 → -12.48
- TR       -18.9 → -18.57 → -18.57
- blend -16.15  (dispersion 6.22)

## 4. Assembly
- anchor -16.15  class +0.00  k×resid +4.26 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.45) → **-11.55**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×2) = ±7.19

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T19:45:00Z (Missouri State)