You are compiling a source digest for a college football power-ratings model. I
maintain unit-level grades (QB, RB, WR/TE, OL, DL, LB, DB, special teams) for every
FBS team, frozen to a **July 12, 2026 information snapshot**. Your job is to sweep
coverage of the **rebuilt Pac-12's 2026 media day(s)** (believed **late July 2026 —
confirm exact dates/venue from coverage; if still upcoming, say so and return
pre-event roster/camp news for these teams instead**) and report every *concrete,
sourced* item that could change what I believed on July 12. This is the league's
first season in its new eight-team form (Boise State, Colorado State, Fresno State,
Oregon State, San Diego State, Texas State, Utah State, Washington State) — confirm
membership as covered and note any discrepancy.

You are a **reporter, not an analyst**. No projections, no grade suggestions.
Machine-ingested: follow the output format exactly.

## What to find (priority order)
1. **QB competitions & depth charts** — named starters, order, exact coach quotes.
2. **Injuries / availability**; 3. **Roster changes since July 12**;
4. **Position switches / first-team reveals**; 5. **Coordinator/scheme substance**;
6. **Conference-wide items** — inaugural media poll (verbatim, votes), scheduling
   format, CCG plans, any expansion statements;
7. **Answers to my open questions** — ANSWERED / PARTIAL / NOTHING FOUND verdicts.

**Sourcing (hard rules):** source name + URL + date on every item; tag
[QUOTE]/[REPORTED]/[AGGREGATED]/[RUMOR-pointer only]; no prior knowledge;
conflicting reports separate; honest empty beats filler.

## Open questions, by team (cover ALL 8, this order)

**Oregon State** *(highest priority — low-confidence QB and WR/TE rooms)* —
QB: who leads the race, and is a starter named? Exact staff language.
WRTE: first-team reveals in a rebuilt room. TEAM: new-staff install specifics.
**Washington State** *(low-confidence QB)* — QB: battle status and names running
first-team; roster stability after another portal cycle.
**Fresno State** *(low-confidence QB)* — QB: is Martin (Maryland transfer)
confirmed QB1, or open competition? Who else is in the room?
**Colorado State** — QB: Hejny's (Oklahoma State transfer) grip on the job —
confirmed or contested? Any hedge language.
**Utah State** — QB: Hillstead (BYU transfer) named, or race? Backup order.
**San Diego State** — QB: starter status; DB: first-team reveals
(low-confidence room); Saunders (Kentucky) role.
**Boise State** — WRTE: rebuilt receiver room first-team reveals
(low-confidence); QB confirmation.
**Texas State** — DL: first-team reveals (low-confidence room); QB room order.

## Output format

```
# Pac-12 2026 media days — source digest
Compiled: <date> · Event: <confirmed name + dates + venue, or "not yet held"> · Baseline: 2026-07-12

## 0. Top signals
## 1. Media poll & preseason honors  <verbatim with votes; links>
## 2. Conference-wide news  <scheduling/CCG/membership, cited>
## 3. Teams
### <Team>
**Answers to open questions:** - <question> — VERDICT: <evidence>. (Source, URL, date)
**Findings:** - [<UNIT>][<TAG>][<date>] <finding>. (Source, URL, date)
**Coverage note:** <one line>
## 4. Coverage gaps
```

Cover all 8 teams. No betting analysis anywhere.
