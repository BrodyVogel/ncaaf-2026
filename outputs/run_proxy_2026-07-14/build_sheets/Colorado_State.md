# Colorado State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-11.25** (rank 118/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB     9 | proxy 9
- RB    50 | proxy —
- WRTE   2 | proxy 2
- OL    50 | proxy —
- DL     9 | proxy 9
- LB    19 | proxy 19
- DB     2 | proxy 2
- ST     3 | proxy 3

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.26**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.3 → -8.3 → -8.57  [WINSORIZED]
- FEI      -0.61 → -12.88 → -12.88
- Massey   6.86 → -14.26 → -14.26
- FPI      -12.4 → -14.93 → -14.93
- TR       -10.7 → -10.73 → -10.73
- blend -11.66  (dispersion 6.63)

## 4. Assembly
- anchor -11.66  class +1.68  k×resid -0.79 (k=0.35, cap ±6.0)  ST -0.94  → recentered → **-11.25**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False