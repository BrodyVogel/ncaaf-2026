You are compiling a source digest for a college football power-ratings model. I maintain unit-level grades (QB, RB, WR/TE, OL, DL, LB, DB, special teams) for every FBS team, frozen to a **July 12, 2026 information snapshot**. Your job is to sweep coverage of the **Mid-American Conference's 2026 media day** (believed **July 22, 2026** — traditionally in Detroit; confirm the exact date, venue, and format from coverage) and report every *concrete, sourced* piece of information that could change what I believed on July 12.

You are a **reporter, not an analyst**. Do not project wins, suggest grades, or editorialize about what anything "means" for a team's quality — that analysis happens downstream, by me. Your report will be machine-ingested, so following the output format exactly matters more than prose style.

**League context (important):** the 2026 MAC in my model is 13 teams: Akron, Ball State, Bowling Green, Buffalo, Central Michigan, Eastern Michigan, Kent State, Massachusetts, Miami (OH), Ohio, Sacramento State, Toledo, Western Michigan. **Northern Illinois left for the Mountain West (football) — do not cover them.** UMass is newly a full member; **Sacramento State is a 2026 FCS reclassification** — my roster data on them is thinner than usual, so treat them as a double-priority sweep. This league had extreme QB turnover: by my count, eight of the thirteen rooms have no returning starter or an unresolved battle — QB clarity is the single most valuable thing you can return.

## What to find (in priority order)

1. **QB competitions & depth-chart clarity.** Named starters, coach language on races, transfer pecking orders. For unresolved battles, capture the coach's *framing* even if no starter is named.
2. **Injuries, surgeries, availability.** Recovery timelines, players out/cleared, spring absences now practicing.
3. **Roster changes since the snapshot.** Late portal exits/entries, dismissals, suspensions, eligibility rulings, retirements.
4. **Position switches and lineup reveals.** First-team reps, OL alignments, named specialists/returners.
5. **Coordinator/scheme substance.** New head coaches/coordinators with specifics — several MAC programs changed staff this cycle; establish each team's current HC/coordinators from coverage rather than assuming.
6. **Conference-wide items.** The preseason media poll (full order, verbatim, with votes) and preseason all-MAC team (verbatim). Any commissioner statements on membership, scheduling format, or Sacramento State's transition status.
7. **Answers to my open questions** — per team below.

**Downweight but don't discard:** "best shape of his life," culture talk, generic optimism. Include only if there's a factual nugget, tagged LOW. Pure fluff: omit.

## Sourcing rules — hard requirements

- **Every item carries: source name, URL, and the source's publication date.** No citation, no inclusion.
- **Tag every item** with exactly one of:
  - `[QUOTE]` — direct on-record words (include the exact quote).
  - `[REPORTED]` — a fact from an identified beat reporter/credentialed outlet.
  - `[AGGREGATED]` — secondary write-ups, roundups, rankings.
  - `[RUMOR]` — message boards/Reddit/unsourced social. Usable **only as a pointer** to find a primary source; a rumor with no primary source may appear only in the coverage note, never as a finding.
- **Do not rely on your prior knowledge of these teams.** Everything must come from sources you found during this research. If memory and a source disagree, the source wins; no source, no claim.
- **Do not merge conflicting reports.** If two sources disagree, present both with citations. (Miami (OH) below has a known print conflict to resolve.)
- **An honest empty section beats filler.** Thin coverage → say what you searched and found nothing; do not pad with old news.
- Prefer primary/written material: official MAC media-day pages/transcripts, beat-writer write-ups, team athletics sites. Then national outlets (ESPN, CBS, The Athletic, On3, 247Sports), then local papers (MLive, Toledo Blade, Akron Beacon Journal, Buffalo News, etc.). Search patterns: "[team] MAC media day 2026", "[coach] MAC kickoff 2026 quotes", "[team] QB competition July 2026".

## Open questions, by team

Cover **every team below, in this order.** For each listed question, return a verdict: **ANSWERED / PARTIAL / NOTHING FOUND**, with the evidence or the searches that failed.

**Akron**
- QB: Is **Poffenbarger** (North Texas backup with a real FCS resume, no FBS starter tape) named QB1?
- LB: The entire 2025 unit departed. Named starters?

