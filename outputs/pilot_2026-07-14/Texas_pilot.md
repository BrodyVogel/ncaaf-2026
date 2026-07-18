# Texas — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+17.71** (rank 11/138 in hybrid field)  band ±6.60

## 1. Unit grades (LLM real | shadow proxy)
- QB    64 | proxy 97
- RB    60 | proxy 86
- WRTE  62 | proxy 85
- OL    56 | proxy 92
- DL    62 | proxy 82
- LB    56 | proxy 78
- DB    56 | proxy 93
- ST    52 | proxy 70

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.53)
- def: DL:-0.083 LB:-0.059 DB:-0.095  (R²=0.61)
- grade-implied off +28.89 vs anchor off +37.32
- grade-implied def +23.39 vs anchor def +14.58  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-17.24**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -12.30 (=-0.541x anchor margin) + shape -4.94 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      23.7 → 23.7 → 23.7
- FEI      0.88 → 19.25 → 19.25
- Massey   8.7 → 20.24 → 20.24
- FPI      26.9 → 30.85 → 26.68  [WINSORIZED]
- TR       28.4 → 26.7 → 26.68  [WINSORIZED]
- PickSix  7 → 21.68 → 21.68
- blend 23.13  (dispersion 11.61, FLAGGED

## 4. Assembly
- anchor +23.13  class -0.00  k×resid -6.00 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.54) → **+17.71**
- band: 6.0 × coach(1.0) × dispersion(1.10) × conf(1+0.03×0) = ±6.60

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T05:20:00Z (Texas)