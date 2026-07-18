# Florida — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+9.89** (rank 29/138 in hybrid field)  band ±7.19

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy —
- RB    60 | proxy 88
- WRTE  50 | proxy 57
- OL    44 | proxy 40
- DL    54 | proxy 58
- LB    56 | proxy 74
- DB    50 | proxy 75
- ST    56 | proxy 36

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.058 DB:-0.095  (R²=0.61)
- grade-implied off +26.31 vs anchor off +29.26
- grade-implied def +24.64 vs anchor def +16.84  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-10.75**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -6.72 (=-0.541x anchor margin) + shape -4.03 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      14.9 → 14.9 → 14.9
- FEI      0.36 → 8.03 → 9.9  [WINSORIZED]
- Massey   8.12 → 9.37 → 9.9  [WINSORIZED]
- FPI      13.6 → 15.36 → 15.36
- TR       17.4 → 16.17 → 15.58  [WINSORIZED]
- PickSix  29 → 10.58 → 10.58
- blend 13.02  (dispersion 8.14)

## 4. Assembly
- anchor +13.02  class -0.00  k×resid -3.76 (k=0.35, cap ±6.0)  ST +0.12  → recentered (-0.51) → **+9.89**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×2) = ±7.19

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T03:04:34Z (2443754)