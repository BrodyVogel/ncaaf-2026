# Penn State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+14.96** (rank 18/138 in hybrid field)  band ±6.78

## 1. Unit grades (LLM real | shadow proxy)
- QB    74 | proxy 84
- RB    68 | proxy 73
- WRTE  58 | proxy 60
- OL    58 | proxy 78
- DL    60 | proxy 57
- LB    68 | proxy 65
- DB    70 | proxy 78
- ST    66 | proxy 91

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.53)
- def: DL:-0.083 LB:-0.059 DB:-0.095  (R²=0.61)
- grade-implied off +30.34 vs anchor off +34.05
- grade-implied def +21.52 vs anchor def +18.15
- residual (off-minus-def, grades-vs-anchor): **-7.08**
- resid decomposition (diagnostic): level -8.60 (=-0.541x anchor margin - the calibrated fade) + shape +1.52 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      15.7 → 15.7 → 15.7
- FEI      0.89 → 19.46 → 19.46
- Massey   8.73 → 20.8 → 20.48  [WINSORIZED]
- FPI      13.7 → 15.48 → 15.48
- TR       16.4 → 15.21 → 15.21
- PickSix  20 → 14.15 → 14.15
- blend 16.6  (dispersion 6.65)

## 4. Assembly
- anchor +16.60  class -0.00  k×resid -2.48 (k=0.35, cap ±6.0)  ST +0.32  → recentered (-0.51) → **+14.96**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×0) = ±6.78

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (5cceb68)