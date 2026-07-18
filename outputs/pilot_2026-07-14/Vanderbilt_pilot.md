# Vanderbilt — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+7.90** (rank 35/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy —
- RB    58 | proxy 81
- WRTE  50 | proxy 96
- OL    46 | proxy 56
- DL    50 | proxy 59
- LB    50 | proxy 85
- DB    58 | proxy 75
- ST    60 | proxy 90

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.091 WRTE:+0.036 OL:+0.083  (R²=0.53)
- def: DL:-0.082 LB:-0.061 DB:-0.096  (R²=0.62)
- grade-implied off +26.13 vs anchor off +33.29
- grade-implied def +24.49 vs anchor def +24.21  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-7.44**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -4.91 (=-0.541x anchor margin) + shape -2.53 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      10.0 → 10.0 → 10.0
- FEI      0.59 → 12.99 → 12.99
- Massey   8.24 → 11.62 → 11.62
- FPI      9.0 → 10.0 → 10.0
- TR       9.8 → 8.9 → 8.9
- PickSix  46 → 4.85 → 5.0  [WINSORIZED]
- blend 9.79  (dispersion 8.15)

## 4. Assembly
- anchor +9.79  class -0.00  k×resid -2.60 (k=0.35, cap ±6.0)  ST +0.20  → recentered (-0.51) → **+7.90**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T05:44:00Z (Vanderbilt)