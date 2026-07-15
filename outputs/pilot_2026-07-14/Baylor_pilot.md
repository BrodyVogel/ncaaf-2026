# Baylor — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+1.59** (rank 55/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 57
- RB    44 | proxy 45
- WRTE  44 | proxy 87
- OL    40 | proxy 36
- DL    47 | proxy 50
- LB    38 | proxy 20
- DB    52 | proxy 60
- ST    52 | proxy 97

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.094 WRTE:+0.033 OL:+0.084  (R²=0.54)
- def: DL:-0.084 LB:-0.057 DB:-0.097  (R²=0.62)
- grade-implied off +24.52 vs anchor off +32.30
- grade-implied def +26.02 vs anchor def +28.20
- residual (off-minus-def, grades-vs-anchor): **-5.60**
- resid decomposition (diagnostic): level -2.22 (=-0.541x anchor margin - the calibrated fade) + shape -3.38 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      4.5 → 4.5 → 4.5
- FEI      0.2 → 4.58 → 4.58
- Massey   7.86 → 4.49 → 4.49
- FPI      6.5 → 7.09 → 7.09
- TR       4.6 → 3.92 → 3.92
- PickSix  52 → 3.81 → 3.81
- blend 4.7  (dispersion 3.28)

## 4. Assembly
- anchor +4.70  class -1.68  k×resid -1.96 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.49) → **+1.59**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15