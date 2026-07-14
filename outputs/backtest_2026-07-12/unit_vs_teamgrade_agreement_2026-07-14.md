# Player-aggregate unit grades vs PFF's own team-grade columns (2025, raw scale)

Question (user): is there a systemic gulf between our snap-weighted player aggregates
and PFF's team-level grades? Correlations + percentile-gap stats per unit:

| unit | corr | median |gap| | p90 |gap| | gaps>25 |
|---|---|---|---|---|
| QB | 0.92 | 7.3 | 19.5 | 5 |
| RB | 0.80 | 11.9 | 31.1 | 24 |
| WRTE | 0.85 | 8.3 | 25.8 | 16 |
| OL | 0.93 | 7.1 | 17.3 | 6 |
| DL | 0.86 | 9.4 | 23.3 | 12 |
| **LB** | **0.50** | **22.5** | **43.3** | **51** |
| DB | 0.88 | 8.1 | 24.3 | 11 |

CONCLUSION: no systemic gulf for 6 of 7 units - two views of the same reality agreeing
at 0.80-0.93. LB is the documented exception (also: largest competition offsets, smallest
learned conversion loading) -> prompt v1.2.1 adds the LB-caution rule. The two measures
differ BY DESIGN: team columns grade the side-of-ball FUNCTION on all snaps (RDEF counts
DL+LB+S run defense); our aggregates grade the POSITION GROUP's >=200-snap personnel -
the only construction that supports returning-weighting, and the one the calibration
validated predictively (gamma=0.389).

Northwestern post-mortem: DL raw gap 17 pctile pts (inside DL's normal band); the B10
+10 offset stretched the DISPLAYED gap to 35 -> anchor filter (correctly) evicted it.
Run-front context confirms the user's hypothesis in part: non-DL run defenders were
mediocre-to-poor (S Wallace 55.0 overall/61.5 runD on 630 snaps; LBs Brus 61.7/66.3,
Uihlein 70.4/70.7; one standout S Fitzgerald 90.2 runD), stacking with the DL's own
soft run-D sub-grades (54-71) to produce team RDEF p33 while the DL's pass rush was
genuinely elite (PRSH p81; player sub-grades 79.8-84.1).
