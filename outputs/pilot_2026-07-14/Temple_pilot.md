# Temple — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-7.72** (rank 102/138 in hybrid field)  band ±6.72

## 1. Unit grades (LLM real | shadow proxy)
- QB    35 | proxy —
- RB    40 | proxy —
- WRTE  55 | proxy 75
- OL    58 | proxy 69
- DL    15 | proxy —
- LB    25 | proxy 8
- DB    14 | proxy 2
- ST    45 | proxy 31

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.091 WRTE:+0.038 OL:+0.084  (R²=0.54)
- def: DL:-0.085 LB:-0.057 DB:-0.095  (R²=0.61)
- grade-implied off +24.96 vs anchor off +24.12
- grade-implied def +33.09 vs anchor def +35.38
- residual (off-minus-def, grades-vs-anchor): **+3.13**
- resid decomposition (diagnostic): level +6.09 (=-0.541x anchor margin - the calibrated fade) + shape -2.96 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.7 → -8.7 → -8.7
- FEI      -0.64 → -13.53 → -13.53
- Massey   6.94 → -12.76 → -12.76
- FPI      -8.6 → -10.5 → -10.5
- TR       -10.9 → -10.92 → -10.92
- blend -10.85  (dispersion 4.83)

## 4. Assembly
- anchor -10.85  class +1.68  k×resid +1.10 (k=0.35, cap ±6.0)  ST -0.10  → recentered (-0.46) → **-7.72**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×4) = ±6.72

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15