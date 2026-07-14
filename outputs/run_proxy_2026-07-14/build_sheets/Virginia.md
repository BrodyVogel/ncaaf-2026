# Virginia — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+3.80** (rank 42/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    62 | proxy 62
- RB    48 | proxy 48
- WRTE  36 | proxy 36
- OL    50 | proxy —
- DL    39 | proxy 39
- LB    54 | proxy 54
- DB    52 | proxy 52
- ST    63 | proxy 63

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-6.39**

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.6 → 6.6 → 6.6
- FEI      0.22 → 5.02 → 5.02
- Massey   7.96 → 6.37 → 6.37
- FPI      7.9 → 8.72 → 8.72
- TR       9.0 → 8.13 → 8.13
- PickSix  35 → 7.52 → 7.52
- blend 6.99  (dispersion 3.7)

## 4. Assembly
- anchor +6.99  class -1.68  k×resid -2.24 (k=0.35, cap ±6.0)  ST +0.26  → recentered → **+3.80**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False