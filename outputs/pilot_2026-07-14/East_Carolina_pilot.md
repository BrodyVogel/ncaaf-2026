# East Carolina — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-1.10** (rank 71/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    44 | proxy —
- RB    50 | proxy 55
- WRTE  46 | proxy 35
- OL    30 | proxy 34
- DL    54 | proxy 38
- LB    25 | proxy 1
- DB    55 | proxy 38
- ST    52 | proxy 49

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.082 LB:-0.064 DB:-0.095  (R²=0.62)
- grade-implied off +23.81 vs anchor off +24.62
- grade-implied def +26.12 vs anchor def +25.58  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-1.35**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +0.52 (=-0.541x anchor margin) + shape -1.87 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.0 → -2.0 → -2.0
- FEI      0.04 → 1.13 → 1.13
- Massey   7.68 → 1.12 → 1.12
- FPI      -0.6 → -1.18 → -1.18
- TR       -3.7 → -4.03 → -4.03
- blend -1.16  (dispersion 5.16)

## 4. Assembly
- anchor -1.16  class +0.00  k×resid -0.47 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.49) → **-1.10**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15