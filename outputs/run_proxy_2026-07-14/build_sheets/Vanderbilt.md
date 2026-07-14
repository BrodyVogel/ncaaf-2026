# Vanderbilt — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+10.05** (rank 25/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    81 | proxy 81
- WRTE  96 | proxy 96
- OL    56 | proxy 56
- DL    59 | proxy 59
- LB    85 | proxy 85
- DB    75 | proxy 75
- ST    90 | proxy 90

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+1.92**

## 3. Anchor (per source: raw → normalized → used)
- SP+      10.0 → 10.0 → 10.0
- FEI      0.59 → 12.99 → 12.99
- Massey   8.24 → 11.62 → 11.62
- FPI      9.0 → 10.0 → 10.0
- TR       9.8 → 8.9 → 8.9
- PickSix  46 → 4.85 → 5.0  [WINSORIZED]
- blend 9.79  (dispersion 8.15)

## 4. Assembly
- anchor +9.79  class -1.68  k×resid +0.67 (k=0.35, cap ±6.0)  ST +0.80  → recentered → **+10.05**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False