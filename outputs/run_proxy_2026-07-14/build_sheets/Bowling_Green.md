# Bowling Green — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-10.75** (rank 115/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB     7 | proxy 7
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    10 | proxy 10
- LB    58 | proxy 58
- DB    18 | proxy 18
- ST    44 | proxy 44

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+5.89**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.3 → -13.3 → -13.3
- FEI      -0.71 → -15.04 → -15.04
- Massey   6.9 → -13.51 → -13.51
- FPI      -13.7 → -16.44 → -16.44
- TR       -17.7 → -17.43 → -17.43
- blend -14.84  (dispersion 4.13)

## 4. Assembly
- anchor -14.84  class +1.68  k×resid +2.06 (k=0.35, cap ±6.0)  ST -0.12  → recentered → **-10.75**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False