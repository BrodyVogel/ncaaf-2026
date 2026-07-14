# South Florida — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-0.09** (rank 66/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    62 | proxy 62
- RB    50 | proxy —
- WRTE  20 | proxy 20
- OL    34 | proxy 34
- DL    49 | proxy 49
- LB    50 | proxy —
- DB    19 | proxy 19
- ST    38 | proxy 38

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.20**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.8 → -2.8 → -2.8
- FEI      0.1 → 2.43 → 2.43
- Massey   7.74 → 2.24 → 2.24
- FPI      -0.9 → -1.53 → -1.53
- TR       -2.4 → -2.78 → -2.78
- blend -0.87  (dispersion 5.23)

## 4. Assembly
- anchor -0.87  class +1.68  k×resid -1.12 (k=0.35, cap ±6.0)  ST -0.24  → recentered → **-0.09**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False