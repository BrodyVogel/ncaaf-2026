# South Florida — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-2.42** (rank 77/138 in hybrid field)  band ±7.39

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy 62
- RB    38 | proxy —
- WRTE  48 | proxy 20
- OL    32 | proxy 34
- DL    35 | proxy 49
- LB    30 | proxy —
- DB    30 | proxy 19
- ST    48 | proxy 38

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.092 WRTE:+0.039 OL:+0.083  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +23.20 vs anchor off +28.46
- grade-implied def +29.63 vs anchor def +29.14
- residual (off-minus-def, grades-vs-anchor): **-5.76**
- resid decomposition (diagnostic): level +0.37 (=-0.541x anchor margin - the calibrated fade) + shape -6.12 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.8 → -2.8 → -2.8
- FEI      0.1 → 2.43 → 2.43
- Massey   7.74 → 2.24 → 2.24
- FPI      -0.9 → -1.53 → -1.53
- TR       -2.4 → -2.78 → -2.78
- blend -0.87  (dispersion 5.23)

## 4. Assembly
- anchor -0.87  class +0.00  k×resid -2.01 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.50) → **-2.42**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×3) = ±7.39

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15