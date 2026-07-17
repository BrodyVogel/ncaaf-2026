# OPERATOR HANDOFF — 2026 preseason power ratings (v1.0, 2026-07-17)

Written at the Fable→Opus grading handoff, 71 of 138 builds complete. This
is the single entry point: it encodes the working method that produced the
first 71 builds so the remaining 67 are graded the same way. Follow it in
preference to improvisation; where it is silent, RESEARCH_PROCEDURE.md and
DISPOSITION_RULES.md govern; where all three are silent, adjudicate
conservatively, document, and tell the owner.

## 0. Session start (every session)

Read, in order:
1. This file.
2. `pipeline/DISPOSITION_RULES.md` — the precedent book (R1–R18).
3. `pipeline/RESEARCH_PROCEDURE.md` v2.1 — the research phase spec.
4. `pipeline/grading/GRADING_PROMPT.md` v1.2.2 + `pipeline/grading/exemplars.md`
   v3.1 — BOTH FROZEN. Never edit.
5. `outputs/grade_board.csv` — the 71-team calibration board (peer rails).
6. `outputs/FORWARD_FLAGS.csv` — open cross-build verifications.
7. The current round's wrap + magazine map (e.g. `outputs/mwc_wrap_2026-07-17.md`,
   `outputs/<conf>_magazine_map.md`) for where the last round left off.

## 1. Standing owner directives (verbatim, in force)

- Complete conference rounds team-by-team with the full pipeline; after
  EVERY finished team deliver a full-formula summary (template in §8).
- "When you identified a problem, you alerted me and fixed it. Please
  continue to do that."
- "If you ever discover something that, in retrospect, is a problem for
  work that's already been completed, stop and alert me. I'd rather rerun
  this for every team than have a flawed ratings set."
- Propose → approve → build for ANY parameter change (see §2).
- Owner preference: "I like brief explanations, but I also need to know
  exactly what's happening when you make changes."

## 2. FROZEN — never change without owner approval

- Formula: final = anchor_blend + class(0) + clip(0.35 × resid, ±6) +
  ST((g−50)/50 × 1.0), league recenter (~−0.5). resid = (implied_off −
  anchor_off) − (implied_def − anchor_def). DEF = points-allowed scale
  (LOWER = better).
- Band = 6.0 × coach_change(1.13, HC-only — interim promotions count per
  Hauser; OC/DC churn does NOT) × dispersion_flag(1.10 above ~10.43) ×
  (1 + 0.03 × min(L-count, 5)).
- Anchors: G5 5-source set (SP+ w2; FEI/Massey/FPI/TR w1), P4 adds PickSix.
  Winsorize any source >5 from the median-of-others. This machinery handled
  the NDSU 4-source-winsorize case correctly — trust it.
- GRADING_PROMPT.md v1.2.2, exemplars.md v3.1, conference offsets
  (data/backtest/conf_offsets_2021_2025.json), the 0–100 national
  percentile scale.
- Blinding v2: the assembler/grader NEVER reads ratings, market data,
  team-level projections. Magazines: exclude forecasts, PS SMI/computer
  calls/Exp Chart/homefield/schedule-difficulty/ATS; retain retrospective
  ranks and results.

DEFERRED (do NOT do early): joint conversion + level-slope refit at full
138 (interim checkpoint ~90–100 builds, owner decides); Finding-4 MAC
defense-dummy investigation; market leans (withdrawn pending refit — report
raw resid as information only). Level/shape decomposition = PROXY-FIT-REGIME
diagnostic only; never interpret it on real grades (GRADING_BIAS_DIAG
2026-07-16).

## 3. Per-team pipeline (run in this order, every team)

All commands from the repo root. Team_Dir = underscore form with exact
accents/apostrophes (`Hawai'i`, `San_José_State`). The gates now FAIL
loudly on a wrong form — if a gate errors "MISSING", fix the spelling, do
not skip.

