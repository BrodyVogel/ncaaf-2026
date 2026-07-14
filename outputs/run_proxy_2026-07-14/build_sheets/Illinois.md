# Illinois — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+4.67** (rank 39/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    82 | proxy 82
- RB    33 | proxy 33
- WRTE  53 | proxy 53
- OL    19 | proxy 19
- DL    44 | proxy 44
- LB    61 | proxy 61
- DB    64 | proxy 64
- ST    33 | proxy 33

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-8.02**

## 3. Anchor (per source: raw → normalized → used)
- SP+      9.3 → 9.3 → 9.3
- FEI      0.52 → 11.48 → 11.48
- Massey   8.21 → 11.06 → 11.06
- FPI      6.3 → 6.85 → 6.85
- TR       9.2 → 8.32 → 8.32
- PickSix  38 → 6.91 → 6.91
- blend 9.03  (dispersion 4.63)

## 4. Assembly
- anchor +9.03  class -1.68  k×resid -2.81 (k=0.35, cap ±6.0)  ST -0.34  → recentered → **+4.67**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False