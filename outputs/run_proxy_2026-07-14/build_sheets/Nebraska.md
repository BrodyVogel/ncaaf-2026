# Nebraska — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+8.37** (rank 29/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    59 | proxy 59
- RB    84 | proxy 84
- WRTE  40 | proxy 40
- OL    78 | proxy 78
- DL    58 | proxy 58
- LB    78 | proxy 78
- DB    71 | proxy 71
- ST    98 | proxy 98

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+3.34**

## 3. Anchor (per source: raw → normalized → used)
- SP+      7.7 → 7.7 → 7.7
- FEI      0.25 → 5.66 → 5.66
- Massey   8.0 → 7.12 → 7.12
- FPI      8.8 → 9.77 → 9.77
- TR       8.0 → 7.17 → 7.17
- PickSix  37 → 7.03 → 7.03
- blend 7.45  (dispersion 4.11)

## 4. Assembly
- anchor +7.45  class -1.68  k×resid +1.17 (k=0.35, cap ±6.0)  ST +0.96  → recentered → **+8.37**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False