# South Alabama — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-7.21** (rank 102/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    34 | proxy 34
- RB    66 | proxy 66
- WRTE  26 | proxy 26
- OL    50 | proxy —
- DL    23 | proxy 23
- LB    17 | proxy 17
- DB    63 | proxy 63
- ST    32 | proxy 32

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+8.65**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.3 → -13.3 → -13.3
- FEI      -0.52 → -10.94 → -10.94
- Massey   7.03 → -11.07 → -11.07
- FPI      -10.5 → -12.72 → -12.72
- TR       -10.8 → -10.82 → -10.82
- blend -12.02  (dispersion 2.48)

## 4. Assembly
- anchor -12.02  class +1.68  k×resid +3.03 (k=0.35, cap ±6.0)  ST -0.36  → recentered → **-7.21**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False