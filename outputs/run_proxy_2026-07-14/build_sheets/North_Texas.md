# North Texas — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-3.38** (rank 85/138)  band ±7.19

## 1. Unit grades (LLM | shadow proxy)
- QB    31 | proxy 31
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    67 | proxy 67
- DL     1 | proxy 1
- LB    50 | proxy 50
- DB    50 | proxy —
- ST    50 | proxy 50

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+3.10**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -11.8 → -11.8 → -8.32  [WINSORIZED]
- FEI      0.07 → 1.78 → -3.38  [WINSORIZED]
- Massey   7.69 → 1.31 → -3.38  [WINSORIZED]
- FPI      -6.4 → -7.94 → -7.94
- TR       -8.7 → -8.81 → -8.32  [WINSORIZED]
- blend -6.61  (dispersion 13.58, FLAGGED)

## 4. Assembly
- anchor -6.61  class +1.68  k×resid +1.08 (k=0.35, cap ±6.0)  ST +0.00  → recentered → **-3.38**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×3) = ±7.19
- flags: resid_flag=False, dispersion_flag=True