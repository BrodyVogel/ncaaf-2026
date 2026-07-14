# Temple — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-6.50** (rank 98/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  75 | proxy 75
- OL    69 | proxy 69
- DL    50 | proxy —
- LB     8 | proxy 8
- DB     2 | proxy 2
- ST    31 | proxy 31

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+7.40**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.7 → -8.7 → -8.7
- FEI      -0.64 → -13.53 → -13.53
- Massey   6.94 → -12.76 → -12.76
- FPI      -8.6 → -10.5 → -10.5
- TR       -10.9 → -10.92 → -10.92
- blend -10.85  (dispersion 4.83)

## 4. Assembly
- anchor -10.85  class +1.68  k×resid +2.59 (k=0.35, cap ±6.0)  ST -0.38  → recentered → **-6.50**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False