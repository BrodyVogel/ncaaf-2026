# UAB — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-13.84** (rank 123/138 in hybrid field)  band ±7.39

## 1. Unit grades (LLM real | shadow proxy)
- QB    42 | proxy 52
- RB    48 | proxy 27
- WRTE  38 | proxy —
- OL    45 | proxy 74
- DL    16 | proxy 13
- LB    25 | proxy 31
- DB    15 | proxy 5
- ST    55 | proxy 1

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.088 WRTE:+0.037 OL:+0.085  (R²=0.54)
- def: DL:-0.082 LB:-0.060 DB:-0.095  (R²=0.61)
- grade-implied off +24.47 vs anchor off +20.67
- grade-implied def +32.88 vs anchor def +37.53  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+8.45**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +9.12 (=-0.541x anchor margin) + shape -0.67 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -18.1 → -18.1 → -18.1
- FEI      -0.7 → -14.82 → -14.82
- Massey   6.73 → -16.69 → -16.69
- FPI      -15.5 → -18.54 → -18.54
- TR       -18.2 → -17.9 → -17.9
- blend -17.36  (dispersion 3.72)

## 4. Assembly
- anchor -17.36  class +0.00  k×resid +2.96 (k=0.35, cap ±6.0)  ST +0.10  → recentered (-0.46) → **-13.84**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×3) = ±7.39

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15