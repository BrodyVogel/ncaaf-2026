# CFB 2026 Power Ratings — Build-Session Initiation Brief
**Version 2026-07-12. Supersedes the original planning handoff. All SETTLED decisions from that brief carry forward unchanged and are restated here. New sections (§0, §13, §14) and [UPDATED] tags encode what a prior prep session actually did and discovered. Read completely before acting.**

The user's standing preferences: brief explanations, but state exactly what changed whenever you change something.

---

## 0. SESSION START — do these before anything else

1. **Folder access.** The project data folder is the user's connected folder `NCAAF Data 2026` (reached via the device tools / mounted folder). Inventory it against §13. Flag anything missing; don't assume.
2. **CFBD reachability + key check (gating).** The API key is in `secrets/cfbd_api_key.txt` in the folder — read it from there; NEVER print it, never commit it, add `secrets/` to `.gitignore`.
   - Known issue from the prep session: the Cowork cloud sandbox's default network egress is **package managers only** — `api.collegefootballdata.com` was unreachable (connection blocked, not a key problem). The key is therefore **still unverified**.
   - Test with one minimal call (e.g. `/teams/fbs?year=2026`, Bearer auth). If blocked: stop, fail loud, and tell the user to change the session's network egress setting (Settings → Capabilities → code execution / network egress: add `api.collegefootballdata.com` and `apinext.collegefootballdata.com` to allowed domains, or set "All domains"), then retest. Do not attempt fetch workarounds.
   - CFBD **v2 API only** (v1 is dead). Confirm tier limits on first calls.
