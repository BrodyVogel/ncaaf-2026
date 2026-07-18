# Sam Houston — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-17.40** (rank 135/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    38 | proxy 0
- RB    46 | proxy —
- WRTE  42 | proxy 4
- OL    32 | proxy 16
- DL    40 | proxy 1
- LB    36 | proxy 2
- DB    40 | proxy 2
- ST    42 | proxy 65

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.093 WRTE:+0.036 OL:+0.082  (R²=0.53)
- def: DL:-0.083 LB:-0.058 DB:-0.096  (R²=0.61)
- grade-implied off +23.07 vs anchor off +15.41
- grade-implied def +27.88 vs anchor def +38.69  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+18.46**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +12.59 (=-0.541x anchor margin) + shape +5.87 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -26.3 → -26.3 → -26.3
- FEI      -1.02 → -21.72 → -21.72
- Massey   6.43 → -22.32 → -22.32
- FPI      -18.4 → -21.92 → -21.92
- TR       -24.1 → -23.55 → -23.55
- blend -23.69  (dispersion 4.58)

## 4. Assembly
- anchor -23.69  class +0.00  k×resid +6.00 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.45) → **-17.40**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T20:50:00Z (Sam Houston)