# Ratings finalization plan — for Opus to execute (owner-approved 2026-07-19)

Authored by the Fable session. Prereq reading: docs/FINAL_PASS_HANDOFF.md (the formula,
the repeat loop, the decision record, the authority map). Work top to bottom; every step
ends with a commit. Steps 0-1 are verification of completed work; Steps 3-5 are the real
remaining work. Step 2 is optional.

---

## Step 0 — State check (5 min, every session start)

```
git pull
python3 pipeline/final_pass.py
```
The console line must match the committed baseline: `138 teams | R2 off 0.67 def 0.49 |
level slope -0.146 | capped 0 | recenter +0.55` (small drift only if grades were edited
since). `git status` must be clean afterward except regenerated outputs. Any mismatch ->
stop and investigate before proceeding; do not grade or bet off an unverified state.

## Step 1 — Residual-mode decision (DONE — verify only)

Conference-demeaned residual is the OFFICIAL mode (default), Independents pseudo-pooled
(ND->P4, UConn->G5), frozen mode preserved behind `--frozen-resid`. Verify the decision
record exists (HANDOFF §6) and `outputs/FINAL_BOARD_2026.md` header says
"CONFERENCE-DEMEANED (official...)". Nothing to execute.

## Step 2 — OPTIONAL corroboration: anchor-side conference persistence (≤1 hr, non-blocking)

Question: do the MARKET's preseason conference-level errors persist year over year? A
null result corroborates demeaning; per the owner's policy even a positive result does
NOT reverse Step 1 (realignment skepticism) — only a large, stable, realignment-robust
effect goes back to him.

Method: uploads `NCAAF Data 2026/SP+ History/` has PRESEASON SP+ 2021-2025 only; pull
FINAL SP+ per season from CFBD (the API creds already power the pipeline pulls). For
each season: error_t = final - preseason per team; conference-mean error using THAT
season's membership; then correlate conference-mean errors year-to-year, separately for
2024+ (post-realignment) vs before. Write outputs/CONF_PERSISTENCE_TEST.md with the
correlations + n. Skip freely if time is short.

## Step 3 — Staleness sweep before ANY wager (the real pre-bet work)

Everything froze ~2026-07-18; August camps will resolve much of it. The L-flags are the
checklist — 52 teams carry an L-graded QB, 31 teams carry >=3 L units (query:
`awk -F, 'NR>1 && $12>=3' outputs/grade_board.csv`). Priorities, highest first:

1. Teams the owner intends to bet (whatever the Step-4 edge list surfaces).
2. Open QB battles graded as battles — re-verify the winner when named: Liberty
   (Purdie/Henderson), WKU (Tisdale/Glenn), Missouri State (Locklear/Belin), NMSU
   (Hedden/Damante), UConn (Merklinger/Osborne), + the P4 L-QBs (Alabama, Florida,
   Clemson, FSU, ...).
3. Named upside/downside contingencies: NMSU LB Tory Gethers (counted GONE,
   uncommitted-in-portal — a rejoin is LB upside); Liberty QB Vasko's shoulder;
   ND C Craig / G Jagusah health.
4. August injury/suspension news for any team on the bet list.

Source rules unchanged (R16): P4 = 3-source (Athlon + Phil Steele + Pick Six), G5 =
2-source (Athlon + best available; PS SBC/CUSA text layers are garbled — use CFN/beat/
official rosters). Any resulting grade change goes through the repeat loop (HANDOFF §3):
edit grades.json -> grades_check -> final_pass -> commit. Log each change's reason in
_meta.planned_vs_final_deviations.

## Step 4 — Schedule conversion: ratings -> win totals -> edges (the product)

Build `pipeline/win_totals.py`:

- Inputs: outputs/FINAL_BOARD_2026.csv (rating + band), each team's
  snapshots/<T>/pulls/schedule_2026.json, and the market file (uploads "Win Totals from
  2025.csv" has multi-book totals + prices — CONFIRM WITH THE OWNER it reflects current
  lines before use; refresh if stale).
- Per game: p(win) = Phi((R_team - R_opp + HFA*site) / SD_MARGIN), site in {+1 home,
  -1 away, 0 neutral}. Defaults: HFA=2.3, SD_MARGIN=15.0 (calibrate SD quickly against
  2025 results vs anchor diffs if time permits; document whatever is used). FCS
  opponents: rating = -32 with p(win) capped at 0.97.
- Expected wins = sum of regular-season p(win). Uncertainty: recompute expected wins at
  rating ± band -> a wins-range per team.
- Edge = expected_wins - market_total (use the most favorable book per side; carry the
  prices). SURFACE ONLY edges that (a) exceed 1.0 wins at the central rating AND
  (b) do not fall below 0.5 wins at the adverse end of the band. Everything else is
  noise by construction.
- Output: outputs/WIN_TOTAL_EDGES.csv (team, proj wins, band-range, market by book,
  edge, side, price) + a short .md ranked by robust edge. Deterministic; document
  constants at the top of the file.

## Step 5 — Pre-bet checklist (apply to the Step-4 edge list)

Discard or downweight any surfaced edge that fails these screens:
- Staleness unresolved (Step 3 not done for that team).
- MAC total (diag Finding 4 — MAC defense grading question still open).
- FBS-newcomer data (Delaware, Missouri State — thin FBS history behind the grades).
- New-HC team (band already wider, but demand the full 1.0-win margin at the ADVERSE
  band end, not just 0.5).
- Sportsbook total moved >=1.0 win from the market file used (stale line).
- The three frozen-mode capped teams (MTSU, Sam Houston, ULM) if the edge direction
  matches the old model-vs-market disagreement — that disagreement was judged artifact.

Also fix (or consciously defer) the team_dump.py alias bugs (FORWARD_FLAGS.csv) before
any re-grading session: exact-match the percentile lookup + alias map entries
'LA MONROE'->UL Monroe, 'Sam Houston'->'Sam Houston State', 'UConn'->'Connecticut'.

---

Final note for Opus: the owner reads deltas, not dumps — after each step, report what
changed, what moved, and what you verified, in that order. He has final say on every
grade and every wager; your job is to keep the machine honest.
