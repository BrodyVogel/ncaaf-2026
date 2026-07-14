# Jacksonville State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-8.66** (rank 109/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    20 | proxy 20
- RB    50 | proxy —
- WRTE  12 | proxy 12
- OL    27 | proxy 27
- DL    14 | proxy 14
- LB     8 | proxy 8
- DB    47 | proxy 47
- ST    21 | proxy 21

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.13**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.7 → -7.7 → -7.7
- FEI      -0.49 → -10.29 → -10.29
- Massey   6.97 → -12.19 → -12.19
- FPI      -8.5 → -10.39 → -10.39
- TR       -10.7 → -10.73 → -10.73
- blend -9.83  (dispersion 4.49)

## 4. Assembly
- anchor -9.83  class +1.68  k×resid -0.40 (k=0.35, cap ±6.0)  ST -0.58  → recentered → **-8.66**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False