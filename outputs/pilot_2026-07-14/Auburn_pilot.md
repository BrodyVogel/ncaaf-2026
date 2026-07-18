# Auburn — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+9.08** (rank 29/138 in hybrid field)  band ±6.78

## 1. Unit grades (LLM real | shadow proxy)
- QB    60 | proxy 95
- RB    54 | proxy 58
- WRTE  48 | proxy 65
- OL    48 | proxy 69
- DL    54 | proxy 85
- LB    54 | proxy 82
- DB    50 | proxy 64
- ST    56 | proxy 33

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.074 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.082 LB:-0.058 DB:-0.096  (R²=0.61)
- grade-implied off +26.93 vs anchor off +28.62
- grade-implied def +24.74 vs anchor def +17.28  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-9.16**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -6.13 (=-0.541x anchor margin) + shape -3.02 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      11.2 → 11.2 → 11.2
- FEI      0.51 → 11.27 → 11.27
- Massey   8.18 → 10.49 → 10.49
- FPI      12.0 → 13.5 → 13.5
- TR       13.4 → 12.34 → 12.34
- PickSix  26 → 11.55 → 11.55
- blend 11.65  (dispersion 3.0)

## 4. Assembly
- anchor +11.65  class -0.00  k×resid -3.20 (k=0.35, cap ±6.0)  ST +0.12  → recentered (-0.51) → **+9.08**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×0) = ±6.78

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T02:54:00Z (09136c4)