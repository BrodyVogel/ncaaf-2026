# Oklahoma State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+3.73** (rank 51/138 in hybrid field)  band ±7.46

## 1. Unit grades (LLM real | shadow proxy)
- QB    62 | proxy 76
- RB    60 | proxy 97
- WRTE  55 | proxy 76
- OL    44 | proxy 58
- DL    45 | proxy 42
- LB    52 | proxy 81
- DB    48 | proxy 51
- ST    45 | proxy 7

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.073 RB:+0.096 WRTE:+0.038 OL:+0.081  (R²=0.54)
- def: DL:-0.083 LB:-0.060 DB:-0.096  (R²=0.61)
- grade-implied off +27.60 vs anchor off +28.40
- grade-implied def +25.77 vs anchor def +25.00
- residual (off-minus-def, grades-vs-anchor): **-1.57**
- resid decomposition (diagnostic): level -1.84 (=-0.541x anchor margin - the calibrated fade) + shape +0.27 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      7.1 → 7.1 → 7.1
- FEI      -0.25 → -5.12 → -0.41  [WINSORIZED]
- Massey   7.39 → -4.32 → -0.41  [WINSORIZED]
- FPI      3.3 → 3.36 → 3.36
- TR       6.7 → 5.93 → 5.93
- PickSix  47 → 4.59 → 4.59
- blend 3.89  (dispersion 12.22, FLAGGED

## 4. Assembly
- anchor +3.89  class -0.00  k×resid -0.55 (k=0.35, cap ±6.0)  ST -0.10  → recentered (-0.49) → **+3.73**
- band: 6.0 × coach(1.13) × dispersion(1.10) × conf(1+0.03×0) = ±7.46

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15