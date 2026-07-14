# Utah — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+11.62** (rank 21/138)  band ±6.6

## 1. Unit grades (LLM | shadow proxy)
- QB    68 | proxy 68
- RB    72 | proxy 72
- WRTE  48 | proxy 48
- OL    96 | proxy 96
- DL    66 | proxy 66
- LB    68 | proxy 68
- DB    52 | proxy 52
- ST    81 | proxy 81

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.87**

## 3. Anchor (per source: raw → normalized → used)
- SP+      11.9 → 11.9 → 11.9
- FEI      0.97 → 21.19 → 16.9  [WINSORIZED]
- Massey   8.62 → 18.74 → 16.9  [WINSORIZED]
- FPI      8.5 → 9.42 → 9.42
- TR       12.8 → 11.77 → 11.77
- PickSix  22 → 13.78 → 13.78
- blend 13.22  (dispersion 11.77, FLAGGED)

## 4. Assembly
- anchor +13.22  class -1.68  k×resid -1.01 (k=0.35, cap ±6.0)  ST +0.62  → recentered → **+11.62**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×0) = ±6.6
- flags: resid_flag=False, dispersion_flag=True