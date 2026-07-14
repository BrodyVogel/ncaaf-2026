# LSU — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+14.34** (rank 16/138)  band ±6.6

## 1. Unit grades (LLM | shadow proxy)
- QB    78 | proxy 78
- RB    34 | proxy 34
- WRTE  85 | proxy 85
- OL    69 | proxy 69
- DL    79 | proxy 79
- LB    68 | proxy 68
- DB    64 | proxy 64
- ST    52 | proxy 52

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-9.77**

## 3. Anchor (per source: raw → normalized → used)
- SP+      20.2 → 20.2 → 20.2
- FEI      0.55 → 12.13 → 15.2  [WINSORIZED]
- Massey   8.29 → 12.56 → 15.2  [WINSORIZED]
- FPI      20.0 → 22.81 → 22.81
- TR       22.1 → 20.67 → 20.67
- PickSix  12 → 18.21 → 18.21
- blend 18.93  (dispersion 10.68, FLAGGED)

## 4. Assembly
- anchor +18.93  class -1.68  k×resid -3.42 (k=0.35, cap ±6.0)  ST +0.04  → recentered → **+14.34**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×0) = ±6.6
- flags: resid_flag=False, dispersion_flag=True