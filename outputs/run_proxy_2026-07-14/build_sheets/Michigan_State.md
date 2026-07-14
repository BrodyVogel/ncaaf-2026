# Michigan State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-2.25** (rank 80/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy 50
- RB    31 | proxy 31
- WRTE  50 | proxy —
- OL    46 | proxy 46
- DL    50 | proxy —
- LB    52 | proxy 52
- DB    50 | proxy 50
- ST     2 | proxy 2

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.36**

## 3. Anchor (per source: raw → normalized → used)
- SP+      0.4 → 0.4 → 0.4
- FEI      -0.02 → -0.16 → -0.16
- Massey   7.82 → 3.74 → 3.74
- FPI      0.3 → -0.13 → -0.13
- TR       -0.3 → -0.77 → -0.77
- PickSix  59 → 1.77 → 1.77
- blend 0.75  (dispersion 4.51)

## 4. Assembly
- anchor +0.75  class -1.68  k×resid -0.83 (k=0.35, cap ±6.0)  ST -0.96  → recentered → **-2.25**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False