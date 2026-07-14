# Ohio State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+26.93** (rank 1/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    96 | proxy 96
- RB    87 | proxy 87
- WRTE  91 | proxy 91
- OL    81 | proxy 81
- DL    74 | proxy 74
- LB    96 | proxy 96
- DB    91 | proxy 91
- ST    84 | proxy 84

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-11.25**

## 3. Anchor (per source: raw → normalized → used)
- SP+      31.8 → 31.8 → 31.8
- FEI      1.52 → 33.05 → 33.05
- Massey   9.3 → 31.49 → 31.49
- FPI      28.7 → 32.95 → 32.95
- TR       32.3 → 30.43 → 30.43
- PickSix  2 → 28.28 → 28.28
- blend 31.4  (dispersion 4.77)

## 4. Assembly
- anchor +31.40  class -1.68  k×resid -3.94 (k=0.35, cap ±6.0)  ST +0.68  → recentered → **+26.93**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=True, dispersion_flag=False