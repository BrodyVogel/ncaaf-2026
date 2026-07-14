# Southern Miss — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-9.82** (rank 114/138)  band ±7.59

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    15 | proxy 15
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    50 | proxy —
- LB    34 | proxy 34
- DB    50 | proxy —
- ST    63 | proxy 63

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+12.77**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -23.3 → -23.3 → -20.27  [WINSORIZED]
- FEI      -0.69 → -14.61 → -14.61
- Massey   6.77 → -15.94 → -15.94
- FPI      -5.1 → -6.43 → -11.68  [WINSORIZED]
- TR       -17.7 → -17.43 → -17.43
- blend -16.7  (dispersion 16.87, FLAGGED)

## 4. Assembly
- anchor -16.70  class +1.68  k×resid +4.47 (k=0.35, cap ±6.0)  ST +0.26  → recentered → **-9.82**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×5) = ±7.59
- flags: resid_flag=True, dispersion_flag=True