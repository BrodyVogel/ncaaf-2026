# Army — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+0.99** (rank 59/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    62 | proxy 62
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    92 | proxy 92
- DL    18 | proxy 18
- LB    50 | proxy —
- DB    36 | proxy 36
- ST    58 | proxy 58

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+3.78**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -3.0 → -3.0 → -3.0
- FEI      -0.02 → -0.16 → -0.16
- Massey   7.54 → -1.51 → -1.51
- FPI      -5.6 → -7.01 → -6.57  [WINSORIZED]
- TR       -1.2 → -1.63 → -1.63
- blend -2.64  (dispersion 6.85)

## 4. Assembly
- anchor -2.64  class +1.68  k×resid +1.32 (k=0.35, cap ±6.0)  ST +0.16  → recentered → **+0.99**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False