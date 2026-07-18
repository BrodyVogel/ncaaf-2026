# Tennessee — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+12.55** (rank 21/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy —
- RB    60 | proxy 93
- WRTE  56 | proxy 99
- OL    58 | proxy 91
- DL    50 | proxy 57
- LB    58 | proxy 90
- DB    54 | proxy 74
- ST    54 | proxy 73

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.091 WRTE:+0.035 OL:+0.081  (R²=0.53)
- def: DL:-0.083 LB:-0.061 DB:-0.096  (R²=0.62)
- grade-implied off +27.47 vs anchor off +38.98
- grade-implied def +24.40 vs anchor def +22.72  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-13.19**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -8.80 (=-0.541x anchor margin) + shape -4.40 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      16.0 → 16.0 → 16.0
- FEI      0.8 → 17.52 → 17.52
- Massey   8.47 → 15.93 → 15.93
- FPI      15.1 → 17.11 → 17.11
- TR       16.8 → 15.6 → 15.6
- PickSix  15 → 17.8 → 17.8
- blend 16.56  (dispersion 2.2)

## 4. Assembly
- anchor +16.56  class -0.00  k×resid -4.62 (k=0.35, cap ±6.0)  ST +0.08  → recentered (-0.53) → **+12.55**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T05:05:00Z (Tennessee)