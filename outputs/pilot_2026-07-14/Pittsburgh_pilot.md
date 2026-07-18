# Pittsburgh — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+5.83** (rank 41/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 22
- RB    56 | proxy 53
- WRTE  42 | proxy 4
- OL    52 | proxy 51
- DL    58 | proxy 60
- LB    54 | proxy 67
- DB    50 | proxy 53
- ST    46 | proxy 41

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.075 RB:+0.090 WRTE:+0.042 OL:+0.079  (R²=0.55)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +26.48 vs anchor off +30.52
- grade-implied def +24.38 vs anchor def +23.48  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-4.95**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -3.81 (=-0.541x anchor margin) + shape -1.14 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.5 → 6.5 → 6.5
- FEI      0.33 → 7.39 → 7.39
- Massey   7.98 → 6.74 → 6.74
- FPI      6.6 → 7.2 → 7.2
- TR       10.0 → 9.09 → 9.09
- PickSix  39 → 6.55 → 6.55
- blend 7.14  (dispersion 2.59)

## 4. Assembly
- anchor +7.14  class -0.00  k×resid -1.73 (k=0.35, cap ±6.0)  ST -0.08  → recentered (-0.50) → **+5.83**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (ae53f6c)