# Louisville — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+8.80** (rank 28/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  75 | proxy 75
- OL    54 | proxy 54
- DL    90 | proxy 90
- LB    50 | proxy —
- DB    63 | proxy 63
- ST    47 | proxy 47

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-5.25**

## 3. Anchor (per source: raw → normalized → used)
- SP+      11.0 → 11.0 → 11.0
- FEI      0.5 → 11.05 → 11.05
- Massey   8.3 → 12.74 → 12.74
- FPI      9.5 → 10.58 → 10.58
- TR       13.7 → 12.63 → 12.63
- PickSix  19 → 14.36 → 14.36
- blend 11.91  (dispersion 3.78)

## 4. Assembly
- anchor +11.91  class -1.68  k×resid -1.84 (k=0.35, cap ±6.0)  ST -0.06  → recentered → **+8.80**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False