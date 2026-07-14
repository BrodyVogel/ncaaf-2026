# Massachusetts — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-22.87** (rank 138/138)  band ±7.39

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL     2 | proxy 2
- DL    50 | proxy —
- LB    33 | proxy 33
- DB     0 | proxy 0
- ST    10 | proxy 10

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+20.81**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -30.9 → -30.9 → -30.9
- FEI      -1.54 → -32.93 → -32.93
- Massey   5.9 → -32.26 → -32.26
- FPI      -18.8 → -22.39 → -26.58  [WINSORIZED]
- TR       -28.5 → -27.76 → -27.76
- blend -30.22  (dispersion 10.55, FLAGGED)

## 4. Assembly
- anchor -30.22  class +1.68  k×resid +6.00 (k=0.35, cap ±6.0)  ST -0.80  → recentered → **-22.87**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×4) = ±7.39
- flags: resid_flag=True, dispersion_flag=True