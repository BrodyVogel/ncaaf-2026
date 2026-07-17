# Florida State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+5.74** (rank 41/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy 68
- RB    58 | proxy 78
- WRTE  58 | proxy 91
- OL    40 | proxy 44
- DL    46 | proxy 64
- LB    48 | proxy 43
- DB    48 | proxy 52
- ST    44 | proxy 70

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.093 WRTE:+0.038 OL:+0.082  (R²=0.54)
- def: DL:-0.082 LB:-0.060 DB:-0.096  (R²=0.61)
- grade-implied off +26.12 vs anchor off +29.45
- grade-implied def +25.96 vs anchor def +20.85  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-8.44**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -4.65 (=-0.541x anchor margin) + shape -3.79 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      8.8 → 8.8 → 8.8
- FEI      0.47 → 10.41 → 10.41
- Massey   8.03 → 7.68 → 7.68
- FPI      9.3 → 10.35 → 10.35
- TR       7.3 → 6.5 → 6.5
- PickSix  42 → 5.56 → 5.56
- blend 8.3  (dispersion 4.84)

## 4. Assembly
- anchor +8.30  class -0.00  k×resid -2.95 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.52) → **+5.74**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (84b681b)