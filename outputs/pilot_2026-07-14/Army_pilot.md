# Army — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-0.52** (rank 67/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    62 | proxy 62
- RB    38 | proxy —
- WRTE  40 | proxy —
- OL    84 | proxy 92
- DL    25 | proxy 18
- LB    15 | proxy —
- DB    22 | proxy 36
- ST    65 | proxy 58

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.090 WRTE:+0.036 OL:+0.086  (R²=0.54)
- def: DL:-0.084 LB:-0.058 DB:-0.096  (R²=0.62)
- grade-implied off +28.45 vs anchor off +24.68
- grade-implied def +32.14 vs anchor def +27.42
- residual (off-minus-def, grades-vs-anchor): **-0.95**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -3.0 → -3.0 → -3.0
- FEI      -0.02 → -0.16 → -0.16
- Massey   7.54 → -1.51 → -1.51
- FPI      -5.6 → -7.01 → -6.57  [WINSORIZED]
- TR       -1.2 → -1.63 → -1.63
- blend -2.64  (dispersion 6.85)

## 4. Assembly
- anchor -2.64  class +1.68  k×resid -0.33 (k=0.35, cap ±6.0)  ST +0.30  → recentered (-0.47) → **-0.52**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15