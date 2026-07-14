# Alabama — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+17.57** (rank 9/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    92 | proxy 92
- RB    50 | proxy —
- WRTE  69 | proxy 69
- OL    98 | proxy 98
- DL    72 | proxy 72
- LB    50 | proxy —
- DB   100 | proxy 100
- ST    81 | proxy 81

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-5.62**

## 3. Anchor (per source: raw → normalized → used)
- SP+      18.2 → 18.2 → 18.2
- FEI      1.07 → 23.34 → 23.34
- Massey   8.74 → 20.99 → 20.99
- FPI      20.1 → 22.93 → 22.93
- TR       21.6 → 20.19 → 20.19
- PickSix  16 → 17.06 → 17.06
- blend 20.13  (dispersion 6.28)

## 4. Assembly
- anchor +20.13  class -1.68  k×resid -1.97 (k=0.35, cap ±6.0)  ST +0.62  → recentered → **+17.57**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False