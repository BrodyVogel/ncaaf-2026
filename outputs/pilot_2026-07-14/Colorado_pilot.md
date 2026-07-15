# Colorado — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+0.36** (rank 61/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    45 | proxy 64
- RB    48 | proxy —
- WRTE  56 | proxy 75
- OL    40 | proxy 44
- DL    55 | proxy 68
- LB    50 | proxy 53
- DB    47 | proxy 47
- ST    42 | proxy 61

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +24.90 vs anchor off +26.07
- grade-implied def +25.15 vs anchor def +25.13
- residual (off-minus-def, grades-vs-anchor): **-1.19**
- resid decomposition (diagnostic): level -0.51 (=-0.541x anchor margin - the calibrated fade) + shape -0.68 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      0.9 → 0.9 → 0.9
- FEI      -0.15 → -2.96 → -2.96
- Massey   7.65 → 0.56 → 0.56
- FPI      4.5 → 4.76 → 4.76
- TR       -1.4 → -1.82 → -1.82
- PickSix  62 → 0.78 → 0.78
- blend 0.44  (dispersion 7.72)

## 4. Assembly
- anchor +0.44  class -0.00  k×resid -0.42 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.50) → **+0.36**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15