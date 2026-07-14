# Rice — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-11.60** (rank 120/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    35 | proxy 35
- WRTE  50 | proxy —
- OL    43 | proxy 43
- DL    12 | proxy 12
- LB    50 | proxy —
- DB     1 | proxy 1
- ST    30 | proxy 30

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+7.34**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -14.7 → -14.7 → -14.7
- FEI      -0.85 → -18.06 → -18.06
- Massey   6.72 → -16.88 → -16.88
- FPI      -13.4 → -16.09 → -16.09
- TR       -15.2 → -15.03 → -15.03
- blend -15.91  (dispersion 3.36)

## 4. Assembly
- anchor -15.91  class +1.68  k×resid +2.57 (k=0.35, cap ±6.0)  ST -0.40  → recentered → **-11.60**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False