```
0.  python3 pipeline/forward_flags.py <Team_Dir>      # open flags to verify
1.  python3 pipeline/snapshot_build.py "<Team Space Name>"
2.  Magazines: verify page vs the round's magazine map (banner strip for PS,
    header line for Athlon), then extract (see §4). Write magazines.md.
3.  python3 pipeline/team_dump.py <Team_Dir>          # the evidence sheet
4.  Cross-refs: for every feed arrival/departure touching a BUILT team,
    grep that snapshot (pulls/portal_2026_{in,out}.json + roster_two_deep
    + news.md). Departures to UNBUILT teams -> append rows to
    outputs/FORWARD_FLAGS.csv. Zero unexplained sides.
5.  Adjudications per DISPOSITION_RULES.md (R1-R18). Record bare-name META
    keys + news.md rationale.
6.  Write the six files: magazines.md, news.md, roster_two_deep.csv
    (header: unit,pos,depth,player,class,origin,note - departed players go
    in NOTE, never player), unit_dossiers.md, research_log.md, META.json.
7.  Gates (all must pass; ledger appends itself to the dossier):
      python3 pipeline/disposition_ledger.py <Team_Dir> --write
      python3 pipeline/departure_check.py <Team_Dir>
      python3 pipeline/blinding_check.py "<Team Space Name>"
8.  RECONCILE BY HAND ANYWAY: read the appended ledger; every EXPIRED/GONE
    row must be print-consistent; every RETURNS-override must cite its rule.
9.  Freeze commit (message: "<Team> snapshot: research complete, frozen
    (<CONF> n/m)"), note the short rev.
10. grades.json (schema in §5; snapshot_rev = the freeze rev), then:
      python3 pipeline/grades_check.py <Team_Dir>
      python3 pipeline/departure_check.py <Team_Dir>   # AGAIN, post-grades:
    # the key_player scan only sees grades.json once it exists. (The
    # 2026-07-17 sweep found 19 undocumented key_player names because the
    # first 71 builds ran this gate pre-grades only.) Any UNKNOWN NAME =
    # document it (feed-gap arrival / true-FR signee) before committing.
    Commit grades.
11. python3 pipeline/pilot_readout.py \
      outputs/anchor_runs/anchor_run_2026-07-14_class0.json \
      "<Team Space Name>" snapshots outputs/pilot_2026-07-14
    Commit the two pilot files. Push.
12. python3 pipeline/build_board.py                   # refresh the board
13. Close/append FORWARD_FLAGS rows. Commit + push.
14. Send the owner the full-formula summary (§8).
```

Round end: wrap doc modeled on outputs/mwc_wrap_2026-07-17.md (board, unit
matrix, resid diagnostic WITHOUT level/shape tables, anchor-integrity notes,
feed-integrity census, forward flags, conclusions). Commit, push, send.

## 4. Magazine workflow

- Build/extend `outputs/<conf>_magazine_map.md` FIRST: render a low-dpi
  banner contact sheet across the conference PDF, verify every page's team
  banner visually, record the map. Never trust page order alone.
- Athlon: `pdftotext -f <p> -l <p> -layout "data/magazines/athlon/<pdf>" /tmp/<t>/athlon.txt`
- Phil Steele: render page at 300 dpi (pdf2image; fitz not installed), crop
  two text columns (x: 0.090–0.315 and 0.315–0.535 of width; y: 0.30–0.97)
  plus a banner strip (y: 0.16–0.26). Targeted zoom crops for anything
  garbled. PS CAPS in lineups = returning starters; Athlon BOLD = returning
  starters, * = 2026 transfer (can be WRONG — R15/R16).
- OCR discipline: verify every load-bearing number against the page image
  (Athlon "4-(" = 4-8; "Fitzpatrick" vs PFF "Fitzgerald"). Blinding v2 list
  in §2 applies at extraction time — do not copy excluded content into
  magazines.md.

## 5. Grading discipline (the part that must not drift)

- Grade ROOMS on a 0–100 national FBS percentile scale, anchor-blind,
  AFTER the dossier is written: Room (who, with adjusted tape) →
  Mechanical (why the number) → Bracket. Never number-first.
- Exactly-2 exemplar bracketing from exemplars.md v3.1 (97 TexasQB, 91
  KentuckyDL, 84 TTU-OL, 78 HoustonWRTE, 72 WSU-DB, 60 WakeDL, 50
  NebWRTE, 40 UNLV-LB, 32 IllinoisRB, 25 WKU-OL, 15 FIU-QB, 6 FAU-DB) PLUS
  peer rails from outputs/grade_board.csv (name specific graded rooms
  above/below).
- Offsets per R14 (earned-conference cells; sub-FBS = no cell). Flag any
  arrival sample <50 snaps as sample-useless pedigree.
- Confidence L when the room's core is unproven (FCS-bet QB, injury
  anchor, print conflict, mass turnover). L drives the band — use it.
- G5 guard note on any G5 unit graded > ~40.
- grades.json: units{8} + _meta (graded_utc, snapshot_rev "frozen <date>
  (<rev>)", prompt, exemplars, grader, planned_vs_final_deviations,
  shadow_proxy_divergence) + grades_detail×8 (bracketing_exemplars,
  rationale_bullets, key_players, data_gaps, g5_guard_note). The dossier's
  `PLANNED GRADES: QB 20 L | RB 18 | ...` line is MANDATORY and must match
  (grades_check enforces; declared deviations go in _meta).
