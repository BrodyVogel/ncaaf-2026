# Missouri State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-14.05** (rank 128/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    16 | proxy 16
- RB    50 | proxy —
- WRTE  30 | proxy 30
- OL    50 | proxy —
- DL     3 | proxy 3
- LB    19 | proxy 19
- DB     0 | proxy 0
- ST     1 | proxy 1

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+2.66**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -18.7 → -18.7 → -18.7
- FEI      -0.6 → -12.67 → -12.67
- Massey   6.78 → -15.76 → -15.76
- FPI      -10.3 → -12.48 → -12.48
- TR       -18.9 → -18.57 → -18.57
- blend -16.15  (dispersion 6.22)

## 4. Assembly
- anchor -16.15  class +1.68  k×resid +0.93 (k=0.35, cap ±6.0)  ST -0.98  → recentered → **-14.05**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False