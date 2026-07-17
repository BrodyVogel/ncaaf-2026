# Duke — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+3.72** (rank 51/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    50 | proxy 19
- RB    62 | proxy 97
- WRTE  48 | proxy 85
- OL    52 | proxy 66
- DL    44 | proxy 60
- LB    46 | proxy 40
- DB    46 | proxy 19
- ST    50 | proxy 72

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.091 WRTE:+0.036 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +27.20 vs anchor off +32.11
- grade-implied def +26.41 vs anchor def +28.19  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-3.12**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -2.12 (=-0.541x anchor margin) + shape -1.00 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      5.7 → 5.7 → 5.7
- FEI      0.17 → 3.94 → 3.94
- Massey   7.96 → 6.37 → 6.37
- FPI      3.5 → 3.59 → 3.59
- TR       1.9 → 1.33 → 1.33
- PickSix  54 → 3.56 → 3.56
- blend 4.31  (dispersion 5.03)

## 4. Assembly
- anchor +4.31  class -0.00  k×resid -1.09 (k=0.35, cap ±6.0)  ST +0.00  → recentered (-0.50) → **+3.72**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (c4edefa)