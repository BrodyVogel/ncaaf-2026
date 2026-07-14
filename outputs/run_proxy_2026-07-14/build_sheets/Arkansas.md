# Arkansas — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+2.35** (rank 52/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    45 | proxy 45
- WRTE  48 | proxy 48
- OL    69 | proxy 69
- DL    50 | proxy 50
- LB    45 | proxy 45
- DB    66 | proxy 66
- ST    15 | proxy 15

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.61**

## 3. Anchor (per source: raw → normalized → used)
- SP+      5.0 → 5.0 → 5.0
- FEI      0.28 → 6.31 → 6.31
- Massey   7.98 → 6.74 → 6.74
- FPI      4.4 → 4.64 → 4.64
- TR       4.7 → 4.01 → 4.01
- PickSix  58 → 2.07 → 2.07
- blend 4.83  (dispersion 4.67)

## 4. Assembly
- anchor +4.83  class -1.68  k×resid -0.56 (k=0.35, cap ±6.0)  ST -0.70  → recentered → **+2.35**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False