**Ball State**
- QB: Their 2025 starter expired and our snapshot has no clear successor — **who is in the room, and who leads?** This is our biggest information gap in the league.
- LB: The entire room (top six tacklers) expired at once. Named starters?

**Bowling Green**
- QB: The only FBS tape in the room is Najm's (poor, 3 starts) — is he QB1, or has someone emerged? Any transfer/freshman framing. Get the coach's exact language.

**Buffalo**
- QB: The room has **zero career FBS pass attempts** (both 2025 QBs expired; the returning QB was a designated runner). Who is QB1?
- LB: Consensus All-American Murdock + both other high-volume LBs gone. Named starters?

**Central Michigan**
- QB: Both quality returners (Flores — the designated runner; Glasser — strong spring) are back. Is it one guy, a two-QB plan, or open? Coach framing.
- LB: Both leading tacklers expired. Named starters?

**Eastern Michigan**
- QB: Noah Kim returns on a granted 7th season — confirm QB1 and health; otherwise sweep for deltas.

**Kent State**
- QB: DeShields returns (kept out of the portal) — confirm QB1; otherwise sweep for deltas.

**Massachusetts**
- QB: All three 2025 QBs left; the room is entirely transfers with no returning FBS tape. Who is QB1, or how is the battle framed?

**Miami (OH)** *(print conflict to resolve)*
- QB: Our two sources disagree — one expects **Gotkowski** to be QB1 in the fall, the other prints Kansas transfer **McComb** (zero tape) atop the lineup. Resolve it: who leads per the staff at media day?

**Ohio**
- QB: Navarro (their standout) is gone to the pros — who is QB1, or how is the battle framed?

**Sacramento State** *(FCS reclass — double-priority sweep)*
- QB: Is **Conklin** (boomerang transfer back from Fresno; strong FCS resume, poor FBS sample) named QB1?
- RB: Is **Curtis** (FCS All-American with a two-year injury cloud; withdrew from the portal) healthy and the lead back? Health status matters.
- DL / DB: Both units lost nearly everything from the FCS roster. Named starters?
- Sweep broadly: first FBS season — depth chart, scheme, transition-eligibility notes, anything concrete.

**Toledo** *(staff turnover — establish the facts)*
- TEAM: Our snapshot indicates HC Candle left for UConn (their QB2 followed him). **Establish Toledo's current head coach and coordinators from coverage**, and capture any scheme specifics.
- QB: Gleason (elite 2025 tape) expired and the QB2 left — who is QB1, or how is the battle framed?
- WRTE: The top three WRs and TE1 are all gone. Named starters?

**Western Michigan**
- QB: Lowry (MAC Offensive POY, 10-1 as starter) returns — confirm QB1/health; otherwise sweep for deltas.
- LB: Their two elite LBs (both one-year rentals) departed. Named starters?

## Output format — follow exactly

Produce a single markdown report, nothing else (no preamble about your process):

```
# MAC 2026 media day — source digest
Compiled: <date> · Event: <confirmed event name + date + venue> · Baseline: 2026-07-12 snapshot

## 0. Top signals
<~10 highest-signal items conference-wide, one line each: TEAM — finding (unit).>

## 1. Media poll & preseason honors
<Poll verbatim with votes; all-MAC team verbatim; source links.>

## 2. Conference-wide news
<Membership/scheduling/commissioner/transition items, with citations.>

## 3. Teams
### <Team name>
**Answers to open questions:**
- <question> — ANSWERED/PARTIAL/NOTHING FOUND: <evidence>. (Source: <name>, <URL>, <date>)
**Findings:**
- [<UNIT>][<TAG>][<date>] <finding, with exact quote if QUOTE>. (Source: <name>, <URL>, <date>)
<Unit keys: QB, RB, WRTE, OL, DL, LB, DB, ST, TEAM. LOW-signal items last, tagged LOW.>
**Coverage note:** <one line — depth of coverage, anything unverified>

## 4. Coverage gaps
<Thin-coverage teams; failed searches; sources to check next.>
```

First, confirm the event's exact date and venue. Cover all 13 teams listed (Northern Illinois excluded). Do not include betting analysis, win projections, or grade recommendations anywhere.
