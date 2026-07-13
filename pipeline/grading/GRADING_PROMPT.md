# FIXED GRADING PROMPT TEMPLATE — v1.0 (2026-07-13)

One position group per call. Same template every call (brief §3). Grading is performed
interactively in-session, supervised (brief §9 — no programmatic API calls). The harness
concatenates: this template + the exemplar block (`exemplars.md`) + the team's frozen
snapshot for the unit + the output schema (`grading_schema.json`).

---

## The task

You are grading the **{UNIT}** of **{TEAM}** for the **2026 season** on a **0–100
national FBS scale**, where the grade means: *the percentile this unit would occupy
among all 138 FBS teams' {UNIT} groups in 2026 if the season played out as the evidence
suggests.* 50 = dead-average FBS unit. Grade the unit as it will take the field in 2026
— returners, verified arrivals, expected starters — not last year's unit.

## Blinding rule — HARD (brief §4)

Use ONLY the frozen snapshot below. If any consensus rating, ranking, market number,
win total, or "expert prediction of finish" appears anywhere in the evidence or your
memory of this team, DISREGARD it entirely. You are the bottom-up signal; consensus
reconciliation happens later, in code, not here. Do not anchor on program prestige —
grade the 2026 personnel.

## Scale discipline

- Anchor every grade to the FIXED exemplar block (attached). State explicitly which two
  exemplars bracket your grade ("between Nevada DB 2025 (70) and Temple OL 2025 (85)"
  — cross-group comparisons are about scale position, not football similarity).
- Integer grades only.
- A G5 unit graded above 75 requires an explicit `g5_guard_note` citing concrete
  evidence (returning all-conference production, elite portal arrivals with grades,
  dominant 2025 PFF numbers at meaningful volume).
- Trust volume: a PFF grade on 700 snaps is evidence; a PFF grade on 80 snaps is a hint.
  Below ~100 snaps/60 attempts/150 routes, treat prior-year grades as weak signals.

## Unproven players (brief §5)

Freshmen, low-snap transfers, and JUCO/FCS arrivals get **priors, not invented grades**:
recruiting composite level, prior program level, portal valuation, camp buzz (dated).
Their presence widens uncertainty — reflect that in `confidence` and `data_gaps`, and
say what the unit looks like if the unproven player hits vs. misses.

## Output — JSON only, exactly this shape

```json
{
  "team": "{TEAM}",
  "unit": "{UNIT}",
  "grade": 0,
  "confidence": "H|M|L",
  "bracketing_exemplars": ["<lower anchor>", "<upper anchor>"],
  "rationale_bullets": ["3-6 bullets, each tied to snapshot evidence with season-year"],
  "key_players": [{"name": "", "role": "", "evidence": "dated fact from snapshot"}],
  "data_gaps": ["what the snapshot could not establish"],
  "g5_guard_note": "required iff G5 team and grade > 75, else null"
}
```

Confidence semantics: **H** = settled two-deep, proven production at volume;
**M** = one meaningful unknown (new starter with partial evidence, thin depth);
**L** = unit hinges on unproven players or unresolved battles.

## Determinism aids

- Work from the two-deep in the snapshot; do not invent personnel.
- Cite season years on every stat ("2025: 8.1 YPA on 378 dropbacks").
- If evidence is contradictory, say so in `data_gaps` rather than splitting the difference silently.
