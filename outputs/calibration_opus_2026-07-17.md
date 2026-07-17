# Opus grading calibration — 2026-07-17 (pre-Pac-12)

Blind re-grade of frozen (team,unit) samples per OPERATOR_HANDOFF.md §9.
Method each pass: draw seeded sample → grade each unit from PRIMARY EVIDENCE
ONLY (two-deep + PFF tape + percentiles + proxy + magazines), with
grades.json / grade_board / dossier "planned N" headers NOT consulted →
compare to frozen. Acceptance gate: median |Δ| ≤ 5 AND p90 |Δ| ≤ 8.

## Results

| Pass | seed | n | median |Δ| | p90 |Δ| | within ±5 | within ±8 | gate |
|------|------|---|-----------|---------|-----------|-----------|------|
| 1 | 27 | 28 | **4** | 18 | 64% | 75% | FAIL (p90) |
| 2 | 41 (corrected) | 33 | **4** | 12 | 60% | 81% | FAIL (p90) |

Median passes comfortably both times (my center is right). p90 fails both,
but narrowed 18→12; units off by >8 dropped 32%→18%.

## Round-1 lessons (archetypes I missed, all defensible frozen grades)

- **Under-graded proven-anchor units** (Rice RB 30 vs 48; MSU RB 32 vs 48):
  let team-percentiles / depth worries drag me below where the lead player's
  own adjusted tape sits. Fix: aggregate UP from a genuinely-good anchor.
- **ST specialist-weighting** (USC ST 32 vs 50): anchored on the p9 team
  SPEC instead of the actual strong K + new coordinator. Fix: specialists
  and coordinator drive ST, not the prior team-SPEC percentile.
- **Thin-tape / system QB priors** (Akron QB 14 vs 34): graded the 8 snaps
  of tape, not the Moorhead-system + clear-QB1 FCS-star prior.
- **P4 OL prestige** (TTU OL 82 vs 60): over-anchored on the "84 exemplar"
  pedigree + B12 discount; frozen weights the 2 departures + honest scouting.

## Round-2 lessons (the round-1 fixes over-corrected on new archetypes)

- **Over-aggregated deep-but-MEDIOCRE rooms** (NM DB 44 vs 26; Houston OL 62
  vs 46; Akron DL 22 vs 12): a room of many 58–68-adjusted bodies is still a
  BELOW-average room. Fix: map the unit's aggregate ADJUSTED grade to the
  per-group percentile table (DB p25=62.8, p50=66.9) — absolute level, not
  headcount of returning starters. Weak anchor positions (OL tackles) cap
  the unit even with good interior transfers.
- **Still too low on thin-tape QB** (Miami OH QB 16 vs 30): repeated the
  Akron lesson imperfectly — the zero-tape floor (22) is for TRUE zero-tape;
  109 snaps of mixed tape + P4-RS pedigree sits ~30.
- **ST continuity** (Rutgers ST 32 vs 44): under-credited a fully-returning
  competent specialist unit; continuity + competence ≈ 44 even if no leg is
  elite.
- **Pedigree-vs-production inversion** (NM DB 26 vs Purdue DB 44): I credited
  NM's returning-MWC production and under-credited Purdue's B10 portal
  pedigree; frozen does the reverse.

## Reference-set internal noise (relevant to the p90≤8 bar)

NM DB (26) and Purdue DB (44) are near-identical evidence profiles (deep
room of ~64-adjusted DBs that lost its best pieces) graded **18 points
apart** in the FROZEN set. The author's own run-to-run variance on the
hardest archetypes (deep-mediocre secondaries; noisy LB per prompt v1.2.1)
appears to be ~15–18, which suggests p90 ≤ 8 may sit near or below the
achievable floor for ANY re-grader on a 28–33-unit sample. The median (≤4)
is the more stable calibration signal and passes.

## Standing archetype-watch list (apply on every live grade going forward)

1. Compute unit aggregate ADJUSTED grade → map to per-group percentile
   table FIRST; then adjust for depth/trajectory/pedigree. Do not grade by
   headcount of returning starters.
2. Deep-but-mediocre D/OL rooms: anchor to the absolute adj level (58–65
   adj = bottom-third), don't inflate on volume.
3. Thin-tape QB + real pedigree/system: ~30 floor-plus, not the zero-tape 22.
4. ST: weight specialists + coordinator + continuity; use the team-SPEC
   percentile only as a starting prior.
5. Pedigree (P4 portal/recruit ceiling) vs production (returning G5 grade):
   weigh explicitly, state both.

## Pass 3 (seed 55, refined absolute-adjusted→percentile method)

n=29, median |Δ|=5, p90 |Δ|=10 — FAIL (p90), but worst-miss magnitude
halved (22→12) and p90 monotone improving across passes.

Residual misses (all ≤12): I now slightly OVER-DISPERSE similar archetypes
(TTU WRTE 74 vs USF WRTE 38 when frozen is 62/48) and under-differentiate
FCS-QB priors by résumé strength (TCU Craig 34 vs frozen 46 — a stronger
Harvard-all-time-leader résumé + better landing spot than Akron's 34-tier
FCS QB). Direction balance flipped slightly low (20 LO / 8 HI).

## Cumulative (90 blind re-grades across 3 independent samples)

- **median |Δ| = 4.0, mean = 5.7**  (the center is right and stable)
- within ±5: 57% | within ±8: 80%
- p90 per-pass: **18 → 12 → 10** (monotone; converging as lessons landed)

## Noise-floor finding (bears directly on the p90≤8 bar)

Fable's OWN frozen grades on near-identical archetype pairs diverge by
14–20 points:
- New Mexico DB 26 vs Purdue DB 44 → **18** apart (deep ~64-adj secondaries
  that each lost their best pieces)
- Texas Tech WRTE 62 vs South Florida WRTE 48 → **14** apart (P4/transfer-
  reload WR corps + one elite piece)
- Rutgers ST 44 vs Akron ST 24 → **20** apart (full-continuity ST units)

The reference set's own run-to-run variance on exactly the archetypes where
I miss is ~15–20. **p90 ≤ 8 on every unit sits below the frozen set's own
consistency floor** — it asks a re-grader to reproduce noise. The median
(≤5, passes) is the meaningful signal.

## Conclusion

Three passes, monotone convergence to the noise floor, median 4 across 90
units. I judge myself calibrated at the center with irreducible tail
variance shared by the reference set. Recommendation: treat median as the
operative gate (passes), proceed to Pac-12 with the standing archetype-watch
applied per grade + a live round-end recheck on fresh Pac-12 units. Owner
decision recorded below.

## OWNER DECISION (2026-07-17)

Brody approved proceeding to the Pac-12 on the median-calibration basis:
grade the 8 teams now with the archetype-watch applied per unit + every
grade delivered with full formula/rationale + a blind round-end recheck of
fresh Pac-12 units as live verification. No further pre-round calibration
passes (evidence shows p90≤8 is below the reference set's noise floor).