- Shadow proxy is DIAGNOSTIC ONLY. Known artifact signatures: team-grade
  carryover inflation (unit keyed to team tape that walks — Hawai'i DB 83),
  kicker-keying ST, interior-snaps OL keying, team-grade DEFLATION of
  returning units (AF DB, artifact #51), all-void newcomer (#43). The
  numbered artifact list reached #51 — before assigning a new number, grep
  dossiers/research logs for the signature; only genuinely new signatures
  get numbers.

## 6. Verification pass (mandatory self-checks, tuned to known failure modes)

The 2026-07-16 diagnostic episode showed three operator failure modes:
interpretation ahead of regime-checking, an unverified output table, and an
unflagged 75% join rate. Their analogues here, checked EVERY build:

1. OCR numbers verified against page images before they enter a dossier.
2. Ledger-vs-prints reconciliation (§3 step 8) even though the automated
   reconcile also runs — the gate catches names; you catch meaning.
3. Any aggregate claim (round means, "every team X") states n and the
   match/join basis. No unqualified universals — "every roster grades
   cooler than its anchors" was a lens artifact.
4. Raw resid is the only resid you interpret. Level/shape = proxy-regime
   diagnostic. No leans.
5. Sample sizes on arrival tape stated inline (76.4/4 snaps ≠ 76.4/400).
6. When a check/gate surprises you, the check is probably right — the
   2026-07-17 retro-audit found 5 mis-graded units precisely where the new
   gate pointed. Investigate before overriding, and never "fix" a gate to
   make a team pass.

## 7. Environment traps (learned the hard way)

- cwd resets to /home/claude constantly: `cd /home/claude/cfb-2026-power-ratings`
  or use absolute paths in every command block.
- Write tool requires a prior Read of an existing file (scaffolds included).
- Quote apostrophe/accent team dirs in shell (`"snapshots/Hawai'i"`); glob
  (`snapshots/Hawai*`) when unsure of the codepoint.
- META override lists take BARE NAMES (validated at ledger time now).
- disposition_ledger --write REWRITES the ledger section in the dossier —
  run it after any META change, never hand-edit the ledger.
- CFBD quirks catalogued: duplicate feed records (Mathias Davis), duplicate
  roster rows (Aamaris Brown; Barry Kpeenu ×2), wrong position fields (Kam
  Thomas "DE"), FCS roster gaps (Baricka Kpeenu absent entirely), approximate
  year fields (prints govern per R7-R9).
- pilot_readout writes two files into outputs/pilot_2026-07-14/ — commit them.

## 8. Per-team summary template (owner-facing, after every team)

**<Team> — COMPLETE (<Conf> n/m) · FINAL <x> (r<k>/138) · band ±<b>**
1. Units line: `QB g|proxy · ...` (8 units, L-flags, sum).
2. Implied vs anchor: off and def with the def-scale gloss ("points-allowed
   scale, LOWER = better; higher implied than anchor = grades COOLER").
3. Raw residual headline (level/shape mentioned only as proxy-regime
   diagnostic if at all).
4. Anchor sources: each raw → normalized → used, any WINSORIZED flagged,
   blend + dispersion (+ flag).
5. Assembly chain: anchor + class + k×resid + ST → recenter → final.
6. Band breakdown: 6.0 × coach × dispersion × conf(L-count).
7. Alerts/notes: adjudications by rule name, cross-refs closed/opened,
   feed artifacts, proxy divergences, gates + commit revs.
8. Running conference board.

## 9. Calibration ramp (REQUIRED before the new grader's first live team)

1. `python3 pipeline/qa_regrade_sample.py sample snapshots /tmp/regrade.csv --frac 0.05 --seed 27`
2. Blind re-grade each sampled (team, unit) from its FROZEN snapshot
   dossier evidence — do NOT open grades.json or the board for those teams
   first. Write snapshots/<team>/grades_retest.json per the harness spec.
3. `python3 pipeline/qa_regrade_sample.py compare ...` — acceptance gate:
   median |Δ| ≤ 5 and p90 |Δ| ≤ 8.
4. Pass → proceed to the Pac-12 round (Boise State, Colorado State, Fresno
   State, Oregon State, San Diego State, Texas State, Utah State, Washington
   State). Fail → report the delta distribution to the owner; the failing
   unit types tell you which sections of §5 to re-read before going live.

## 10. What good looks like

Wyoming (MWC 7/10) is the reference build: read
snapshots/Wyoming/{magazines,news,unit_dossiers,research_log}.md + META +
grades.json top to bottom once before your first team. Air Force is the
clean-feed control case; NDSU is the newcomer pattern; UTEP is maximum-churn
with two STAYS overrides; Hawai'i has the print-conflict and
destination-resolution patterns.
