# Texas — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+21.57** (rank 6/138)  band ±6.6

## 1. Unit grades (LLM | shadow proxy)
- QB    97 | proxy 97
- RB    86 | proxy 86
- WRTE  85 | proxy 85
- OL    92 | proxy 92
- DL    82 | proxy 82
- LB    78 | proxy 78
- DB    93 | proxy 93
- ST    70 | proxy 70

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.13**

## 3. Anchor (per source: raw → normalized → used)
- SP+      23.7 → 23.7 → 23.7
- FEI      0.88 → 19.25 → 19.25
- Massey   8.7 → 20.24 → 20.24
- FPI      26.9 → 30.85 → 26.68  [WINSORIZED]
- TR       28.4 → 26.7 → 26.68  [WINSORIZED]
- PickSix  7 → 21.68 → 21.68
- blend 23.13  (dispersion 11.61, FLAGGED)

## 4. Assembly
- anchor +23.13  class -1.68  k×resid -0.75 (k=0.35, cap ±6.0)  ST +0.40  → recentered → **+21.57**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×0) = ±6.6
- flags: resid_flag=False, dispersion_flag=True