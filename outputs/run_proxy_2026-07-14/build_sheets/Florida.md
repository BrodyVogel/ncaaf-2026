# Florida — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+10.03** (rank 26/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    88 | proxy 88
- WRTE  57 | proxy 57
- OL    40 | proxy 40
- DL    58 | proxy 58
- LB    74 | proxy 74
- DB    75 | proxy 75
- ST    36 | proxy 36

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-4.26**

## 3. Anchor (per source: raw → normalized → used)
- SP+      14.9 → 14.9 → 14.9
- FEI      0.36 → 8.03 → 9.9  [WINSORIZED]
- Massey   8.12 → 9.37 → 9.9  [WINSORIZED]
- FPI      13.6 → 15.36 → 15.36
- TR       17.4 → 16.17 → 15.58  [WINSORIZED]
- PickSix  29 → 10.58 → 10.58
- blend 13.02  (dispersion 8.14)

## 4. Assembly
- anchor +13.02  class -1.68  k×resid -1.49 (k=0.35, cap ±6.0)  ST -0.28  → recentered → **+10.03**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False