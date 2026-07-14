# 2026 cross-source anchor dispersion (measured 2026-07-14)

5 live sources normalized to SP+ scale. Median per-team range 4.7 pts; p90 10.4;
22 teams > 8 pts; 7 teams > 12 pts. Widest: NDSU 21.3 (FEI -21.3 vs Massey -0.0 -
FEI treats FBS newcomers differently), Southern Miss 16.9, Charlotte 14.9,
North Texas 13.6, Iowa State 13.5, Toledo 13.3, Oklahoma State 12.2, Utah 11.8.

Adopted policy (compute-phase spec, build step 5):
1. WINSORIZE (logged): source > 5 pts from median of other sources -> pulled to
   median +-5 before blending (data-error guard; preserves direction).
2. FLAG: top-decile dispersion teams auto-join the review pass.
3. BAND: x1.10 multiplier for top-decile dispersion (judgment-based, uncalibrated -
   no historical multi-source captures; revisit after 2026).

Also recorded: learned unit loadings from 2025 adjusted-grade proxy fit
(pts per 1 SD of unit quality): OFF OL +2.1, QB +1.9, RB +1.1, WRTE +1.0;
DEF DL 3.2, DB 2.9, LB 1.3. Production re-learns per run.
