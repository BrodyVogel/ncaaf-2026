# UNLV — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-4.59** (rank 86/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    36 | proxy 57
- RB    30 | proxy 49
- WRTE  16 | proxy 12
- OL    20 | proxy 16
- DL    18 | proxy 33
- LB    16 | proxy 27
- DB    20 | proxy 26
- ST    20 | proxy 40

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.068 RB:+0.090 WRTE:+0.041 OL:+0.085  (R²=0.55)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +19.29 vs anchor off +29.98
- grade-implied def +32.85 vs anchor def +29.62  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-13.93**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -0.19 (=-0.541x anchor margin) + shape -13.73 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      2.8 → 2.8 → 2.8
- FEI      -0.12 → -2.32 → -2.32
- Massey   7.54 → -1.51 → -1.51
- FPI      1.8 → 1.61 → 1.61
- TR       -0.8 → -1.25 → -1.25
- blend 0.36  (dispersion 5.12)

## 4. Assembly
- anchor +0.36  class +0.00  k×resid -4.87 (k=0.35, cap ±6.0)  ST -0.60  → recentered (-0.53) → **-4.59**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (779046e)