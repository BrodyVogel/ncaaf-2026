# Central Michigan — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-11.13** (rank 117/138)  band ±6.72

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL     4 | proxy 4
- DL     0 | proxy 0
- LB    50 | proxy —
- DB    15 | proxy 15
- ST     7 | proxy 7

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+2.54**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -12.4 → -12.4 → -12.4
- FEI      -0.64 → -13.53 → -13.53
- Massey   6.9 → -13.51 → -13.51
- FPI      -12.8 → -15.4 → -15.4
- TR       -12.6 → -12.54 → -12.54
- blend -13.3  (dispersion 3.0)

## 4. Assembly
- anchor -13.30  class +1.68  k×resid +0.89 (k=0.35, cap ±6.0)  ST -0.86  → recentered → **-11.13**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×4) = ±6.72
- flags: resid_flag=False, dispersion_flag=False