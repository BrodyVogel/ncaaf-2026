# Rutgers — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+2.01** (rank 59/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 53
- RB    74 | proxy 58
- WRTE  60 | proxy 101
- OL    50 | proxy 12
- DL    54 | proxy 70
- LB    54 | proxy 43
- DB    36 | proxy 6
- ST    44 | proxy 19

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.033 OL:+0.086  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.095  (R²=0.61)
- grade-implied off +28.68 vs anchor off +30.03
- grade-implied def +26.04 vs anchor def +29.07
- residual (off-minus-def, grades-vs-anchor): **+1.67**
- resid decomposition (diagnostic): level -0.52 (=-0.541x anchor margin - the calibrated fade) + shape +2.19 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      1.8 → 1.8 → 1.8
- FEI      0.01 → 0.49 → 0.49
- Massey   7.79 → 3.18 → 3.18
- FPI      -0.2 → -0.72 → -0.72
- TR       0.8 → 0.28 → 0.28
- PickSix  63 → 0.58 → 0.58
- blend 1.06  (dispersion 3.9)

## 4. Assembly
- anchor +1.06  class -0.00  k×resid +0.59 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.48) → **+2.01**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (2d49954)