3. **Repo durability (gating decision, one question).** This session's workspace is EPHEMERAL — it does not survive the session. The project spans weeks and ~138 team runs, so the git repo must live somewhere durable:
   - **Recommended: a private GitHub repo** (private is required — it will contain paid PFF exports and magazine-derived content). Clone into the workspace each session, push every freeze.
   - Fallback: treat the connected folder as the durable store and mirror the repo there each session (clunkier: the folder's VM cannot delete files and has no network).
   - If no remote is configured when you start, ask the user this one question before building.
4. **Canonical team list + name map.** Derive the canonical 2026 FBS team list from CFBD (expected ~138, including 2026 newcomers North Dakota State and Sacramento State). Then complete `anchors/team_name_map.csv` — it already maps all 138 teams across SP+/FEI/Massey/FPI/TeamRankings/PFF spellings via `norm_key`; **fill the `cfbd_school_FILL_AT_STEP0` column from the live API** and validate 138/138. Every later join keys on the CFBD name.

---

## 1. Goal & deliverable
Preseason power ratings for **every FBS team** (2026 season; derive the canonical list from the CFBD API, don't hardcode). The user bets season win totals and will bet any team.
Per team, the final output is:
- **Power rating** — points vs. an average FBS team (0 = average, +30 ≈ best, −30 ≈ worst).
- **Variance band** — ± points of *epistemic* uncertainty about true strength.
- **Compact justification** — unit grades, key drivers, flags. A grade sheet, not an essay.
These feed the user's existing simulation engine (out of scope). **Anti-goal:** ~20-page narrative team reports. Explicitly not wanted.
Timing: season starts late August 2026. KFord publishes in August; the pipeline must be trivially re-runnable when new anchors land. [UPDATED: FPI and TeamRankings 2026 preseason are already live and captured — see §6.]

## 2. Architecture — SETTLED
Two strictly separated phases:
**Research phase** (expensive, non-deterministic, once per team): produce a frozen, dated snapshot per team. All web search, PDF reading, and roster verification happens here. A snapshot committed to git is frozen.
**Compute phase** (cheap, deterministic): snapshots → position-group grades → league-wide blend → rating + variance. Re-runnable across all teams in minutes. When new anchors publish, only this phase re-runs — snapshots don't change.
Rationale: last year, research/judgment/arithmetic were entangled in one LLM pass, producing ~6-point run-to-run swings, stale stats, and unauditable numbers. The split is the fix. The user accepts modest run-to-run wobble but not thesis changes.

## 3. Rating math — SETTLED (replaces the old rubric entirely)
The v1 tier rubric is **dead**. Do not resurrect it or any hand-authored grade→points mapping.
**Top-down anchor.** Mean of available consensus preseason projections, normalized to a common points scale (SP+'s scale as reference). Live and captured today: **SP+**, **Massey**, **FPI**, **TeamRankings** (see §6 and `anchors/`). Add KFord in August; Pick Six's Game Grader can join as a P4-only input. Every compute run logs which anchors were live and their capture dates.
**Bottom-up grades.** Eight position groups per team — QB, RB, WR/TE, OL, DL, LB, DB, ST — each graded 0–100 on a **national FBS scale** from the frozen snapshot only (see §5 blinding). Every grading call uses one fixed prompt template containing a **fixed calibration exemplar block**: ~6–10 named 2025 units spanning roughly 15–90, including G5 examples, built once before grading team #1 and never varied. (Historical exemplars are fine — the blinding rule targets 2026 consensus, not last season's facts.) Soft guard preserved: a G5 unit graded above ~75 requires an explicit evidence note.
**Conversion — the self-calibrating step.** Once all teams are graded, fit two cross-sectional regressions across the full league:
- anchor offense rating ~ f(QB, RB, WR/TE, OL grades)
- anchor defense rating ~ f(DL, LB, DB grades)
Linear to start. Fitted values = each team's **grade-implied** O/D on the anchor's point scale. Handle ST simply. The league-wide fit sets the points-per-grade scale automatically; anything the anchor already prices is absorbed by the fit — only *relative* disagreement moves a team.
**Blend.**
```
residual_i   = grade_implied_i − anchor_i
adjustment_i = clip(k × residual_i, ±cap)
final_i      = anchor_i + adjustment_i
```
Defaults: **k = 0.5, cap = ±5.0 points.** OPEN to tuning after the pilot.
**Variance.**
```
band_i = base_sigma × Π(multipliers_i)
```
- `base_sigma` from the backtest (§7): dispersion of preseason-anchor misses vs. realized season strength.
- Multipliers (modest bumps, backtest-disciplined where possible): low returning production; new/unproven QB starter; new HC/OC/DC; heavy portal churn; low snapshot data-confidence.
- Sanity scale: average ±3.5–4.5, low ±2–4, high ±5–7, extreme ±8–11 reserved for a handful of teams nationally.
- The band is epistemic. Game-level randomness belongs in the user's sim — see OPEN item on double-counting.
**Sequencing:** the cross-sectional fit needs *all* teams' grades. Per-team runs produce **grades + a provisional vs-anchor readout**; final ratings compute league-wide at the end. Do not fit the regression on partial data except as a rough progress check.

## 4. Blinding rule — SETTLED, HARD
The grading layer must never see consensus ratings, market lines, win totals, SP+/FPI/KFord/Massey/TeamRankings numbers, or any 2026 power ranking. Enforce at two points:
1. **Snapshot creation:** no consensus/market numbers are copied into snapshots. In particular: **nothing from `anchors/` or the win-totals files may be read during research/snapshot/grading work.** Those live in the folder for the compute phase only (the manifest inside says the same).
2. **Grading prompts:** instruct the grader to disregard any ranking it happens to encounter and grade solely from snapshot evidence.
Reconciliation with consensus happens **only in code** (§3). The flag is `|residual| > threshold`, and it goes to the user, never to a silent model-side correction.

## 5. Verification & data-hygiene rules — SETTLED, HARD
- **Stats come from CFBD wherever possible.** Machine-read beats web search. Pin every stat and accolade to an explicit season year; discard undated claims.
- **Source hierarchy:** official team rosters + OurLads = primary for depth charts; magazines = secondary (identification and history — verify current status against primary); beat coverage = tertiary.
- **Fringe roster status requires ≥2 independent sources** (OurLads plus one of ESPN / RotoWire / The Sideline). One source suffices only when context is overwhelming.
- **Every player in the two-deep carries a data-confidence flag.** Low confidence widens the variance band.
- **Unproven players get priors, not fake grades** — recruiting composite, prior program level, portal valuation, draft/scout buzz, with explicitly wide uncertainty.
- [NEW] **Team-name hygiene:** all joins key on the CFBD school name via `anchors/team_name_map.csv`. Do not string-match team names ad hoc — the sources use six different spelling conventions (Ole Miss/Mississippi, UConn/Connecticut, USF, UL Monroe/ULM, both Miamis, TR's "J Madison"/"Georgia So", Massey's "CS Sacramento"/"MTSU"/"Kent", etc.).

## 6. Data sources & status — [UPDATED 2026-07-12: acquisition is essentially done]
| Source | Status | Notes |
|---|---|---|
| CFBD API | key in `secrets/cfbd_api_key.txt`; **unverified** (prep sandbox egress blocked) | v2 only. Backbone: teams, rosters, SP+, `/player/returning`, `/team/talent`, portal, schedules, historical results/lines. Verify at §0 step 2. |
| Phil Steele 2026 | **in folder, ready** | Scanned magazine, but the prep session OCR'd it: use the 12 `Phil Steele 2026 - <Conf> (searchable).pdf` files (rotated upright, full text layer, stat tables included at 250 DPI). Originals + a 1.23 GB combined file also present — ignore those. OCR of dense stat tables is good but not perfect: verify any load-bearing number against the page image. |
| Athlon 2026 | **in folder, ready** | 13 born-digital PDFs (`Athlon 2026 - *.pdf`), fully text-searchable as-is. Only 3 image-only pages exist and they're ads/section art. Depth charts, predicted order, all-conference, rival-coach quotes. |
| Pick Six 2026 | **arriving ~2026-07-13** | P4 only (68 teams). Game Grader = P4-only anchor input, not a talent-prior source. Inventory at session start. |
| PFF+ premium stats | **exported, in folder** | 27 `PFF_*.csv` player/team tables (2025 season, ~79k rows) + `PFF_data_dictionary.json`/`.md` defining all 2,354 columns (per-file context, base metrics, bucket decoder, PFF's verbatim key legends). The "verify what's exportable" OPEN item is resolved — these are the exports. Use targeted per §8; do not scrape PFF for more. PFF's `team_name` uses display names ("USF") — map via team_name_map. NDSU/Sac State absent (not FBS in 2025). |
| Preseason anchors | **captured, in `anchors/`** | Dated 2026-07-12 captures: SP+ (ESPN ref — swap to CFBD pull once key live), FEI, Massey, ESPN FPI (2026 vintage confirmed), TeamRankings. `anchors_overall_2026-07-12.csv` = 5×138 tidy blend input; `anchor_sources.json` = manifest (URLs, scales, cadences, blinding flags). Massey and FPI/TR drift over the summer — **re-pull all live anchors in the days before Week 0** and re-date. |
| 2025 preseason win totals | **in folder** (user added; multiple books) | Resolves the OPEN item. Enables the backtest enrichment and the Odds API decision. Compute-phase only (blinding). |
| The Sideline | free | Portal valuations, CSV/JSON. Scrape at research time per team; freeze into snapshots. |
| OurLads | free | Primary depth-chart source. Scrape at research time. |
| FEI / coordinator trackers / beat coverage | FEI captured; rest at research time | ⚠ FEI placement unresolved: brief §6 called it a research supplement, but it IS a 2026 projection so §4 says the grader can't see it. Resolve when building snapshot tooling (recommend: compute-only, like the other anchors). |
| The Odds API | parked | Decide with the backtest, now that last year's win totals are in hand. |
| Massey composite | ⚠ note | The captured Massey page is **Massey's own model** (Rat/Pwr), not the composite consensus at masseyratings.com/cf/compare named in the original brief. Decide which feeds the blend before the first real compute run; if composite, capture it separately. |

## 7. Backtest — SETTLED scope
**Anchor only. Never attempt to backtest the grading layer.** Using CFBD historical data over several clean seasons:
1. **Base variance:** distribution of preseason-anchor misses vs. realized season strength → `base_sigma`. First verify preseason-vintage ratings are actually retrievable from CFBD (preseason SP+ should be; confirm before building). If only final-season ratings exist, say so and propose an approximation.
2. **Churn multipliers:** bucket historical teams by returning production / portal volume / coaching change; measure miss dispersion per bucket.
3. **Directional test:** do churn features predict the *sign* of anchor misses? If stable, a small fully-mechanical pre-adjustment; else variance-only.
Do this early (build step 2). The win-totals files in the folder can now enrich this with a market-based miss comparison.

## 8. Flag mechanism — SETTLED
After the league-wide fit: flag teams where `|residual|` exceeds a threshold (set after seeing the first full-pass distribution; roughly top decile). Flagged teams get a second research pass, **targeted PFF work from the 27 CSVs already in the folder** (OL: `PFF_offense_blocking/pass_blocking/run_blockng`; run D: `PFF_run_defense_summary`; coverage: `PFF_defense_coverage_*`, `PFF_slot_coverage` — consult the data dictionary), and only then a finalized adjustment. Flags = edge candidates.

## 9. Operating constraints — HARD
**Billing:** everything runs on the user's Claude Max plan, interactively, in-session. **No programmatic Anthropic API calls, no artifacts that call it, no lights-out grading runs.** Supervised batches only.
**Repo:** git-backed. Suggested layout:
```
/data        league-wide CFBD pulls, Sideline CSVs, backtest data, win totals
/snapshots/{team}/   frozen research: pulls/, roster (two-deep + confidence flags),
                     magazines.md, news.md (dated finds), META.json (date, sources, gaps)
/pipeline    code: CFBD client, backtest, grading harness, blend, variance, flags
/outputs     ratings table, run logs
```
Commit = freeze. Python (cfbd client library); flag if the user prefers R. Repo must be **private** and durable across sessions (§0 step 3). `secrets/` is gitignored.
**Interaction protocol:**
- Session start: run §0, inventory §13, then begin the build order.
- **Fail loud, ask one question.** Never guess silently. Never multi-question interviews.
- **Clean teams first, messy last.**
- Per-team trigger: **"Run the pipeline for Team X."** Most runs complete cleanly; a minority stop with one question. That's the design working.
- **Log every compute run:** date, anchor set + capture dates, k, cap, code version.

## 10. Build order — start here
1. **Repo scaffold + CFBD client.** One batched league-wide pull: team list, rosters, SP+, returning production, talent, portal, schedules, plus historical data for the backtest. (§0 steps 2–4 are prerequisites.)
2. **Backtest** (§7).
3. **Snapshot-freeze tooling.** Per-team research procedure implementing §5. Magazine ingestion is unblocked: searchable Phil Steele + digital Athlon are in the folder. Resolve the FEI placement question here.
4. **Grading harness.** Blinded prompt template + fixed exemplar block + JSON output per group: `{grade, confidence, rationale_bullets, key_players, data_gaps}`.
5. **Compute.** Cross-sectional fit, blend, variance, flags, run log. Short, deterministic code. Includes anchor loaders that re-pull live sources and re-date captures.
6. **Pilot: two teams end-to-end** — one stable low-churn P4, one high-churn G5. User reviews both before scaling.
7. **Scale:** freeze all snapshots → grade all → league-wide fit → flag pass (second research + targeted PFF) → final ratings table.

## 11. OPEN items — ask when relevant, not all at once
- ~~Magazine formats~~ RESOLVED: Phil Steele scanned→searchable conversions done; Athlon born-digital.
- ~~Last year's preseason win totals~~ RESOLVED: in folder. Odds API decision now decidable with the backtest.
- ~~PFF+ export reality check~~ RESOLVED: 27 tables exported + data dictionary.
- ~~Sim double-counting~~ RESOLVED 2026-07-12 (session 2): user confirms the simulator injects game-level randomness itself → the variance band is epistemic-only, scaled below raw backtest miss (which includes in-season noise).
- ~~FEI blinding placement~~ RESOLVED 2026-07-13: FEI is IN the anchor blend; compute-only, blinded from grading.
- ~~Massey own-model vs. composite~~ RESOLVED 2026-07-13: own model (composite ingests SP+/FPI → double-weighting).
- **k and cap tuning** — CALIBRATED 2026-07-13 from PFF-unit backtest: k=0.30, cap=±6 (see outputs/backtest_2026-07-12/PARAMETERS.json). Re-check after pilot + August anchors.
- **Python vs. R** — Python assumed, unconfirmed.
- **Pick Six ingestion** — inventory when it arrives (~tomorrow); P4 anchor input only.

## 12. Anti-goals — do not
- Re-litigate settled design: the tier rubric is dead; the blend is the mechanism; blinding is mandatory.
- Produce narrative team reports.
- Let any consensus or market number touch the grading layer (that includes everything in `anchors/` and the win-totals files).
- Bulk-export or scrape PFF (the 27 CSVs already in the folder are the PFF data).
- Make programmatic Anthropic API calls or build artifacts that do.
- Silently "correct" a rating that disagrees with consensus — that disagreement is the product. Flag it.
- Print or commit the CFBD key.

## 13. Folder inventory (verified 2026-07-12; re-verify at session start)
`NCAAF Data 2026/` (user's connected folder):
- `Phil Steele 2026 - <Conf> (searchable).pdf` ×12 — USE THESE (AAC, ACC, B10, B12, CUSA, General, Independents, MAC, Mountain West, PAC12, SBC, SEC). One leftover raw scan (`Phil Steele 2026 - CUSA.pdf`, 70 MB) — ignore; user may delete.
- `Athlon 2026 - *.pdf` ×13 — born-digital, searchable (11 conference files + General Rankings + General Stories).
- `PFF_*.csv` — 2025 player/team premium stats (27 files) plus historical team grades: `PFF_20XX_team_grades.csv` per season (2024 done; more years may be added — same schema, year in filename). Useful for backtest context and grading exemplars.
  - [repo-sync note 2026-07-12, session 2] The historical delivery landed as `PFF History/{2021..2024}/` on the device — 7 tables per year (team grades + passing/rushing/receiving/blocking/defense/special-teams summaries), mirrored to `data/pff_history/` in the repo and schema-verified against the 2025 exports (`pipeline/check_pff_history.py`).
- `PFF_data_dictionary.json` / `PFF_data_dictionary.md` — definitions for all 2,354 columns across the 27 files; look up any PFF column here (the original key images were deleted as superseded).
- `anchors/` — `anchor_sources.json` (manifest), `anchors_overall_2026-07-12.csv` (5×138 blend input), per-source captures (SP+, FEI, Massey, FPI, TeamRankings), `team_name_map.csv` (fill the CFBD column at §0). **Compute-phase only.**
- `Win Totals from 2025.csv` — 2025 preseason win totals, ~135 FBS teams. Schema: `TEAM`, then per-book season win totals with the price in parens ("5.5 (-200)") for Bet365/FanDuel/DraftKings/Caesars/BetRivers, plus DK/BR/Bet365 conference win totals (sparse). Parse total and juice separately. **Compute-phase only.**
- `secrets/cfbd_api_key.txt` — CFBD v2 key. Never print/commit.
- Pick Six 2026 PDF — expected ~2026-07-13; inventory when present.

## 14. Environment facts learned in prep (save yourself the debugging)
- The connected folder is reached via device tools; its local VM has **no network** and **cannot delete files** (move refuse into `_to_delete/` instead; `rm` fails with "Operation not permitted").
- Staging device→cloud stalls on files over ~60 MB. Everything you need is already under that (searchable PDFs are 4–39 MB) except the raw scans, which you shouldn't need. Cloud→device commits of normal-sized outputs work fine.
- Cloud sandbox egress defaults to package managers only — see §0 step 2 for the CFBD fix. Do not fetch around blocks.
- The cloud workspace does not persist across sessions — hence §0 step 3 (durable repo) and the habit of committing/pushing every freeze.
- ESPN pages serve **stale prior-season tables to non-JS fetchers** (an FPI fetch returned 2025 data while the browser showed 2026). Always verify the season vintage of anything fetched; prefer CFBD.
- OCR'd Phil Steele numbers: prose is reliable; for any single stat that matters, glance at the page image (the text layer sits on the original scan, so it's a one-click check).

---
**Kickoff:** run §0, report the four check results in a few lines (folder ✓/✗, CFBD ✓/✗, repo decision, name map 138/138 ✓/✗), then start Build Order step 1.
