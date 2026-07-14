# James Madison — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+1.47** (rank 56/138)  band ±6.72

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    38 | proxy 38
- DL    50 | proxy —
- LB    28 | proxy 28
- DB    50 | proxy 50
- ST    66 | proxy 66

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.45**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.1 → -2.1 → -2.1
- FEI      0.29 → 6.52 → 2.99  [WINSORIZED]
- Massey   7.89 → 5.06 → 2.99  [WINSORIZED]
- FPI      -2.0 → -2.81 → -2.81
- TR       -1.5 → -1.92 → -1.92
- blend -0.49  (dispersion 9.34)

## 4. Assembly
- anchor -0.49  class +1.68  k×resid -0.51 (k=0.35, cap ±6.0)  ST +0.32  → recentered → **+1.47**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×4) = ±6.72
- flags: resid_flag=False, dispersion_flag=False