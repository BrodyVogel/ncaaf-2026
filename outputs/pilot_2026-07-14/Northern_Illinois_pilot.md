# Northern Illinois — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-17.92** (rank 134/138 in hybrid field)  band ±7.39

## 1. Unit grades (LLM real | shadow proxy)
- QB    18 | proxy 0
- RB    12 | proxy 2
- WRTE  16 | proxy —
- OL    12 | proxy 16
- DL    10 | proxy —
- LB    10 | proxy —
- DB    12 | proxy —
- ST    18 | proxy 33

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.091 WRTE:+0.037 OL:+0.082  (R²=0.53)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.62)
- grade-implied off +15.90 vs anchor off +14.32
- grade-implied def +34.60 vs anchor def +31.28  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-1.73**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +9.18 (=-0.541x anchor margin) + shape -10.91 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -18.2 → -18.2 → -18.2
- FEI      -0.68 → -14.39 → -14.39
- Massey   6.84 → -14.63 → -14.63
- FPI      -14.5 → -17.38 → -17.38
- TR       -20.6 → -20.2 → -20.2
- blend -17.17  (dispersion 5.81)

## 4. Assembly
- anchor -17.17  class +0.00  k×resid -0.61 (k=0.35, cap ±6.0)  ST -0.64  → recentered (-0.50) → **-17.92**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×3) = ±7.39

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (f400d06)