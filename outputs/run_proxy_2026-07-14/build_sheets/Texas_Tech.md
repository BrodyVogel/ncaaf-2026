# Texas Tech — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+21.49** (rank 7/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    96 | proxy 96
- RB    92 | proxy 92
- WRTE  91 | proxy 91
- OL    87 | proxy 87
- DL    85 | proxy 85
- LB    89 | proxy 89
- DB    93 | proxy 93
- ST    96 | proxy 96

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+0.32**

## 3. Anchor (per source: raw → normalized → used)
- SP+      23.1 → 23.1 → 23.1
- FEI      0.89 → 19.46 → 19.46
- Massey   8.65 → 19.3 → 19.3
- FPI      20.0 → 22.81 → 22.81
- TR       23.8 → 22.3 → 22.3
- PickSix  8 → 21.63 → 21.63
- blend 21.67  (dispersion 3.8)

## 4. Assembly
- anchor +21.67  class -1.68  k×resid +0.11 (k=0.35, cap ±6.0)  ST +0.92  → recentered → **+21.49**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False