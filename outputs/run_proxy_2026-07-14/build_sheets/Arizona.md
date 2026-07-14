# Arizona — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+6.23** (rank 34/138)  band ±6.0

## 1. Unit grades (LLM | shadow proxy)
- QB    93 | proxy 93
- RB    42 | proxy 42
- WRTE  37 | proxy 37
- OL    77 | proxy 77
- DL    45 | proxy 45
- LB    50 | proxy 50
- DB    64 | proxy 64
- ST    33 | proxy 33

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.91**

## 3. Anchor (per source: raw → normalized → used)
- SP+      10.2 → 10.2 → 10.2
- FEI      0.38 → 8.47 → 8.47
- Massey   8.18 → 10.49 → 10.49
- FPI      7.2 → 7.9 → 7.9
- TR       8.7 → 7.84 → 7.84
- PickSix  33 → 8.95 → 8.95
- blend 9.15  (dispersion 2.65)

## 4. Assembly
- anchor +9.15  class -1.68  k×resid -1.37 (k=0.35, cap ±6.0)  ST -0.34  → recentered → **+6.23**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×0) = ±6.0
- flags: resid_flag=False, dispersion_flag=False