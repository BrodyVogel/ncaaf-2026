# Oklahoma — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+15.98** (rank 11/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    49 | proxy 49
- RB    44 | proxy 44
- WRTE  76 | proxy 76
- OL    78 | proxy 78
- DL    84 | proxy 84
- LB    92 | proxy 92
- DB    94 | proxy 94
- ST    67 | proxy 67

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-5.61**

## 3. Anchor (per source: raw → normalized → used)
- SP+      17.2 → 17.2 → 17.2
- FEI      0.8 → 17.52 → 17.52
- Massey   8.5 → 16.49 → 16.49
- FPI      17.8 → 20.25 → 20.25
- TR       22.0 → 20.57 → 20.57
- PickSix  6 → 24.07 → 22.52  [WINSORIZED]
- blend 18.82  (dispersion 7.58)

## 4. Assembly
- anchor +18.82  class -1.68  k×resid -1.96 (k=0.35, cap ±6.0)  ST +0.34  → recentered → **+15.98**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False