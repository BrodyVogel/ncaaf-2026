# Air Force — build sheet [PROXY-PROVISIONAL (mechanical shadow grades - NOT the product)]

FINAL: **-4.84** (rank 92/138)  band ±6.18

## 1. Unit grades (LLM | shadow proxy)
- QB    54 | proxy 54
- RB    13 | proxy 13
- WRTE  50 | proxy —
- OL    32 | proxy 32
- DL    41 | proxy 41
- LB    27 | proxy 27
- DB     5 | proxy 5
- ST    59 | proxy 59

## 2. Conversion (league-learned weights this run)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied vs anchor residual: **-4.81**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.4 → -2.4 → -2.44  [WINSORIZED]
- FEI      -0.23 → -4.69 → -4.69
- Massey   7.23 → -7.32 → -7.32
- FPI      -6.8 → -8.41 → -8.41
- TR       -7.4 → -7.57 → -7.57
- blend -5.48  (dispersion 6.01)

## 4. Assembly
- anchor -5.48  class +1.68  k×resid -1.68 (k=0.35, cap ±6.0)  ST +0.18  → recentered → **-4.84**
- band: 6.0 × dispersion(1.00) × conf(1+0.03×1) = ±6.18
- flags: resid_flag=False, dispersion_flag=False