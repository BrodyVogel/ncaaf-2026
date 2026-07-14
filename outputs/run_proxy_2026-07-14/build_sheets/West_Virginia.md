# West Virginia — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-2.23** (rank 79/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    20 | proxy 20
- RB    55 | proxy 55
- WRTE  43 | proxy 43
- OL    45 | proxy 45
- DL    33 | proxy 33
- LB    35 | proxy 35
- DB    29 | proxy 29
- ST    61 | proxy 61

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-7.06**

## 3. Anchor (per source: raw → normalized → used)
- SP+      0.8 → 0.8 → 0.8
- FEI      -0.07 → -1.24 → -1.24
- Massey   7.66 → 0.74 → 0.74
- FPI      0.2 → -0.25 → -0.25
- TR       4.5 → 3.82 → 3.82
- PickSix  51 → 3.93 → 3.93
- blend 1.23  (dispersion 5.17)

## 4. Assembly
- anchor +1.23  class -1.68  k×resid -2.47 (k=0.35, cap ±6.0)  ST +0.22  → recentered → **-2.23**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False