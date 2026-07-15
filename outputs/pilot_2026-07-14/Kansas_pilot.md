# Kansas — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+2.64** (rank 56/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    42 | proxy 40
- RB    48 | proxy 23
- WRTE  44 | proxy 25
- OL    45 | proxy 46
- DL    50 | proxy 57
- LB    52 | proxy 31
- DB    42 | proxy 29
- ST    40 | proxy 78

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.096 WRTE:+0.039 OL:+0.080  (R²=0.55)
- def: DL:-0.082 LB:-0.060 DB:-0.096  (R²=0.62)
- grade-implied off +24.56 vs anchor off +29.16
- grade-implied def +25.96 vs anchor def +25.74
- residual (off-minus-def, grades-vs-anchor): **-4.82**
- resid decomposition (diagnostic): level -1.85 (=-0.541x anchor margin - the calibrated fade) + shape -2.97 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.7 → 3.7 → 3.7
- FEI      0.28 → 6.31 → 6.31
- Massey   7.93 → 5.81 → 5.81
- FPI      2.8 → 2.78 → 2.78
- TR       5.4 → 4.68 → 4.68
- PickSix  61 → 1.14 → 1.14
- blend 4.02  (dispersion 5.17)

## 4. Assembly
- anchor +4.02  class -0.00  k×resid -1.69 (k=0.35, cap ±6.0)  ST -0.20  → recentered (-0.51) → **+2.64**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15