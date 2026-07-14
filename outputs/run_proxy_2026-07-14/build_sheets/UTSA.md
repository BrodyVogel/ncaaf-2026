# UTSA — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-1.94** (rank 76/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy 50
- RB    88 | proxy 88
- WRTE  57 | proxy 57
- OL    38 | proxy 38
- DL     1 | proxy 1
- LB    19 | proxy 19
- DB    11 | proxy 11
- ST    16 | proxy 16

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.90**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.5 → -1.5 → -1.5
- FEI      -0.02 → -0.16 → -0.16
- Massey   7.57 → -0.94 → -0.94
- FPI      -5.3 → -6.66 → -6.22  [WINSORIZED]
- TR       -1.5 → -1.92 → -1.92
- blend -2.04  (dispersion 6.5)

## 4. Assembly
- anchor -2.04  class +1.68  k×resid -1.37 (k=0.35, cap ±6.0)  ST -0.68  → recentered → **-1.94**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False