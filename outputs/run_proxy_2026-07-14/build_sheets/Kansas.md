# Kansas — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-0.03** (rank 64/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    40 | proxy 40
- RB    23 | proxy 23
- WRTE  25 | proxy 25
- OL    46 | proxy 46
- DL    57 | proxy 57
- LB    31 | proxy 31
- DB    29 | proxy 29
- ST    78 | proxy 78

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-9.69**

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.7 → 3.7 → 3.7
- FEI      0.28 → 6.31 → 6.31
- Massey   7.93 → 5.81 → 5.81
- FPI      2.8 → 2.78 → 2.78
- TR       5.4 → 4.68 → 4.68
- PickSix  61 → 1.14 → 1.14
- blend 4.02  (dispersion 5.17)

## 4. Assembly
- anchor +4.02  class -1.68  k×resid -3.39 (k=0.35, cap ±6.0)  ST +0.56  → recentered → **-0.03**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False