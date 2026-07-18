# Arkansas State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-7.02** (rank 95/138 in hybrid field)  band ±6.18

## 1. Unit grades (LLM real | shadow proxy)
- QB    44 | proxy —
- RB    52 | proxy 19
- WRTE  50 | proxy 34
- OL    54 | proxy 41
- DL    40 | proxy 34
- LB    42 | proxy 2
- DB    44 | proxy 5
- ST    56 | proxy 69

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.059 DB:-0.096  (R²=0.61)
- grade-implied off +26.11 vs anchor off +22.37
- grade-implied def +27.17 vs anchor def +33.63  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+10.19**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +6.09 (=-0.541x anchor margin) + shape +4.10 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -8.5 → -8.5 → -8.5
- FEI      -0.64 → -13.53 → -13.53
- Massey   6.86 → -14.26 → -14.26
- FPI      -9.2 → -11.2 → -11.2
- TR       -11.0 → -11.01 → -11.01
- blend -11.17  (dispersion 5.76)

## 4. Assembly
- anchor -11.17  class +0.00  k×resid +3.57 (k=0.35, cap ±6.0)  ST +0.12  → recentered (-0.47) → **-7.02**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×1) = ±6.18

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T14:34:00Z (Arkansas State)