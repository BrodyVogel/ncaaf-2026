# Nevada — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-8.62** (rank 107/138)  band ±6.72

## 1. Unit grades (LLM | shadow proxy)
- QB     1 | proxy 1
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    79 | proxy 79
- LB    50 | proxy —
- DB    31 | proxy 31
- ST    13 | proxy 13

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+12.68**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -12.2 → -12.2 → -12.2
- FEI      -0.77 → -16.33 → -16.33
- Massey   6.88 → -13.88 → -13.88
- FPI      -11.9 → -14.35 → -14.35
- TR       -18.1 → -17.81 → -17.81
- blend -14.46  (dispersion 5.61)

## 4. Assembly
- anchor -14.46  class +1.68  k×resid +4.44 (k=0.35, cap ±6.0)  ST -0.74  → recentered → **-8.62**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×4) = ±6.72
- flags: resid_flag=True, dispersion_flag=False