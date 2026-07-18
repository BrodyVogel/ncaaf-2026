# Arkansas — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+3.02** (rank 54/138 in hybrid field)  band ±6.98

## 1. Unit grades (LLM real | shadow proxy)
- QB    42 | proxy —
- RB    46 | proxy 45
- WRTE  44 | proxy 48
- OL    44 | proxy 69
- DL    48 | proxy 50
- LB    44 | proxy 45
- DB    48 | proxy 66
- ST    44 | proxy 15

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.094 WRTE:+0.038 OL:+0.079  (R²=0.54)
- def: DL:-0.083 LB:-0.058 DB:-0.098  (R²=0.62)
- grade-implied off +24.31 vs anchor off +34.01
- grade-implied def +25.96 vs anchor def +29.39  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-6.27**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -2.50 (=-0.541x anchor margin) + shape -3.77 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      5.0 → 5.0 → 5.0
- FEI      0.28 → 6.31 → 6.31
- Massey   7.98 → 6.74 → 6.74
- FPI      4.4 → 4.64 → 4.64
- TR       4.7 → 4.01 → 4.01
- PickSix  58 → 2.07 → 2.07
- blend 4.83  (dispersion 4.67)

## 4. Assembly
- anchor +4.83  class -0.00  k×resid -2.19 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.50) → **+3.02**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×1) = ±6.98

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T02:42:15Z (7b57cb1)