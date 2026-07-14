# Pittsburgh — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+3.11** (rank 48/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    22 | proxy 22
- RB    53 | proxy 53
- WRTE   4 | proxy 4
- OL    51 | proxy 51
- DL    60 | proxy 60
- LB    67 | proxy 67
- DB    53 | proxy 53
- ST    41 | proxy 41

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-7.52**

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.5 → 6.5 → 6.5
- FEI      0.33 → 7.39 → 7.39
- Massey   7.98 → 6.74 → 6.74
- FPI      6.6 → 7.2 → 7.2
- TR       10.0 → 9.09 → 9.09
- PickSix  39 → 6.55 → 6.55
- blend 7.14  (dispersion 2.59)

## 4. Assembly
- anchor +7.14  class -1.68  k×resid -2.63 (k=0.35, cap ±6.0)  ST -0.18  → recentered → **+3.11**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False