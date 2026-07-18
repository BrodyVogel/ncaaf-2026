# Mississippi State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+4.00** (rank 51/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    54 | proxy 54
- RB    52 | proxy 78
- WRTE  50 | proxy 50
- OL    44 | proxy 63
- DL    44 | proxy 39
- LB    46 | proxy 65
- DB    56 | proxy 88
- ST    54 | proxy 43

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.081 LB:-0.060 DB:-0.099  (R²=0.62)
- grade-implied off +26.00 vs anchor off +30.48
- grade-implied def +25.39 vs anchor def +26.32  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-3.55**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -2.25 (=-0.541x anchor margin) + shape -1.30 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      3.9 → 3.9 → 3.9
- FEI      0.22 → 5.02 → 5.02
- Massey   7.86 → 4.49 → 4.49
- FPI      4.1 → 4.29 → 4.29
- TR       6.4 → 5.64 → 5.64
- PickSix  43 → 5.35 → 5.35
- blend 4.66  (dispersion 1.74)

## 4. Assembly
- anchor +4.66  class -0.00  k×resid -1.24 (k=0.35, cap ±6.0)  ST +0.08  → recentered (-0.50) → **+4.00**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T04:09:05Z (cd01f52)