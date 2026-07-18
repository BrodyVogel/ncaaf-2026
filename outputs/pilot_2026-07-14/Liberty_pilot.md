# Liberty — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-6.49** (rank 92/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    44 | proxy 22
- RB    42 | proxy —
- WRTE  42 | proxy —
- OL    48 | proxy 38
- DL    42 | proxy 14
- LB    44 | proxy 2
- DB    42 | proxy 26
- ST    38 | proxy 24

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +24.39 vs anchor off +24.30
- grade-implied def +27.08 vs anchor def +32.90  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+5.91**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +4.65 (=-0.541x anchor margin) + shape +1.26 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -6.4 → -6.4 → -6.4
- FEI      -0.41 → -8.57 → -8.57
- Massey   6.91 → -13.32 → -13.32
- FPI      -7.7 → -9.45 → -9.45
- TR       -8.5 → -8.62 → -8.62
- blend -8.79  (dispersion 6.92)

## 4. Assembly
- anchor -8.79  class +0.00  k×resid +2.07 (k=0.35, cap ±6.0)  ST -0.24  → recentered (-0.47) → **-6.49**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T18:20:00Z (Liberty); post-freeze name corrections 2026-07-18 (see planned_vs_final_deviations)