# Coastal Carolina — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-11.04** (rank 116/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    24 | proxy 24
- WRTE  29 | proxy 29
- OL     5 | proxy 5
- DL    33 | proxy 33
- LB    50 | proxy —
- DB    29 | proxy 29
- ST    16 | proxy 16

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+3.76**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.8 → -13.8 → -13.8
- FEI      -0.58 → -12.23 → -12.23
- Massey   6.83 → -14.82 → -14.82
- FPI      -12.1 → -14.58 → -14.58
- TR       -13.8 → -13.69 → -13.69
- blend -13.82  (dispersion 2.58)

## 4. Assembly
- anchor -13.82  class +1.68  k×resid +1.32 (k=0.35, cap ±6.0)  ST -0.68  → recentered → **-11.04**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False