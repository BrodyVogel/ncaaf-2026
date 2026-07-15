# Houston — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+6.15** (rank 40/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    62 | proxy 73
- RB    52 | proxy —
- WRTE  58 | proxy 76
- OL    46 | proxy 62
- DL    55 | proxy 71
- LB    48 | proxy 52
- DB    60 | proxy 70
- ST    42 | proxy 40

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +27.02 vs anchor off +30.93
- grade-implied def +24.01 vs anchor def +23.17
- residual (off-minus-def, grades-vs-anchor): **-4.75**
- resid decomposition (diagnostic): level -4.20 (=-0.541x anchor margin - the calibrated fade) + shape -0.55 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      8.2 → 8.2 → 8.2
- FEI      0.13 → 3.07 → 3.2  [WINSORIZED]
- Massey   7.9 → 5.24 → 5.24
- FPI      7.1 → 7.79 → 7.79
- TR       10.6 → 9.66 → 9.66
- PickSix  30 → 9.97 → 9.97
- blend 7.47  (dispersion 6.89)

## 4. Assembly
- anchor +7.47  class -0.00  k×resid -1.66 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.50) → **+6.15**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15