# Michigan — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+14.91** (rank 18/138 in hybrid field)  band ±6.98

## 1. Unit grades (LLM real | shadow proxy)
- QB    60 | proxy 43
- RB    71 | proxy 88
- WRTE  56 | proxy 79
- OL    64 | proxy 43
- DL    76 | proxy 85
- LB    42 | proxy —
- DB    70 | proxy 80
- ST    55 | proxy 99

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.089 WRTE:+0.035 OL:+0.084  (R²=0.54)
- def: DL:-0.081 LB:-0.061 DB:-0.095  (R²=0.61)
- grade-implied off +30.00 vs anchor off +33.67
- grade-implied def +21.82 vs anchor def +15.33
- residual (off-minus-def, grades-vs-anchor): **-10.16**
- resid decomposition (diagnostic): level -9.92 (=-0.541x anchor margin - the calibrated fade) + shape -0.24 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      16.1 → 16.1 → 16.1
- FEI      0.89 → 19.46 → 19.46
- Massey   8.63 → 18.93 → 18.93
- FPI      15.9 → 18.04 → 18.04
- TR       19.8 → 18.47 → 18.47
- PickSix  14 → 17.85 → 17.85
- blend 17.85  (dispersion 3.36)

## 4. Assembly
- anchor +17.85  class -0.00  k×resid -3.56 (k=0.35, cap ±6.0)  ST +0.10  → recentered (-0.52) → **+14.91**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×1) = ±6.98

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (ec6341a)