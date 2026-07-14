# Louisiana — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-6.01** (rank 96/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    33 | proxy 33
- RB    50 | proxy —
- WRTE  29 | proxy 29
- OL    32 | proxy 32
- DL     0 | proxy 0
- LB    50 | proxy —
- DB    76 | proxy 76
- ST    51 | proxy 51

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+5.20**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -9.1 → -9.1 → -9.1
- FEI      -0.46 → -9.65 → -9.65
- Massey   7.0 → -11.63 → -11.63
- FPI      -8.3 → -10.15 → -10.15
- TR       -10.3 → -10.34 → -10.34
- blend -10.0  (dispersion 2.53)

## 4. Assembly
- anchor -10.00  class +1.68  k×resid +1.82 (k=0.35, cap ±6.0)  ST +0.02  → recentered → **-6.01**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False