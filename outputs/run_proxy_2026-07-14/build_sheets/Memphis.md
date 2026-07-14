# Memphis — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+1.97** (rank 53/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  26 | proxy 26
- OL    40 | proxy 40
- DL    33 | proxy 33
- LB    50 | proxy —
- DB    76 | proxy 76
- ST    52 | proxy 52

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+1.43**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.1 → -1.1 → -1.1
- FEI      0.05 → 1.35 → 1.35
- Massey   7.68 → 1.12 → 1.12
- FPI      -1.9 → -2.7 → -2.7
- TR       -1.5 → -1.92 → -1.92
- blend -0.72  (dispersion 4.05)

## 4. Assembly
- anchor -0.72  class +1.68  k×resid +0.50 (k=0.35, cap ±6.0)  ST +0.04  → recentered → **+1.97**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False