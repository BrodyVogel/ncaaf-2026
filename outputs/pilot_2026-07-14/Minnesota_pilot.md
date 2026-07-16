# Minnesota — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+5.25** (rank 44/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    58 | proxy 48
- RB    54 | proxy 51
- WRTE  44 | proxy 35
- OL    60 | proxy 60
- DL    64 | proxy 64
- LB    55 | proxy 76
- DB    64 | proxy 88
- ST    56 | proxy 100

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +27.58 vs anchor off +25.04
- grade-implied def +22.48 vs anchor def +19.76
- residual (off-minus-def, grades-vs-anchor): **-0.17**
- resid decomposition (diagnostic): level -2.86 (=-0.541x anchor margin - the calibrated fade) + shape +2.69 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      5.2 → 5.2 → 5.2
- FEI      0.2 → 4.58 → 4.58
- Massey   7.89 → 5.06 → 5.06
- FPI      0.6 → 0.21 → 0.21
- TR       8.1 → 7.27 → 7.27
- PickSix  44 → 5.28 → 5.28
- blend 4.69  (dispersion 7.05)

## 4. Assembly
- anchor +4.69  class -0.00  k×resid -0.06 (k=0.35, cap ±6.0)  ST +0.12  → recentered (-0.50) → **+5.25**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (056d942)