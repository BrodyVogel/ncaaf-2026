# Pre-registration — Study 17: FCS→FBS grade translation (2026-08-02)

Phase A of SUBFBS_TRANSLATION_PLAN. Owner emphasis registered up front: FCS
internal competition spread is enormous ("NDSU and MVSU might as well have
been playing on different planets") — origin strength within FCS is
CO-PRIMARY, not a secondary conditioning term.

**Peek disclosure:** migration census only (pair counts 151/235/240/409 by
year, total 1,035; 2026 coverage 220/427, 88 starters). No translation
statistic, grade mean, or regression has been computed. Prior context: S16
(within-FBS continuous origin effect −0.077, G5-concentrated −0.204,
trench/back-7 carried, skill dead) and S10 (down-transfer QB pathology).

## Panel

FCS year Y (data/pff_history/fcs, ≥6 games) → FBS year Y+1 (existing FBS
loaders, ≥6 games), player NOT in FBS year Y; folds = origin years
2021–2024. Grade = grades_offense/defense from the canonical five files
(same operationalization as S16). Origin-strength proxy (no SP+ exists for
FCS): **team tape-mean** — game-count-weighted mean grade of all graded
players on the FCS team-year, min 20 players (computable from these
files). Destination strength: SP+ preseason year Y+1. Position groups: QB /
skill / trench / back-7 (S16 convention).

## Legs and bars

- **S17-L1 (baseline translation):** grade_FBS ~ grade_FCS + position-group
  dummies. Report slope, level drop, R² — the raw exchange rate. No
  pass/fail (descriptive foundation); claim only that slope > 0 at t ≥ 2
  (tape carries ANY signal across the jump — the license to use it at all).
- **S17-L2 (CO-PRIMARY, owner-emphasized):** + origin team tape-mean
  (centered within year). PASS iff |t| ≥ 2 AND ΔR² ≥ 0.01 over L1 AND LOYO
  sign ≥3/4. Report the implied NDSU-vs-MVSU spread: predicted FBS grade
  difference for the same FCS grade earned at a 90th- vs 10th-percentile
  FCS program.
- **S17-L3 (destination gap):** + destination SP+ (or origin-mean minus
  destination-SP as a single gap term if collinearity demands). Same bars,
  claimed separately.
- **S17-L4 (position groups, report):** L2 term × group. S16 predicts
  trench/back-7 carry it and skill travels; QB reported but governed by the
  S10 prior regardless.
- **S17-L5 (2026 projections, runs regardless of L2/L3 verdicts if L1's
  slope-positive claim holds):** fitted model → projected FBS grades for
  the 220 matched 2026 entrants (uncertainty band from fold scatter);
  deliverable table sorted by projected grade × two-deep slot, flagging
  (a) projected-strong starters on held/candidate teams, (b) projected-weak
  starters the brackets may be over-crediting. This is the Phase B
  case-read queue, NOT a grade change — adjudication stays case-by-case.
- **December:** the 220 get scored (projection vs realized 2026 FBS grade)
  as the out-of-sample fold; registered now.

## Limitations

Survivorship is STRUCTURAL: the panel conditions on earning ≥6 FBS games —
the translation is "given a real FBS role," not "given a roster spot";
Phase B reads must remember the selection. Team tape-mean is a proxy with
own-player contamination (a star lifts his own team mean; mitigated by
20-player minimum and by centering). PFF grade scale drift across
divisions unknown (intercept absorbs the mean; scale differences load on
the slope). QB n will be small. D2/D3 files now complete but EXCLUDED from
S17 (separate, thinner study once FCS sets the template).
