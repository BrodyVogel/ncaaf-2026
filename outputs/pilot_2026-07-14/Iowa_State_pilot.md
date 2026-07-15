# Iowa State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-0.00** (rank 63/138 in hybrid field)  band ±8.13

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy 47
- RB    42 | proxy —
- WRTE  40 | proxy 43
- OL    32 | proxy 26
- DL    46 | proxy 60
- LB    40 | proxy —
- DB    40 | proxy 40
- ST    52 | proxy 21

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.082 LB:-0.059 DB:-0.097  (R²=0.62)
- grade-implied off +23.31 vs anchor off +22.89
- grade-implied def +27.20 vs anchor def +22.41
- residual (off-minus-def, grades-vs-anchor): **-4.38**
- resid decomposition (diagnostic): level -0.26 (=-0.541x anchor margin - the calibrated fade) + shape -4.12 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      1.0 → 1.0 → 1.0
- FEI      0.43 → 9.54 → 4.52  [WINSORIZED]
- Massey   8.26 → 11.99 → 4.52  [WINSORIZED]
- FPI      -0.9 → -1.53 → -1.53
- TR       0.0 → -0.48 → -0.48
- PickSix  65 → -2.11 → -2.11
- blend 0.99  (dispersion 14.1, FLAGGED

## 4. Assembly
- anchor +0.99  class -0.00  k×resid -1.53 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.50) → **-0.00**
- band: 6.0 × coach(1.13) × dispersion(1.10) × conf(1+0.03×3) = ±8.13

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15