# UTSA — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-1.25** (rank 73/138 in hybrid field)  band ±6.72

## 1. Unit grades (LLM real | shadow proxy)
- QB    55 | proxy 50
- RB    58 | proxy 88
- WRTE  48 | proxy 57
- OL    30 | proxy 38
- DL    20 | proxy 1
- LB    30 | proxy 19
- DB    23 | proxy 11
- ST    52 | proxy 16

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.085 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +25.40 vs anchor off +29.23
- grade-implied def +31.63 vs anchor def +31.47
- residual (off-minus-def, grades-vs-anchor): **-3.99**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.5 → -1.5 → -1.5
- FEI      -0.02 → -0.16 → -0.16
- Massey   7.57 → -0.94 → -0.94
- FPI      -5.3 → -6.66 → -6.22  [WINSORIZED]
- TR       -1.5 → -1.92 → -1.92
- blend -2.04  (dispersion 6.5)

## 4. Assembly
- anchor -2.04  class +1.68  k×resid -1.40 (k=0.35, cap ±6.0)  ST +0.04  → recentered (-0.47) → **-1.25**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×4) = ±6.72

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15