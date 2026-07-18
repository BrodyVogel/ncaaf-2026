# James Madison — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-0.39** (rank 65/138 in hybrid field)  band ±6.98

## 1. Unit grades (LLM real | shadow proxy)
- QB    44 | proxy —
- RB    46 | proxy —
- WRTE  46 | proxy —
- OL    44 | proxy 38
- DL    46 | proxy —
- LB    46 | proxy 28
- DB    48 | proxy 50
- ST    54 | proxy 66

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +24.58 vs anchor off +25.80
- grade-implied def +26.06 vs anchor def +25.90  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-1.37**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +0.05 (=-0.541x anchor margin) + shape -1.43 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -2.1 → -2.1 → -2.1
- FEI      0.29 → 6.52 → 2.99  [WINSORIZED]
- Massey   7.89 → 5.06 → 2.99  [WINSORIZED]
- FPI      -2.0 → -2.81 → -2.81
- TR       -1.5 → -1.92 → -1.92
- blend -0.49  (dispersion 9.34)

## 4. Assembly
- anchor -0.49  class +0.00  k×resid -0.48 (k=0.35, cap ±6.0)  ST +0.08  → recentered (-0.50) → **-0.39**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×1) = ±6.98

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T15:08:00Z (James Madison)