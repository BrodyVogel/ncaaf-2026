You are compiling a source digest for a college football power-ratings model. I maintain unit-level grades (QB, RB, WR/TE, OL, DL, LB, DB, special teams) for every FBS team, frozen to a **July 12, 2026 information snapshot**. Your job is to sweep coverage of **Conference USA's 2026 media days** (believed **July 20–21, 2026** — confirm the exact dates, venue, and format from coverage) and report every *concrete, sourced* piece of information that could change what I believed on July 12.

You are a **reporter, not an analyst**. Do not project wins, suggest grades, or editorialize about what anything "means" for a team's quality — that analysis happens downstream, by me. Your report will be machine-ingested, so following the output format exactly matters more than prose style.

**League context (important):** the 2026 CUSA in my model is 10 teams: Delaware, Florida International, Jacksonville State, Kennesaw State, Liberty, Middle Tennessee, Missouri State, New Mexico State, Sam Houston, Western Kentucky. **Louisiana Tech left for the Sun Belt — do not cover them.** Delaware and Missouri State are 2026 FBS newcomers; Jacksonville State, Kennesaw State, and Sam Houston are recent FCS reclassifications. **For four teams — Kennesaw State, Jacksonville State, Delaware, Missouri State — my roster data is thinner than usual** (short or nonexistent FBS track records), so concrete roster/depth-chart/scheme facts on them are worth extra effort: treat those four as double-priority sweeps.

## What to find (in priority order)

1. **QB competitions & depth-chart clarity.** Named starters, coach language on races ("X is our guy" vs "down to two"), transfer pecking orders. For unresolved battles, capture the coach's *framing* even if no starter is named. Highest priority throughout.
2. **Injuries, surgeries, availability.** Recovery timelines, players out/cleared, spring absences now practicing. (Liberty has a specific health question below.)
3. **Roster changes since the snapshot.** Late portal exits/entries, dismissals, suspensions, eligibility rulings, retirements.
4. **Position switches and lineup reveals.** First-team reps, OL alignments, named specialists/returners.
5. **Coordinator/scheme substance.** New play-callers/staff specifics — only where a coach or beat reporter says something concrete.
6. **Conference-wide items.** The preseason media/coaches poll (full order, verbatim, with votes) and preseason all-CUSA team (verbatim). Any commissioner statements on membership, scheduling, or the FBS-transition status of Delaware/Missouri State (e.g., postseason eligibility).
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
- **Do not merge conflicting reports.** If two sources disagree, present both with citations.
- **An honest empty section beats filler.** Thin coverage → say what you searched and found nothing; do not pad with old news.
- Prefer primary/written material: official CUSA transcripts/media-day pages, beat-writer write-ups, team athletics sites. Then national outlets (ESPN, CBS, The Athletic, On3, 247Sports), then local papers. Search patterns: "[team] CUSA media day 2026", "[coach] Conference USA media days quotes", "[team] QB competition July 2026".

## Open questions, by team

Cover **every team below, in this order.** For each listed question, return a verdict: **ANSWERED / PARTIAL / NOTHING FOUND**, with the evidence or the searches that failed.

**Delaware** *(FBS newcomer — double-priority sweep)*
- QB: Is Minicucci (2nd-team All-CUSA, led the league in passing) confirmed QB1? Otherwise sweep broadly: any depth-chart, roster, or scheme facts on their first FBS season, plus any statement on transition-year postseason eligibility.

**Florida International**
- QB: Is App State transfer JJ Kohl confirmed QB1 (they lost Jenkins to UCF)? Coach framing.

**Jacksonville State** *(recent reclass — double-priority sweep)*
- QB: Is dual-threat Creel confirmed QB1 (they lost backup Wimsatt)?
- Sweep broadly for roster/depth-chart facts — my data on this roster is thinner than usual.

**Kennesaw State** *(recent reclass — double-priority sweep)*
- QB: Our snapshot has Syracuse transfer **Rickie Collins** vs JUCO **Varnes** "even in spring" (they lost Odom to Syracuse in a de facto QB swap). Did the staff name a leader? Exact language.
- RB: An all-new room (D2 transfer Morgan, FCS transfer Murrell) after losing the top two backs. Any named RB1 or committee framing?
- Sweep broadly for roster/depth-chart facts.

**Liberty**
- QB: A three-way — our snapshot has Wake transfer **Purdie** vs WVU transfer **Henderson** vs returner **Vasko** (12 INTs in 2025, **recovering from shoulder surgery — get his current health status**). Named leader or framing?
- RB: Is redshirt freshman **Coleman** (their highest-rated recruit ever, no FBS tape) the lead back, or do the transfers (Davis–FSU, Jones–Duke) lead?
- ST: Both specialists are gone — kicker battle (Black–Wake vs Reeves–D2) and the new punter. Any resolution?

**Middle Tennessee**
- QB: Is sophomore Gagliano confirmed the full-time starter (our snapshot says yes — verify nothing changed)?
- RB: Who leads — sophomore Taylor (tiny sample) or Kansas State transfer Martin? They lost their lead back to Virginia.
- OL / DL: Both heavily rebuilt with transfers — any named starting five or defensive-front rotation?

**Missouri State** *(FBS newcomer — double-priority sweep)*
- QB: An open transfer battle — UTEP transfer **Locklear** vs Duke transfer **Belin** ("both have a chance" per the coach in our snapshot). Named leader? Exact language.
- OL: One returning starter (Greene) plus a transfer line — any named five?
- Any statement on transition-year postseason eligibility; sweep broadly.

**New Mexico State**
- QB: Furman FCS transfer **Hedden** (a magazine QB1) vs returner **Damante** — the beat called it open. Named leader or framing?
- RB / OL: Both thin/rebuilt (FCS and small-sample transfers) — any named starters?

**Sam Houston**
- QB: Is sophomore **Locke** confirmed ("solidified his hold" in our snapshot — verify)?
- OL: They lost **every** starter — has a starting five been named from the transfer group?
- LB: Rebuilt with transfers — named starters?

**Western Kentucky**
- QB: A battle — returning sophomore **Tisdale** (took over midseason) vs FSU transfer **Glenn**, under a new pass-first OC (Reeder). Named leader? Exact language.
- OL: "Almost a complete rebuild" — one returning starter (Upchurch) plus a P4-transfer line. Named five?
- LB: They lost both leading tacklers — named starters?

## Output format — follow exactly

Produce a single markdown report, nothing else (no preamble about your process):

```
# CUSA 2026 media days — source digest
Compiled: <date> · Event: <confirmed event name + dates + venue/format> · Baseline: 2026-07-12 snapshot

## 0. Top signals
<~10 highest-signal items conference-wide, one line each: TEAM — finding (unit).>

## 1. Media poll & preseason honors
<Poll verbatim with votes; all-CUSA team verbatim; source links.>

## 2. Conference-wide news
<Membership/transition-eligibility/scheduling/commissioner items, with citations.>

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

First, confirm the event's exact dates and venue. Cover all 10 teams listed (Louisiana Tech excluded). Do not include betting analysis, win projections, or grade recommendations anywhere.
