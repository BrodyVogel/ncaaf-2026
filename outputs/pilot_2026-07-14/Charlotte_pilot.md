# Charlotte — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-19.14** (rank 135/138 in hybrid field)  band ±7.59

## 1. Unit grades (LLM real | shadow proxy)
- QB    38 | proxy 24
- RB    35 | proxy —
- WRTE  44 | proxy 80
- OL    18 | proxy 31
- DL    14 | proxy 0
- LB    30 | proxy 2
- DB    20 | proxy 26
- ST    22 | proxy 4

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.067 RB:+0.091 WRTE:+0.043 OL:+0.080  (R²=0.54)
- def: DL:-0.082 LB:-0.057 DB:-0.097  (R²=0.61)
- grade-implied off +21.09 vs anchor off +15.10
- grade-implied def +32.28 vs anchor def +37.60
- residual (off-minus-def, grades-vs-anchor): **+11.30**
- resid decomposition (diagnostic): level +12.17 (=-0.541x anchor margin - the calibrated fade) + shape -0.87 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -32.4 → -32.4 → -26.89  [WINSORIZED]
- FEI      -1.06 → -22.58 → -22.58
- Massey   6.49 → -21.19 → -21.19
- FPI      -14.6 → -17.49 → -17.69  [WINSORIZED]
- TR       -23.3 → -22.79 → -22.79
- blend -23.0  (dispersion 14.91, FLAGGED

## 4. Assembly
- anchor -23.00  class +0.00  k×resid +3.96 (k=0.35, cap ±6.0)  ST -0.56  → recentered (-0.46) → **-19.14**
- band: 6.0 × coach(1.0) × dispersion(1.10) × conf(1+0.03×5) = ±7.59

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15