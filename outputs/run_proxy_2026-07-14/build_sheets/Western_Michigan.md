# Western Michigan — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-3.67** (rank 87/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    64 | proxy 64
- RB    19 | proxy 19
- WRTE  17 | proxy 17
- OL     8 | proxy 8
- DL    82 | proxy 82
- LB    50 | proxy —
- DB    29 | proxy 29
- ST    74 | proxy 74

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+1.16**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.2 → -7.2 → -7.2
- FEI      -0.25 → -5.12 → -5.12
- Massey   7.24 → -7.13 → -7.13
- FPI      -4.0 → -5.14 → -5.14
- TR       -8.3 → -8.43 → -8.43
- blend -6.7  (dispersion 3.31)

## 4. Assembly
- anchor -6.70  class +1.68  k×resid +0.41 (k=0.35, cap ±6.0)  ST +0.48  → recentered → **-3.67**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False