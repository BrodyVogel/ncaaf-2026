# Per-team research procedure — v1.0 (2026-07-13). Implements brief §5. Commit = freeze.

Trigger: **"Run the pipeline for Team X."** Steps 0-7, in order, interactively
(brief §9: supervised, in-session). Most teams complete cleanly; stop with ONE question
when blocked (brief §9). Clean teams first, messy last.

## 0. Assemble the deterministic pack
`python3 pipeline/snapshot_build.py "<CFBD school name>"` → stages CFBD pulls (team,
2025 roster, 2026 portal in/out, schedule, talent/recruiting history, coaches), the PFF
evidence pack (2025 rows for the team's players + every verified arrival's 2025 rows at
their origin school, provenance-tagged), team grades row, and skeletons.

## 1. Two-deep (PRIMARY sources: OurLads + official roster)
- Fetch OurLads depth chart (research-time web fetch) and the school's official 2026
  roster page. Fill `roster_two_deep.csv`: starter + backup per unit.
- Every player: `confidence_HML` + at least `source_1`. **Fringe/disputed status needs
  TWO independent sources** (OurLads + one of ESPN / RotoWire / The Sideline). One
  source suffices only when context is overwhelming (e.g., returning All-American).
- Portal arrivals: verify **enrolled**, not merely committed (school release or two
  trackers). Departures: confirm actually gone (portal_2026_out + roster absence).
- Low confidence anywhere in the two-deep → say so in META; it widens the band later.

## 2. Stats (CFBD + staged PFF only)
Machine-read beats web search (brief §5). Every number carries a season year. The PFF
pack is already filtered/tagged — do not re-scrape PFF (brief §12). CFBD 2026 returning
production is a known gap until August; note it, don't approximate silently.

## 3. Magazines (SECONDARY: identification + history)
Phil Steele conference file (searchable) + Athlon conference file, this team's pages:
- EXTRACT: personnel notes, injuries, position battles, scheme changes, coach quotes,
  two-deep discrepancies vs step 1 (resolve toward primary sources; note conflicts).
- **NEVER copy**: predicted order of finish, unit rankings, ratings, win totals — those
  are 2026 predictions (brief §4). Facts yes, forecasts no.
- OCR rule (brief §14): any load-bearing Phil Steele number gets checked against the
  page image.
- Dated entries in `magazines.md` ("2026 PS p.212: ...").

## 4. Portal valuations (The Sideline)
Research-time fetch for this team's arrivals/departures; save raw into `pulls/`
(dated). Used as PRIORS for unproven arrivals, not as grades.

## 5. News sweep (TERTIARY)
Beat coverage since spring: QB battle status, injuries, suspensions, retirements,
late portal moves. Dated entries in `news.md`; discard anything undated/unsourced.
Disregard every ranking/prediction encountered (brief §4).

## 6. Unproven players
Priors, not fake grades: 247 composite (for 2026 classes: 247 site until CFBD loads),
prior program level, Sideline valuation, dated camp reports — with explicit
uncertainty. Record in the two-deep `notes` + unit `data_gaps`.

## 7. Freeze
- Fill META.json: gaps, per-unit data-confidence summary, sources used.
- `python3 pipeline/blinding_check.py snapshots/<Team_Dir>` → resolve every flag
  (edit or justify; the lint is a reviewer, not an absolute).
- `git add snapshots/<Team_Dir> && git commit -m "snapshot(<team>): freeze <date>"`
  and push. **A committed snapshot is frozen** — grading reads only frozen snapshots.

## Then: grading (separate pass, brief §3/§4)
Eight calls per team using `grading/GRADING_PROMPT.md` + `grading/exemplars.md` +
the frozen snapshot, one unit each, JSON per `grading/grading_schema.json`, saved to
`snapshots/<Team_Dir>/grades.json`. Grades + provisional readout per team; league-wide
fit only when all teams are graded (brief §3 sequencing).
