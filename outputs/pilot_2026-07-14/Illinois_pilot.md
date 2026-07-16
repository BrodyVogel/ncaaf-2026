# Illinois — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+5.75** (rank 41/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    62 | proxy 82
- RB    32 | proxy 33
- WRTE  48 | proxy 53
- OL    38 | proxy 19
- DL    41 | proxy 44
- LB    46 | proxy 61
- DB    62 | proxy 64
- ST    30 | proxy 33

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.066 RB:+0.094 WRTE:+0.036 OL:+0.086  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +23.96 vs anchor off +31.37
- grade-implied def +25.13 vs anchor def +22.83
- residual (off-minus-def, grades-vs-anchor): **-9.71**
- resid decomposition (diagnostic): level -4.62 (=-0.541x anchor margin - the calibrated fade) + shape -5.09 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      9.3 → 9.3 → 9.3
- FEI      0.52 → 11.48 → 11.48
- Massey   8.21 → 11.06 → 11.06
- FPI      6.3 → 6.85 → 6.85
- TR       9.2 → 8.32 → 8.32
- PickSix  38 → 6.91 → 6.91
- blend 9.03  (dispersion 4.63)

## 4. Assembly
- anchor +9.03  class -0.00  k×resid -3.40 (k=0.35, cap ±6.0)  ST -0.40  → recentered (-0.51) → **+5.75**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (511c1b2)