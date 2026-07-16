# Bowling Green — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-13.67** (rank 121/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    34 | proxy —
- RB    28 | proxy 7
- WRTE  18 | proxy —
- OL    10 | proxy —
- DL    34 | proxy 10
- LB    30 | proxy 58
- DB    30 | proxy 18
- ST    18 | proxy 44

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.084 WRTE:+0.039 OL:+0.085  (R²=0.54)
- def: DL:-0.084 LB:-0.058 DB:-0.097  (R²=0.61)
- grade-implied off +18.49 vs anchor off +14.03
- grade-implied def +29.74 vs anchor def +29.07  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+3.79**
- resid decomposition (diagnostic): level +8.14 (=-0.541x anchor margin - the calibrated fade) + shape -4.34 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.3 → -13.3 → -13.3
- FEI      -0.71 → -15.04 → -15.04
- Massey   6.9 → -13.51 → -13.51
- FPI      -13.7 → -16.44 → -16.44
- TR       -17.7 → -17.43 → -17.43
- blend -14.84  (dispersion 4.13)

## 4. Assembly
- anchor -14.84  class +0.00  k×resid +1.33 (k=0.35, cap ±6.0)  ST -0.64  → recentered (-0.49) → **-13.67**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (e6c4d93)