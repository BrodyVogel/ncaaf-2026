# Memphis — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+1.71** (rank 54/138 in hybrid field)  band ±7.59

## 1. Unit grades (LLM real | shadow proxy)
- QB    40 | proxy —
- RB    42 | proxy —
- WRTE  45 | proxy 26
- OL    38 | proxy 40
- DL    52 | proxy 33
- LB    30 | proxy —
- DB    74 | proxy 76
- ST    50 | proxy 52

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.092 WRTE:+0.038 OL:+0.082  (R²=0.54)
- def: DL:-0.081 LB:-0.059 DB:-0.099  (R²=0.62)
- grade-implied off +23.38 vs anchor off +28.49
- grade-implied def +23.89 vs anchor def +29.81
- residual (off-minus-def, grades-vs-anchor): **+0.81**
- resid decomposition (diagnostic): level +0.71 (=-0.541x anchor margin - the calibrated fade) + shape +0.09 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.1 → -1.1 → -1.1
- FEI      0.05 → 1.35 → 1.35
- Massey   7.68 → 1.12 → 1.12
- FPI      -1.9 → -2.7 → -2.7
- TR       -1.5 → -1.92 → -1.92
- blend -0.72  (dispersion 4.05)

## 4. Assembly
- anchor -0.72  class +1.68  k×resid +0.28 (k=0.35, cap ±6.0)  ST +0.00  → recentered (-0.46) → **+1.71**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×4) = ±7.59

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-14 (post c091163)