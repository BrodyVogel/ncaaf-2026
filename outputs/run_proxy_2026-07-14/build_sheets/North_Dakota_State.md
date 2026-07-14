# North Dakota State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-0.05** (rank 65/138)  band ±7.59

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    50 | proxy —
- LB    50 | proxy —
- DB    50 | proxy —
- ST    50 | proxy —

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+4.52**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.4 → -1.4 → -1.66  [WINSORIZED]
- FEI      -1.0 → -21.29 → -7.28  [WINSORIZED]
- Massey   7.62 → -0.01 → -1.66  [WINSORIZED]
- FPI      -8.3 → -10.15 → -7.28  [WINSORIZED]
- TR       -2.8 → -3.16 → -3.16
- blend -3.78  (dispersion 21.28, FLAGGED)

## 4. Assembly
- anchor -3.78  class +1.68  k×resid +1.58 (k=0.35, cap ±6.0)  ST +0.00  → recentered → **-0.05**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×8) = ±7.59
- flags: resid_flag=False, dispersion_flag=True