# Ohio State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **+26.36** (rank 2/138 in hybrid field)  band ±6.00

## 1. Unit grades (LLM real | shadow proxy)
- QB    91 | proxy 96
- RB    76 | proxy 87
- WRTE  86 | proxy 91
- OL    80 | proxy 81
- DL    76 | proxy 74
- LB    64 | proxy 96
- DB    72 | proxy 91
- ST    64 | proxy 84

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.070 RB:+0.091 WRTE:+0.036 OL:+0.082  (R²=0.52)
- def: DL:-0.084 LB:-0.055 DB:-0.095  (R²=0.61)
- grade-implied off +34.98 vs anchor off +40.40
- grade-implied def +20.32 vs anchor def +9.00  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **-16.74**
- resid decomposition (diagnostic): level -16.99 (=-0.541x anchor margin - the calibrated fade) + shape +0.25 (roster signal)

## 3. Anchor (per source: raw → normalized → used)
- SP+      31.8 → 31.8 → 31.8
- FEI      1.52 → 33.05 → 33.05
- Massey   9.3 → 31.49 → 31.49
- FPI      28.7 → 32.95 → 32.95
- TR       32.3 → 30.43 → 30.43
- PickSix  2 → 28.28 → 28.28
- blend 31.4  (dispersion 4.77)

## 4. Assembly
- anchor +31.40  class -0.00  k×resid -5.86 (k=0.35, cap ±6.0)  ST +0.28  → recentered (-0.54) → **+26.36**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×0) = ±6.00

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-16 (b0c0d89)