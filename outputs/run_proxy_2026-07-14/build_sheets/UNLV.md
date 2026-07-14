# UNLV — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-0.66** (rank 68/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    57 | proxy 57
- RB    49 | proxy 49
- WRTE  12 | proxy 12
- OL    16 | proxy 16
- DL    33 | proxy 33
- LB    27 | proxy 27
- DB    26 | proxy 26
- ST    40 | proxy 40

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-8.49**

## 3. Anchor (per source: raw → normalized → used)
- SP+      2.8 → 2.8 → 2.8
- FEI      -0.12 → -2.32 → -2.32
- Massey   7.54 → -1.51 → -1.51
- FPI      1.8 → 1.61 → 1.61
- TR       -0.8 → -1.25 → -1.25
- blend 0.36  (dispersion 5.12)

## 4. Assembly
- anchor +0.36  class +1.68  k×resid -2.97 (k=0.35, cap ±6.0)  ST -0.20  → recentered → **-0.66**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False