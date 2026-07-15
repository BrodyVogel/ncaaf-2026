# Texas Tech — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+17.75** (rank 10/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    50 | proxy 96
- RB    72 | proxy 92
- WRTE  62 | proxy 91
- OL    60 | proxy 87
- DL    65 | proxy 85
- LB    62 | proxy 89
- DB    70 | proxy 93
- ST    65 | proxy 96

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.53)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +29.33 vs anchor off +36.89
- grade-implied def +21.42 vs anchor def +15.41
- residual (off-minus-def, grades-vs-anchor): **-13.57**
- resid decomposition (diagnostic): level -11.62 (=-0.541x anchor margin - the calibrated fade) + shape -1.95 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      23.1 → 23.1 → 23.1
- FEI      0.89 → 19.46 → 19.46
- Massey   8.65 → 19.3 → 19.3
- FPI      20.0 → 22.81 → 22.81
- TR       23.8 → 22.3 → 22.3
- PickSix  8 → 21.63 → 21.63
- blend 21.67  (dispersion 3.8)

## 4. Assembly
- anchor +21.67  class -0.00  k×resid -4.75 (k=0.35, cap ±6.0)  ST +0.30  → recentered (-0.53) → **+17.75**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15