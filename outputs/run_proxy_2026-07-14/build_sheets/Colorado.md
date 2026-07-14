# Colorado — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+0.36** (rank 62/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    64 | proxy 64
- RB    50 | proxy —
- WRTE  75 | proxy 75
- OL    44 | proxy 44
- DL    68 | proxy 68
- LB    53 | proxy 53
- DB    47 | proxy 47
- ST    61 | proxy 61

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+2.62**

## 3. Anchor (per source: raw → normalized → used)
- SP+      0.9 → 0.9 → 0.9
- FEI      -0.15 → -2.96 → -2.96
- Massey   7.65 → 0.56 → 0.56
- FPI      4.5 → 4.76 → 4.76
- TR       -1.4 → -1.82 → -1.82
- PickSix  62 → 0.78 → 0.78
- blend 0.44  (dispersion 7.72)

## 4. Assembly
- anchor +0.44  class -1.68  k×resid +0.92 (k=0.35, cap ±6.0)  ST +0.22  → recentered → **+0.36**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False