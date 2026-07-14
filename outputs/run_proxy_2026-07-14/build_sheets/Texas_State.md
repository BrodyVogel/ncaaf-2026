# Texas State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-2.43** (rank 81/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    65 | proxy 65
- RB    81 | proxy 81
- WRTE  69 | proxy 69
- OL    58 | proxy 58
- DL    17 | proxy 17
- LB    16 | proxy 16
- DB     6 | proxy 6
- ST    44 | proxy 44

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+2.45**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -5.9 → -5.9 → -5.9
- FEI      -0.28 → -5.77 → -5.77
- Massey   7.28 → -6.38 → -6.38
- FPI      -4.3 → -5.49 → -5.49
- TR       -2.0 → -2.4 → -2.4
- blend -5.31  (dispersion 3.98)

## 4. Assembly
- anchor -5.31  class +1.68  k×resid +0.86 (k=0.35, cap ±6.0)  ST -0.12  → recentered → **-2.43**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False