# Georgia — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+21.20** (rank 8/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    70 | proxy 88
- RB    70 | proxy 95
- WRTE  56 | proxy 81
- OL    60 | proxy 95
- DL    58 | proxy 81
- LB    62 | proxy 95
- DB    66 | proxy 78
- ST    60 | proxy 78

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.53)
- def: DL:-0.083 LB:-0.057 DB:-0.096  (R²=0.61)
- grade-implied off +30.32 vs anchor off +38.68
- grade-implied def +22.45 vs anchor def +12.82  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-17.99**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -13.99 (=-0.541x anchor margin) + shape -4.00 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      25.5 → 25.5 → 25.5
- FEI      1.34 → 29.16 → 29.16
- Massey   8.89 → 23.8 → 23.8
- FPI      24.8 → 28.41 → 28.41
- TR       28.4 → 26.7 → 26.7
- PickSix  5 → 26.13 → 26.13
- blend 26.46  (dispersion 5.36)

## 4. Assembly
- anchor +26.46  class -0.00  k×resid -6.00 (k=0.35, cap ±6.0)  ST +0.20  → recentered (-0.54) → **+21.20**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T03:39:34Z (31badf0)