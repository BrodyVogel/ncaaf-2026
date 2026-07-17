# Boise State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+1.60** (rank 60/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    32 | proxy 12
- RB    50 | proxy 40
- WRTE  14 | proxy 4
- OL    20 | proxy 17
- DL    50 | proxy 43
- LB    30 | proxy 31
- DB    46 | proxy 58
- ST    44 | proxy 60

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.076 RB:+0.090 WRTE:+0.042 OL:+0.083  (R²=0.56)
- def: DL:-0.083 LB:-0.060 DB:-0.095  (R²=0.62)
- grade-implied off +20.60 vs anchor off +29.20
- grade-implied def +26.90 vs anchor def +23.50  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-12.00**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -3.08 (=-0.541x anchor margin) + shape -8.91 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.8 → 6.8 → 6.8
- FEI      0.19 → 4.37 → 4.37
- Massey   7.85 → 4.31 → 4.31
- FPI      4.0 → 4.18 → 4.18
- TR       6.7 → 5.93 → 5.93
- blend 5.4  (dispersion 2.62)

## 4. Assembly
- anchor +5.40  class +0.00  k×resid -4.20 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.52) → **+1.60**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (958082e)