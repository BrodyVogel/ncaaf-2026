# Boston College — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-4.68** (rank 91/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    45 | proxy 45
- WRTE  13 | proxy 13
- OL    44 | proxy 44
- DL    33 | proxy 33
- LB    58 | proxy 58
- DB    19 | proxy 19
- ST    70 | proxy 70

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.74**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.5 → -1.5 → -1.5
- FEI      -0.22 → -4.47 → -4.47
- Massey   7.51 → -2.07 → -2.07
- FPI      -2.7 → -3.63 → -3.63
- TR       -6.2 → -6.42 → -6.42
- PickSix  67 → -3.26 → -3.26
- blend -3.26  (dispersion 4.92)

## 4. Assembly
- anchor -3.26  class -1.68  k×resid -0.61 (k=0.35, cap ±6.0)  ST +0.40  → recentered → **-4.68**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False