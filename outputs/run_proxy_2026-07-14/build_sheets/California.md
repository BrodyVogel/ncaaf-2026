# California — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-2.45** (rank 82/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB     5 | proxy 5
- RB    41 | proxy 41
- WRTE  85 | proxy 85
- OL    60 | proxy 60
- DL     5 | proxy 5
- LB    50 | proxy —
- DB    50 | proxy —
- ST    10 | proxy 10

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-7.40**

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.7 → 3.7 → 3.7
- FEI      -0.07 → -1.24 → -1.24
- Massey   7.65 → 0.56 → 0.56
- FPI      0.9 → 0.56 → 0.56
- TR       4.0 → 3.34 → 3.34
- PickSix  50 → 4.44 → 4.44
- blend 2.15  (dispersion 5.68)

## 4. Assembly
- anchor +2.15  class -1.68  k×resid -2.59 (k=0.35, cap ±6.0)  ST -0.80  → recentered → **-2.45**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False