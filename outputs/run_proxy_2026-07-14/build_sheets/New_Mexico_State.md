# New Mexico State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-14.34** (rank 130/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    10 | proxy 10
- RB    50 | proxy —
- WRTE   6 | proxy 6
- OL    15 | proxy 15
- DL     6 | proxy 6
- LB    26 | proxy 26
- DB    12 | proxy 12
- ST    84 | proxy 84

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+2.78**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -16.4 → -16.4 → -16.4
- FEI      -0.89 → -18.92 → -18.92
- Massey   6.54 → -20.26 → -20.26
- FPI      -15.7 → -18.77 → -18.77
- TR       -18.4 → -18.1 → -18.1
- blend -18.14  (dispersion 3.86)

## 4. Assembly
- anchor -18.14  class +1.68  k×resid +0.97 (k=0.35, cap ±6.0)  ST +0.68  → recentered → **-14.34**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False