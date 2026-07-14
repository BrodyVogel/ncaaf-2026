# Kentucky — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+3.72** (rank 43/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  40 | proxy 40
- OL    73 | proxy 73
- DL    72 | proxy 72
- LB    50 | proxy —
- DB    64 | proxy 64
- ST    19 | proxy 19

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-0.17**

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.8 → 3.8 → 3.8
- FEI      0.27 → 6.09 → 6.09
- Massey   7.98 → 6.74 → 6.74
- FPI      5.4 → 5.81 → 5.81
- TR       8.9 → 8.03 → 8.03
- PickSix  45 → 4.97 → 4.97
- blend 5.61  (dispersion 4.23)

## 4. Assembly
- anchor +5.61  class -1.68  k×resid -0.06 (k=0.35, cap ±6.0)  ST -0.62  → recentered → **+3.72**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False