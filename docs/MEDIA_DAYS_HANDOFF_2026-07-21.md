# Media-days integration — handoff to Opus (2026-07-21)

Owner-approved plan (this session): delta-driven integration of the four media-days digests.
Fable completed steps 1–3 for the **Big 12** (result: 0 grade changes, 0 confidence changes —
see `docs/MEDIA_DAYS_TRIAGE_B12_2026-07-21.md`, the **worked example whose Decision Rules
R1–R4 govern everything below**). Opus owns: steps 1–3 for **ACC, Mountain West, Sun Belt**,
then steps 4–6 globally.

Sources are committed: `data/media_days/{ACC,MWC,SBC}_2026_media_days.md`. Digest quality is
good (verdict-per-question, tagged sourcing, honest gaps) but **URLs are unverified** — R1's
corroboration bar exists for that reason.

## Pre-triage already done by Fable — do not redo discovery

### Regrade candidates (2) — open these fully (dossier + mags + PFF + news.md, frozen method)

1. **Hawai'i LB 12 (conf L)** — the canonical R2 flip. Dossier says literally
   "L: Otis availability" with the PS/Athlon print conflict logged. MWC digest resolves it
   decisively: Otis attended media days, named preseason All-MW, February beat reporting
   "fully healthy ahead of camp," moving MIKE→weak-side/dime. Regrade the unit with Otis
   available (bracket line in dossier: "Nevada 12 L, > NIU 10 L, < UNLV 16" — availability
   risk was holding it at 12; expect landing ~16–20) and flip confidence L→M.
   **Band note:** Hawai'i L-count drops 4→3 (band ×1.12→×1.09) — tighter distribution AND
   higher rating both matter. **Bet impact: moves AGAINST our Hawai'i U7.5 (0.60u at −120
   CZR). Quantify honestly in the step-5 memo; partial offset via NIU below (Hawai'i
   opponent).**
2. **Northern Illinois QB 18 (conf L)** — new material fact, room composition changed.
   **Taron Dickens is absent from our graded room** (we graded Davidson/Macon/Hamric;
   Dickens — WCU, 2025 SoCon OPOY, 38 total TD — signed ~July 3 and missed the freeze).
   SI: "Barring an unlikely scenario, Dickens is in line to start"; interim HC has not
   named him (competition officially open). Regrade the room WITH Dickens (bracket vs
   Wyoming QB 20 L — Hughes, comparable FCS-transfer tier — and SJSU QB 20 L); confidence
   stays **L** (FCS projection + unofficial). NIU is a Hawai'i/MW opponent — its rating
   feeds our Hawai'i bet's schedule.

### Verified non-deltas — confirmations; log in triage, do NOT reopen
- **MWC:** NDSU membership CORRECT (football-only member 7/1; postseason-ineligible — irrelevant
  to regular-season totals); UTEP Colson already in dossier w/ exact UIW stats; NIU HC change
  (Hammock→Seahawks Feb, Harley interim) already in news.md as a MULTIPLIER CALL.
- **ACC:** Wake QB Gio Lopez already keyed ("my grade keys Lopez," 75.2 adj); ACC 8/9-game split
  matches our schedule data team-for-team (BC/Clemson/FSU/GT/UNC at 8) — structural validation,
  no data change; tiebreaker/title-game items are sim-irrelevant.
- **SBC:** LaTech Baker's ACL return already priced ("back through spring drills"); Marshall's
  defensive gutting already priced ("decimated," 3 of top 4 sack leaders out).

### Handed-over checks (verify during your triage; I did not confirm these)
- ACC: Miami Mensah + Duke Eget-vs-Mahan vs our dossiers (portfolio history says known — confirm);
  Syracuse Angeli (Achilles) return status vs our QB grade; Virginia LB Kam Robinson Week-0 target
  (priced?); Stanford Warren "positioned as starter, healthy" (QB 42 L likely stays L per R2 —
  tape uncertainty, not identity, drives it); UNC's explicitly-open QB (48 L consistent — no action
  unless our grade assumed Edwards locked); Pitt WR names (official-site sourced — likely
  confidence color only; we hold Pitt conf U5.5, nothing here moves it).
- MWC: Hawai'i K/P resolution (Olvera-Harle kicks; punter TBD international) vs ST 12 L — the L
  is quality-driven (both elite specialists gone), likely NO flip per R2; SJSU/Nevada/Wyoming QB
  battles all consistent with graded L's; UNLV Arnold "presumptive, not clear QB1" consistent
  with 36 M.
- SBC: Southern Miss staff (Anderson 1st yr, Bolden DC) vs our dossier header; new QB name
  **John White** in the race (our dossier had Hampton/Price/Lyddy — if White is real and leading,
  that's an R1 room-composition question like NIU; check whether the grade leaned on Hampton);
  Marshall DC Lambert-vs-Morrison vs our dossier's "## Specialists / staff" section (defense
  already priced as rebuilt; likely note-only); South Alabama = digest's thinnest team (NOTHING
  FOUND) — grades stand untouched.

## Steps 4–6 spec

**4. Rebuild** (only after all regrades land):
   - Per changed team: edit `snapshots/<Team>/grades.json` (units + matching grades_detail,
     `_meta.planned_vs_final_deviations` entry, `_meta` provenance note "media-days integration
     2026-07-21") + dated `media_days_addendum.md` → `python3 pipeline/grades_check.py <Team_Dir>`.
   - `python3 pipeline/final_pass.py` (deterministic refit; DEFAULT demeaned residual).
   - **Fold in the devig fix**: `win_totals_compute._market_block` still uses the
     `st.median()`-of-American-odds construction that is invalid when odds straddle ±100
     (the bug found 2026-07-20; bet_tracker.market_fair has the correct pattern: de-vig each
     book's two-way implied probabilities — 30-cent convention for the unposted side — and
     average the fair PROBABILITIES). Artifact conference-market edges are affected; regular
     mostly unaffected (5-book medians).
   - Rebuild payload (`win_totals_compute.build_payload`) → `build_win_totals_artifact.py` →
     `python3 pipeline/bet_tracker.py` (reads payload; the 14 open bets re-price automatically).
     Screenshot-verify the artifact + tracker render.

**5. Before/after memo** (`outputs/MEDIA_DAYS_IMPACT_2026-07-21.md` or similar):
   - Every open bet: our_p / EV / % edge, old→new. Expect: Hawai'i U7.5 worsens (say so
     plainly, with the NIU offset quantified); everything else ≈ unchanged.
   - Ratings movers table (any team whose final moved ≥0.3 pts), unplaced top-10 board
     deltas, and a "considered, not changed" list (the discipline record).
   - Note for any NEW bet: our line snapshot is July-12-stale; media-day info is public and
     priced by books — re-check live prices before acting.

**6. Deliver + commit:**
   - SendUserFile: impact memo + refreshed tracker (+ artifact if changed).
   - Commit per logical step with Opus trailers
     (`Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` +
     `Claude-Session: https://claude.ai/code/session_01XjFvWoX6BuaitKuxXiTfB3`), push to main.
   - Persisted-artifact gallery update for the tracker if the desktop is connected.

**Queued follow-ups (do NOT do in this pass):** ACC official poll July 28 re-sweep; fall-camp
QB-battle resolutions (~13 open rooms across the four digests — each triage lists its queue).
