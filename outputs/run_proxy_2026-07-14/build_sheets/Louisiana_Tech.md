# Louisiana Tech — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-3.46** (rank 86/138)  band ±6.9

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    50 | proxy —
- LB    50 | proxy —
- DB    50 | proxy —
- ST    74 | proxy 74

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+10.50**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.3 → -8.3 → -8.3
- FEI      -0.51 → -10.72 → -10.72
- Massey   7.04 → -10.88 → -10.88
- FPI      -9.6 → -11.67 → -11.67
- TR       -8.6 → -8.72 → -8.72
- blend -9.76  (dispersion 3.37)

## 4. Assembly
- anchor -9.76  class +1.68  k×resid +3.67 (k=0.35, cap ±6.0)  ST +0.48  → recentered → **-3.46**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×7) = ±6.9
- flags: resid_flag=False, dispersion_flag=False