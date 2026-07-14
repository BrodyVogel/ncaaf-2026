# Old Dominion — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-2.09** (rank 78/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    57 | proxy 57
- RB    30 | proxy 30
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL     9 | proxy 9
- LB    50 | proxy —
- DB    66 | proxy 66
- ST    25 | proxy 25

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+0.84**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.8 → -5.8 → -5.8
- FEI      -0.03 → -0.38 → -0.38
- Massey   7.53 → -1.69 → -1.69
- FPI      -4.4 → -5.61 → -5.61
- TR       -4.6 → -4.89 → -4.89
- blend -4.03  (dispersion 5.42)

## 4. Assembly
- anchor -4.03  class +1.68  k×resid +0.29 (k=0.35, cap ±6.0)  ST -0.50  → recentered → **-2.09**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False