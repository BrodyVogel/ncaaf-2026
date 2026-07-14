# San Diego State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-0.74** (rank 70/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    16 | proxy 16
- RB    37 | proxy 37
- WRTE  48 | proxy 48
- OL     5 | proxy 5
- DL    39 | proxy 39
- LB    50 | proxy —
- DB    48 | proxy 48
- ST    58 | proxy 58

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-6.35**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -1.3 → -1.3 → -1.3
- FEI      -0.06 → -1.02 → -1.02
- Massey   7.46 → -3.01 → -3.01
- FPI      1.4 → 1.15 → 1.15
- TR       1.1 → 0.57 → 0.57
- blend -0.82  (dispersion 4.15)

## 4. Assembly
- anchor -0.82  class +1.68  k×resid -2.22 (k=0.35, cap ±6.0)  ST +0.16  → recentered → **-0.74**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False