# Florida State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+6.78** (rank 32/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    68 | proxy 68
- RB    78 | proxy 78
- WRTE  91 | proxy 91
- OL    44 | proxy 44
- DL    64 | proxy 64
- LB    43 | proxy 43
- DB    52 | proxy 52
- ST    70 | proxy 70

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.03**

## 3. Anchor (per source: raw → normalized → used)
- SP+      8.8 → 8.8 → 8.8
- FEI      0.47 → 10.41 → 10.41
- Massey   8.03 → 7.68 → 7.68
- FPI      9.3 → 10.35 → 10.35
- TR       7.3 → 6.5 → 6.5
- PickSix  42 → 5.56 → 5.56
- blend 8.3  (dispersion 4.84)

## 4. Assembly
- anchor +8.30  class -1.68  k×resid -0.71 (k=0.35, cap ±6.0)  ST +0.40  → recentered → **+6.78**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False