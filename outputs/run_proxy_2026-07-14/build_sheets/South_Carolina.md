# South Carolina — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+9.27** (rank 27/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    75 | proxy 75
- RB    50 | proxy —
- WRTE  25 | proxy 25
- OL    47 | proxy 47
- DL    82 | proxy 82
- LB    78 | proxy 78
- DB    85 | proxy 85
- ST    36 | proxy 36

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.73**

## 3. Anchor (per source: raw → normalized → used)
- SP+      12.1 → 12.1 → 12.1
- FEI      0.43 → 9.54 → 9.54
- Massey   8.16 → 10.12 → 10.12
- FPI      11.7 → 13.15 → 13.15
- TR       12.2 → 11.19 → 11.19
- PickSix  28 → 11.37 → 11.37
- blend 11.37  (dispersion 3.6)

## 4. Assembly
- anchor +11.37  class -1.68  k×resid -0.60 (k=0.35, cap ±6.0)  ST -0.28  → recentered → **+9.27**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False