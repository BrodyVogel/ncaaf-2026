# TCU — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+6.99** (rank 35/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy —
- RB    52 | proxy 83
- WRTE  50 | proxy 72
- OL    52 | proxy 72
- DL    58 | proxy 46
- LB    42 | proxy —
- DB    52 | proxy 63
- ST    55 | proxy 45

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.095  (R²=0.61)
- grade-implied off +26.09 vs anchor off +31.42
- grade-implied def +24.92 vs anchor def +21.78
- residual (off-minus-def, grades-vs-anchor): **-8.47**
- resid decomposition (diagnostic): level -5.22 (=-0.541x anchor margin - the calibrated fade) + shape -3.26 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      9.1 → 9.1 → 9.1
- FEI      0.43 → 9.54 → 9.54
- Massey   8.23 → 11.43 → 11.43
- FPI      6.4 → 6.97 → 6.97
- TR       8.4 → 7.56 → 7.56
- PickSix  25 → 11.67 → 11.67
- blend 9.34  (dispersion 4.69)

## 4. Assembly
- anchor +9.34  class -0.00  k×resid -2.97 (k=0.35, cap ±6.0)  ST +0.10  → recentered (-0.51) → **+6.99**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15