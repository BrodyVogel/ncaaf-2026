You are compiling a source digest for a college football power-ratings model. I
maintain unit-level grades (QB, RB, WR/TE, OL, DL, LB, DB, ST) for every FBS team,
frozen to a **July 12, 2026 snapshot and patched through each conference's media
days as integrated** (all conferences EXCEPT the Big Ten and Pac-12, which are
being swept separately). Fall camps opened this week. Your job: sweep coverage of
the **20 teams below** and report every *concrete, sourced* piece of information
since each team's baseline (its conference's media-day integration date, or
July 12 for Big Ten / Pac-12 teams) that could change what I believed then.

You are a **reporter, not an analyst**. No win projections, no grade suggestions,
no editorializing. Machine-ingested: follow the output format exactly.

## What to find (priority order)
1. **QB depth charts and battles** — named starters, first-team rep splits, coach
   language with exact quotes. This is the highest-leverage item for every team below.
2. **Injuries / surgeries / availability** — camp injuries, recoveries, opt-outs.
3. **Roster changes since the snapshot** — late portal moves, dismissals,
   eligibility rulings, retirements, JUCO/grad additions.
4. **Position switches, OL first-five reveals, named specialists.**
5. **Coordinator/scheme substance** — specific statements only.

**Sourcing (hard rules):** every item carries source name + URL + date; tag
[QUOTE]/[REPORTED]/[AGGREGATED]/[RUMOR-pointer only]; no prior-knowledge reliance;
conflicting reports stay separate; honest empty sections beat filler. Prefer beat
writers and team announcements; search "[team] fall camp 2026", "[team] QB
competition August 2026", "[coach] camp opening press conference 2026".

## TIER 1 — held-position freshness (deepest effort here)

**East Carolina** — QB: Griffis (Texas Tech, prior Wake starts) vs the field:
named, leading, or open? Rep splits, coach quotes. Any WR/TE or LB starter news.
**UConn** — QB: Merklinger vs Osborne battle status under Candle; any hierarchy
language. OL/DL first-team reveals (heavy-transfer rooms). Any late arrivals.
**Rutgers** — QB: Lonergan vs Surace — who runs first-team? Exact quotes.
**Tulsa** — QB: Hayes health/durability and offseason passing-game work; confirm
no competition. LB first-team.
**UCF** — QB: room hierarchy — named starter? Any movement since July.
**Kennesaw State** — QB: Collins (Syracuse) role vs incumbents; any attrition on
the two-deep; anything on the offensive rebuild.

## TIER 2 — candidate screens (status confirmation)

**UNLV** — QB: Jackson Arnold (Auburn) — named QB1 or competition? Camp reports on
his play; OC scheme fit; backup order. Any defense attrition.
**Miami (OH)** — QB: McComb (Kansas) — named starter? Who else is in the room?
Coaching staff continuity notes.
**Charlotte** — QB: the three-way battle — any hierarchy after camp opening?
**Louisiana-Monroe** — QB1 and general camp reveals.
**Sam Houston** — QB and staff notes; roster stability after the transition year.
**Ohio** — QB battle status; any key departures since July.
**Navy** — QB health (Woodson) and option-personnel notes.
**Troy** — QB1 named? Injuries.
**Boston College** — QB status; any surprise attrition.
**Toledo** — QB and two-deep reveals; post-Candle staff notes.
**Western Kentucky** — QB: Glenn (FSU) vs field; receiver room status.
**Washington State** — QB and roster stability notes.
**Georgia State** — QB1; roster changes.
**Old Dominion** — QB; secondary reveals.

## Output format

```
# Fall camp sweep 1 — source digest
Compiled: <date> · Baseline: 2026-07-12 snapshot (AAC/SEC: 2026-07-27)

## 0. Top signals
<up to 10 one-liners: TEAM — finding (unit)>

## 1. Teams (Tier 1 first, in the order above)
### <Team>
**Findings:**
- [<UNIT>][<TAG>][<date>] <finding, exact quote if QUOTE>. (Source: <name>, <URL>, <date>)
**Coverage note:** <one line; "no camp coverage yet" is a valid answer this early>

## 2. Coverage gaps
<teams with nothing yet; searches that failed>
```

Camps are days old — thin coverage is expected and honest emptiness beats filler.
Do not include betting analysis anywhere.
