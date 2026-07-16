# Northwestern — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+4.13** (rank 50/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 40
- RB    58 | proxy 52
- WRTE  64 | proxy 95
- OL    46 | proxy 69
- DL    52 | proxy 90
- LB    52 | proxy 74
- DB    68 | proxy 88
- ST    40 | proxy 28

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.069 RB:+0.090 WRTE:+0.040 OL:+0.083  (R²=0.54)
- def: DL:-0.085 LB:-0.059 DB:-0.097  (R²=0.62)
- grade-implied off +27.17 vs anchor off +23.96
- grade-implied def +23.22 vs anchor def +20.94
- residual (off-minus-def, grades-vs-anchor): **+0.92**
- resid decomposition (diagnostic): level -1.63 (=-0.541x anchor margin - the calibrated fade) + shape +2.56 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      4.6 → 4.6 → 4.6
- FEI      0.09 → 2.21 → 2.21
- Massey   7.87 → 4.68 → 4.68
- FPI      1.4 → 1.15 → 1.15
- TR       4.8 → 4.11 → 4.11
- PickSix  55 → 3.31 → 3.31
- blend 3.52  (dispersion 3.53)

## 4. Assembly
- anchor +3.52  class -0.00  k×resid +0.32 (k=0.35, cap ±6.0)  ST -0.20  → recentered (-0.49) → **+4.13**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (78722de)