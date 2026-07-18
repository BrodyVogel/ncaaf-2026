# Kentucky — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+4.50** (rank 49/138 in hybrid field)  band ±6.98

## 1. Unit grades (LLM real | shadow proxy)
- QB    50 | proxy —
- RB    48 | proxy —
- WRTE  48 | proxy 40
- OL    54 | proxy 73
- DL    58 | proxy 72
- LB    44 | proxy —
- DB    50 | proxy 64
- ST    48 | proxy 19

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.083 LB:-0.060 DB:-0.096  (R²=0.61)
- grade-implied off +26.12 vs anchor off +25.90
- grade-implied def +25.00 vs anchor def +20.30  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-4.48**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -3.03 (=-0.541x anchor margin) + shape -1.45 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.8 → 3.8 → 3.8
- FEI      0.27 → 6.09 → 6.09
- Massey   7.98 → 6.74 → 6.74
- FPI      5.4 → 5.81 → 5.81
- TR       8.9 → 8.03 → 8.03
- PickSix  45 → 4.97 → 4.97
- blend 5.61  (dispersion 4.23)

## 4. Assembly
- anchor +5.61  class -0.00  k×resid -1.57 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.50) → **+4.50**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×1) = ±6.98

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T03:50:29Z (f2a50a9)