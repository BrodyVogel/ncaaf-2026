# USC — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+13.40** (rank 18/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    85 | proxy 85
- RB    62 | proxy 62
- WRTE  99 | proxy 99
- OL    29 | proxy 29
- DL    80 | proxy 80
- LB    78 | proxy 78
- DB    77 | proxy 77
- ST     9 | proxy 9

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-7.14**

## 3. Anchor (per source: raw → normalized → used)
- SP+      16.8 → 16.8 → 16.8
- FEI      0.79 → 17.31 → 17.31
- Massey   8.53 → 17.05 → 17.05
- FPI      17.0 → 19.32 → 19.32
- TR       20.9 → 19.52 → 19.52
- PickSix  11 → 18.69 → 18.69
- blend 17.93  (dispersion 2.72)

## 4. Assembly
- anchor +17.93  class -1.68  k×resid -2.50 (k=0.35, cap ±6.0)  ST -0.82  → recentered → **+13.40**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False