# Syracuse — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-4.67** (rank 90/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    32 | proxy 32
- RB    50 | proxy —
- WRTE  22 | proxy 22
- OL    34 | proxy 34
- DL    42 | proxy 42
- LB    27 | proxy 27
- DB    51 | proxy 51
- ST    16 | proxy 16

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-2.55**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -0.7 → -0.7 → -0.7
- FEI      -0.26 → -5.33 → -5.33
- Massey   7.37 → -4.69 → -4.69
- FPI      -0.8 → -1.42 → -1.42
- TR       -0.2 → -0.68 → -0.68
- PickSix  64 → 0.39 → 0.39
- blend -1.88  (dispersion 5.72)

## 4. Assembly
- anchor -1.88  class -1.68  k×resid -0.89 (k=0.35, cap ±6.0)  ST -0.68  → recentered → **-4.67**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False