# TCU — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+7.21** (rank 31/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    83 | proxy 83
- WRTE  72 | proxy 72
- OL    72 | proxy 72
- DL    46 | proxy 46
- LB    50 | proxy —
- DB    63 | proxy 63
- ST    45 | proxy 45

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.33**

## 3. Anchor (per source: raw → normalized → used)
- SP+      9.1 → 9.1 → 9.1
- FEI      0.43 → 9.54 → 9.54
- Massey   8.23 → 11.43 → 11.43
- FPI      6.4 → 6.97 → 6.97
- TR       8.4 → 7.56 → 7.56
- PickSix  25 → 11.67 → 11.67
- blend 9.34  (dispersion 4.69)

## 4. Assembly
- anchor +9.34  class -1.68  k×resid -0.81 (k=0.35, cap ±6.0)  ST -0.10  → recentered → **+7.21**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False