# Western Kentucky — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-4.14** (rank 86/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 15
- RB    46 | proxy 15
- WRTE  48 | proxy 53
- OL    42 | proxy 12
- DL    44 | proxy 1
- LB    36 | proxy —
- DB    50 | proxy 63
- ST    48 | proxy 85

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.075 RB:+0.096 WRTE:+0.033 OL:+0.084  (R²=0.55)
- def: DL:-0.080 LB:-0.060 DB:-0.098  (R²=0.61)
- grade-implied off +25.00 vs anchor off +24.61
- grade-implied def +26.59 vs anchor def +31.59  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+5.39**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +3.78 (=-0.541x anchor margin) + shape +1.61 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.3 → -5.3 → -5.3
- FEI      -0.3 → -6.2 → -6.2
- Massey   7.23 → -7.32 → -7.32
- FPI      -4.9 → -6.19 → -6.19
- TR       -8.4 → -8.52 → -8.52
- blend -6.47  (dispersion 3.22)

## 4. Assembly
- anchor -6.47  class +0.00  k×resid +1.89 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.48) → **-4.14**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T21:20:00Z (Western Kentucky)