# North Dakota State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-8.67** (rank 101/138 in hybrid field)  band ±7.19

## 1. Unit grades (LLM real | shadow proxy)
- QB    14 | proxy —
- RB    16 | proxy —
- WRTE  12 | proxy —
- OL    20 | proxy —
- DL    16 | proxy —
- LB    14 | proxy —
- DB    14 | proxy —
- ST    14 | proxy —

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.62)
- grade-implied off +16.47 vs anchor off +23.21
- grade-implied def +33.69 vs anchor def +26.99  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-13.44**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +2.04 (=-0.541x anchor margin) + shape -15.48 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.4 → -1.4 → -1.66  [WINSORIZED]
- FEI      -1.0 → -21.29 → -7.28  [WINSORIZED]
- Massey   7.62 → -0.01 → -1.66  [WINSORIZED]
- FPI      -8.3 → -10.15 → -7.28  [WINSORIZED]
- TR       -2.8 → -3.16 → -3.16
- blend -3.78  (dispersion 21.28, FLAGGED

## 4. Assembly
- anchor -3.78  class +0.00  k×resid -4.70 (k=0.35, cap ±6.0)  ST -0.72  → recentered (-0.53) → **-8.67**
- band: 6.0 × coach(1.0) × dispersion(1.10) × conf(1+0.03×3) = ±7.19

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (8344a65)