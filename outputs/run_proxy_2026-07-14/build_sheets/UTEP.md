# UTEP — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-14.05** (rank 129/138)  band ±6.72

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL     9 | proxy 9
- LB    39 | proxy 39
- DB    11 | proxy 11
- ST    27 | proxy 27

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+12.55**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -20.5 → -20.5 → -20.5
- FEI      -0.89 → -18.92 → -18.92
- Massey   6.53 → -20.44 → -20.44
- FPI      -16.6 → -19.82 → -19.82
- TR       -21.0 → -20.58 → -20.58
- blend -20.13  (dispersion 1.67)

## 4. Assembly
- anchor -20.13  class +1.68  k×resid +4.39 (k=0.35, cap ±6.0)  ST -0.46  → recentered → **-14.05**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×4) = ±6.72
- flags: resid_flag=True, dispersion_flag=False