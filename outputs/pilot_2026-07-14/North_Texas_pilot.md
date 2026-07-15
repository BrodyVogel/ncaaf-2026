# North Texas — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-4.46** (rank 89/138 in hybrid field)  band ±8.35

## 1. Unit grades (LLM real | shadow proxy)
- QB    35 | proxy 31
- RB    52 | proxy —
- WRTE  38 | proxy —
- OL    35 | proxy 67
- DL    15 | proxy 1
- LB    40 | proxy 50
- DB    35 | proxy —
- ST    55 | proxy 50

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.080 LB:-0.060 DB:-0.097  (R²=0.61)
- grade-implied off +23.46 vs anchor off +26.20
- grade-implied def +30.15 vs anchor def +32.60
- residual (off-minus-def, grades-vs-anchor): **-0.29**

## 3. Anchor (per source: raw → normalized → used)
- SP+      -11.8 → -11.8 → -8.32  [WINSORIZED]
- FEI      0.07 → 1.78 → -3.38  [WINSORIZED]
- Massey   7.69 → 1.31 → -3.38  [WINSORIZED]
- FPI      -6.4 → -7.94 → -7.94
- TR       -8.7 → -8.81 → -8.32  [WINSORIZED]
- blend -6.61  (dispersion 13.58, FLAGGED

## 4. Assembly
- anchor -6.61  class +1.68  k×resid -0.10 (k=0.35, cap ±6.0)  ST +0.10  → recentered (-0.47) → **-4.46**
- band: 6.0 × coach(1.13) × dispersion(1.10) × conf(1+0.03×4) = ±8.35

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-15