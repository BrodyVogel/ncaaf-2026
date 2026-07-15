# Iowa — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+10.72** (rank 21/138 in hybrid field)  band ±6.72

## 1. Unit grades (LLM real | shadow proxy)
- QB    32 | proxy —
- RB    70 | proxy 71
- WRTE  42 | proxy —
- OL    87 | proxy 95
- DL    48 | proxy 31
- LB    58 | proxy 90
- DB    80 | proxy 93
- ST    60 | proxy 94

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.086 LB:-0.057 DB:-0.094  (R²=0.61)
- grade-implied off +29.39 vs anchor off +30.42
- grade-implied def +22.20 vs anchor def +17.18
- residual (off-minus-def, grades-vs-anchor): **-6.05**
- resid decomposition (diagnostic): level -7.16 (=-0.541x anchor margin - the calibrated fade) + shape +1.11 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      13.6 → 13.6 → 13.6
- FEI      0.74 → 16.23 → 16.23
- Massey   8.5 → 16.49 → 16.49
- FPI      10.6 → 11.86 → 11.86
- TR       13.9 → 12.82 → 12.82
- PickSix  24 → 12.23 → 12.23
- blend 13.83  (dispersion 4.63)

## 4. Assembly
- anchor +13.83  class -1.68  k×resid -2.12 (k=0.35, cap ±6.0)  ST +0.20  → recentered (-0.49) → **+10.72**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×4) = ±6.72

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: c091163 (frozen 2026-07-14)