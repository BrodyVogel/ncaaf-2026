# Delaware — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-11.27** (rank 119/138)  band ±6.6

## 1. Unit grades (LLM | shadow proxy)
- QB    21 | proxy 21
- RB     7 | proxy 7
- WRTE  51 | proxy 51
- OL    31 | proxy 31
- DL    48 | proxy 48
- LB    18 | proxy 18
- DB    21 | proxy 21
- ST    39 | proxy 39

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+1.90**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.0 → -13.0 → -13.0
- FEI      -0.8 → -16.98 → -16.98
- Massey   6.56 → -19.88 → -17.72  [WINSORIZED]
- FPI      -6.6 → -8.17 → -9.99  [WINSORIZED]
- TR       -12.5 → -12.45 → -12.45
- blend -13.86  (dispersion 11.71, FLAGGED)

## 4. Assembly
- anchor -13.86  class +1.68  k×resid +0.66 (k=0.35, cap ±6.0)  ST -0.22  → recentered → **-11.27**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×0) = ±6.6
- flags: resid_flag=False, dispersion_flag=True