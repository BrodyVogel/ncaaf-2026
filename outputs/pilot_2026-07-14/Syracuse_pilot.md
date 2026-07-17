# Syracuse — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-2.34** (rank 76/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 32
- RB    30 | proxy —
- WRTE  32 | proxy 22
- OL    42 | proxy 34
- DL    36 | proxy 42
- LB    34 | proxy 27
- DB    50 | proxy 51
- ST    40 | proxy 16

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.060 DB:-0.096  (R²=0.62)
- grade-implied off +23.00 vs anchor off +23.31
- grade-implied def +27.42 vs anchor def +25.59  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-2.14**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +1.23 (=-0.541x anchor margin) + shape -3.38 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -0.7 → -0.7 → -0.7
- FEI      -0.26 → -5.33 → -5.33
- Massey   7.37 → -4.69 → -4.69
- FPI      -0.8 → -1.42 → -1.42
- TR       -0.2 → -0.68 → -0.68
- PickSix  64 → 0.39 → 0.39
- blend -1.88  (dispersion 5.72)

## 4. Assembly
- anchor -1.88  class -0.00  k×resid -0.75 (k=0.35, cap ±6.0)  ST -0.20  → recentered (-0.49) → **-2.34**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (e63329f)