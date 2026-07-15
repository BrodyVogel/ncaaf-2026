# Navy — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+0.31** (rank 63/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    45 | proxy —
- RB    40 | proxy —
- WRTE  38 | proxy —
- OL    48 | proxy 44
- DL    18 | proxy 5
- LB    40 | proxy 16
- DB    32 | proxy 18
- ST    55 | proxy 57

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.085 LB:-0.060 DB:-0.096  (R²=0.62)
- grade-implied off +24.13 vs anchor off +27.39
- grade-implied def +30.39 vs anchor def +27.31
- residual (off-minus-def, grades-vs-anchor): **-6.34**
- resid decomposition (diagnostic): level -0.04 (=-0.541x anchor margin - the calibrated fade) + shape -6.30 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      1.1 → 1.1 → 1.1
- FEI      0.03 → 0.92 → 0.92
- Massey   7.59 → -0.57 → -0.57
- FPI      -0.7 → -1.3 → -1.3
- TR       0.9 → 0.38 → 0.38
- blend 0.27  (dispersion 2.4)

## 4. Assembly
- anchor +0.27  class +1.68  k×resid -2.22 (k=0.35, cap ±6.0)  ST +0.10  → recentered (-0.48) → **+0.31**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15