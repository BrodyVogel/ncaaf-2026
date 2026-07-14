# UConn — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-9.01** (rank 111/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB     8 | proxy 8
- WRTE  50 | proxy —
- OL    12 | proxy 12
- DL     5 | proxy 5
- LB    33 | proxy 33
- DB    46 | proxy 46
- ST    37 | proxy 37

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+0.16**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -11.2 → -11.2 → -11.2
- FEI      -0.46 → -9.65 → -9.65
- Massey   7.13 → -9.19 → -9.19
- FPI      -11.2 → -13.53 → -13.53
- TR       -10.9 → -10.92 → -10.92
- blend -10.95  (dispersion 4.34)

## 4. Assembly
- anchor -10.95  class +1.68  k×resid +0.05 (k=0.35, cap ±6.0)  ST -0.26  → recentered → **-9.01**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False