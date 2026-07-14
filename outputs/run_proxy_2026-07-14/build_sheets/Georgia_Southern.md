# Georgia Southern — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-8.63** (rank 108/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    80 | proxy 80
- WRTE  50 | proxy —
- OL    27 | proxy 27
- DL     7 | proxy 7
- LB     7 | proxy 7
- DB     9 | proxy 9
- ST    13 | proxy 13

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+2.43**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.9 → -8.9 → -8.9
- FEI      -0.6 → -12.67 → -12.67
- Massey   6.95 → -12.57 → -12.57
- FPI      -8.7 → -10.62 → -10.62
- TR       -11.7 → -11.68 → -11.68
- blend -10.89  (dispersion 3.77)

## 4. Assembly
- anchor -10.89  class +1.68  k×resid +0.85 (k=0.35, cap ±6.0)  ST -0.74  → recentered → **-8.63**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False