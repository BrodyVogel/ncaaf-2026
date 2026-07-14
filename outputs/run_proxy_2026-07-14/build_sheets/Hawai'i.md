# Hawai'i — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-2.78** (rank 83/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    42 | proxy 42
- RB    50 | proxy —
- WRTE  21 | proxy 21
- OL     3 | proxy 3
- DL    33 | proxy 33
- LB    16 | proxy 16
- DB    83 | proxy 83
- ST    67 | proxy 67

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+1.29**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -3.9 → -3.9 → -3.9
- FEI      -0.37 → -7.71 → -7.71
- Massey   7.14 → -9.01 → -9.01
- FPI      -2.4 → -3.28 → -3.28
- TR       -6.3 → -6.51 → -6.51
- blend -5.72  (dispersion 5.73)

## 4. Assembly
- anchor -5.72  class +1.68  k×resid +0.45 (k=0.35, cap ±6.0)  ST +0.34  → recentered → **-2.78**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False