# Tennessee — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+15.41** (rank 13/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    93 | proxy 93
- WRTE  99 | proxy 99
- OL    91 | proxy 91
- DL    57 | proxy 57
- LB    90 | proxy 90
- DB    74 | proxy 74
- ST    73 | proxy 73

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.13**

## 3. Anchor (per source: raw → normalized → used)
- SP+      16.0 → 16.0 → 16.0
- FEI      0.8 → 17.52 → 17.52
- Massey   8.47 → 15.93 → 15.93
- FPI      15.1 → 17.11 → 17.11
- TR       16.8 → 15.6 → 15.6
- PickSix  15 → 17.8 → 17.8
- blend 16.56  (dispersion 2.2)

## 4. Assembly
- anchor +16.56  class -1.68  k×resid -0.40 (k=0.35, cap ±6.0)  ST +0.46  → recentered → **+15.41**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False