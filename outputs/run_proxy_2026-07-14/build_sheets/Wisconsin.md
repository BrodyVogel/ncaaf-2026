# Wisconsin — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+4.57** (rank 40/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    49 | proxy 49
- RB    49 | proxy 49
- WRTE  50 | proxy —
- OL    47 | proxy 47
- DL    43 | proxy 43
- LB    89 | proxy 89
- DB    77 | proxy 77
- ST    87 | proxy 87

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.08**

## 3. Anchor (per source: raw → normalized → used)
- SP+      1.8 → 1.8 → 2.24  [WINSORIZED]
- FEI      0.27 → 6.09 → 6.09
- Massey   8.02 → 7.49 → 7.49
- FPI      4.8 → 5.11 → 5.11
- TR       8.4 → 7.56 → 7.56
- PickSix  36 → 7.24 → 7.24
- blend 5.42  (dispersion 5.76)

## 4. Assembly
- anchor +5.42  class -1.68  k×resid -0.38 (k=0.35, cap ±6.0)  ST +0.74  → recentered → **+4.57**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False