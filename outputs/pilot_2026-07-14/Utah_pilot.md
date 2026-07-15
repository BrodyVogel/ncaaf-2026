# Utah — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+10.51** (rank 28/138 in hybrid field)  band ±7.46

## 1. Unit grades (LLM real | shadow proxy)
- QB    70 | proxy 68
- RB    65 | proxy 72
- WRTE  52 | proxy 48
- OL    46 | proxy 96
- DL    44 | proxy 66
- LB    46 | proxy 68
- DB    58 | proxy 52
- ST    62 | proxy 81

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.53)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +28.58 vs anchor off +33.66
- grade-implied def +25.27 vs anchor def +20.44
- residual (off-minus-def, grades-vs-anchor): **-9.91**
- resid decomposition (diagnostic): level -7.15 (=-0.541x anchor margin - the calibrated fade) + shape -2.76 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      11.9 → 11.9 → 11.9
- FEI      0.97 → 21.19 → 16.9  [WINSORIZED]
- Massey   8.62 → 18.74 → 16.9  [WINSORIZED]
- FPI      8.5 → 9.42 → 9.42
- TR       12.8 → 11.77 → 11.77
- PickSix  22 → 13.78 → 13.78
- blend 13.22  (dispersion 11.77, FLAGGED

## 4. Assembly
- anchor +13.22  class -0.00  k×resid -3.47 (k=0.35, cap ±6.0)  ST +0.24  → recentered (-0.52) → **+10.51**
- band: 6.0 × coach(1.13) × dispersion(1.10) × conf(1+0.03×0) = ±7.46

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15