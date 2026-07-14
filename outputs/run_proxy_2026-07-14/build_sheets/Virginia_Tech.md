# Virginia Tech — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+3.46** (rank 45/138)  band ±7.19

## 1. Unit grades (LLM | shadow proxy)
- QB    42 | proxy 42
- RB    41 | proxy 41
- WRTE  43 | proxy 43
- OL    50 | proxy —
- DL    50 | proxy —
- LB    50 | proxy —
- DB    90 | proxy 90
- ST     7 | proxy 7

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-4.32**

## 3. Anchor (per source: raw → normalized → used)
- SP+      9.4 → 9.4 → 9.4
- FEI      -0.08 → -1.45 → 3.14  [WINSORIZED]
- Massey   7.65 → 0.56 → 3.14  [WINSORIZED]
- FPI      7.4 → 8.14 → 8.14
- TR       8.2 → 7.36 → 7.36
- PickSix  34 → 8.76 → 8.76
- blend 7.05  (dispersion 10.85, FLAGGED)

## 4. Assembly
- anchor +7.05  class -1.68  k×resid -1.51 (k=0.35, cap ±6.0)  ST -0.86  → recentered → **+3.46**
- band: 6.0 × dispersion(1.10) × conf(1+0.03×3) = ±7.19
- flags: resid_flag=False, dispersion_flag=True