# San José State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-9.66** (rank 112/138)  band ±6.54

## 1. Unit grades (LLM | shadow proxy)
- QB     5 | proxy 5
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL     9 | proxy 9
- DL    42 | proxy 42
- LB    31 | proxy 31
- DB    50 | proxy —
- ST    67 | proxy 67

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+6.18**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -15.5 → -15.5 → -15.5
- FEI      -0.53 → -11.16 → -11.16
- Massey   6.99 → -11.82 → -11.82
- FPI      -14.3 → -17.14 → -17.14
- TR       -14.9 → -14.75 → -14.75
- blend -14.31  (dispersion 5.99)

## 4. Assembly
- anchor -14.31  class +1.68  k×resid +2.16 (k=0.35, cap ±6.0)  ST +0.34  → recentered → **-9.66**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×3) = ±6.54
- flags: resid_flag=False, dispersion_flag=False