# Cincinnati — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+3.06** (rank 54/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    44 | proxy 29
- RB    50 | proxy 44
- WRTE  40 | proxy —
- OL    76 | proxy 97
- DL    32 | proxy 13
- LB    55 | proxy 52
- DB    45 | proxy 52
- ST    52 | proxy 52

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.093 WRTE:+0.037 OL:+0.081  (R²=0.54)
- def: DL:-0.085 LB:-0.058 DB:-0.095  (R²=0.62)
- grade-implied off +27.31 vs anchor off +29.14
- grade-implied def +27.01 vs anchor def +25.86
- residual (off-minus-def, grades-vs-anchor): **-2.98**
- resid decomposition (diagnostic): level -1.77 (=-0.541x anchor margin - the calibrated fade) + shape -1.21 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      4.5 → 4.5 → 4.5
- FEI      0.24 → 5.45 → 5.45
- Massey   7.87 → 4.68 → 4.68
- FPI      4.4 → 4.64 → 4.64
- TR       0.3 → -0.2 → -0.2
- PickSix  60 → 1.45 → 1.45
- blend 3.57  (dispersion 5.64)

## 4. Assembly
- anchor +3.57  class -0.00  k×resid -1.04 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.50) → **+3.06**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15