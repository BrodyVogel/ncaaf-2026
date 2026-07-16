# Michigan State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+0.04** (rank 64/138 in hybrid field)  band ±6.78

## 1. Unit grades (LLM real | shadow proxy)
- QB    53 | proxy 50
- RB    48 | proxy 31
- WRTE  38 | proxy —
- OL    46 | proxy 46
- DL    44 | proxy —
- LB    53 | proxy 52
- DB    44 | proxy 50
- ST    26 | proxy 2

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.093 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +25.26 vs anchor off +26.87
- grade-implied def +26.18 vs anchor def +25.73
- residual (off-minus-def, grades-vs-anchor): **-2.06**
- resid decomposition (diagnostic): level -0.62 (=-0.541x anchor margin - the calibrated fade) + shape -1.44 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      0.4 → 0.4 → 0.4
- FEI      -0.02 → -0.16 → -0.16
- Massey   7.82 → 3.74 → 3.74
- FPI      0.3 → -0.13 → -0.13
- TR       -0.3 → -0.77 → -0.77
- PickSix  59 → 1.77 → 1.77
- blend 0.75  (dispersion 4.51)

## 4. Assembly
- anchor +0.75  class -0.00  k×resid -0.72 (k=0.35, cap ±6.0)  ST -0.48  → recentered (-0.49) → **+0.04**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×0) = ±6.78

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (d4c47dc)