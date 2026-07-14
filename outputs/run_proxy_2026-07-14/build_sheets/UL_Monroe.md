# UL Monroe — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-14.72** (rank 132/138)  band ±6.9

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    50 | proxy —
- LB    50 | proxy —
- DB    50 | proxy —
- ST    27 | proxy 27

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+22.46**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -24.3 → -24.3 → -24.3
- FEI      -1.02 → -21.72 → -21.72
- Massey   6.46 → -21.76 → -21.76
- FPI      -19.3 → -22.97 → -22.97
- TR       -19.8 → -19.44 → -19.44
- blend -22.41  (dispersion 4.86)

## 4. Assembly
- anchor -22.41  class +1.68  k×resid +6.00 (k=0.35, cap ±6.0)  ST -0.46  → recentered → **-14.72**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×7) = ±6.9
- flags: resid_flag=True, dispersion_flag=False