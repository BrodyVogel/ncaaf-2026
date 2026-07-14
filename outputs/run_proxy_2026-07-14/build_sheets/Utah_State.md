# Utah State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-6.93** (rank 101/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  14 | proxy 14
- OL    12 | proxy 12
- DL    16 | proxy 16
- LB    26 | proxy 26
- DB    19 | proxy 19
- ST    10 | proxy 10

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-4.88**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -7.7 → -7.7 → -7.7
- FEI      -0.28 → -5.77 → -5.77
- Massey   7.31 → -5.82 → -5.82
- FPI      -6.7 → -8.29 → -8.29
- TR       -3.8 → -4.12 → -4.12
- blend -6.57  (dispersion 4.17)

## 4. Assembly
- anchor -6.57  class +1.68  k×resid -1.71 (k=0.35, cap ±6.0)  ST -0.80  → recentered → **-6.93**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False