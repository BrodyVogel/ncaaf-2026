# Nebraska — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+6.96** (rank 35/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    62 | proxy 59
- RB    40 | proxy 84
- WRTE  52 | proxy 40
- OL    66 | proxy 78
- DL    46 | proxy 58
- LB    62 | proxy 78
- DB    65 | proxy 71
- ST    62 | proxy 98

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.093 WRTE:+0.036 OL:+0.083  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +27.38 vs anchor off +29.07
- grade-implied def +23.46 vs anchor def +21.63
- residual (off-minus-def, grades-vs-anchor): **-3.53**
- resid decomposition (diagnostic): level -4.03 (=-0.541x anchor margin - the calibrated fade) + shape +0.50 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      7.7 → 7.7 → 7.7
- FEI      0.25 → 5.66 → 5.66
- Massey   8.0 → 7.12 → 7.12
- FPI      8.8 → 9.77 → 9.77
- TR       8.0 → 7.17 → 7.17
- PickSix  37 → 7.03 → 7.03
- blend 7.45  (dispersion 4.11)

## 4. Assembly
- anchor +7.45  class -0.00  k×resid -1.23 (k=0.35, cap ±6.0)  ST +0.24  → recentered (-0.50) → **+6.96**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (adac096)