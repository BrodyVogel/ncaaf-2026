# Stanford — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-1.32** (rank 73/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    88 | proxy 88
- WRTE  50 | proxy —
- OL    31 | proxy 31
- DL    54 | proxy 54
- LB    61 | proxy 61
- DB    62 | proxy 62
- ST    74 | proxy 74

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+7.39**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.9 → -1.9 → -1.9
- FEI      -0.24 → -4.9 → -4.9
- Massey   7.43 → -3.57 → -3.57
- FPI      -3.3 → -4.33 → -4.33
- TR       -3.0 → -3.36 → -3.36
- PickSix  66 → -2.25 → -2.25
- blend -3.17  (dispersion 3.0)

## 4. Assembly
- anchor -3.17  class -1.68  k×resid +2.59 (k=0.35, cap ±6.0)  ST +0.48  → recentered → **-1.32**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False