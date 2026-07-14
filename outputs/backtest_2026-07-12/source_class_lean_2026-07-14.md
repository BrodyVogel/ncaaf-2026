# 2026 anchor sources: class lean relative to SP+ (measured 2026-07-14)

Method: normalize each captured source to SP+ scale (z x SP+SD + SP+mean), take mean
(source - SP+) by class, tilt = G5 mean - P4 mean. Answers whether the SP+-calibrated
class term transfers to the blended anchor.

| source | n | P4 lean | G5 lean | G5-vs-P4 tilt vs SP+ |
|---|---|---|---|---|
| ESPN FPI | 138 | +0.07 | -0.06 | -0.13 |
| FEI | 138 | -0.52 | +0.51 | +1.03 |
| Massey (own) | 138 | -0.06 | +0.06 | +0.12 |
| TeamRankings | 138 | +0.13 | -0.13 | -0.27 |

Blend-weighted tilt (SP+ x2, others x1; Pick Six excluded - P4-only, and its
order-statistic conversion cannot move the P4/G5 gap by construction): +0.13.

CONCLUSION: the P4-flattering bias is industry-wide, not an SP+ quirk. Class term
transfers ~unchanged: SP+-only +-1.75 -> blend +-1.68. Production rule: the anchor
loader recomputes the term per run from the live composition (SP+ historical bias
minus that run's measured blend tilt), so August's KFord addition auto-rescales it.
