# Rutgers — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-1.99** (rank 77/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    53 | proxy 53
- RB    58 | proxy 58
- WRTE 101 | proxy 101
- OL    12 | proxy 12
- DL    70 | proxy 70
- LB    43 | proxy 43
- DB     6 | proxy 6
- ST    19 | proxy 19

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.48**

## 3. Anchor (per source: raw → normalized → used)
- SP+      1.8 → 1.8 → 1.8
- FEI      0.01 → 0.49 → 0.49
- Massey   7.79 → 3.18 → 3.18
- FPI      -0.2 → -0.72 → -0.72
- TR       0.8 → 0.28 → 0.28
- PickSix  63 → 0.58 → 0.58
- blend 1.06  (dispersion 3.9)

## 4. Assembly
- anchor +1.06  class -1.68  k×resid -1.22 (k=0.35, cap ±6.0)  ST -0.62  → recentered → **-1.99**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False