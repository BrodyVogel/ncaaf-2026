# Florida International — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-14.04** (rank 127/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    36 | proxy 36
- RB     2 | proxy 2
- WRTE   7 | proxy 7
- OL    12 | proxy 12
- DL     0 | proxy 0
- LB    25 | proxy 25
- DB    29 | proxy 29
- ST    47 | proxy 47

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.75**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.7 → -13.7 → -13.7
- FEI      -0.83 → -17.62 → -17.62
- Massey   6.66 → -18.01 → -18.01
- FPI      -12.6 → -15.16 → -15.16
- TR       -15.0 → -14.84 → -14.84
- blend -15.51  (dispersion 4.31)

## 4. Assembly
- anchor -15.51  class +1.68  k×resid -0.61 (k=0.35, cap ±6.0)  ST -0.06  → recentered → **-14.04**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False