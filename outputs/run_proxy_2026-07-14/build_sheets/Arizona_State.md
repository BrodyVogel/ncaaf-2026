# Arizona State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+3.24** (rank 46/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    38 | proxy 38
- RB    50 | proxy —
- WRTE  71 | proxy 71
- OL    32 | proxy 32
- DL    57 | proxy 57
- LB    50 | proxy 50
- DB    75 | proxy 75
- ST    20 | proxy 20

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-5.36**

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.4 → 6.4 → 6.4
- FEI      0.26 → 5.88 → 5.88
- Massey   8.03 → 7.68 → 7.68
- FPI      4.8 → 5.11 → 5.11
- TR       8.7 → 7.84 → 7.84
- PickSix  32 → 9.18 → 9.18
- blend 6.93  (dispersion 4.08)

## 4. Assembly
- anchor +6.93  class -1.68  k×resid -1.88 (k=0.35, cap ±6.0)  ST -0.60  → recentered → **+3.24**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False