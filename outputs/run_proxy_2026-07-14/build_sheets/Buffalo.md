# Buffalo — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-6.13** (rank 97/138)  band ±6.9

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    50 | proxy —
- LB    50 | proxy —
- DB    45 | proxy 45
- ST    82 | proxy 82

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+14.88**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -11.9 → -11.9 → -11.9
- FEI      -0.72 → -15.25 → -15.25
- Massey   6.75 → -16.32 → -16.32
- FPI      -10.8 → -13.07 → -13.07
- TR       -16.5 → -16.28 → -16.28
- blend -14.12  (dispersion 4.42)

## 4. Assembly
- anchor -14.12  class +1.68  k×resid +5.21 (k=0.35, cap ±6.0)  ST +0.64  → recentered → **-6.13**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×6) = ±6.9
- flags: resid_flag=True, dispersion_flag=False