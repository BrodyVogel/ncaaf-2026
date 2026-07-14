# Ball State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-14.98** (rank 133/138)  band ±6.9

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL     2 | proxy 2
- DL    50 | proxy —
- LB    50 | proxy —
- DB    50 | proxy —
- ST    12 | proxy 12

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+18.45**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -25.2 → -25.2 → -25.2
- FEI      -0.95 → -20.21 → -20.21
- Massey   6.53 → -20.44 → -20.44
- FPI      -17.3 → -20.64 → -20.64
- TR       -23.0 → -22.5 → -22.5
- blend -22.37  (dispersion 4.99)

## 4. Assembly
- anchor -22.37  class +1.68  k×resid +6.00 (k=0.35, cap ±6.0)  ST -0.76  → recentered → **-14.98**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×6) = ±6.9
- flags: resid_flag=True, dispersion_flag=False