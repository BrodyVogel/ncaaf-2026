# Clemson — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+9.50** (rank 29/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    48 | proxy —
- RB    52 | proxy 45
- WRTE  56 | proxy 75
- OL    48 | proxy 48
- DL    58 | proxy 86
- LB    54 | proxy 61
- DB    54 | proxy 84
- ST    56 | proxy 79

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.093 WRTE:+0.036 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +26.09 vs anchor off +29.28
- grade-implied def +24.02 vs anchor def +17.22  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-9.98**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level -6.52 (=-0.541x anchor margin) + shape -3.46 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      12.8 → 12.8 → 12.8
- FEI      0.47 → 10.41 → 10.41
- Massey   8.24 → 11.62 → 11.62
- FPI      13.4 → 15.13 → 15.13
- TR       11.6 → 10.62 → 10.62
- PickSix  23 → 13.12 → 13.12
- blend 12.36  (dispersion 4.72)

## 4. Assembly
- anchor +12.36  class -0.00  k×resid -3.49 (k=0.35, cap ±6.0)  ST +0.12  → recentered (-0.52) → **+9.50**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18 (3bec049)