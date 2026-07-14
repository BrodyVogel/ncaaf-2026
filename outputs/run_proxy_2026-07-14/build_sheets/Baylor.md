# Baylor — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+3.06** (rank 49/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    57 | proxy 57
- RB    45 | proxy 45
- WRTE  87 | proxy 87
- OL    36 | proxy 36
- DL    50 | proxy 50
- LB    20 | proxy 20
- DB    60 | proxy 60
- ST    97 | proxy 97

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.92**

## 3. Anchor (per source: raw → normalized → used)
- SP+      4.5 → 4.5 → 4.5
- FEI      0.2 → 4.58 → 4.58
- Massey   7.86 → 4.49 → 4.49
- FPI      6.5 → 7.09 → 7.09
- TR       4.6 → 3.92 → 3.92
- PickSix  52 → 3.81 → 3.81
- blend 4.7  (dispersion 3.28)

## 4. Assembly
- anchor +4.70  class -1.68  k×resid -1.37 (k=0.35, cap ±6.0)  ST +0.94  → recentered → **+3.06**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False