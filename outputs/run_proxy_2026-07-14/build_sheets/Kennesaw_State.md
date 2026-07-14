# Kennesaw State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-12.08** (rank 122/138)  band ±6.36

## 1. Unit grades (LLM | shadow proxy)
- QB     9 | proxy 9
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL     5 | proxy 5
- DL    10 | proxy 10
- LB    11 | proxy 11
- DB     9 | proxy 9
- ST    16 | proxy 16

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-3.73**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -9.3 → -9.3 → -9.3
- FEI      -0.61 → -12.88 → -12.88
- Massey   6.57 → -19.69 → -16.93  [WINSORIZED]
- FPI      -9.0 → -10.97 → -10.97
- TR       -14.2 → -14.08 → -14.08
- blend -12.24  (dispersion 10.39)

## 4. Assembly
- anchor -12.24  class +1.68  k×resid -1.30 (k=0.35, cap ±6.0)  ST -0.68  → recentered → **-12.08**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×2) = ±6.36
- flags: resid_flag=False, dispersion_flag=False