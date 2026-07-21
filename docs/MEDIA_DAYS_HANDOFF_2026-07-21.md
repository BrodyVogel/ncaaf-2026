# Media-days integration — status & rebuild spec (2026-07-21, rev 3)

**All four conference triages are COMPLETE (steps 1–3 done by Fable).** What remains is
steps 4–6: the global rebuild, the impact memo, and delivery. This file is now the spec
for whoever runs them.

## Triage results (read the memos for detail)
- `docs/MEDIA_DAYS_TRIAGE_B12_2026-07-21.md` — 0 changes; Decision Rules R1–R4 live here.
- `docs/MEDIA_DAYS_TRIAGE_MWC_2026-07-21.md` — **2 grade changes applied + gated**
  (Hawai'i LB 12L→14M; NIU QB 18L→20L; dated addenda in each snapshot dir) and the
  **NDSU–SJSU is_conf=False fix** staged in `pipeline/win_totals_data.py`.
- `docs/MEDIA_DAYS_TRIAGE_ACC_2026-07-21.md` — 0 changes; 8/9 split validated; poll re-sweep queued (July 28).
- `docs/MEDIA_DAYS_TRIAGE_SBC_2026-07-21.md` — 0 changes; John White candidate dissolved (already in room).

Net input change to the field: **two units on two G5 teams + one schedule flag.**
`final_pass.py` has NOT been run — grades.json (Hawai'i, NIU) is ahead of the
boards/payload/artifact/tracker until step 4 executes.

## Step 4 — rebuild
1. `python3 pipeline/final_pass.py` (deterministic; picks up both regrades; refit runs on
   all 138 — expect micro-shifts everywhere from the OLS refit, material shifts only for
   Hawai'i (rating + band ×1.12→×1.09) and NIU (rating)).
2. **Devig fix (fold in here):** `win_totals_compute._market_block` still computes market
   fair prices with a `st.median()`-of-American-odds construction that is invalid when a
   book's odds straddle ±100 (found 2026-07-20; conference markets with 2 books are the
   exposed case). Port the correct pattern from `bet_tracker.market_fair`: de-vig each
   book's two-way implied probabilities (30-cent convention for the unposted side), then
   average the fair PROBABILITIES across books.
3. Rebuild payload (`win_totals_compute.build_payload`) → `build_win_totals_artifact.py`
   → `python3 pipeline/bet_tracker.py`.
4. **Post-build asserts:** MW conf-game census = {8: 10} (NDSU–SJSU fix live); ACC census
   = {8: 5, 9: 12}; tracker regenerates 14 bets; artifact + tracker screenshot-verified.

## Step 5 — impact memo (`outputs/MEDIA_DAYS_IMPACT_2026-07-21.md`)
- All 14 open bets: our_p / EV / % edge, old→new (old values are in the current
  committed `outputs/bet_tracker.csv`; capture them BEFORE rebuilding).
- **Hawai'i U7.5 worsens** — say it plainly and quantify, including the partial
  NIU-opponent offset (NIU is on Hawai'i's schedule; a stronger NIU pushes Hawai'i's
  win distribution down slightly).
- Ratings movers ≥0.3 pts (expect: Hawai'i, NIU; everything else refit noise <0.1).
- Unplaced top-10 board deltas; the "considered, not changed" record (the four triage
  memos are the source); conference-tab edges before/after the devig fix.
- New-bet caveat: the July-12 price snapshot is stale — re-check live lines before acting.

## Step 6 — deliver + commit
- SendUserFile: impact memo + refreshed tracker (+ artifact if visibly changed).
- Commit per logical step with the runner's trailers + the session URL
  (`Claude-Session: https://claude.ai/code/session_01XjFvWoX6BuaitKuxXiTfB3`);
  push to main; persisted-artifact gallery update if the desktop is connected.

## Queued follow-ups (NOT this pass)
ACC official poll re-sweep (July 28); fall-camp QB resolutions (each triage memo's queue);
Dickens eligibility confirmation; watch items A1–A2, S1–S4, W1–W5 (B12), MWC W1–W3.
