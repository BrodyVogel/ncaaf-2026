# Maryland — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+1.34** (rank 57/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy 50
- RB    25 | proxy 25
- WRTE  24 | proxy 24
- OL    40 | proxy 40
- DL    79 | proxy 79
- LB    78 | proxy 78
- DB    81 | proxy 81
- ST    21 | proxy 21

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+1.48**

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.8 → 3.8 → 3.8
- FEI      0.08 → 2.0 → 2.0
- Massey   7.79 → 3.18 → 3.18
- FPI      1.0 → 0.68 → 0.68
- TR       2.9 → 2.29 → 2.29
- PickSix  56 → 2.62 → 2.62
- blend 2.62  (dispersion 3.12)

## 4. Assembly
- anchor +2.62  class -1.68  k×resid +0.52 (k=0.35, cap ±6.0)  ST -0.58  → recentered → **+1.34**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False