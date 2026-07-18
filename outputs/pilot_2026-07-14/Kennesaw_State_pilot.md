# Kennesaw State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-8.97** (rank 103/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    44 | proxy 9
- RB    40 | proxy —
- WRTE  42 | proxy —
- OL    40 | proxy 5
- DL    44 | proxy 10
- LB    46 | proxy 11
- DB    42 | proxy 9
- ST    42 | proxy 16

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.060 DB:-0.096  (R²=0.61)
- grade-implied off +23.56 vs anchor off +19.83
- grade-implied def +26.82 vs anchor def +31.57  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+8.48**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +6.35 (=-0.541x anchor margin) + shape +2.12 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -9.3 → -9.3 → -9.3
- FEI      -0.61 → -12.88 → -12.88
- Massey   6.57 → -19.69 → -16.93  [WINSORIZED]
- FPI      -9.0 → -10.97 → -10.97
- TR       -14.2 → -14.08 → -14.08
- blend -12.24  (dispersion 10.39)

## 4. Assembly
- anchor -12.24  class +0.00  k×resid +2.97 (k=0.35, cap ±6.0)  ST -0.16  → recentered (-0.47) → **-8.97**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T18:08:00Z (Kennesaw State)