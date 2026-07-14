# Northern Illinois — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-12.95** (rank 124/138)  band ±6.72

## 1. Unit grades (LLM | shadow proxy)
- QB     0 | proxy 0
- RB     2 | proxy 2
- WRTE  50 | proxy —
- OL    16 | proxy 16
- DL    50 | proxy —
- LB    50 | proxy —
- DB    50 | proxy —
- ST    33 | proxy 33

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+6.90**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -18.2 → -18.2 → -18.2
- FEI      -0.68 → -14.39 → -14.39
- Massey   6.84 → -14.63 → -14.63
- FPI      -14.5 → -17.38 → -17.38
- TR       -20.6 → -20.2 → -20.2
- blend -17.17  (dispersion 5.81)

## 4. Assembly
- anchor -17.17  class +1.68  k×resid +2.42 (k=0.35, cap ±6.0)  ST -0.34  → recentered → **-12.95**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×4) = ±6.72
- flags: resid_flag=False, dispersion_flag=False