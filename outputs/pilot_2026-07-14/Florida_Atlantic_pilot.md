# Florida Atlantic — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-7.74** (rank 103/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    55 | proxy 57
- RB    40 | proxy —
- WRTE  50 | proxy 54
- OL    35 | proxy 44
- DL    30 | proxy 14
- LB    20 | proxy 5
- DB    15 | proxy 2
- ST    50 | proxy 45

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +24.24 vs anchor off +25.10
- grade-implied def +32.05 vs anchor def +37.00
- residual (off-minus-def, grades-vs-anchor): **+4.09**
- resid decomposition (diagnostic): level +6.44 (=-0.541x anchor margin - the calibrated fade) + shape -2.34 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.1 → -7.1 → -8.7  [WINSORIZED]
- FEI      -0.65 → -13.74 → -13.74
- Massey   6.86 → -14.26 → -14.26
- FPI      -11.3 → -13.65 → -13.65
- TR       -8.7 → -8.81 → -8.81
- blend -11.31  (dispersion 7.16)

## 4. Assembly
- anchor -11.31  class +1.68  k×resid +1.43 (k=0.35, cap ±6.0)  ST +0.00  → recentered (-0.46) → **-7.74**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15