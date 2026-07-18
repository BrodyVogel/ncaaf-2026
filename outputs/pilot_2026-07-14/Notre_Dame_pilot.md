# Notre Dame — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+23.57** (rank 5/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    86 | proxy 95
- RB    66 | proxy 90
- WRTE  74 | proxy —
- OL    78 | proxy 95
- DL    80 | proxy 90
- LB    76 | proxy 94
- DB    80 | proxy 91
- ST    62 | proxy 82

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.069 RB:+0.090 WRTE:+0.039 OL:+0.080  (R²=0.52)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +33.11 vs anchor off +40.84
- grade-implied def +18.42 vs anchor def +13.96  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-12.19**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -14.54 (=-0.541x anchor margin) + shape +2.35 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      25.8 → 25.8 → 25.8
- FEI      1.29 → 28.09 → 28.09
- Massey   9.02 → 26.24 → 26.24
- FPI      25.9 → 29.69 → 29.69
- TR       29.1 → 27.37 → 27.37
- PickSix  4 → 26.51 → 26.51
- blend 27.07  (dispersion 3.89)

## 4. Assembly
- anchor +27.07  class -0.00  k×resid -4.27 (k=0.35, cap ±6.0)  ST +0.24  → recentered (-0.52) → **+23.57**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T21:50:00Z (Notre Dame)