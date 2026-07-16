# Maryland — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+2.54** (rank 56/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    60 | proxy 50
- RB    38 | proxy 25
- WRTE  40 | proxy 24
- OL    40 | proxy 40
- DL    63 | proxy 79
- LB    53 | proxy 78
- DB    60 | proxy 81
- ST    36 | proxy 21

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.093 WRTE:+0.038 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.060 DB:-0.096  (R²=0.62)
- grade-implied off +24.39 vs anchor off +25.51
- grade-implied def +23.00 vs anchor def +23.29
- residual (off-minus-def, grades-vs-anchor): **-0.83**
- resid decomposition (diagnostic): level -1.20 (=-0.541x anchor margin - the calibrated fade) + shape +0.37 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.8 → 3.8 → 3.8
- FEI      0.08 → 2.0 → 2.0
- Massey   7.79 → 3.18 → 3.18
- FPI      1.0 → 0.68 → 0.68
- TR       2.9 → 2.29 → 2.29
- PickSix  56 → 2.62 → 2.62
- blend 2.62  (dispersion 3.12)

## 4. Assembly
- anchor +2.62  class -0.00  k×resid -0.29 (k=0.35, cap ±6.0)  ST -0.28  → recentered (-0.49) → **+2.54**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (fcc394e)