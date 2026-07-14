# Sam Houston — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-19.70** (rank 137/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB     0 | proxy 0
- RB    50 | proxy —
- WRTE   4 | proxy 4
- OL    16 | proxy 16
- DL     1 | proxy 1
- LB     2 | proxy 2
- DB     2 | proxy 2
- ST    65 | proxy 65

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+4.42**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -26.3 → -26.3 → -26.3
- FEI      -1.02 → -21.72 → -21.72
- Massey   6.43 → -22.32 → -22.32
- FPI      -18.4 → -21.92 → -21.92
- TR       -24.1 → -23.55 → -23.55
- blend -23.69  (dispersion 4.58)

## 4. Assembly
- anchor -23.69  class +1.68  k×resid +1.55 (k=0.35, cap ±6.0)  ST +0.30  → recentered → **-19.70**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False