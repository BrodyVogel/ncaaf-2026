# Iowa — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+12.81** (rank 19/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    71 | proxy 71
- WRTE  50 | proxy —
- OL    95 | proxy 95
- DL    31 | proxy 31
- LB    90 | proxy 90
- DB    93 | proxy 93
- ST    94 | proxy 94

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.96**

## 3. Anchor (per source: raw → normalized → used)
- SP+      13.6 → 13.6 → 13.6
- FEI      0.74 → 16.23 → 16.23
- Massey   8.5 → 16.49 → 16.49
- FPI      10.6 → 11.86 → 11.86
- TR       13.9 → 12.82 → 12.82
- PickSix  24 → 12.23 → 12.23
- blend 13.83  (dispersion 4.63)

## 4. Assembly
- anchor +13.83  class -1.68  k×resid -0.69 (k=0.35, cap ±6.0)  ST +0.88  → recentered → **+12.81**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False