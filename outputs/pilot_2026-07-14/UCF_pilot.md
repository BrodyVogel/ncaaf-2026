# UCF — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+2.05** (rank 58/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 24
- RB    46 | proxy —
- WRTE  48 | proxy 63
- OL    40 | proxy 32
- DL    48 | proxy 57
- LB    52 | proxy 48
- DB    58 | proxy 67
- ST    45 | proxy 77

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.036 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +24.90 vs anchor off +24.56
- grade-implied def +24.58 vs anchor def +22.04
- residual (off-minus-def, grades-vs-anchor): **-2.20**
- resid decomposition (diagnostic): level -1.36 (=-0.541x anchor margin - the calibrated fade) + shape -0.84 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      2.3 → 2.3 → 2.3
- FEI      0.04 → 1.13 → 1.13
- Massey   7.73 → 2.06 → 2.06
- FPI      2.1 → 1.96 → 1.96
- TR       3.3 → 2.67 → 2.67
- PickSix  48 → 4.54 → 4.54
- blend 2.42  (dispersion 3.41)

## 4. Assembly
- anchor +2.42  class -0.00  k×resid -0.77 (k=0.35, cap ±6.0)  ST -0.10  → recentered (-0.50) → **+2.05**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15