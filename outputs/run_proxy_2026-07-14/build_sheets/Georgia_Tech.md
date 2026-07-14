# Georgia Tech — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+3.68** (rank 44/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    66 | proxy 66
- WRTE  12 | proxy 12
- OL    50 | proxy —
- DL    33 | proxy 33
- LB    50 | proxy —
- DB    67 | proxy 67
- ST    85 | proxy 85

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.96**

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.0 → 6.0 → 6.0
- FEI      0.2 → 4.58 → 4.58
- Massey   8.01 → 7.31 → 7.31
- FPI      4.2 → 4.41 → 4.41
- TR       5.8 → 5.07 → 5.07
- PickSix  40 → 5.71 → 5.71
- blend 5.58  (dispersion 2.9)

## 4. Assembly
- anchor +5.58  class -1.68  k×resid -1.38 (k=0.35, cap ±6.0)  ST +0.70  → recentered → **+3.68**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False