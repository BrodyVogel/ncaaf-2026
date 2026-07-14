# Missouri — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+11.81** (rank 20/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    13 | proxy 13
- RB    98 | proxy 98
- WRTE  79 | proxy 79
- OL    98 | proxy 98
- DL    48 | proxy 48
- LB    98 | proxy 98
- DB    51 | proxy 51
- ST    93 | proxy 93

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.67**

## 3. Anchor (per source: raw → normalized → used)
- SP+      14.8 → 14.8 → 14.8
- FEI      0.56 → 12.35 → 12.35
- Massey   8.3 → 12.74 → 12.74
- FPI      12.2 → 13.73 → 13.73
- TR       15.4 → 14.26 → 14.26
- PickSix  27 → 11.5 → 11.5
- blend 13.45  (dispersion 3.3)

## 4. Assembly
- anchor +13.45  class -1.68  k×resid -1.28 (k=0.35, cap ±6.0)  ST +0.86  → recentered → **+11.81**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False