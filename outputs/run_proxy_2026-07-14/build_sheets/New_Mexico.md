# New Mexico — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-1.69** (rank 75/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    35 | proxy 35
- RB    50 | proxy —
- WRTE   2 | proxy 2
- OL    17 | proxy 17
- DL    53 | proxy 53
- LB    74 | proxy 74
- DB    36 | proxy 36
- ST    56 | proxy 56

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+0.10**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -0.5 → -0.5 → -0.94  [WINSORIZED]
- FEI      -0.37 → -7.71 → -7.71
- Massey   7.23 → -7.32 → -7.32
- FPI      -3.5 → -4.56 → -4.56
- TR       -2.1 → -2.49 → -2.49
- blend -3.99  (dispersion 7.21)

## 4. Assembly
- anchor -3.99  class +1.68  k×resid +0.04 (k=0.35, cap ±6.0)  ST +0.12  → recentered → **-1.69**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False