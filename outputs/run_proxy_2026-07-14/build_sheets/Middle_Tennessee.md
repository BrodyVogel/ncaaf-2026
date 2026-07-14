# Middle Tennessee — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-15.71** (rank 134/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    60 | proxy 60
- RB    50 | proxy —
- WRTE   9 | proxy 9
- OL     9 | proxy 9
- DL    33 | proxy 33
- LB    50 | proxy —
- DB     2 | proxy 2
- ST     5 | proxy 5

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+11.85**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -26.0 → -26.0 → -24.47  [WINSORIZED]
- FEI      -0.86 → -18.27 → -18.27
- Massey   6.57 → -19.69 → -19.69
- FPI      -16.1 → -19.24 → -19.24
- TR       -20.9 → -20.49 → -20.49
- blend -21.1  (dispersion 7.73)

## 4. Assembly
- anchor -21.10  class +1.68  k×resid +4.15 (k=0.35, cap ±6.0)  ST -0.90  → recentered → **-15.71**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=True, dispersion_flag=False