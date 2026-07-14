# Washington State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-1.18** (rank 72/138)  band ±7.39

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    29 | proxy 29
- DL    39 | proxy 39
- LB    50 | proxy —
- DB    22 | proxy 22
- ST    29 | proxy 29

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.73**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.3 → -5.3 → -4.14  [WINSORIZED]
- FEI      0.23 → 5.23 → 1.36  [WINSORIZED]
- Massey   7.82 → 3.74 → 1.36  [WINSORIZED]
- FPI      -4.1 → -5.26 → -4.14  [WINSORIZED]
- TR       -1.6 → -2.02 → -2.02
- blend -1.95  (dispersion 10.53, FLAGGED)

## 4. Assembly
- anchor -1.95  class +1.68  k×resid -0.96 (k=0.35, cap ±6.0)  ST -0.42  → recentered → **-1.18**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×4) = ±7.39
- flags: resid_flag=False, dispersion_flag=True