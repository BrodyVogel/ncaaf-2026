# UCLA — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+2.58** (rank 51/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    51 | proxy 51
- RB    46 | proxy 46
- WRTE  28 | proxy 28
- OL    34 | proxy 34
- DL    64 | proxy 64
- LB    74 | proxy 74
- DB    64 | proxy 64
- ST    73 | proxy 73

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.66**

## 3. Anchor (per source: raw → normalized → used)
- SP+      5.1 → 5.1 → 5.1
- FEI      0.08 → 2.0 → 2.0
- Massey   7.79 → 3.18 → 3.18
- FPI      0.5 → 0.1 → 0.1
- TR       8.2 → 7.36 → 7.36
- PickSix  49 → 4.5 → 4.5
- blend 3.91  (dispersion 7.27)

## 4. Assembly
- anchor +3.91  class -1.68  k×resid -0.58 (k=0.35, cap ±6.0)  ST +0.46  → recentered → **+2.58**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False