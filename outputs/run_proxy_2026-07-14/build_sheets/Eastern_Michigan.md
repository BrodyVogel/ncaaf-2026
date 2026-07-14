# Eastern Michigan — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-13.63** (rank 126/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE   6 | proxy 6
- OL    14 | proxy 14
- DL     5 | proxy 5
- LB    50 | proxy —
- DB     3 | proxy 3
- ST     3 | proxy 3

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+4.22**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -15.0 → -15.0 → -15.0
- FEI      -0.8 → -16.98 → -16.98
- Massey   6.68 → -17.63 → -17.63
- FPI      -16.3 → -19.47 → -19.47
- TR       -13.9 → -13.79 → -13.79
- blend -16.31  (dispersion 5.68)

## 4. Assembly
- anchor -16.31  class +1.68  k×resid +1.48 (k=0.35, cap ±6.0)  ST -0.94  → recentered → **-13.63**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False