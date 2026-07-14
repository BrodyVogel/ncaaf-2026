# Texas A&M — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+17.54** (rank 10/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    61 | proxy 61
- RB    88 | proxy 88
- WRTE  75 | proxy 75
- OL    84 | proxy 84
- DL    70 | proxy 70
- LB    90 | proxy 90
- DB    75 | proxy 75
- ST    88 | proxy 88

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-4.79**

## 3. Anchor (per source: raw → normalized → used)
- SP+      20.3 → 20.3 → 20.3
- FEI      0.85 → 18.6 → 18.6
- Massey   8.49 → 16.3 → 16.3
- FPI      20.0 → 22.81 → 22.81
- TR       22.7 → 21.24 → 21.24
- PickSix  13 → 18.1 → 18.1
- blend 19.67  (dispersion 6.51)

## 4. Assembly
- anchor +19.67  class -1.68  k×resid -1.68 (k=0.35, cap ±6.0)  ST +0.76  → recentered → **+17.54**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False