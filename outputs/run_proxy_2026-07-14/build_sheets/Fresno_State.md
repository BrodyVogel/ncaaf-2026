# Fresno State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-1.10** (rank 71/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    24 | proxy 24
- WRTE   0 | proxy 0
- OL    11 | proxy 11
- DL    33 | proxy 33
- LB    27 | proxy 27
- DB    75 | proxy 75
- ST    79 | proxy 79

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-5.00**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.3 → -2.3 → -2.3
- FEI      -0.14 → -2.75 → -2.75
- Massey   7.45 → -3.19 → -3.19
- FPI      -2.5 → -3.4 → -3.4
- TR       2.0 → 1.43 → 1.43
- blend -2.08  (dispersion 4.83)

## 4. Assembly
- anchor -2.08  class +1.68  k×resid -1.75 (k=0.35, cap ±6.0)  ST +0.58  → recentered → **-1.10**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False