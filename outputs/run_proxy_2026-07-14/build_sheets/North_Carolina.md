# North Carolina — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+1.85** (rank 54/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    42 | proxy 42
- WRTE  80 | proxy 80
- OL    50 | proxy —
- DL    80 | proxy 80
- LB    50 | proxy —
- DB    65 | proxy 65
- ST    47 | proxy 47

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+3.59**

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.8 → 3.8 → 3.8
- FEI      -0.23 → -4.69 → -2.66  [WINSORIZED]
- Massey   7.57 → -0.94 → -0.94
- FPI      4.9 → 5.22 → 5.22
- TR       2.1 → 1.53 → 1.53
- PickSix  57 → 2.34 → 2.34
- blend 1.87  (dispersion 9.91)

## 4. Assembly
- anchor +1.87  class -1.68  k×resid +1.26 (k=0.35, cap ±6.0)  ST -0.06  → recentered → **+1.85**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False