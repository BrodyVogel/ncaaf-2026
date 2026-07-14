# Arkansas State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-8.88** (rank 110/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    19 | proxy 19
- WRTE  34 | proxy 34
- OL    41 | proxy 41
- DL    34 | proxy 34
- LB     2 | proxy 2
- DB     5 | proxy 5
- ST    69 | proxy 69

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-0.67**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.5 → -8.5 → -8.5
- FEI      -0.64 → -13.53 → -13.53
- Massey   6.86 → -14.26 → -14.26
- FPI      -9.2 → -11.2 → -11.2
- TR       -11.0 → -11.01 → -11.01
- blend -11.17  (dispersion 5.76)

## 4. Assembly
- anchor -11.17  class +1.68  k×resid -0.24 (k=0.35, cap ±6.0)  ST +0.38  → recentered → **-8.88**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False