# BYU — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+13.03** (rank 21/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    72 | proxy 83
- RB    82 | proxy 95
- WRTE  48 | proxy 51
- OL    68 | proxy 69
- DL    52 | proxy 57
- LB    50 | proxy 30
- DB    70 | proxy 90
- ST    42 | proxy 99

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.093 WRTE:+0.036 OL:+0.082  (R²=0.53)
- def: DL:-0.083 LB:-0.062 DB:-0.093  (R²=0.61)
- grade-implied off +32.01 vs anchor off +32.87
- grade-implied def +23.29 vs anchor def +18.53
- residual (off-minus-def, grades-vs-anchor): **-5.62**
- resid decomposition (diagnostic): level -7.76 (=-0.541x anchor margin - the calibrated fade) + shape +2.13 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      15.5 → 15.5 → 15.5
- FEI      0.61 → 13.42 → 13.42
- Massey   8.34 → 13.49 → 13.49
- FPI      13.1 → 14.78 → 14.78
- TR       14.6 → 13.49 → 13.49
- PickSix  17 → 16.36 → 16.36
- blend 14.65  (dispersion 2.93)

## 4. Assembly
- anchor +14.65  class -0.00  k×resid -1.97 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.51) → **+13.03**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15