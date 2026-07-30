You are compiling a source digest for a college football power-ratings model. I
maintain unit-level grades (QB, RB, WR/TE, OL, DL, LB, DB, special teams) for every
FBS team, frozen to a **July 12, 2026 information snapshot**. Your job is to sweep
coverage of **Big Ten Media Days 2026** (believed to have run in **late July 2026 —
confirm exact dates and venue from coverage; if the event is still upcoming, say so
and return pre-event roster/camp news for these teams instead**) and report every
*concrete, sourced* piece of information that could change what I believed on
July 12.

You are a **reporter, not an analyst**. Do not project wins, suggest grades, or
editorialize. Machine-ingested: follow the output format exactly.

## What to find (priority order)
1. **QB competitions & depth-chart clarity** — named starters, pecking order,
   exact coach language on any race. Top priority for the model.
2. **Injuries, surgeries, availability** — timelines, cleared/not-cleared.
3. **Roster changes since July 12** — late portal, dismissals, eligibility rulings.
4. **Position switches and first-team reveals** — OL alignments, specialists.
5. **Coordinator/scheme substance** — specific statements only.
6. **Conference-wide items** — any media poll/preseason honors (verbatim, with
   votes where published); commissioner statements on schedule format and CFP.
7. **Answers to my open questions**, listed per team — explicit verdicts:
   ANSWERED / PARTIAL / NOTHING FOUND, with evidence or the failed searches.

**Sourcing (hard rules):** every item carries source name + URL + date; tag
[QUOTE]/[REPORTED]/[AGGREGATED]/[RUMOR-pointer only]; no prior-knowledge reliance;
conflicting reports stay separate; honest empty sections beat filler. Prefer
official transcripts and beat writers.

## Open questions, by team (cover ALL 18, this order)

**Illinois** — QB: who is QB1 after the turnover, and is it settled or a race?
**Indiana** — QB: named starter and staff language on the offense.
**Iowa** *(four low-confidence rooms — highest-priority team in this sweep)* —
QB: room hierarchy with exact quotes. DL/LB: first-team reveals after departures.
ST: specialist jobs settled?
**Maryland** — QB: confirmed starter?
**Michigan** — QB: hierarchy and any freshman-vs-veteran framing.
**Michigan State** — QB: status; any roster attrition.
**Minnesota** — QB: confirmed? OL first-five.
**Nebraska** — QB: named starter; staff continuity notes.
**Northwestern** — QB: who starts; any late portal adds (roster returns a lot —
confirm nothing broke since July 12).
**Ohio State** — QB: Sayin health/status only (expect confirmation). Any
first-team reveals on defense.
**Oregon** — QB: confirmation; OL alignment.
**Penn State** — QB: the room's hierarchy with exact coach language (my sources
conflict on how settled this is — highest-value single answer in the conference).
**Purdue** — QB: named starter after the turnover.
**Rutgers** — QB: **Lonergan vs Surace — hierarchy, rep splits, Schiano's exact
words.** This is my single most important question in the sweep.
**UCLA** — QB and skill continuity — confirm the returning core is intact.
**USC** — QB: confirmation; any defensive first-team reveals.
**Washington** — QB: status and availability of the projected starter — any
eligibility/health developments since July 12.
**Wisconsin** — QB: who is QB1 and how open is it; OL first-five; any
Fickell/coordinator scheme specifics.

## Output format

```
# Big Ten 2026 media days — source digest
Compiled: <date> · Event: <confirmed name + dates + venue, or "not yet held"> · Baseline: 2026-07-12

## 0. Top signals
<~10 one-liners: TEAM — finding (unit)>

## 1. Predicted order & preseason honors
<any media poll verbatim with votes; all-conference teams; links>

## 2. Conference-wide news
<schedule format / CFP / commissioner items, cited>

## 3. Teams
### <Team>
**Answers to open questions:**
- <question> — ANSWERED/PARTIAL/NOTHING FOUND: <evidence>. (Source, URL, date)
**Findings:**
- [<UNIT>][<TAG>][<date>] <finding, exact quote if QUOTE>. (Source, URL, date)
**Coverage note:** <one line>

## 4. Coverage gaps
```

Cover all 18 teams. No betting analysis, win projections, or grade recommendations.
