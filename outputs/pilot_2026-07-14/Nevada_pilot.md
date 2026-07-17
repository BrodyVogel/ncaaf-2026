# Nevada — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-14.93** (rank 125/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    18 | proxy 1
- RB    14 | proxy —
- WRTE  12 | proxy —
- OL    22 | proxy —
- DL    26 | proxy 79
- LB    12 | proxy —
- DB    18 | proxy 31
- ST    16 | proxy 13

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.066 RB:+0.092 WRTE:+0.038 OL:+0.084  (R²=0.54)
- def: DL:-0.088 LB:-0.059 DB:-0.093  (R²=0.62)
- grade-implied off +16.86 vs anchor off +16.27
- grade-implied def +32.53 vs anchor def +31.13  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-0.81**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +8.04 (=-0.541x anchor margin) + shape -8.85 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -12.2 → -12.2 → -12.2
- FEI      -0.77 → -16.33 → -16.33
- Massey   6.88 → -13.88 → -13.88
- FPI      -11.9 → -14.35 → -14.35
- TR       -18.1 → -17.81 → -17.81
- blend -14.46  (dispersion 5.61)

## 4. Assembly
- anchor -14.46  class +0.00  k×resid -0.28 (k=0.35, cap ±6.0)  ST -0.68  → recentered (-0.49) → **-14.93**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (908b834)