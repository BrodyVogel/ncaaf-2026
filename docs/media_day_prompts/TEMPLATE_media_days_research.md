# TEMPLATE — conference media days research prompt

<!-- HOW TO USE (for Brody — delete this comment block before sending):
     1. Replace every {{PLACEHOLDER}}.
     2. The {{OPEN_QUESTIONS_BLOCK}} is per-team; ask Claude in the project
        chat to generate it for any conference — it's extracted from our own
        grade files (low-confidence units + owner flags).
     3. Paste the whole thing into a fresh Research chat.
     4. Upload the returned report into the project as
        data/media_days/{{CONF_SHORT}}_2026_media_days.md
     A filled example lives next to this file: ACC_2026_media_days_research.md -->

---

You are compiling a source digest for a college football power-ratings model. I maintain unit-level grades (QB, RB, WR/TE, OL, DL, LB, DB, special teams) for every FBS team, frozen to a **July 12, 2026 information snapshot**. Your job is to sweep coverage of the **{{CONFERENCE}} 2026 media days** ({{EVENT_NAME_AND_DATES}}) and report every *concrete, sourced* piece of information that could change what I believed on July 12.

You are a **reporter, not an analyst**. Do not project wins, suggest grades, or editorialize about what anything "means" for a team's quality — that analysis happens downstream, by me. Your report will be machine-ingested, so following the output format exactly matters more than prose style.

## What to find (in priority order)

1. **QB competitions & depth-chart clarity.** Named starters, pecking order changes, coach language on any race ("X is our guy" vs "it'll go to camp"). QB is the highest-leverage position for the model — treat any QB news as top priority.
2. **Injuries, surgeries, availability.** Recovery timelines, players out for the season, players cleared, players who missed spring now practicing.
3. **Roster changes since July 12.** Late transfer-portal exits/entries, dismissals, suspensions, eligibility rulings and waiver decisions, academic casualties, retirements. Anything that changes who is actually on the roster versus my snapshot.
4. **Position switches and lineup reveals.** Who is running with the first team, OL alignments, a WR moving to CB, a named kick returner, "we'll rotate eight on the DL."
5. **Coordinator/scheme substance.** New play-caller, tempo change, front change — only where the coach or a beat reporter says something specific, not generic scheme talk.
6. **Conference-wide items.** The preseason media poll (full order, with points/first-place votes, verbatim) and the preseason all-conference team (verbatim). Any commissioner or league statements on 2026 scheduling formats or structural changes.
7. **Answers to my open questions** — listed per-team below. These are the units where my grade is explicitly low-confidence; direct evidence on them is the most valuable thing you can return.

**Downweight but don't discard:** "best shape of his life," culture/leadership talk, generic optimism. If a borderline item has any factual content (e.g., a weight change on an OL starter, a specific role statement buried in fluff), include it tagged LOW. Pure fluff with no factual content: omit.

**Secondary objective:** while you're inside a team's coverage, also capture material roster/injury news from **July 12 → today** even if it didn't happen at the podium. My snapshot only cares about the delta.

Note: a coach *confirming* something previously reported as unsettled counts as new information. A recap of things already public before July 12 does not — unless it answers one of my open questions.

## Sourcing rules — these are hard requirements

- **Every item carries: source name, URL, and the source's publication date.** No exceptions. An item you cannot cite does not go in the report.
- **Tag every item** with exactly one of:
  - `[QUOTE]` — direct, on-record words from a coach/player. Include the exact words in quotation marks.
  - `[REPORTED]` — a fact stated by an identified beat reporter or credentialed outlet.
  - `[AGGREGATED]` — secondary write-ups, roundups, rankings articles.
  - `[RUMOR]` — message boards, Reddit, unsourced social posts. Reddit and forums may be used **only as pointers** to locate a primary source; a rumor with no primary source found may appear only in the team's coverage-notes line, never as a finding.
- **Do not rely on your prior knowledge of these teams.** Everything in the report must come from sources you found during this research. If your memory says something a source doesn't, the source wins; if you can't find a source, it doesn't go in.
- **Do not merge conflicting reports into one claim.** If two sources disagree, present both with citations.
- **An honest empty section beats filler.** If a team's media-day coverage is thin, write exactly what you searched and found nothing — do not pad with season previews or old news.
- Prefer primary/written material: official conference transcripts (ASAP Sports often posts them), the conference's own media-day pages, on-record pressers written up by beat writers. Then national outlets (ESPN, CBS, The Athletic, On3, 247Sports, Rivals), then team-specific sites and local papers. Use search patterns like "[team] media days quotes 2026", "[coach last name] {{EVENT_NAME}} 2026", "[team] QB competition July 2026".

## Open questions, by team

Cover **every team below, in this order**, even the ones with no listed questions. For each listed question, return an explicit verdict: **ANSWERED / PARTIAL / NOTHING FOUND**, with the evidence or the searches that came up empty.

{{OPEN_QUESTIONS_BLOCK}}

## Output format — follow exactly

Produce a single markdown report, nothing else (no preamble about your process):

```
# {{CONFERENCE}} 2026 media days — source digest
Compiled: <date> · Event: <confirmed event name + dates> · Baseline: 2026-07-12 snapshot

## 0. Top signals
<The ~10 highest-signal items conference-wide, one line each: TEAM — finding (unit). Details live in the team sections.>

## 1. Media poll & preseason honors
<Poll verbatim with points/votes; all-conference team verbatim; source links.>

## 2. Conference-wide news
<Scheduling/format/commissioner items, with citations.>

## 3. Teams
### <Team name>
**Answers to open questions:**
- <question> — ANSWERED/PARTIAL/NOTHING FOUND: <evidence>. (Source: <name>, <URL>, <date>)
**Findings:**
- [<UNIT>][<TAG>][<date>] <finding, with exact quote if QUOTE>. (Source: <name>, <URL>, <date>)
<Use unit keys: QB, RB, WRTE, OL, DL, LB, DB, ST, TEAM (staff/scheme/whole-roster). LOW-signal items go last, tagged LOW.>
**Coverage note:** <one line — how deep the coverage ran, anything you couldn't verify>

## 4. Coverage gaps
<Teams with thin coverage; searches that failed; sources you'd check next.>
```

First, confirm the event's exact dates from coverage and state them in the header. Cover all {{N_TEAMS}} teams. Do not include betting analysis, win projections, or grade recommendations anywhere.
