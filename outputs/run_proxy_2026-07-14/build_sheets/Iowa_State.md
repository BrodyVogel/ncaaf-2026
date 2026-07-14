# Iowa State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-1.61** (rank 74/138)  band ±7.0

## 1. Unit grades (LLM | shadow proxy)
- QB    47 | proxy 47
- RB    50 | proxy —
- WRTE  43 | proxy 43
- OL    26 | proxy 26
- DL    60 | proxy 60
- LB    50 | proxy —
- DB    40 | proxy 40
- ST    21 | proxy 21

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.32**

## 3. Anchor (per source: raw → normalized → used)
- SP+      1.0 → 1.0 → 1.0
- FEI      0.43 → 9.54 → 4.52  [WINSORIZED]
- Massey   8.26 → 11.99 → 4.52  [WINSORIZED]
- FPI      -0.9 → -1.53 → -1.53
- TR       0.0 → -0.48 → -0.48
- PickSix  65 → -2.11 → -2.11
- blend 0.99  (dispersion 14.1, FLAGGED)

## 4. Assembly
- anchor +0.99  class -1.68  k×resid -0.81 (k=0.35, cap ±6.0)  ST -0.58  → recentered → **-1.61**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×2) = ±7.0
- flags: resid_flag=False, dispersion_flag=True