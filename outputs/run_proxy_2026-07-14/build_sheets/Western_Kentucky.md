# Western Kentucky — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-4.97** (rank 93/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    15 | proxy 15
- RB    15 | proxy 15
- WRTE  53 | proxy 53
- OL    12 | proxy 12
- DL     1 | proxy 1
- LB    50 | proxy —
- DB    63 | proxy 63
- ST    85 | proxy 85

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.85**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.3 → -5.3 → -5.3
- FEI      -0.3 → -6.2 → -6.2
- Massey   7.23 → -7.32 → -7.32
- FPI      -4.9 → -6.19 → -6.19
- TR       -8.4 → -8.52 → -8.52
- blend -6.47  (dispersion 3.22)

## 4. Assembly
- anchor -6.47  class +1.68  k×resid -1.35 (k=0.35, cap ±6.0)  ST +0.70  → recentered → **-4.97**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False