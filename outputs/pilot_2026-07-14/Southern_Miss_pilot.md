# Southern Miss — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-11.95** (rank 114/138 in hybrid field)  band ±8.13

## 1. Unit grades (LLM real | shadow proxy)
- QB    42 | proxy —
- RB    40 | proxy 15
- WRTE  44 | proxy —
- OL    40 | proxy —
- DL    42 | proxy —
- LB    40 | proxy 34
- DB    44 | proxy —
- ST    42 | proxy 63

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.090 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.085 LB:-0.056 DB:-0.097  (R²=0.62)
- grade-implied off +23.54 vs anchor off +19.70
- grade-implied def +27.03 vs anchor def +35.90  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+12.70**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +8.76 (=-0.541x anchor margin) + shape +3.94 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -23.3 → -23.3 → -20.27  [WINSORIZED]
- FEI      -0.69 → -14.61 → -14.61
- Massey   6.77 → -15.94 → -15.94
- FPI      -5.1 → -6.43 → -11.68  [WINSORIZED]
- TR       -17.7 → -17.43 → -17.43
- blend -16.7  (dispersion 16.87, FLAGGED

## 4. Assembly
- anchor -16.70  class +0.00  k×resid +4.45 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.46) → **-11.95**
- band: 6.0 × coach(1.13) × dispersion(1.10) × conf(1+0.03×3) = ±8.13

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T16:30:00Z (Southern Miss)