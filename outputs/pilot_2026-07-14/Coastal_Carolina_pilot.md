# Coastal Carolina — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-9.77** (rank 105/138 in hybrid field)  band ±7.19

## 1. Unit grades (LLM real | shadow proxy)
- QB    38 | proxy —
- RB    46 | proxy 24
- WRTE  40 | proxy 29
- OL    36 | proxy 5
- DL    48 | proxy 33
- LB    50 | proxy —
- DB    44 | proxy 29
- ST    44 | proxy 16

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.093 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.083 LB:-0.061 DB:-0.095  (R²=0.62)
- grade-implied off +23.26 vs anchor off +21.09
- grade-implied def +25.98 vs anchor def +34.41  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+10.60**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +7.21 (=-0.541x anchor margin) + shape +3.39 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.8 → -13.8 → -13.8
- FEI      -0.58 → -12.23 → -12.23
- Massey   6.83 → -14.82 → -14.82
- FPI      -12.1 → -14.58 → -14.58
- TR       -13.8 → -13.69 → -13.69
- blend -13.82  (dispersion 2.58)

## 4. Assembly
- anchor -13.82  class +0.00  k×resid +3.71 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.46) → **-9.77**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×2) = ±7.19

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T14:42:00Z (Coastal Carolina)