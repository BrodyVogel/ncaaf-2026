# West Virginia — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+0.36** (rank 62/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    44 | proxy 20
- RB    52 | proxy 55
- WRTE  44 | proxy 43
- OL    46 | proxy 45
- DL    42 | proxy 33
- LB    40 | proxy 35
- DB    40 | proxy 29
- ST    42 | proxy 61

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.62)
- grade-implied off +25.20 vs anchor off +26.51
- grade-implied def +27.54 vs anchor def +25.39
- residual (off-minus-def, grades-vs-anchor): **-3.46**
- resid decomposition (diagnostic): level -0.61 (=-0.541x anchor margin - the calibrated fade) + shape -2.85 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      0.8 → 0.8 → 0.8
- FEI      -0.07 → -1.24 → -1.24
- Massey   7.66 → 0.74 → 0.74
- FPI      0.2 → -0.25 → -0.25
- TR       4.5 → 3.82 → 3.82
- PickSix  51 → 3.93 → 3.93
- blend 1.23  (dispersion 5.17)

## 4. Assembly
- anchor +1.23  class -0.00  k×resid -1.21 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.50) → **+0.36**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15