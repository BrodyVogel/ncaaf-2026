# Northwestern — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+4.95** (rank 37/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    40 | proxy 40
- RB    52 | proxy 52
- WRTE  95 | proxy 95
- OL    69 | proxy 69
- DL    90 | proxy 90
- LB    74 | proxy 74
- DB    88 | proxy 88
- ST    28 | proxy 28

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+8.80**

## 3. Anchor (per source: raw → normalized → used)
- SP+      4.6 → 4.6 → 4.6
- FEI      0.09 → 2.21 → 2.21
- Massey   7.87 → 4.68 → 4.68
- FPI      1.4 → 1.15 → 1.15
- TR       4.8 → 4.11 → 4.11
- PickSix  55 → 3.31 → 3.31
- blend 3.52  (dispersion 3.53)

## 4. Assembly
- anchor +3.52  class -1.68  k×resid +3.08 (k=0.35, cap ±6.0)  ST -0.44  → recentered → **+4.95**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False