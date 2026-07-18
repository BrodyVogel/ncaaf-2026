# App State — PILOT build sheet [REAL grades, proxy-fitted conversion (OOS)]

FINAL: **-8.21** (rank 99/138 in hybrid field)  band ±6.36

## 1. Unit grades (LLM real | shadow proxy)
- QB    40 | proxy —
- RB    48 | proxy 31
- WRTE  38 | proxy 4
- OL    40 | proxy 38
- DL    42 | proxy 33
- LB    54 | proxy 70
- DB    40 | proxy 5
- ST    44 | proxy 41

## 2. Conversion (fitted on 137 proxy teams, applied OOS)
- off: QB:+0.072 RB:+0.092 WRTE:+0.037 OL:+0.082  (R²=0.54)
- def: DL:-0.083 LB:-0.063 DB:-0.093  (R²=0.61)
- grade-implied off +23.86 vs anchor off +21.33
- grade-implied def +26.61 vs anchor def +33.47  (def is points-allowed scale: LOWER = better; higher implied than anchor = grades COOLER on the defense)
- (anchor off/def = SP+'s published splits, level-shifted by half the blend-vs-SP+ gap so off - def == blend; the residual nets to implied_margin - blend, so the SP+ shape never moves the final number)
- residual (off-minus-def, grades-vs-anchor): **+9.40**
- resid decomposition (diagnostic, PROXY-FIT REGIME): level +6.57 (=-0.541x anchor margin) + shape +2.83 (roster signal + conversion artifact; see GRADING_BIAS_DIAG)

## 3. Anchor (per source: raw → normalized → used)
- SP+      -12.1 → -12.1 → -12.1
- FEI      -0.52 → -10.94 → -10.94
- Massey   6.92 → -13.13 → -13.13
- FPI      -9.8 → -11.9 → -11.9
- TR       -10.9 → -10.92 → -10.92
- blend -11.85  (dispersion 2.21)

## 4. Assembly
- anchor -11.85  class +0.00  k×resid +3.29 (k=0.35, cap ±6.0)  ST -0.12  → recentered (-0.47) → **-8.21**
- band: 6.0 × coach(1.0) × dispersion(1.00) × conf(1+0.03×2) = ±6.36

## 5. Pilot caveats
- Conversion weights are proxy-fitted (real-grade refit happens at full 138).
- Rank is vs a 137-proxy field — indicative only.
- grades snapshot rev: frozen 2026-07-18T14:26:00Z (App State)