# Houston — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+6.18** (rank 35/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    73 | proxy 73
- RB    50 | proxy —
- WRTE  76 | proxy 76
- OL    62 | proxy 62
- DL    71 | proxy 71
- LB    52 | proxy 52
- DB    70 | proxy 70
- ST    40 | proxy 40

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+0.36**

## 3. Anchor (per source: raw → normalized → used)
- SP+      8.2 → 8.2 → 8.2
- FEI      0.13 → 3.07 → 3.2  [WINSORIZED]
- Massey   7.9 → 5.24 → 5.24
- FPI      7.1 → 7.79 → 7.79
- TR       10.6 → 9.66 → 9.66
- PickSix  30 → 9.97 → 9.97
- blend 7.47  (dispersion 6.89)

## 4. Assembly
- anchor +7.47  class -1.68  k×resid +0.13 (k=0.35, cap ±6.0)  ST -0.20  → recentered → **+6.18**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False