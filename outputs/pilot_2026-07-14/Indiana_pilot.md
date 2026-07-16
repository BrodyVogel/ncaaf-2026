# Indiana — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+21.65** (rank 7/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    70 | proxy 87
- RB    62 | proxy 70
- WRTE  65 | proxy 96
- OL    74 | proxy 72
- DL    77 | proxy 82
- LB    77 | proxy 95
- DB    72 | proxy 100
- ST    65 | proxy 94

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.092 WRTE:+0.035 OL:+0.082  (R²=0.53)
- def: DL:-0.083 LB:-0.058 DB:-0.095  (R²=0.61)
- grade-implied off +31.00 vs anchor off +37.88
- grade-implied def +19.39 vs anchor def +13.02
- residual (off-minus-def, grades-vs-anchor): **-13.25**
- resid decomposition (diagnostic): level -13.45 (=-0.541x anchor margin - the calibrated fade) + shape +0.20 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      24.5 → 24.5 → 24.5
- FEI      1.14 → 24.85 → 24.85
- Massey   9.18 → 29.24 → 29.24
- FPI      23.1 → 26.43 → 26.43
- TR       29.0 → 27.27 → 27.27
- PickSix  9 → 20.64 → 21.43  [WINSORIZED]
- blend 25.46  (dispersion 8.6)

## 4. Assembly
- anchor +25.46  class -0.00  k×resid -4.64 (k=0.35, cap ±6.0)  ST +0.30  → recentered (-0.53) → **+21.65**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (1fd56c8)