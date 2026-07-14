# Tulsa — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-6.77** (rank 100/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    15 | proxy 15
- RB    30 | proxy 30
- WRTE  34 | proxy 34
- OL    38 | proxy 38
- DL    33 | proxy 33
- LB    29 | proxy 29
- DB    64 | proxy 64
- ST    63 | proxy 63

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+5.04**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.6 → -7.6 → -7.6
- FEI      -0.66 → -13.96 → -13.96
- Massey   6.81 → -15.19 → -15.19
- FPI      -9.0 → -10.97 → -10.97
- TR       -10.3 → -10.34 → -10.34
- blend -10.94  (dispersion 7.59)

## 4. Assembly
- anchor -10.94  class +1.68  k×resid +1.76 (k=0.35, cap ±6.0)  ST +0.26  → recentered → **-6.77**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False