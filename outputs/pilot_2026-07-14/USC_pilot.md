# USC — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+15.56** (rank 17/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    80 | proxy 85
- RB    72 | proxy 62
- WRTE  68 | proxy 99
- OL    54 | proxy 29
- DL    72 | proxy 80
- LB    66 | proxy 78
- DB    68 | proxy 77
- ST    50 | proxy 9

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.066 RB:+0.092 WRTE:+0.030 OL:+0.089  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +30.88 vs anchor off +38.26
- grade-implied def +20.76 vs anchor def +19.94
- residual (off-minus-def, grades-vs-anchor): **-8.20**
- resid decomposition (diagnostic): level -9.91 (=-0.541x anchor margin - the calibrated fade) + shape +1.71 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      16.8 → 16.8 → 16.8
- FEI      0.79 → 17.31 → 17.31
- Massey   8.53 → 17.05 → 17.05
- FPI      17.0 → 19.32 → 19.32
- TR       20.9 → 19.52 → 19.52
- PickSix  11 → 18.69 → 18.69
- blend 17.93  (dispersion 2.72)

## 4. Assembly
- anchor +17.93  class -0.00  k×resid -2.87 (k=0.35, cap ±6.0)  ST +0.00  → recentered (-0.50) → **+15.56**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (03d3d96)