# Wisconsin — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+5.49** (rank 42/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    62 | proxy 49
- RB    58 | proxy 49
- WRTE  44 | proxy —
- OL    48 | proxy 47
- DL    52 | proxy 43
- LB    74 | proxy 89
- DB    62 | proxy 77
- ST    48 | proxy 87

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.086 LB:-0.056 DB:-0.095  (R²=0.61)
- grade-implied off +27.26 vs anchor off +22.41
- grade-implied def +22.66 vs anchor def +16.69
- residual (off-minus-def, grades-vs-anchor): **-1.12**
- resid decomposition (diagnostic): level -3.09 (=-0.541x anchor margin - the calibrated fade) + shape +1.97 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      1.8 → 1.8 → 2.24  [WINSORIZED]
- FEI      0.27 → 6.09 → 6.09
- Massey   8.02 → 7.49 → 7.49
- FPI      4.8 → 5.11 → 5.11
- TR       8.4 → 7.56 → 7.56
- PickSix  36 → 7.24 → 7.24
- blend 5.42  (dispersion 5.76)

## 4. Assembly
- anchor +5.42  class -0.00  k×resid -0.39 (k=0.35, cap ±6.0)  ST -0.04  → recentered (-0.50) → **+5.49**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (abf95f8)