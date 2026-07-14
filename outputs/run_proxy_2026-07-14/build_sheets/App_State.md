# App State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-8.52** (rank 106/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    31 | proxy 31
- WRTE   4 | proxy 4
- OL    38 | proxy 38
- DL    33 | proxy 33
- LB    70 | proxy 70
- DB     5 | proxy 5
- ST    41 | proxy 41

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+3.89**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -12.1 → -12.1 → -12.1
- FEI      -0.52 → -10.94 → -10.94
- Massey   6.92 → -13.13 → -13.13
- FPI      -9.8 → -11.9 → -11.9
- TR       -10.9 → -10.92 → -10.92
- blend -11.85  (dispersion 2.21)

## 4. Assembly
- anchor -11.85  class +1.68  k×resid +1.36 (k=0.35, cap ±6.0)  ST -0.18  → recentered → **-8.52**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False