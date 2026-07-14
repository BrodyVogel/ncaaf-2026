# Clemson — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+10.29** (rank 24/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    45 | proxy 45
- WRTE  75 | proxy 75
- OL    48 | proxy 48
- DL    86 | proxy 86
- LB    61 | proxy 61
- DB    84 | proxy 84
- ST    79 | proxy 79

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-4.11**

## 3. Anchor (per source: raw → normalized → used)
- SP+      12.8 → 12.8 → 12.8
- FEI      0.47 → 10.41 → 10.41
- Massey   8.24 → 11.62 → 11.62
- FPI      13.4 → 15.13 → 15.13
- TR       11.6 → 10.62 → 10.62
- PickSix  23 → 13.12 → 13.12
- blend 12.36  (dispersion 4.72)

## 4. Assembly
- anchor +12.36  class -1.68  k×resid -1.44 (k=0.35, cap ±6.0)  ST +0.58  → recentered → **+10.29**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False