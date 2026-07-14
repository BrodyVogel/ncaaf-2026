# Liberty — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-7.79** (rank 103/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    22 | proxy 22
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    38 | proxy 38
- DL    14 | proxy 14
- LB     2 | proxy 2
- DB    26 | proxy 26
- ST    24 | proxy 24

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-1.79**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -6.4 → -6.4 → -6.4
- FEI      -0.41 → -8.57 → -8.57
- Massey   6.91 → -13.32 → -13.32
- FPI      -7.7 → -9.45 → -9.45
- TR       -8.5 → -8.62 → -8.62
- blend -8.79  (dispersion 6.92)

## 4. Assembly
- anchor -8.79  class +1.68  k×resid -0.63 (k=0.35, cap ±6.0)  ST -0.52  → recentered → **-7.79**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False