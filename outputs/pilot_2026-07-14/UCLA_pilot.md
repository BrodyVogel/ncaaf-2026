# UCLA — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+4.70** (rank 50/138 in hybrid field)  band ±6.78

## 1. Unit grades (LLM real | shadow proxy)
- QB    60 | proxy 51
- RB    60 | proxy 46
- WRTE  52 | proxy 28
- OL    42 | proxy 34
- DL    56 | proxy 64
- LB    60 | proxy 74
- DB    66 | proxy 64
- ST    56 | proxy 73

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.038 OL:+0.083  (R²=0.54)
- def: DL:-0.083 LB:-0.060 DB:-0.096  (R²=0.62)
- grade-implied off +27.04 vs anchor off +28.40
- grade-implied def +22.63 vs anchor def +24.50
- residual (off-minus-def, grades-vs-anchor): **+0.51**
- resid decomposition (diagnostic): level -2.11 (=-0.541x anchor margin - the calibrated fade) + shape +2.62 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      5.1 → 5.1 → 5.1
- FEI      0.08 → 2.0 → 2.0
- Massey   7.79 → 3.18 → 3.18
- FPI      0.5 → 0.1 → 0.1
- TR       8.2 → 7.36 → 7.36
- PickSix  49 → 4.5 → 4.5
- blend 3.91  (dispersion 7.27)

## 4. Assembly
- anchor +3.91  class -0.00  k×resid +0.18 (k=0.35, cap ±6.0)  ST +0.12  → recentered (-0.49) → **+4.70**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×0) = ±6.78

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (f032e11)