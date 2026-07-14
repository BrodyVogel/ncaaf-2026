# Mississippi State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+4.75** (rank 38/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    54 | proxy 54
- RB    78 | proxy 78
- WRTE  50 | proxy 50
- OL    63 | proxy 63
- DL    39 | proxy 39
- LB    65 | proxy 65
- DB    88 | proxy 88
- ST    43 | proxy 43

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+4.13**

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.9 → 3.9 → 3.9
- FEI      0.22 → 5.02 → 5.02
- Massey   7.86 → 4.49 → 4.49
- FPI      4.1 → 4.29 → 4.29
- TR       6.4 → 5.64 → 5.64
- PickSix  43 → 5.35 → 5.35
- blend 4.66  (dispersion 1.74)

## 4. Assembly
- anchor +4.66  class -1.68  k×resid +1.44 (k=0.35, cap ±6.0)  ST -0.14  → recentered → **+4.75**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False