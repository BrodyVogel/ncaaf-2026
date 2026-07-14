# Ohio — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-5.94** (rank 95/138)  band ±6.9

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    50 | proxy —
- LB    47 | proxy 47
- DB    12 | proxy 12
- ST    23 | proxy 23

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+5.77**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -13.6 → -13.6 → -12.78  [WINSORIZED]
- FEI      -0.28 → -5.77 → -5.77
- Massey   7.34 → -5.26 → -5.36  [WINSORIZED]
- FPI      -8.0 → -9.8 → -9.8
- TR       -10.9 → -10.92 → -10.92
- blend -9.57  (dispersion 8.34)

## 4. Assembly
- anchor -9.57  class +1.68  k×resid +2.02 (k=0.35, cap ±6.0)  ST -0.54  → recentered → **-5.94**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×5) = ±6.9
- flags: resid_flag=False, dispersion_flag=False