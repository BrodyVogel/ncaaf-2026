You are compiling a source digest for a college football power-ratings model. I maintain unit-level grades (QB, RB, WR/TE, OL, DL, LB, DB, special teams) for every FBS team, frozen to a **July 12, 2026 information snapshot**. Your job is to sweep coverage of the **American Athletic Conference's 2026 media days** (believed to have run **July 23–24, 2026** — confirm exact dates and venue from coverage) and report every *concrete, sourced* piece of information that could change what I believed on July 12.

You are a **reporter, not an analyst**. Do not project wins, suggest grades, or editorialize about what anything "means" for a team's quality — that analysis happens downstream, by me. Your report will be machine-ingested, so following the output format exactly matters more than prose style.

## What to find (in priority order)

1. **QB competitions & depth-chart clarity.** Named starters, pecking order changes, coach language on any race ("X is our guy" vs "it'll go to camp"). QB is the highest-leverage position for the model — treat any QB news as top priority.
2. **Injuries, surgeries, availability.** Recovery timelines, players out for the season, players cleared, players who missed spring now practicing.
3. **Roster changes since July 12.** Late portal exits/entries, dismissals, suspensions, eligibility rulings and waivers, academic casualties, retirements.
4. **Position switches and lineup reveals.** Who is running with the first team, OL alignments, named specialists/returners, rotation statements.
5. **Coordinator/scheme substance.** New play-caller, tempo/front changes — only where a coach or beat reporter says something specific.
6. **Conference-wide items.** The AAC preseason media poll (full order, points/first-place votes, verbatim) and preseason all-conference team (verbatim). Any league statements on scheduling or membership.
7. **Answers to my open questions** — listed per-team below. These are the units where my grade is explicitly low-confidence; direct evidence on them is the most valuable thing you can return.

**Downweight but don't discard:** "best shape of his life," culture talk, generic optimism. Borderline items with any factual content: include tagged LOW. Pure fluff: omit.

**Secondary objective:** while inside a team's coverage, also capture material roster/injury news from **July 12 → today** even if it didn't happen at the podium. The snapshot only cares about the delta. A coach *confirming* something previously unsettled counts as new information; recaps of pre-July-12 news do not, unless they answer an open question.

## Sourcing rules — hard requirements

- **Every item carries: source name, URL, publication date.** An item you cannot cite does not go in.
- **Tag every item** `[QUOTE]` (exact on-record words, quoted) / `[REPORTED]` (identified beat reporter or credentialed outlet) / `[AGGREGATED]` (roundups, rankings articles) / `[RUMOR]` (boards/social — usable only as pointers to a primary source; unconfirmed rumors go only in the coverage-notes line).
- **Do not rely on prior knowledge of these teams.** Everything must come from sources found in this research; conflicting reports stay separate with both citations.
- **An honest empty section beats filler.** Thin coverage → state exactly what you searched and found nothing.
- Prefer primary/written material: official AAC media-day pages and transcripts, on-record pressers written up by beat writers; then national outlets (ESPN, CBS, The Athletic, On3, 247Sports); then team sites and local papers. Search patterns: "[team] AAC media day quotes 2026", "[coach last name] American media day 2026", "[team] QB competition July 2026".

## Open questions, by team

Cover **every team below, in this order**, even those with no listed questions. For each listed question return an explicit verdict: **ANSWERED / PARTIAL / NOTHING FOUND**, with evidence or the searches that came up empty.

**Army**
- LB: Post-graduation rebuild — who runs with the first unit? Any Hellums (RB) workload/health notes.

**Charlotte**
- QB: The three-way battle (Gonzales–Pitt/WCU vs the others) — any hierarchy named or coach language on timing?
- OL / LB / ST: First-team reveals or transfer additions on any of the three (all low-confidence rooms).

**East Carolina**
- QB: Houser's replacement — Griffis (Texas Tech, prior Wake starts) vs the field: named, leading, or "to camp"?
- WRTE: Who emerges as the top targets? Any TE role statements.
- LB: Starters after the turnover — names running first-team.

**Florida Atlantic**
- QB: Veltkamp's grip on the job — any competition language at all, or full confirmation?
- LB / DB: First-team reveals in the two low-confidence back-seven rooms.

**Memphis** *(new HC — highest priority team in this sweep)*
- TEAM: Anything specific on the new staff's scheme install, play-caller, and how spring/summer went.
- QB: Who leads the room? Any named starter or explicit race framing.
- OL / ST: Starting-five composition; specialist jobs settled?

**Navy**
- QB: Woodson's health and any statements on the option install/adjustments under the current staff.

**North Texas** *(new HC)*
- QB: Jackson (UCF) vs Jimerson (yr-2) — hierarchy named?
- DB: First-team reveals in the rebuilt secondary.

**Rice**
- QB: Jacurri Brown confirmed as the guy, or competition language?
- LB / DB: Starters after the turnover.

**South Florida** *(new HC)*
- QB: Van Buren (LSU/MSU starts) — confirmed QB1?
- OL / LB: First-team composition in both low-confidence rooms.

**Temple**
- QB: Smolik (PSU) vs Sheppard (WSU) — any movement from the spring charting?
- LB / DB: Starters named.

**Tulane** *(new HC)*
- QB: Chriss (Houston) vs Semonza (MAC production) — hierarchy, and any scheme-fit language from the new staff.
- OL: Starting five settling?

**Tulsa**
- QB: Anything on Hayes year two — durability, passing-game development work, staff language on his off-season. Any hint of competition (there should be none — confirm).
- LB: First-team reveals in the low-confidence room.

**UAB** *(new HC)*
- QB: Burton's job security under the new staff — confirmed or opened?
- DL / LB / DB: Any first-team reveals across the rebuilt defense (all three low-confidence).

**UTSA**
- QB: McCown's health post-hernia surgery — fully cleared? Practice participation specifics.
- DL / LB / DB: Starters across the defense (all low-confidence).

## Output format

Produce a single markdown report, nothing else (no preamble about your process):

```
# AAC 2026 media days — source digest
Compiled: <date> · Event: <confirmed event name + dates> · Baseline: 2026-07-12 snapshot

## 0. Top signals
<The ~10 highest-signal items conference-wide, one line each: TEAM — finding (unit).>

## 1. Media poll & preseason honors
<Poll verbatim with points/votes; all-AAC team verbatim; source links.>

## 2. Conference-wide news
<Scheduling/membership/commissioner items, with citations.>

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

First, confirm the event's exact dates from coverage and state them in the header. Cover all 14 teams. Do not include betting analysis, win projections, or grade recommendations anywhere.
