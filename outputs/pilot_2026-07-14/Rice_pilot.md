# Rice — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-12.76** (rank 117/138 in hybrid field)  band ±6.54

## 1. Unit grades (LLM real | shadow proxy)
- QB    38 | proxy —
- RB    48 | proxy 35
- WRTE  30 | proxy —
- OL    42 | proxy 43
- DL    30 | proxy 12
- LB    18 | proxy —
- DB    12 | proxy 1
- ST    52 | proxy 30

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.089 WRTE:+0.038 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +23.63 vs anchor off +16.39
- grade-implied def +32.50 vs anchor def +32.81
- residual (off-minus-def, grades-vs-anchor): **+7.56**
- resid decomposition (diagnostic): level +8.88 (=-0.541x anchor margin - the calibrated fade) + shape -1.33 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -14.7 → -14.7 → -14.7
- FEI      -0.85 → -18.06 → -18.06
- Massey   6.72 → -16.88 → -16.88
- FPI      -13.4 → -16.09 → -16.09
- TR       -15.2 → -15.03 → -15.03
- blend -15.91  (dispersion 3.36)

## 4. Assembly
- anchor -15.91  class +0.00  k×resid +2.65 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.47) → **-12.76**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×3) = ±6.54

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15