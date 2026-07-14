# Purdue — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-2.78** (rank 84/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    43 | proxy 43
- RB    44 | proxy 44
- WRTE  25 | proxy 25
- OL    32 | proxy 32
- DL    74 | proxy 74
- LB    52 | proxy 52
- DB    19 | proxy 19
- ST    96 | proxy 96

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-0.60**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.9 → -2.9 → -2.9
- FEI      -0.1 → -1.88 → -1.88
- Massey   7.57 → -0.94 → -0.94
- FPI      -0.9 → -1.53 → -1.53
- TR       -2.1 → -2.49 → -2.49
- PickSix  68 → -3.33 → -3.33
- blend -2.28  (dispersion 2.38)

## 4. Assembly
- anchor -2.28  class -1.68  k×resid -0.21 (k=0.35, cap ±6.0)  ST +0.92  → recentered → **-2.78**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False