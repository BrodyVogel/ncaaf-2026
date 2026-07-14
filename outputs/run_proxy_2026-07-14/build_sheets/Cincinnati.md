# Cincinnati — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+1.17** (rank 58/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    29 | proxy 29
- RB    44 | proxy 44
- WRTE  50 | proxy —
- OL    97 | proxy 97
- DL    13 | proxy 13
- LB    52 | proxy 52
- DB    52 | proxy 52
- ST    52 | proxy 52

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.50**

## 3. Anchor (per source: raw → normalized → used)
- SP+      4.5 → 4.5 → 4.5
- FEI      0.24 → 5.45 → 5.45
- Massey   7.87 → 4.68 → 4.68
- FPI      4.4 → 4.64 → 4.64
- TR       0.3 → -0.2 → -0.2
- PickSix  60 → 1.45 → 1.45
- blend 3.57  (dispersion 5.64)

## 4. Assembly
- anchor +3.57  class -1.68  k×resid -1.23 (k=0.35, cap ±6.0)  ST +0.04  → recentered → **+1.17**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False