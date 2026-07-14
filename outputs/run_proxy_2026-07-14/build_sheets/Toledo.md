# Toledo — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-4.42** (rank 89/138)  band ±7.19

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL     5 | proxy 5
- DL     9 | proxy 9
- LB    14 | proxy 14
- DB    17 | proxy 17
- ST    90 | proxy 90

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-7.07**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -11.5 → -11.5 → -7.56  [WINSORIZED]
- FEI      0.07 → 1.78 → -1.35  [WINSORIZED]
- Massey   7.56 → -1.13 → -1.35  [WINSORIZED]
- FPI      -3.0 → -3.98 → -3.98
- TR       -8.6 → -8.72 → -7.56  [WINSORIZED]
- blend -4.89  (dispersion 13.28, FLAGGED)

## 4. Assembly
- anchor -4.89  class +1.68  k×resid -2.47 (k=0.35, cap ±6.0)  ST +0.80  → recentered → **-4.42**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×3) = ±7.19
- flags: resid_flag=False, dispersion_flag=True