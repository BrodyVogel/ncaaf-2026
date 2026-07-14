# Oregon State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-4.03** (rank 88/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    36 | proxy 36
- RB    50 | proxy —
- WRTE   4 | proxy 4
- OL    33 | proxy 33
- DL    60 | proxy 60
- LB    93 | proxy 93
- DB    22 | proxy 22
- ST     0 | proxy 0

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+4.30**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -6.3 → -6.3 → -6.3
- FEI      -0.37 → -7.71 → -7.71
- Massey   7.31 → -5.82 → -5.82
- FPI      -8.1 → -9.92 → -9.92
- TR       -10.0 → -10.06 → -10.06
- blend -7.68  (dispersion 4.24)

## 4. Assembly
- anchor -7.68  class +1.68  k×resid +1.51 (k=0.35, cap ±6.0)  ST +0.00  → recentered → **-4.03**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False