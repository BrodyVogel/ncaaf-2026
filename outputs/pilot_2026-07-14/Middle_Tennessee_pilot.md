# Middle Tennessee — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-14.89** (rank 126/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    50 | proxy 60
- RB    40 | proxy —
- WRTE  42 | proxy 9
- OL    30 | proxy 9
- DL    36 | proxy 33
- LB    44 | proxy —
- DB    42 | proxy 2
- ST    40 | proxy 5

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.075 RB:+0.094 WRTE:+0.034 OL:+0.079  (R²=0.54)
- def: DL:-0.084 LB:-0.062 DB:-0.092  (R²=0.61)
- grade-implied off +23.26 vs anchor off +16.15
- grade-implied def +27.52 vs anchor def +37.45  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+17.04**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +11.52 (=-0.541x anchor margin) + shape +5.52 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -26.0 → -26.0 → -24.47  [WINSORIZED]
- FEI      -0.86 → -18.27 → -18.27
- Massey   6.57 → -19.69 → -19.69
- FPI      -16.1 → -19.24 → -19.24
- TR       -20.9 → -20.49 → -20.49
- blend -21.1  (dispersion 7.73)

## 4. Assembly
- anchor -21.10  class +0.00  k×resid +5.96 (k=0.35, cap ±6.0)  ST -0.20  → recentered (-0.44) → **-14.89**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T19:10:00Z (Middle Tennessee)