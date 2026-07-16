# Washington — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+13.03** (rank 22/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    74 | proxy 15
- RB    50 | proxy —
- WRTE  56 | proxy 62
- OL    62 | proxy 53
- DL    62 | proxy 77
- LB    72 | proxy 89
- DB    72 | proxy 86
- ST    58 | proxy 49

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.078 RB:+0.093 WRTE:+0.034 OL:+0.080  (R²=0.55)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +28.99 vs anchor off +32.55
- grade-implied def +20.88 vs anchor def +17.45
- residual (off-minus-def, grades-vs-anchor): **-6.98**
- resid decomposition (diagnostic): level -8.17 (=-0.541x anchor margin - the calibrated fade) + shape +1.18 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      14.5 → 14.5 → 14.5
- FEI      0.78 → 17.09 → 17.09
- Massey   8.5 → 16.49 → 16.49
- FPI      9.9 → 11.05 → 11.05
- TR       16.4 → 15.21 → 15.21
- PickSix  18 → 14.81 → 14.81
- blend 14.81  (dispersion 6.04)

## 4. Assembly
- anchor +14.81  class -0.00  k×resid -2.44 (k=0.35, cap ±6.0)  ST +0.16  → recentered (-0.51) → **+13.03**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (8dd0641)