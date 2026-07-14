# Miami — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+19.88** (rank 8/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    84 | proxy 84
- RB    91 | proxy 91
- WRTE  97 | proxy 97
- OL    92 | proxy 92
- DL    89 | proxy 89
- LB    50 | proxy —
- DB    77 | proxy 77
- ST    62 | proxy 62

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.99**

## 3. Anchor (per source: raw → normalized → used)
- SP+      21.0 → 21.0 → 21.0
- FEI      0.88 → 19.25 → 19.25
- Massey   8.68 → 19.87 → 19.87
- FPI      21.8 → 24.91 → 24.91
- TR       25.3 → 23.73 → 23.73
- PickSix  3 → 27.16 → 26.0  [WINSORIZED]
- blend 22.25  (dispersion 7.92)

## 4. Assembly
- anchor +22.25  class -1.68  k×resid -1.40 (k=0.35, cap ±6.0)  ST +0.24  → recentered → **+19.88**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False