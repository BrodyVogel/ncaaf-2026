# East Carolina — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-0.70** (rank 69/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    55 | proxy 55
- WRTE  35 | proxy 35
- OL    34 | proxy 34
- DL    38 | proxy 38
- LB     1 | proxy 1
- DB    38 | proxy 38
- ST    49 | proxy 49

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-4.76**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.0 → -2.0 → -2.0
- FEI      0.04 → 1.13 → 1.13
- Massey   7.68 → 1.12 → 1.12
- FPI      -0.6 → -1.18 → -1.18
- TR       -3.7 → -4.03 → -4.03
- blend -1.16  (dispersion 5.16)

## 4. Assembly
- anchor -1.16  class +1.68  k×resid -1.66 (k=0.35, cap ±6.0)  ST -0.02  → recentered → **-0.70**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False