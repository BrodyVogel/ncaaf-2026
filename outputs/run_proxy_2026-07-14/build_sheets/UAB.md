# UAB — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-13.02** (rank 125/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    52 | proxy 52
- RB    27 | proxy 27
- WRTE  50 | proxy —
- OL    74 | proxy 74
- DL    13 | proxy 13
- LB    31 | proxy 31
- DB     5 | proxy 5
- ST     1 | proxy 1

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+9.08**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -18.1 → -18.1 → -18.1
- FEI      -0.7 → -14.82 → -14.82
- Massey   6.73 → -16.69 → -16.69
- FPI      -15.5 → -18.54 → -18.54
- TR       -18.2 → -17.9 → -17.9
- blend -17.36  (dispersion 3.72)

## 4. Assembly
- anchor -17.36  class +1.68  k×resid +3.18 (k=0.35, cap ±6.0)  ST -0.98  → recentered → **-13.02**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False