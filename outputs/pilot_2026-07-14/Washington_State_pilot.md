# Washington State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-4.12** (rank 85/138 in hybrid field)  band ±7.91

## 1. Unit grades (LLM real | shadow proxy)
- QB    28 | proxy —
- RB    42 | proxy —
- WRTE  44 | proxy —
- OL    26 | proxy 29
- DL    30 | proxy 39
- LB    28 | proxy —
- DB    32 | proxy 22
- ST    32 | proxy 29

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.081  (R²=0.54)
- def: DL:-0.083 LB:-0.058 DB:-0.098  (R²=0.62)
- grade-implied off +21.55 vs anchor off +21.57
- grade-implied def +30.02 vs anchor def +23.43  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-6.61**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +1.01 (=-0.541x anchor margin) + shape -7.62 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.3 → -5.3 → -4.14  [WINSORIZED]
- FEI      0.23 → 5.23 → 1.36  [WINSORIZED]
- Massey   7.82 → 3.74 → 1.36  [WINSORIZED]
- FPI      -4.1 → -5.26 → -4.14  [WINSORIZED]
- TR       -1.6 → -2.02 → -2.02
- blend -1.95  (dispersion 10.53, FLAGGED

## 4. Assembly
- anchor -1.95  class +0.00  k×resid -2.31 (k=0.35, cap ±6.0)  ST -0.36  → recentered (-0.51) → **-4.12**
- band: 6.0 × coach(1.13) × dispersion(1.10) × conf(1+0.03×2) = ±7.91

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (2490cde)