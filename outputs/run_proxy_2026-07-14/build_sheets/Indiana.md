# Indiana — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+23.03** (rank 5/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    87 | proxy 87
- RB    70 | proxy 70
- WRTE  96 | proxy 96
- OL    72 | proxy 72
- DL    82 | proxy 82
- LB    95 | proxy 95
- DB   100 | proxy 100
- ST    94 | proxy 94

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-6.00**

## 3. Anchor (per source: raw → normalized → used)
- SP+      24.5 → 24.5 → 24.5
- FEI      1.14 → 24.85 → 24.85
- Massey   9.18 → 29.24 → 29.24
- FPI      23.1 → 26.43 → 26.43
- TR       29.0 → 27.27 → 27.27
- PickSix  9 → 20.64 → 21.43  [WINSORIZED]
- blend 25.46  (dispersion 8.6)

## 4. Assembly
- anchor +25.46  class -1.68  k×resid -2.10 (k=0.35, cap ±6.0)  ST +0.88  → recentered → **+23.03**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False