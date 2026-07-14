# SMU — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+7.26** (rank 30/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    74 | proxy 74
- RB     2 | proxy 2
- WRTE  59 | proxy 59
- OL    85 | proxy 85
- DL    63 | proxy 63
- LB    52 | proxy 52
- DB    47 | proxy 47
- ST    54 | proxy 54

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-10.06**

## 3. Anchor (per source: raw → normalized → used)
- SP+      10.9 → 10.9 → 10.9
- FEI      0.44 → 9.76 → 9.76
- Massey   8.26 → 11.99 → 11.99
- FPI      11.1 → 12.45 → 12.45
- TR       14.4 → 13.3 → 13.3
- PickSix  21 → 14.1 → 14.1
- blend 11.91  (dispersion 4.34)

## 4. Assembly
- anchor +11.91  class -1.68  k×resid -3.52 (k=0.35, cap ±6.0)  ST +0.08  → recentered → **+7.26**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False