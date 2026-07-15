# Kansas State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+7.34** (rank 35/138 in hybrid field)  band ±6.78

## 1. Unit grades (LLM real | shadow proxy)
- QB    60 | proxy 74
- RB    52 | proxy 53
- WRTE  52 | proxy 52
- OL    44 | proxy 51
- DL    45 | proxy 46
- LB    44 | proxy 26
- DB    52 | proxy 52
- ST    55 | proxy 92

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.092 WRTE:+0.037 OL:+0.083  (R²=0.54)
- def: DL:-0.083 LB:-0.061 DB:-0.095  (R²=0.62)
- grade-implied off +26.45 vs anchor off +32.84
- grade-implied def +25.91 vs anchor def +23.26
- residual (off-minus-def, grades-vs-anchor): **-9.04**
- resid decomposition (diagnostic): level -5.18 (=-0.541x anchor margin - the calibrated fade) + shape -3.85 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      10.4 → 10.4 → 10.4
- FEI      0.6 → 13.21 → 13.21
- Massey   8.21 → 11.06 → 11.06
- FPI      5.1 → 5.46 → 5.46
- TR       10.2 → 9.28 → 9.28
- PickSix  31 → 9.39 → 9.39
- blend 9.88  (dispersion 7.75)

## 4. Assembly
- anchor +9.88  class -0.00  k×resid -3.16 (k=0.35, cap ±6.0)  ST +0.10  → recentered (-0.52) → **+7.34**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×0) = ±6.78

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15