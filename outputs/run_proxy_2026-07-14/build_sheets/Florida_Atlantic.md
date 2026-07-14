# Florida Atlantic — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-8.38** (rank 105/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    57 | proxy 57
- RB    50 | proxy —
- WRTE  54 | proxy 54
- OL    44 | proxy 44
- DL    14 | proxy 14
- LB     5 | proxy 5
- DB     2 | proxy 2
- ST    45 | proxy 45

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+2.53**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.1 → -7.1 → -8.7  [WINSORIZED]
- FEI      -0.65 → -13.74 → -13.74
- Massey   6.86 → -14.26 → -14.26
- FPI      -11.3 → -13.65 → -13.65
- TR       -8.7 → -8.81 → -8.81
- blend -11.31  (dispersion 7.16)

## 4. Assembly
- anchor -11.31  class +1.68  k×resid +0.89 (k=0.35, cap ±6.0)  ST -0.10  → recentered → **-8.38**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False