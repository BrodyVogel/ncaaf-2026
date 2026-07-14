# Georgia State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-12.20** (rank 123/138)  band ±6.9

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    50 | proxy —
- LB    50 | proxy —
- DB    50 | proxy —
- ST    30 | proxy 30

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+20.00**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -25.1 → -25.1 → -23.47  [WINSORIZED]
- FEI      -0.79 → -16.76 → -16.76
- Massey   6.62 → -18.76 → -18.76
- FPI      -15.2 → -18.19 → -18.19
- TR       -19.4 → -19.05 → -19.05
- blend -19.95  (dispersion 8.34)

## 4. Assembly
- anchor -19.95  class +1.68  k×resid +6.00 (k=0.35, cap ±6.0)  ST -0.40  → recentered → **-12.20**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×7) = ±6.9
- flags: resid_flag=True, dispersion_flag=False