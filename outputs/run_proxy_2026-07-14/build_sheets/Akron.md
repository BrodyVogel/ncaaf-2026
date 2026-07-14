# Akron — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-14.42** (rank 131/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB     3 | proxy 3
- WRTE  24 | proxy 24
- OL    50 | proxy —
- DL    14 | proxy 14
- LB    50 | proxy —
- DB    43 | proxy 43
- ST    25 | proxy 25

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+11.14**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -19.5 → -19.5 → -19.5
- FEI      -1.06 → -22.58 → -22.58
- Massey   6.53 → -20.44 → -20.44
- FPI      -16.9 → -20.17 → -20.17
- TR       -17.9 → -17.62 → -17.62
- blend -19.97  (dispersion 4.97)

## 4. Assembly
- anchor -19.97  class +1.68  k×resid +3.90 (k=0.35, cap ±6.0)  ST -0.50  → recentered → **-14.42**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=True, dispersion_flag=False