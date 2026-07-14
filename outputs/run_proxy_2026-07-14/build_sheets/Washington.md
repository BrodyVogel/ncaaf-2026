# Washington — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+10.72** (rank 22/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    15 | proxy 15
- RB    50 | proxy —
- WRTE  62 | proxy 62
- OL    53 | proxy 53
- DL    77 | proxy 77
- LB    89 | proxy 89
- DB    86 | proxy 86
- ST    49 | proxy 49

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-8.17**

## 3. Anchor (per source: raw → normalized → used)
- SP+      14.5 → 14.5 → 14.5
- FEI      0.78 → 17.09 → 17.09
- Massey   8.5 → 16.49 → 16.49
- FPI      9.9 → 11.05 → 11.05
- TR       16.4 → 15.21 → 15.21
- PickSix  18 → 14.81 → 14.81
- blend 14.81  (dispersion 6.04)

## 4. Assembly
- anchor +14.81  class -1.68  k×resid -2.86 (k=0.35, cap ±6.0)  ST -0.02  → recentered → **+10.72**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False