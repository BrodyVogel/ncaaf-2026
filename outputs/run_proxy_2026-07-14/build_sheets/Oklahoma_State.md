# Oklahoma State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+4.06** (rank 41/138)  band ±6.6

## 1. Unit grades (LLM | shadow proxy)
- QB    76 | proxy 76
- RB    97 | proxy 97
- WRTE  76 | proxy 76
- OL    58 | proxy 58
- DL    42 | proxy 42
- LB    81 | proxy 81
- DB    51 | proxy 51
- ST     7 | proxy 7

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+6.41**

## 3. Anchor (per source: raw → normalized → used)
- SP+      7.1 → 7.1 → 7.1
- FEI      -0.25 → -5.12 → -0.41  [WINSORIZED]
- Massey   7.39 → -4.32 → -0.41  [WINSORIZED]
- FPI      3.3 → 3.36 → 3.36
- TR       6.7 → 5.93 → 5.93
- PickSix  47 → 4.59 → 4.59
- blend 3.89  (dispersion 12.22, FLAGGED)

## 4. Assembly
- anchor +3.89  class -1.68  k×resid +2.24 (k=0.35, cap ±6.0)  ST -0.86  → recentered → **+4.06**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×0) = ±6.6
- flags: resid_flag=False, dispersion_flag=True