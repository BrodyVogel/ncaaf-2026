# UConn — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-6.90** (rank 95/138 in hybrid field)  band ±7.39

## 1. Unit grades (LLM real | shadow proxy)
- QB    46 | proxy —
- RB    48 | proxy 8
- WRTE  46 | proxy —
- OL    48 | proxy 12
- DL    46 | proxy 5
- LB    50 | proxy 33
- DB    44 | proxy 46
- ST    44 | proxy 37

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.071 RB:+0.093 WRTE:+0.036 OL:+0.083  (R²=0.54)
- def: DL:-0.082 LB:-0.059 DB:-0.097  (R²=0.61)
- grade-implied off +25.23 vs anchor off +20.43
- grade-implied def +26.19 vs anchor def +31.97  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+10.58**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +6.24 (=-0.541x anchor margin) + shape +4.34 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -11.2 → -11.2 → -11.2
- FEI      -0.46 → -9.65 → -9.65
- Massey   7.13 → -9.19 → -9.19
- FPI      -11.2 → -13.53 → -13.53
- TR       -10.9 → -10.92 → -10.92
- blend -10.95  (dispersion 4.34)

## 4. Assembly
- anchor -10.95  class +0.00  k×resid +3.70 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.46) → **-6.90**
- band: 6.0 × coach(1.13) × dispersion(1.00) × conf(1+0.03×3) = ±7.39

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T22:30:00Z (UConn)