# Duke — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+3.12** (rank 47/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    19 | proxy 19
- RB    97 | proxy 97
- WRTE  85 | proxy 85
- OL    66 | proxy 66
- DL    60 | proxy 60
- LB    40 | proxy 40
- DB    19 | proxy 19
- ST    72 | proxy 72

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.20**

## 3. Anchor (per source: raw → normalized → used)
- SP+      5.7 → 5.7 → 5.7
- FEI      0.17 → 3.94 → 3.94
- Massey   7.96 → 6.37 → 6.37
- FPI      3.5 → 3.59 → 3.59
- TR       1.9 → 1.33 → 1.33
- PickSix  54 → 3.56 → 3.56
- blend 4.31  (dispersion 5.03)

## 4. Assembly
- anchor +4.31  class -1.68  k×resid -0.42 (k=0.35, cap ±6.0)  ST +0.44  → recentered → **+3.12**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False