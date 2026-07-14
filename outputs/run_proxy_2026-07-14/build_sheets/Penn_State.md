# Penn State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+14.88** (rank 14/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    84 | proxy 84
- RB    73 | proxy 73
- WRTE  60 | proxy 60
- OL    78 | proxy 78
- DL    57 | proxy 57
- LB    65 | proxy 65
- DB    78 | proxy 78
- ST    91 | proxy 91

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.78**

## 3. Anchor (per source: raw → normalized → used)
- SP+      15.7 → 15.7 → 15.7
- FEI      0.89 → 19.46 → 19.46
- Massey   8.73 → 20.8 → 20.48  [WINSORIZED]
- FPI      13.7 → 15.48 → 15.48
- TR       16.4 → 15.21 → 15.21
- PickSix  20 → 14.15 → 14.15
- blend 16.6  (dispersion 6.65)

## 4. Assembly
- anchor +16.60  class -1.68  k×resid -1.32 (k=0.35, cap ±6.0)  ST +0.82  → recentered → **+14.88**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False