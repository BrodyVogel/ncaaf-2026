# NC State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+0.37** (rank 61/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    30 | proxy 30
- RB    68 | proxy 68
- WRTE  38 | proxy 38
- OL    47 | proxy 47
- DL    27 | proxy 27
- LB    50 | proxy —
- DB    22 | proxy 22
- ST    39 | proxy 39

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-10.21**

## 3. Anchor (per source: raw → normalized → used)
- SP+      4.9 → 4.9 → 4.9
- FEI      0.33 → 7.39 → 7.39
- Massey   7.92 → 5.62 → 5.62
- FPI      3.7 → 3.83 → 3.83
- TR       6.2 → 5.45 → 5.45
- PickSix  41 → 5.57 → 5.57
- blend 5.38  (dispersion 3.56)

## 4. Assembly
- anchor +5.38  class -1.68  k×resid -3.57 (k=0.35, cap ±6.0)  ST -0.22  → recentered → **+0.37**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False