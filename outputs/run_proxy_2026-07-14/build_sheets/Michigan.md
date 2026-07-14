# Michigan — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+14.71** (rank 15/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    43 | proxy 43
- RB    88 | proxy 88
- WRTE  79 | proxy 79
- OL    43 | proxy 43
- DL    85 | proxy 85
- LB    50 | proxy —
- DB    80 | proxy 80
- ST    99 | proxy 99

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-8.32**

## 3. Anchor (per source: raw → normalized → used)
- SP+      16.1 → 16.1 → 16.1
- FEI      0.89 → 19.46 → 19.46
- Massey   8.63 → 18.93 → 18.93
- FPI      15.9 → 18.04 → 18.04
- TR       19.8 → 18.47 → 18.47
- PickSix  14 → 17.85 → 17.85
- blend 17.85  (dispersion 3.36)

## 4. Assembly
- anchor +17.85  class -1.68  k×resid -2.91 (k=0.35, cap ±6.0)  ST +0.98  → recentered → **+14.71**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False