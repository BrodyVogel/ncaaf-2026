# Georgia — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+23.89** (rank 4/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    88 | proxy 88
- RB    95 | proxy 95
- WRTE  81 | proxy 81
- OL    95 | proxy 95
- DL    81 | proxy 81
- LB    95 | proxy 95
- DB    78 | proxy 78
- ST    78 | proxy 78

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-5.49**

## 3. Anchor (per source: raw → normalized → used)
- SP+      25.5 → 25.5 → 25.5
- FEI      1.34 → 29.16 → 29.16
- Massey   8.89 → 23.8 → 23.8
- FPI      24.8 → 28.41 → 28.41
- TR       28.4 → 26.7 → 26.7
- PickSix  5 → 26.13 → 26.13
- blend 26.46  (dispersion 5.36)

## 4. Assembly
- anchor +26.46  class -1.68  k×resid -1.92 (k=0.35, cap ±6.0)  ST +0.56  → recentered → **+23.89**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False