# Charlotte — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-17.71** (rank 135/138)  band ±6.8

## 1. Unit grades (LLM | shadow proxy)
- QB    24 | proxy 24
- RB    50 | proxy —
- WRTE  80 | proxy 80
- OL    31 | proxy 31
- DL     0 | proxy 0
- LB     2 | proxy 2
- DB    26 | proxy 26
- ST     4 | proxy 4

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+11.62**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -32.4 → -32.4 → -26.89  [WINSORIZED]
- FEI      -1.06 → -22.58 → -22.58
- Massey   6.49 → -21.19 → -21.19
- FPI      -14.6 → -17.49 → -17.69  [WINSORIZED]
- TR       -23.3 → -22.79 → -22.79
- blend -23.0  (dispersion 14.91, FLAGGED)

## 4. Assembly
- anchor -23.00  class +1.68  k×resid +4.07 (k=0.35, cap ±6.0)  ST -0.92  → recentered → **-17.71**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×1) = ±6.8
- flags: resid_flag=True, dispersion_flag=True