# Media-days integration — handoff to Opus (2026-07-21, rev 2)

Owner-approved plan: delta-driven integration of the four media-days digests. **Fable has
completed steps 1–3 for the Big 12 AND the Mountain West.** Opus owns: steps 1–3 for
**ACC and Sun Belt**, then steps 4–6 globally.

Done (read these first — the Decision Rules R1–R4 in the B12 memo govern everything):
- `docs/MEDIA_DAYS_TRIAGE_B12_2026-07-21.md` — 0 changes (event pre-dated baseline); rules R1–R4.
- `docs/MEDIA_DAYS_TRIAGE_MWC_2026-07-21.md` — 2 grade changes applied + gated
  (**Hawai'i LB 12L→14M**, **NIU QB 18L→20L**; addenda in each snapshot dir), 1 schedule
  fix staged (**NDSU–SJSU is_conf=False** in `pipeline/win_totals_data.py`).
- **IMPORTANT: `final_pass.py` has NOT been run.** grades.json for Hawai'i/NIU is ahead of
  the boards; the payload/artifact/tracker are stale until your step-4 rebuild.

Sources committed: `data/media_days/{ACC,SBC}_2026_media_days.md`. Digest quality is good,
but **URLs are unverified** — hence R1's corroboration bar.

## ACC triage — pre-verified by Fable (log as confirmations, do not reopen)
- Wake QB Gio Lopez already keyed in dossier ("my grade keys Lopez," 75.2 adj).
- ACC 8/9-game split matches our schedule data team-for-team (BC/Clemson/FSU/GT/UNC at 8) —
  structural validation, no change. Tiebreaker/title-game items sim-irrelevant.
- Official ACC media poll NOT released until **July 28** — queue a re-sweep, don't wait.

## ACC checks to run (not yet verified)
- Miami Mensah + Duke Eget-vs-Mahan vs our dossiers (portfolio history says known — confirm).
- Syracuse Angeli (Achilles return) vs our QB grade assumption.
- Virginia LB Kam Robinson Week-0 target — was the ACL priced in our LB grade? (Potential
  R2 case if the dossier discounted availability; check the L rationale if the unit is L.)
- Stanford Warren "positioned as starter, healthy at Kickoff" — QB 42 L likely stays L per
  R2 (tape uncertainty, not identity), but confirm the dossier's L driver.
- UNC explicitly-open QB — consistent with 48 L unless our grade assumed Edwards locked.
- Pitt WR names (official-site sourced) — color only; we hold Pitt conf U5.5, nothing moves it.
- BC/GT/Louisville/FSU/Clemson QB confirmations — R2 says no flips (tape-driven Ls); verify
  each dossier's L driver before logging.

## SBC triage — pre-verified by Fable
- LaTech Baker ACL return already priced ("back through spring drills"); Cumbie naming him
  starter = identity confirmation; check whether the dossier's QB confidence hinged on the
  battle (potential R2 flip) or on tape (no flip).
- Marshall defensive gutting already priced ("decimated"); Del Rio-Wilson confirmed.

## SBC checks to run
- **Southern Miss "John White"** — a QB in the race who is NOT in our graded room
  (Hampton/Price/Lyddy). If White is real and genuinely leading (SI "4th string to QB1"
  buzz + Anderson "wouldn't surprise me if he's the guy"), this is an R1 room-composition
  case like NIU QB — the one likely SBC regrade. Read the full dossier QB section first.
- Marshall DC Lambert-vs-Morrison vs our dossier's "## Specialists / staff" section
  (defense already priced as rebuilt; likely note-only).
- Southern Miss staff (Anderson 1st yr) vs our dossier header.
- South Alabama: digest's thinnest team (NOTHING FOUND) — grades stand untouched.
- JMU/Coastal/ODU/ArkState/App State open QB battles — all graded L already; R2 says no flips.
- Georgia Southern Max Johnson (7th-year) framed "starter if season began today" — identity
  color; check dossier priced him (it did per extraction: "Max Johnson ... + frosh Bryan").

## Steps 4–6 (unchanged from rev 1, plus the staged items)

**4. Rebuild** (after ACC/SBC regrades, if any):
   - Any new grade edits: `grades.json` + `_meta.planned_vs_final_deviations` + dated
     `media_days_addendum.md` → `python3 pipeline/grades_check.py <Team_Dir>`.
   - `python3 pipeline/final_pass.py` (picks up Hawai'i/NIU + yours).
   - **Devig fix**: `win_totals_compute._market_block` still uses the invalid
     `st.median()`-of-American-odds construction (straddle bug, found 2026-07-20);
     port the correct pattern from `bet_tracker.market_fair` (de-vig each book's two-way
     implied probs, 30-cent convention, average fair PROBABILITIES).
   - Rebuild payload → `build_win_totals_artifact.py` → `python3 pipeline/bet_tracker.py`.
   - **Post-build asserts:** MW conf-game census = {8: 10} (NDSU–SJSU fix live); ACC census
     = {8: 5, 9: 12}; artifact + tracker screenshot-verified.

**5. Before/after memo** (`outputs/MEDIA_DAYS_IMPACT_2026-07-21.md`):
   - All 14 open bets: our_p / EV / % edge old→new. Expect: **Hawai'i U7.5 worsens**
     (rating +LB, band ×1.12→×1.09 — say it plainly, with the NIU-opponent offset
     quantified); others ≈ unchanged unless ACC/SBC regrades land.
   - Ratings movers ≥0.3 pts; unplaced top-10 board deltas; "considered, not changed" list.
   - New-bet caveat: July-12 price snapshot is stale; re-check live lines before acting.

**6. Deliver + commit:** SendUserFile memo + tracker (+ artifact); commit per logical step
   with Opus trailers (`Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` +
   `Claude-Session: https://claude.ai/code/session_01XjFvWoX6BuaitKuxXiTfB3`); push;
   persisted-artifact gallery update if the desktop is connected.

**Queued follow-ups (NOT this pass):** ACC official poll July 28 re-sweep; fall-camp QB
resolutions (each triage memo lists its queue); Dickens eligibility confirmation.
