# Oregon — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+24.77** (rank 2/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    71 | proxy 71
- RB    93 | proxy 93
- WRTE  93 | proxy 93
- OL    47 | proxy 47
- DL   100 | proxy 100
- LB    90 | proxy 90
- DB    95 | proxy 95
- ST    88 | proxy 88

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-10.21**

## 3. Anchor (per source: raw → normalized → used)
- SP+      28.3 → 28.3 → 28.3
- FEI      1.4 → 30.46 → 30.46
- Massey   9.0 → 25.87 → 25.87
- FPI      25.3 → 28.99 → 28.99
- TR       29.5 → 27.75 → 27.75
- PickSix  1 → 31.92 → 31.92
- blend 28.8  (dispersion 6.05)

## 4. Assembly
- anchor +28.80  class -1.68  k×resid -3.58 (k=0.35, cap ±6.0)  ST +0.76  → recentered → **+24.77**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False