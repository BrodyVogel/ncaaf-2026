# Wyoming — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-13.59** (rank 121/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    20 | proxy —
- RB    18 | proxy 31
- WRTE  12 | proxy —
- OL    18 | proxy 9
- DL    14 | proxy 27
- LB    16 | proxy —
- DB    16 | proxy 12
- ST    16 | proxy 6

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.091 WRTE:+0.038 OL:+0.079  (R²=0.54)
- def: DL:-0.084 LB:-0.057 DB:-0.098  (R²=0.62)
- grade-implied off +16.98 vs anchor off +15.13
- grade-implied def +33.62 vs anchor def +25.87  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-5.90**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +5.81 (=-0.541x anchor margin) + shape -11.71 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -9.6 → -9.6 → -9.6
- FEI      -0.5 → -10.51 → -10.51
- Massey   7.09 → -9.94 → -9.94
- FPI      -13.1 → -15.75 → -15.23  [WINSORIZED]
- TR       -13.3 → -13.21 → -13.21
- blend -11.35  (dispersion 6.15)

## 4. Assembly
- anchor -11.35  class +0.00  k×resid -2.06 (k=0.35, cap ±6.0)  ST -0.68  → recentered (-0.50) → **-13.59**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (53d85f6)