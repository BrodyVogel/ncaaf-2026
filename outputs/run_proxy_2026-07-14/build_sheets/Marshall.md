# Marshall — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-5.18** (rank 94/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    53 | proxy 53
- RB    50 | proxy —
- WRTE  35 | proxy 35
- OL    43 | proxy 43
- DL    50 | proxy —
- LB    22 | proxy 22
- DB    12 | proxy 12
- ST    24 | proxy 24

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+2.52**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -6.4 → -6.4 → -6.4
- FEI      -0.3 → -6.2 → -6.2
- Massey   7.22 → -7.51 → -7.51
- FPI      -8.8 → -10.74 → -10.74
- TR       -8.8 → -8.91 → -8.91
- blend -7.69  (dispersion 4.54)

## 4. Assembly
- anchor -7.69  class +1.68  k×resid +0.88 (k=0.35, cap ±6.0)  ST -0.52  → recentered → **-5.18**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False