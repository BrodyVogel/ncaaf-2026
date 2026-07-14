# FIXED GRADING PROMPT TEMPLATE — v1.2 (2026-07-14)

One position group per call, same template every call (brief §3). Grading is performed
interactively in-session, supervised (brief §9). v1.1 added: assembly manifest,
quant/qual integration rules, worked example, blinding v2 evidence classes.
v1.2 adds: the competition-discount rule (exemplar scale is conference-adjusted).

## Assembly manifest — what a grading call contains, in order
1. This template (with {TEAM}/{UNIT} filled)
2. `exemplars.md` — the FROZEN scale anchors + per-group reference tables
3. From `snapshots/{Team_Dir}/`, inlined verbatim:
   a. `unit_dossiers.md` — section for {UNIT} (primary input) + the team-context header
   b. `roster_two_deep.csv` — {UNIT} rows
   c. `pff/unit_{UNIT}.csv` + `pff/team_grades_2025.csv`
   d. `magazines.md` and `news.md` — entries touching {UNIT}
   e. `META.json` — gaps + confidence summary
4. The output schema (`grading_schema.json`)
A grade produced from anything less than this assembly is invalid.

---

## The task

Grade the **{UNIT}** of **{TEAM}** for the **2026 season** on a **0–100 national FBS
scale**: the percentile this unit would occupy among all 138 FBS teams' {UNIT} groups
in 2026 if the season played out as the evidence suggests. 50 = dead-average FBS unit.
Grade the unit as it will take the field in 2026 — returners, verified arrivals,
expected starters — not last year's unit.

## Evidence rules — blinding v2 (brief §4)

- **Never use, and disregard if encountered:** any overall team rating, ranking,
  projection, or predicted finish (SP+/FPI/FEI/Massey/TR/KFord/Pick Six overall,
  magazine predicted order, national top-25s), and every market number. You are the
  bottom-up signal; reconciliation happens later, in code.
- **Allowed as evidence, always attributed:** unit-level and player-level assessments
  from the magazines and Pick Six ("Athlon: #8 OL nationally"), all-conference teams,
  player ratings (247/On3/Sideline), scheme/coaching analysis, beat reporting.
- Do not anchor on program prestige. Grade the 2026 personnel.

## Integrating quantitative and qualitative evidence

1. **Start from the quantitative baseline** where one exists: returning players' PFF
   grades at meaningful volume, weighted by expected 2026 role from the two-deep.
2. **Move off the baseline only for named, dated, attributed reasons**: scheme change
   with a stated mechanism, credible camp/spring reporting, scouting consensus on a
   player's trajectory, arrival/departure quality the numbers can't see yet.
3. **Unproven players enter via priors, not invented stats**: recruiting composite,
   prior program level, valuation mosaic. State the hit case and the miss case; wide
   uncertainty pulls `confidence` down, not the grade toward false precision.
4. **Qualitative-only units are legal but capped**: a unit whose case rests mostly on
   priors/opinion (elite freshman QB, all-new portal room) can be placed anywhere the
   evidence argues — but confidence is at most M, and the rationale must say what
   would validate or falsify the placement.
5. **Conflicts lean quant**: when credible numbers and credible opinion disagree, the
   grade stays nearer the numbers; the conflict is recorded in `data_gaps` and
   confidence drops. Never split the difference silently.
6. **Both types appear in the rationale** whenever both exist. An opinion is never the
   sole justification for a grade (§4 v2 guardrail).
7. **Trust volume**: a PFF grade on 700 snaps is evidence; on 80 snaps it's a hint.
   Below ~100 snaps / 60 attempts / 150 routes, prior-year grades are weak signals.
8. **LB caution** (v1.2.1): LB is empirically the noisiest PFF unit signal — worst
   agreement with PFF's own team-level view (corr 0.50 vs 0.80–0.93 for every other
   group), largest competition offsets, smallest learned conversion weight. For LB,
   lean on run-defense/coverage SUB-grades and scouting consensus over overall grades,
   and expect wider honest uncertainty.
9. **Discount for competition** (v1.2): raw PFF grades are NOT opponent-adjusted. When
   weighing any player's raw PFF evidence, apply the conference discount table (end of
   exemplars.md) by the conference where the grade was EARNED — a MAC OL grade carries
   ~a 15-point discount vs the same number earned in the SEC; a MAC transfer's grade
   stays discounted after he moves up. Elite G5 seasons survive the discount; ordinary
   ones don't. The exemplar percentiles already have this baked in — never double-apply
   it to the exemplar reference values themselves.

## Scale discipline

- Anchor every grade to the FROZEN exemplar block. State the two bracketing exemplars
  ("between Nevada DB 2025 (70) and the 85 anchor") — cross-group comparisons are
  about scale position, not football similarity. Use the anchors' qualitative sketches
  to compare on substance, not just grade arithmetic.
- Integer grades only.
- A G5 unit graded above 75 requires an explicit `g5_guard_note` with concrete evidence.
- Sanity bands: 90+ ≈ top-10 unit nationally; 75 ≈ top-35; 50 ≈ average; 25 ≈ bottom-35;
  10 ≈ bottom-15.

## Worked example (mixed evidence — the expected common case)

*Hypothetical WRTE unit:* top returning receiver graded 78.5 on 612 routes in 2025
(quant baseline: strong #1). Second returner 64.0 on 401 routes (adequate). Portal
arrival from an FCS program: 89.2 FCS grade, Sideline values him mid-tier P4 starter,
Athlon calls the unit "a top-25 receiving corps if the FCS transfer translates"
(attributed opinion). TE room lost its starter; backup has 112 career routes (hint,
not evidence). Baseline from returners ≈ 65th percentile; the FCS arrival's prior
argues up, TE loss argues down; battle unresolved per news.md.
→ grade 68, confidence M, brackets [Nevada DB 2025 (70) above, DL 60-anchor below],
rationale cites the 78.5/612 fact, the FCS translation prior with hit/miss framing,
the attributed Athlon line, and the TE gap; `data_gaps`: TE battle unresolved as of
<date>. That is the shape every grade should take.

## Output — JSON only, exactly per `grading_schema.json`

```json
{
  "team": "{TEAM}", "unit": "{UNIT}", "grade": 0, "confidence": "H|M|L",
  "bracketing_exemplars": ["<lower anchor>", "<upper anchor>"],
  "rationale_bullets": ["3-6 bullets, each tied to snapshot evidence with season-year"],
  "key_players": [{"name": "", "role": "", "evidence": "dated fact from snapshot"}],
  "data_gaps": ["what the snapshot could not establish (each gap was search-verified)"],
  "g5_guard_note": "required iff G5 team and grade > 75, else null"
}
```

Confidence semantics: **H** = settled two-deep, proven production at volume;
**M** = one meaningful unknown; **L** = unit hinges on unproven players or open battles.

## Determinism aids
Work from the two-deep; do not invent personnel. Season-year every stat. Contradictions
go to `data_gaps`, not silent averaging.
