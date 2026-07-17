# Virginia — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+5.98** (rank 41/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    52 | proxy 62
- RB    56 | proxy 48
- WRTE  44 | proxy 36
- OL    58 | proxy —
- DL    50 | proxy 39
- LB    54 | proxy 54
- DB    52 | proxy 52
- ST    54 | proxy 63

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.084 LB:-0.058 DB:-0.096  (R²=0.62)
- grade-implied off +27.16 vs anchor off +26.50
- grade-implied def +24.91 vs anchor def +19.70  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-4.55**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -3.68 (=-0.541x anchor margin) + shape -0.87 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      6.6 → 6.6 → 6.6
- FEI      0.22 → 5.02 → 5.02
- Massey   7.96 → 6.37 → 6.37
- FPI      7.9 → 8.72 → 8.72
- TR       9.0 → 8.13 → 8.13
- PickSix  35 → 7.52 → 7.52
- blend 6.99  (dispersion 3.7)

## 4. Assembly
- anchor +6.99  class -0.00  k×resid -1.59 (k=0.35, cap ±6.0)  ST +0.08  → recentered (-0.50) → **+5.98**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (246e11f)