# Ole Miss — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+15.96** (rank 12/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    95 | proxy 95
- WRTE  43 | proxy 43
- OL    81 | proxy 81
- DL    85 | proxy 85
- LB    43 | proxy 43
- DB    67 | proxy 67
- ST    87 | proxy 87

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-6.96**

## 3. Anchor (per source: raw → normalized → used)
- SP+      15.9 → 15.9 → 15.9
- FEI      0.93 → 20.32 → 20.32
- Massey   8.74 → 20.99 → 20.99
- FPI      16.0 → 18.16 → 18.16
- TR       22.3 → 20.86 → 20.86
- PickSix  10 → 19.93 → 19.93
- blend 18.87  (dispersion 5.09)

## 4. Assembly
- anchor +18.87  class -1.68  k×resid -2.44 (k=0.35, cap ±6.0)  ST +0.74  → recentered → **+15.96**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False