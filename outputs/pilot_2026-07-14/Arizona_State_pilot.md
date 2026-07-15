# Arizona State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+2.56** (rank 51/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy 38
- RB    45 | proxy —
- WRTE  56 | proxy 71
- OL    36 | proxy 32
- DL    51 | proxy 57
- LB    50 | proxy 50
- DB    48 | proxy 75
- ST    40 | proxy 20

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.035 OL:+0.083  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.095  (R²=0.61)
- grade-implied off +24.44 vs anchor off +28.46
- grade-implied def +25.41 vs anchor def +20.94
- residual (off-minus-def, grades-vs-anchor): **-8.49**
- resid decomposition (diagnostic): level -4.07 (=-0.541x anchor margin - the calibrated fade) + shape -4.42 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.4 → 6.4 → 6.4
- FEI      0.26 → 5.88 → 5.88
- Massey   8.03 → 7.68 → 7.68
- FPI      4.8 → 5.11 → 5.11
- TR       8.7 → 7.84 → 7.84
- PickSix  32 → 9.18 → 9.18
- blend 6.93  (dispersion 4.08)

## 4. Assembly
- anchor +6.93  class -1.68  k×resid -2.97 (k=0.35, cap ±6.0)  ST -0.20  → recentered (-0.48) → **+2.56**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15