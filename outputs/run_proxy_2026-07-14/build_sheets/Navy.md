# Navy — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-0.47** (rank 67/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    44 | proxy 44
- DL     5 | proxy 5
- LB    16 | proxy 16
- DB    18 | proxy 18
- ST    57 | proxy 57

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-8.66**

## 3. Anchor (per source: raw → normalized → used)
- SP+      1.1 → 1.1 → 1.1
- FEI      0.03 → 0.92 → 0.92
- Massey   7.59 → -0.57 → -0.57
- FPI      -0.7 → -1.3 → -1.3
- TR       0.9 → 0.38 → 0.38
- blend 0.27  (dispersion 2.4)

## 4. Assembly
- anchor +0.27  class +1.68  k×resid -3.03 (k=0.35, cap ±6.0)  ST +0.14  → recentered → **-0.47**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False