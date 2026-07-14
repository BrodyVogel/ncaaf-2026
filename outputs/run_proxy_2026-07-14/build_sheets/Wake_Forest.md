# Wake Forest — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+1.65** (rank 55/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    58 | proxy 58
- RB    50 | proxy —
- WRTE  26 | proxy 26
- OL    53 | proxy 53
- DL    57 | proxy 57
- LB    25 | proxy 25
- DB    46 | proxy 46
- ST    93 | proxy 93

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.85**

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.6 → 3.6 → 3.6
- FEI      0.19 → 4.37 → 4.37
- Massey   7.78 → 2.99 → 2.99
- FPI      3.4 → 3.48 → 3.48
- TR       2.4 → 1.81 → 1.81
- PickSix  53 → 3.59 → 3.59
- blend 3.35  (dispersion 2.56)

## 4. Assembly
- anchor +3.35  class -1.68  k×resid -1.35 (k=0.35, cap ±6.0)  ST +0.86  → recentered → **+1.65**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False