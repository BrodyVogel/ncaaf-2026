# BYU — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+13.63** (rank 17/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    83 | proxy 83
- RB    95 | proxy 95
- WRTE  51 | proxy 51
- OL    69 | proxy 69
- DL    57 | proxy 57
- LB    30 | proxy 30
- DB    90 | proxy 90
- ST    99 | proxy 99

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.26**

## 3. Anchor (per source: raw → normalized → used)
- SP+      15.5 → 15.5 → 15.5
- FEI      0.61 → 13.42 → 13.42
- Massey   8.34 → 13.49 → 13.49
- FPI      13.1 → 14.78 → 14.78
- TR       14.6 → 13.49 → 13.49
- PickSix  17 → 16.36 → 16.36
- blend 14.65  (dispersion 2.93)

## 4. Assembly
- anchor +14.65  class -1.68  k×resid -0.79 (k=0.35, cap ±6.0)  ST +0.98  → recentered → **+13.63**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False