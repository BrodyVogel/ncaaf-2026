# Tulane — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-0.40** (rank 66/138 in hybrid field)  band ±7.39

## 1. Unit grades (LLM real | shadow proxy)
- QB    45 | proxy 77
- RB    58 | proxy —
- WRTE  46 | proxy 56
- OL    30 | proxy 33
- DL    35 | proxy 10
- LB    28 | proxy 1
- DB    42 | proxy 15
- ST    52 | proxy 76

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.064 DB:-0.095  (R²=0.63)
- grade-implied off +24.63 vs anchor off +25.19
- grade-implied def +28.79 vs anchor def +25.31
- residual (off-minus-def, grades-vs-anchor): **-4.04**
- resid decomposition (diagnostic): level +0.06 (=-0.541x anchor margin - the calibrated fade) + shape -4.10 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.5 → -5.5 → -2.26  [WINSORIZED]
- FEI      0.14 → 3.29 → 3.29
- Massey   7.84 → 4.12 → 4.12
- FPI      2.3 → 2.2 → 2.2
- TR       -2.8 → -3.16 → -2.26  [WINSORIZED]
- blend 0.47  (dispersion 9.62)

## 4. Assembly
- anchor +0.47  class +0.00  k×resid -1.41 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.50) → **-0.40**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×3) = ±7.39

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15