# Kansas State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+6.62** (rank 33/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    74 | proxy 74
- RB    53 | proxy 53
- WRTE  52 | proxy 52
- OL    51 | proxy 51
- DL    46 | proxy 46
- LB    26 | proxy 26
- DB    52 | proxy 52
- ST    92 | proxy 92

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-8.25**

## 3. Anchor (per source: raw → normalized → used)
- SP+      10.4 → 10.4 → 10.4
- FEI      0.6 → 13.21 → 13.21
- Massey   8.21 → 11.06 → 11.06
- FPI      5.1 → 5.46 → 5.46
- TR       10.2 → 9.28 → 9.28
- PickSix  31 → 9.39 → 9.39
- blend 9.88  (dispersion 7.75)

## 4. Assembly
- anchor +9.88  class -1.68  k×resid -2.89 (k=0.35, cap ±6.0)  ST +0.84  → recentered → **+6.62**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False