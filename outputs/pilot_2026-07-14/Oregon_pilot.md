# Oregon — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+24.48** (rank 5/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    89 | proxy 71
- RB    80 | proxy 93
- WRTE  80 | proxy 93
- OL    56 | proxy 47
- DL    90 | proxy 100
- LB    66 | proxy 90
- DB    74 | proxy 95
- ST    62 | proxy 88

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.087 WRTE:+0.033 OL:+0.086  (R²=0.53)
- def: DL:-0.082 LB:-0.059 DB:-0.096  (R²=0.60)
- grade-implied off +32.83 vs anchor off +40.95
- grade-implied def +18.78 vs anchor def +12.35
- residual (off-minus-def, grades-vs-anchor): **-14.56**
- resid decomposition (diagnostic): level -15.47 (=-0.541x anchor margin - the calibrated fade) + shape +0.92 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      28.3 → 28.3 → 28.3
- FEI      1.4 → 30.46 → 30.46
- Massey   9.0 → 25.87 → 25.87
- FPI      25.3 → 28.99 → 28.99
- TR       29.5 → 27.75 → 27.75
- PickSix  1 → 31.92 → 31.92
- blend 28.8  (dispersion 6.05)

## 4. Assembly
- anchor +28.80  class -0.00  k×resid -5.09 (k=0.35, cap ±6.0)  ST +0.24  → recentered (-0.53) → **+24.48**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (236ad69)