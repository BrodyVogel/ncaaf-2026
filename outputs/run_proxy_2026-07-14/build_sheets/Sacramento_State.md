# Sacramento State — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-11.88** (rank 121/138)  band ±6.9

## 1. Unit grades (LLM | shadow proxy)
- QB    50 | proxy —
- RB    50 | proxy —
- WRTE  50 | proxy —
- OL    50 | proxy —
- DL    50 | proxy —
- LB    50 | proxy —
- DB    50 | proxy —
- ST    50 | proxy —

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **+20.86**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -22.7 → -22.7 → -22.7
- FEI      -1.0 → -21.29 → -21.29
- Massey   6.59 → -19.32 → -19.32
- FPI      -10.4 → -12.6 → -15.3  [WINSORIZED]
- TR       -19.2 → -18.86 → -18.86
- blend -20.03  (dispersion 10.1)

## 4. Assembly
- anchor -20.03  class +1.68  k×resid +6.00 (k=0.35, cap ±6.0)  ST +0.00  → recentered → **-11.88**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×8) = ±6.9
- flags: resid_flag=True, dispersion_flag=False