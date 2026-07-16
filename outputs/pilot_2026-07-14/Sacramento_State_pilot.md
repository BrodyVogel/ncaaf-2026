# Sacramento State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-19.61** (rank 135/138 in hybrid field)  band ±7.59

## 1. Unit grades (LLM real | shadow proxy)
- QB    20 | proxy —
- RB    14 | proxy —
- WRTE  10 | proxy —
- OL     8 | proxy —
- DL    10 | proxy —
- LB    16 | proxy —
- DB    10 | proxy —
- ST    22 | proxy —

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.091 WRTE:+0.037 OL:+0.083  (R²=0.55)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.63)
- grade-implied off +15.70 vs anchor off +16.44
- grade-implied def +34.40 vs anchor def +36.56  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+1.42**
- resid decomposition (diagnostic): level +10.88 (=-0.541x anchor margin - the calibrated fade) + shape -9.47 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -22.7 → -22.7 → -22.7
- FEI      -1.0 → -21.29 → -21.29
- Massey   6.59 → -19.32 → -19.32
- FPI      -10.4 → -12.6 → -15.3  [WINSORIZED]
- TR       -19.2 → -18.86 → -18.86
- blend -20.03  (dispersion 10.1)

## 4. Assembly
- anchor -20.03  class +0.00  k×resid +0.50 (k=0.35, cap ±6.0)  ST -0.56  → recentered (-0.48) → **-19.61**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×4) = ±7.59

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (9dbb540)