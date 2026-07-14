# Per-team research procedure — v2.0 (2026-07-14). Implements brief §5 + blinding §4 v2.

Supersedes v1. Changes: obsessive-depth mandate (research_log, unit dossiers, source
minimums), Pick Six joins the magazine sweep for P4/ND under blinding v2, player
valuations become an explicit mosaic. Commit = freeze, unchanged.

**The standard: obsessive.** Research depth is the edge. Rocks under rocks. A data gap
is a *finding that the information does not exist*, proven by a logged failed search —
never a shrug. There is no "too much research."

Trigger: **"Run the pipeline for Team X."** Interactive, supervised (brief §9). Stop
with ONE question when truly blocked. Clean teams first, messy last.

## 0. Assemble the deterministic pack
`python3 pipeline/snapshot_build.py "<CFBD school name>"` — CFBD pulls, PFF evidence
(team's 2025 rows + every arrival's 2025 rows at origin, provenance-tagged), team
grades row, skeletons. This is the FLOOR of the snapshot, never the snapshot.

## 1. Two-deep (PRIMARY sources: OurLads + official roster)
- OurLads depth chart + the school's official 2026 roster page. Fill
  `roster_two_deep.csv`: starter + backup per unit, `confidence_HML` + `source_1` each.
- **Fringe/disputed status: TWO independent sources** (OurLads + one of ESPN / RotoWire
  / The Sideline / verified beat report). One source only when context is overwhelming.
- Arrivals: verify **enrolled** (school release or two trackers), not merely committed.
  Departures: confirm gone (portal_2026_out + roster absence).
- Position battles: record the battle as a battle (candidates + latest dated reporting),
  don't silently pick a winner.

## 2. Stats (CFBD + staged PFF only)
Machine-read beats web search. Every number carries a season year. Do not re-scrape PFF
(brief §12) — the staged pack has it. CFBD 2026 returning production absent until
August: derive "who returns" bottom-up from the two-deep + player-level PFF instead.

## 3. Magazine + preview sweep (SECONDARY: identification, history, unit/player opinion)
**P4 + Notre Dame: Phil Steele + Athlon + Pick Six team pages. G5: Phil Steele + Athlon.**
- EXTRACT: personnel notes, injuries, battles, scheme changes, coach quotes, unit-level
  assessments and rankings ("#8 OL nationally" — allowed under §4 v2, attributed),
  all-conference selections, two-deep discrepancies vs step 1 (resolve toward primary).
- **NEVER record**: overall team ratings/rankings, predicted order of finish, national
  top-25 placement, projected records, win totals. Pick Six page headers print the
  team's overall rank — read past it; it never enters the snapshot.
- OCR rule (brief §14): any load-bearing Phil Steele number gets checked against the
  page image. Athlon + Pick Six are born-digital; quote exactly.
- Dated entries in `magazines.md` ("2026 PS p.212: ...", "2026 P6 IOWA p.2: ...").

## 4. Player-valuation MOSAIC
For every arrival, key returner, and unproven projected starter, assemble from ALL of:
The Sideline valuation, 247/On3 player page (composite, transfer rating), magazine
blurbs, Pick Six player notes, dated beat reports. Attribute each. No single source is
load-bearing; disagreements recorded, not averaged away. Save raw pulls into `pulls/`.

## 5. News sweep (TERTIARY) — where the obsession shows
Minimum sweep per team, logged in `research_log.md` whether fruitful or not:
- at least TWO local beat outlets (papers, rivals/247 team sites, credible team blogs)
- spring practice + spring game reports; post-spring depth chart takes
- injury/suspension/retirement/late-portal news since spring
- coordinator/staff changes and scheme notes
- anything else the searches surface — follow threads until they die
Dated entries in `news.md`. Facts and attributed assessments only; no forecasts of
records/finish. If an Eastern-Michigan-grade obscure report exists, find it.

## 6. Unit dossiers — the grading input
Write `unit_dossiers.md`: one section per unit (QB, RB, WRTE, OL, DL, LB, DB, ST):
- **Settled facts** (dated: returning production at volume, arrivals/departures, injuries)
- **Quant summary** (PFF evidence pack distilled: who returns at what grade/volume)
- **Attributed opinions** (magazine/Pick Six unit assessments, beat takes)
- **Unproven-player priors** (mosaic values, hit/miss framing)
- **Open questions** (unresolved battles, verified gaps)
Minimum **3 independent sources per unit** or an explicit "exhausted: only N exist"
note. The dossier organizes evidence — it does NOT assign a grade or pre-bake one.

## 7. research_log.md — the audit trail
Every source consulted, dated, including dead ends ("searched <X>: nothing new").
This is how "no rock unturned" is verified after the fact.

## 8. Freeze
- META.json: gaps (each with its failed-search log line), per-unit confidence summary,
  sources used, magazine pages read.
- `python3 pipeline/blinding_check.py snapshots/<Team_Dir>` → resolve or justify every
  flag (it's a reviewer, not a censor — unit-rank citations are legal, overall-rank
  language is not).
- `git add snapshots/<Team_Dir> && git commit -m "snapshot(<team>): freeze <date>"` +
  push. **A committed snapshot is frozen.**

## Then: grading (separate pass)
Eight calls per team: `grading/GRADING_PROMPT.md` (v1.1) + `grading/exemplars.md`
(FROZEN) + the frozen snapshot per the prompt's assembly manifest → JSON per
`grading_schema.json` → `snapshots/<Team_Dir>/grades.json`. League-wide fit only when
all teams are graded (brief §3 sequencing).
