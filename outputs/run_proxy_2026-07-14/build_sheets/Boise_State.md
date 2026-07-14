# Boise State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+2.86** (rank 50/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    12 | proxy 12
- RB    40 | proxy 40
- WRTE   4 | proxy 4
- OL    17 | proxy 17
- DL    43 | proxy 43
- LB    31 | proxy 31
- DB    58 | proxy 58
- ST    60 | proxy 60

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-13.95**

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.8 → 6.8 → 6.8
- FEI      0.19 → 4.37 → 4.37
- Massey   7.85 → 4.31 → 4.31
- FPI      4.0 → 4.18 → 4.18
- TR       6.7 → 5.93 → 5.93
- blend 5.4  (dispersion 2.62)

## 4. Assembly
- anchor +5.40  class +1.68  k×resid -4.88 (k=0.35, cap ±6.0)  ST +0.20  → recentered → **+2.86**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=True, dispersion_flag=False