# Tulane — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+0.35** (rank 63/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    77 | proxy 77
- RB    50 | proxy —
- WRTE  56 | proxy 56
- OL    33 | proxy 33
- DL    10 | proxy 10
- LB     1 | proxy 1
- DB    15 | proxy 15
- ST    76 | proxy 76

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-7.97**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.5 → -5.5 → -2.26  [WINSORIZED]
- FEI      0.14 → 3.29 → 3.29
- Massey   7.84 → 4.12 → 4.12
- FPI      2.3 → 2.2 → 2.2
- TR       -2.8 → -3.16 → -2.26  [WINSORIZED]
- blend 0.47  (dispersion 9.62)

## 4. Assembly
- anchor +0.47  class +1.68  k×resid -2.79 (k=0.35, cap ±6.0)  ST +0.52  → recentered → **+0.35**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False