# Notre Dame — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+24.51** (rank 3/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    95 | proxy 95
- RB    90 | proxy 90
- WRTE  50 | proxy —
- OL    95 | proxy 95
- DL    90 | proxy 90
- LB    94 | proxy 94
- DB    91 | proxy 91
- ST    82 | proxy 82

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-5.67**

## 3. Anchor (per source: raw → normalized → used)
- SP+      25.8 → 25.8 → 25.8
- FEI      1.29 → 28.09 → 28.09
- Massey   9.02 → 26.24 → 26.24
- FPI      25.9 → 29.69 → 29.69
- TR       29.1 → 27.37 → 27.37
- PickSix  4 → 26.51 → 26.51
- blend 27.07  (dispersion 3.89)

## 4. Assembly
- anchor +27.07  class -1.68  k×resid -1.99 (k=0.35, cap ±6.0)  ST +0.64  → recentered → **+24.51**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False