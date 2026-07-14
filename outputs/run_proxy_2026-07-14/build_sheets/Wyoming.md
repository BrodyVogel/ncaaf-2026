# Wyoming — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-9.80** (rank 113/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    31 | proxy 31
- WRTE  50 | proxy —
- OL     9 | proxy 9
- DL    27 | proxy 27
- LB    50 | proxy —
- DB    12 | proxy 12
- ST     6 | proxy 6

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+0.80**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -9.6 → -9.6 → -9.6
- FEI      -0.5 → -10.51 → -10.51
- Massey   7.09 → -9.94 → -9.94
- FPI      -13.1 → -15.75 → -15.23  [WINSORIZED]
- TR       -13.3 → -13.21 → -13.21
- blend -11.35  (dispersion 6.15)

## 4. Assembly
- anchor -11.35  class +1.68  k×resid +0.28 (k=0.35, cap ±6.0)  ST -0.88  → recentered → **-9.80**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False