# San José State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-15.58** (rank 126/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    20 | proxy 5
- RB    16 | proxy —
- WRTE  16 | proxy —
- OL    14 | proxy 9
- DL    16 | proxy 42
- LB    14 | proxy 31
- DB    12 | proxy —
- ST    22 | proxy 67

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.057 DB:-0.097  (R²=0.62)
- grade-implied off +16.54 vs anchor off +19.19
- grade-implied def +33.82 vs anchor def +33.01  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-3.47**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +7.48 (=-0.541x anchor margin) + shape -10.94 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -15.5 → -15.5 → -15.5
- FEI      -0.53 → -11.16 → -11.16
- Massey   6.99 → -11.82 → -11.82
- FPI      -14.3 → -17.14 → -17.14
- TR       -14.9 → -14.75 → -14.75
- blend -14.31  (dispersion 5.99)

## 4. Assembly
- anchor -14.31  class +0.00  k×resid -1.21 (k=0.35, cap ±6.0)  ST -0.56  → recentered (-0.51) → **-15.58**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (cff1aa3)