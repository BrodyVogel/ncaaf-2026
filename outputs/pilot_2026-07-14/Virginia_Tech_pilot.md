# Virginia Tech — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+5.52** (rank 42/138 in hybrid field)  band ±7.91

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy 42
- RB    60 | proxy 41
- WRTE  50 | proxy 43
- OL    42 | proxy —
- DL    50 | proxy —
- LB    44 | proxy —
- DB    60 | proxy 90
- ST    50 | proxy 7

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.093 WRTE:+0.037 OL:+0.081  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.097  (R²=0.61)
- grade-implied off +26.12 vs anchor off +29.92
- grade-implied def +24.66 vs anchor def +22.68  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-5.79**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -3.92 (=-0.541x anchor margin) + shape -1.87 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      9.4 → 9.4 → 9.4
- FEI      -0.08 → -1.45 → 3.14  [WINSORIZED]
- Massey   7.65 → 0.56 → 3.14  [WINSORIZED]
- FPI      7.4 → 8.14 → 8.14
- TR       8.2 → 7.36 → 7.36
- PickSix  34 → 8.76 → 8.76
- blend 7.05  (dispersion 10.85, FLAGGED

## 4. Assembly
- anchor +7.05  class -0.00  k×resid -2.02 (k=0.35, cap ±6.0)  ST +0.00  → recentered (-0.50) → **+5.52**
- band: 6.0 × coach(1.13) × dispersion(1.10) × conf(1+0.03×2) = ±7.91

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (d9a92fa)