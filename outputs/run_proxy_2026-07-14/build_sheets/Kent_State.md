# Kent State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-18.42** (rank 136/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB     9 | proxy 9
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL     2 | proxy 2
- DL     9 | proxy 9
- LB    23 | proxy 23
- DB     1 | proxy 1
- ST    13 | proxy 13

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+5.33**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -20.1 → -20.1 → -20.1
- FEI      -1.06 → -22.58 → -22.58
- Massey   6.32 → -24.38 → -24.38
- FPI      -17.9 → -21.34 → -21.34
- TR       -22.1 → -21.64 → -21.64
- blend -21.69  (dispersion 4.28)

## 4. Assembly
- anchor -21.69  class +1.68  k×resid +1.86 (k=0.35, cap ±6.0)  ST -0.74  → recentered → **-18.42**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False