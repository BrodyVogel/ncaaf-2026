# Texas State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-4.30** (rank 85/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    58 | proxy 65
- RB    46 | proxy 81
- WRTE  54 | proxy 69
- OL    44 | proxy 58
- DL    30 | proxy 17
- LB    32 | proxy 16
- DB    36 | proxy 6
- ST    42 | proxy 44

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.058 DB:-0.095  (R²=0.61)
- grade-implied off +25.88 vs anchor off +32.10
- grade-implied def +29.32 vs anchor def +37.50  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+1.96**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +2.92 (=-0.541x anchor margin) + shape -0.96 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.9 → -5.9 → -5.9
- FEI      -0.28 → -5.77 → -5.77
- Massey   7.28 → -6.38 → -6.38
- FPI      -4.3 → -5.49 → -5.49
- TR       -2.0 → -2.4 → -2.4
- blend -5.31  (dispersion 3.98)

## 4. Assembly
- anchor -5.31  class +0.00  k×resid +0.69 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.49) → **-4.30**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-17 (eff6e84)