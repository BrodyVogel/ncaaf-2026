# Auburn — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+10.66** (rank 23/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    95 | proxy 95
- RB    58 | proxy 58
- WRTE  65 | proxy 65
- OL    69 | proxy 69
- DL    85 | proxy 85
- LB    82 | proxy 82
- DB    64 | proxy 64
- ST    33 | proxy 33

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+1.62**

## 3. Anchor (per source: raw → normalized → used)
- SP+      11.2 → 11.2 → 11.2
- FEI      0.51 → 11.27 → 11.27
- Massey   8.18 → 10.49 → 10.49
- FPI      12.0 → 13.5 → 13.5
- TR       13.4 → 12.34 → 12.34
- PickSix  26 → 11.55 → 11.55
- blend 11.65  (dispersion 3.0)

## 4. Assembly
- anchor +11.65  class -1.68  k×resid +0.57 (k=0.35, cap ±6.0)  ST -0.34  → recentered → **+10.66**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False