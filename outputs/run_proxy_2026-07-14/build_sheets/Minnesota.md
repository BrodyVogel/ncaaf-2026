# Minnesota — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+5.18** (rank 36/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    48 | proxy 48
- RB    51 | proxy 51
- WRTE  35 | proxy 35
- OL    60 | proxy 60
- DL    64 | proxy 64
- LB    76 | proxy 76
- DB    88 | proxy 88
- ST   100 | proxy 100

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+2.02**

## 3. Anchor (per source: raw → normalized → used)
- SP+      5.2 → 5.2 → 5.2
- FEI      0.2 → 4.58 → 4.58
- Massey   7.89 → 5.06 → 5.06
- FPI      0.6 → 0.21 → 0.21
- TR       8.1 → 7.27 → 7.27
- PickSix  44 → 5.28 → 5.28
- blend 4.69  (dispersion 7.05)

## 4. Assembly
- anchor +4.69  class -1.68  k×resid +0.71 (k=0.35, cap ±6.0)  ST +1.00  → recentered → **+5.18**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False