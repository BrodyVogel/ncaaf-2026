# UCF — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **+0.85** (rank 60/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    24 | proxy 24
- RB    50 | proxy —
- WRTE  63 | proxy 63
- OL    32 | proxy 32
- DL    57 | proxy 57
- LB    48 | proxy 48
- DB    67 | proxy 67
- ST    77 | proxy 77

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.55**

## 3. Anchor (per source: raw → normalized → used)
- SP+      2.3 → 2.3 → 2.3
- FEI      0.04 → 1.13 → 1.13
- Massey   7.73 → 2.06 → 2.06
- FPI      2.1 → 1.96 → 1.96
- TR       3.3 → 2.67 → 2.67
- PickSix  48 → 4.54 → 4.54
- blend 2.42  (dispersion 3.41)

## 4. Assembly
- anchor +2.42  class -1.68  k×resid -0.89 (k=0.35, cap ±6.0)  ST +0.54  → recentered → **+0.85**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False