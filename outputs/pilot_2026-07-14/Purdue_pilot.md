# Purdue — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-1.15** (rank 70/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    44 | proxy 43
- RB    48 | proxy 44
- WRTE  40 | proxy 25
- OL    38 | proxy 32
- DL    58 | proxy 74
- LB    46 | proxy 52
- DB    44 | proxy 19
- ST    54 | proxy 96

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.095  (R²=0.61)
- grade-implied off +24.04 vs anchor off +24.11
- grade-implied def +25.42 vs anchor def +27.09
- residual (off-minus-def, grades-vs-anchor): **+1.60**
- resid decomposition (diagnostic): level +1.61 (=-0.541x anchor margin - the calibrated fade) + shape -0.01 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.9 → -2.9 → -2.9
- FEI      -0.1 → -1.88 → -1.88
- Massey   7.57 → -0.94 → -0.94
- FPI      -0.9 → -1.53 → -1.53
- TR       -2.1 → -2.49 → -2.49
- PickSix  68 → -3.33 → -3.33
- blend -2.28  (dispersion 2.38)

## 4. Assembly
- anchor -2.28  class -0.00  k×resid +0.56 (k=0.35, cap ±6.0)  ST +0.08  → recentered (-0.49) → **-1.15**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (56798c9)