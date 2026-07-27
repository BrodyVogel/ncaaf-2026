You are compiling a source digest for a college football power-ratings model. I maintain unit-level grades (QB, RB, WR/TE, OL, DL, LB, DB, special teams) for every FBS team, frozen to a **July 12, 2026 information snapshot**. Your job is to sweep coverage of **SEC Media Days 2026** (believed to have run **July 20–23, 2026** — confirm exact dates and venue from coverage) and report every *concrete, sourced* piece of information that could change what I believed on July 12.

You are a **reporter, not an analyst**. Do not project wins, suggest grades, or editorialize about what anything "means" for a team's quality — that analysis happens downstream, by me. Your report will be machine-ingested, so following the output format exactly matters more than prose style.

## What to find (in priority order)

1. **QB competitions & depth-chart clarity.** Named starters, pecking order changes, coach language on any race. QB is the highest-leverage position for the model — top priority.
2. **Injuries, surgeries, availability.** Recovery timelines, players out, players cleared, missed-spring-now-practicing.
3. **Roster changes since July 12.** Late portal moves, dismissals, suspensions, eligibility rulings and waivers, academic casualties.
4. **Position switches and lineup reveals.** First-team compositions, OL alignments, named specialists.
5. **Coordinator/scheme substance.** Specific statements only, not generic scheme talk.
6. **Conference-wide items.** The SEC media predicted order of finish and preseason all-SEC teams (verbatim, with votes where published). Commissioner/league statements — especially anything on the conference schedule format (game count) and CFP posture.
7. **Answers to my open questions** — listed per-team below.

**Downweight but don't discard:** shape-of-his-life and culture talk; borderline items with factual content go in tagged LOW; pure fluff omitted.

**Secondary objective:** capture material roster/injury news from **July 12 → today** for these teams even if it didn't happen at the podium. Confirmations of previously-unsettled items count as new; recaps of pre-July-12 news do not, unless they answer an open question.

## Sourcing rules — hard requirements

- **Every item carries: source name, URL, publication date.** No exceptions.
- **Tag every item** `[QUOTE]` (exact on-record words, quoted) / `[REPORTED]` (identified beat reporter/credentialed outlet) / `[AGGREGATED]` (roundups) / `[RUMOR]` (pointers only; unconfirmed rumors only in coverage notes).
- **No prior-knowledge reliance; conflicting reports stay separate; honest empty sections beat filler.**
- Prefer primary/written material: official SEC Media Days transcripts (ASAP Sports posts these), sec sports.com media-day pages, beat-writer press coverage; then national outlets; then local papers. Search patterns: "[team] SEC Media Days quotes 2026", "[coach last name] SEC Media Days 2026", "[team] QB July 2026".

## Open questions, by team

Cover **every team below, in this order**, even those with no listed questions. For each listed question return an explicit verdict: **ANSWERED / PARTIAL / NOTHING FOUND**, with evidence or the searches that came up empty.

**Alabama**
- QB: Austin Mack's hold on QB1 — unequivocal, or camp language? Any specifics on the backup order.
- OL: Rebuilt interior — starting five settling?

**Arkansas** *(new HC)*
- QB: KJ Jackson confirmed? Any competition framing from the new staff.
- TEAM: New-staff install specifics (play-caller, front, tempo).

**Auburn** *(new HC)*
- QB: Byrum Brown (USF) — confirmed QB1? Health/durability notes given his running volume.
- TEAM: New-staff specifics.

**Florida** *(new HC — highest priority team in this sweep)*
- QB: Aaron Philo (Georgia Tech) — named the starter, or open race? Exact coach language matters here.
- OL: Rebuilt line — any first-five reveal (low-confidence room).
- TEAM: New-staff scheme install, coordinator roles, how spring went.

**Georgia**
- QB: Stockton's continuity — any competition or health notes at all (expect none — confirm).
- TEAM: Any defensive personnel reveals after the turnover.

**Kentucky** *(new HC)*
- QB: Kenny Minchey (Notre Dame) confirmed?
- LB: First-team reveals (low-confidence room).

**LSU** *(new HC)*
- QB: Sam Leavitt (Arizona State) — cleared, installed, any staff language on the transition.
- TEAM: New-staff specifics.

**Mississippi State**
- QB: Kamario Taylor's grip on the job — confirmed or contested?

**Missouri**
- QB: Austin Simmons (Ole Miss) — named QB1?

**Oklahoma**
- QB: Mateer's health post-2025 injury — fully cleared? Spring/summer participation specifics.

**Ole Miss** *(new HC)*
- QB: Chambliss's eligibility status (the court-won extra year) — any developments, and staff language on him.
- TEAM: New-staff install specifics.

**South Carolina**
- QB: Sellers — health notes.
- OL: Rebuilt line first-five (low-confidence room).

**Tennessee**
- QB: MacIntyre vs Brandon — hierarchy named, or full camp battle? Heupel's exact language.

**Texas**
- QB: Manning — any health/availability notes whatsoever; backup order behind him.
- TEAM: Any first-team reveals on the rebuilt defensive interior; anything specific on the Ohio State opener prep.

**Texas A&M**
- QB: Reed confirmed without qualification?

**Vanderbilt**
- QB: Jared Curtis (true freshman, #1 overall recruit) — is he THE guy day one, or is there bridge-QB language? Exact quotes.

## Output format

Produce a single markdown report, nothing else (no preamble about your process):

```
# SEC 2026 media days — source digest
Compiled: <date> · Event: <confirmed event name + dates + venue> · Baseline: 2026-07-12 snapshot

## 0. Top signals
<The ~10 highest-signal items conference-wide, one line each: TEAM — finding (unit).>

## 1. Predicted order & preseason honors
<Media predicted order of finish verbatim (with votes if published); all-SEC teams verbatim; source links.>

## 2. Conference-wide news
<Schedule-format/CFP/commissioner items, with citations.>

## 3. Teams
### <Team name>
**Answers to open questions:**
- <question> — ANSWERED/PARTIAL/NOTHING FOUND: <evidence>. (Source: <name>, <URL>, <date>)
**Findings:**
- [<UNIT>][<TAG>][<date>] <finding, exact quote if QUOTE>. (Source: <name>, <URL>, <date>)
<Unit keys: QB, RB, WRTE, OL, DL, LB, DB, ST, TEAM. LOW-signal items last, tagged LOW.>
**Coverage note:** <one line>

## 4. Coverage gaps
<Teams with thin coverage; searches that failed; sources you'd check next.>
```

First, confirm the event's exact dates and venue from coverage and state them in the header. Cover all 16 teams. Do not include betting analysis, win projections, or grade recommendations anywhere.
