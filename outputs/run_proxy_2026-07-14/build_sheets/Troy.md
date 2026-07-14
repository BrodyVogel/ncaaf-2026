# Troy — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-6.77** (rank 99/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    34 | proxy 34
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    12 | proxy 12
- DL    30 | proxy 30
- LB     5 | proxy 5
- DB     6 | proxy 6
- ST    55 | proxy 55

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-4.40**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -6.0 → -6.0 → -6.0
- FEI      -0.36 → -7.49 → -7.49
- Massey   7.17 → -8.44 → -8.44
- FPI      -7.4 → -9.1 → -9.1
- TR       -7.7 → -7.85 → -7.85
- blend -7.48  (dispersion 3.1)

## 4. Assembly
- anchor -7.48  class +1.68  k×resid -1.54 (k=0.35, cap ±6.0)  ST +0.10  → recentered → **-6.77**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False