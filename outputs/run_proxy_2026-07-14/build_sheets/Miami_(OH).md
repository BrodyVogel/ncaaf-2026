# Miami (OH) — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-8.00** (rank 104/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB     6 | proxy 6
- RB    50 | proxy —
- WRTE   6 | proxy 6
- OL     3 | proxy 3
- DL     9 | proxy 9
- LB    16 | proxy 16
- DB     3 | proxy 3
- ST    56 | proxy 56

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-10.85**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.9 → -2.9 → -2.9
- FEI      -0.32 → -6.63 → -6.63
- Massey   7.24 → -7.13 → -7.13
- FPI      -7.0 → -8.64 → -8.64
- TR       -10.6 → -10.63 → -10.63
- blend -6.47  (dispersion 7.73)

## 4. Assembly
- anchor -6.47  class +1.68  k×resid -3.80 (k=0.35, cap ±6.0)  ST +0.12  → recentered → **-8.00**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False