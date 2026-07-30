# Camp sweep 1 — triage (2026-07-30)

Digest archived: data/media_days/CAMP_SWEEP_1_digest_2026-07-30.md. B10 media days
incomplete, Pac-12 unscheduled (owner) — those prompts HOLD until events conclude.
Coverage caveat: camps days-old; several items are July-media-day/spring vintage.

## Applied (2 adjudication rows -> regen -> final_pass -> board/payload rebuilt)

- **UCF QB conf L->M, grade holds 46**: Frost named Barnett clear QB1 at B12 media
  days 7/22 (one day after our B12 triage — genuinely new); "full go" after minor
  spring injury. Band tightens; held conf O3.5 edge +8.9% -> +9.1%.
- **UNLV QB 36->34, conf M->L**: OPEN Arnold/Orji race at camp open; Orji off Gr3
  LCL + severe hamstring; S10 down-transfer prior discounts Arnold pedigree.
  (Not held; strengthens the under candidacy. Calibrated now -0.98.)

Rebuild deltas elsewhere: Nevada/Wake ±0.1% (refit ripple). All other held
positions unchanged.

## Held tickets — verdicts (no action)

- **ECU O7.5**: battle CONFIRMED unresolved mid-July (Griffis vs Emory
  Williams-Miami; FR Ditta won the bowl start). Both-coordinators-new already in
  dossier. Fourth knock on the flag; watch for a naming before any add/exit call.
- **UConn O5.5**: battle ongoing; spring ones went Merklinger + Macdonald
  (returnee), Osborne top-two mix. Consistent with grade 44 L. No OL/DL reveals yet.
- **Rutgers O4.5**: Schiano — "far from over," "they both did well." Priced.
- **Tulsa O5.5**: Hayes +20 lbs, framed as returning starter; Lamb: "retained
  probably 80% of our roster" (continuity thesis confirmed); Dexter Williams II
  (from KSU) = QB2 depth upgrade.
- **KSU O6.5**: Collins first-team in spring, "primed"; no coach naming; hold 44 L.

## Candidates — screen notes

- **UNLV under: STRENGTHENED** (open race + injury + S10 prior; grade applied).
- **Miami-OH under: supported** (three-horse race incl. D2 arm; grade 30 L stands;
  note OL returns 4 starters — the under thesis is QB/roster, not trench).
- **Navy under: CAUTION.** Sweep corrected our premise: Horvath GRADUATED; Woodson
  is the successor with strong relief tape (103 yds/2 TD vs USF, 101 vs ND). The
  loud-arm under partly reflects Horvath's departure the dossier already priced.
- **Ohio under: reinforced** (2nd HC change in a year, 5 returning starters, QB
  unresolved). **Troy under: softened** (two returning QBs with production; DL adds).
- **BC O3.5 (F1): viable** — O'Brien has McKenzie (D2 GLIAC POY) as presumptive
  QB1; consensus-carried thesis unaffected.
- **SHSU over: supported** (Locke healthier, 40+ returners, Longo Y2).
  **Charlotte over: pending** (3-way QB incl. ACL recovery). **ULM/GaState/ODU/WSU:
  thin/pending** (WSU 3-way explicitly unnamed; ODU lost SBC POY QB to Wisconsin,
  54 new players).

## Hygiene debt (pre-existing, disclosed)

grades_check fails field-wide at HEAD (planned-vs-final declarations and
grades_detail blocks out of sync since the v2 regen era — e.g. Wyoming, Ohio State
fail identically with no local changes). final_pass's own hard validation passes.
Queue a one-time metadata resync; does not block builds.

## Camp sweep 2 queue (mid-August; carried forward)

Named re-verifications: UTEP Schuchts (dossier GONE-research vs yr4 default),
EMU Devereaux (RETURNS yr4-override, May-print — whole WRTE grade leans on him),
ECU QB naming, UNLV Arnold/Orji, Miami (OH) QB1.

Eligibility-cluster verifications (from two-deep uncertainty census 2026-07-31,
pipeline/research/twodeep_uncertainty_census.py — May-print yr4-override starters
concentrated on held OVERS, adverse direction if any fail to appear in August):

- **ECU (O7.5 held):** defensive spine is 5–6 override/ambiguous names — Wilk
  (639), TyMir Brown (598), D. Wilson LB (532), Robinson DL (407), Jean (419),
  Merrell (347). Confirm all on the August roster/depth chart.
- **Rutgers (O4.5 held):** dossier's own words — "the yr4-skew cluster
  concentrates here": OL Asamoah (849), Needham (751), plus medical/low-tape
  Langsdale, Chin, Salami; DL Angoy (332), Griffin (305), Blue-Eli. Confirm the
  projected five.
- Second tier: Oregon State Voltin (435)/Schuster (212)/R. Davis (131); KSU
  Hopson (765)/Jones (472) (note: KSU board number is override-pinned, so grade
  impact only); Buffalo Gathings (379); Nevada Vaughan/Williams. Wisconsin
  Tyrell Henry has no dossier grade line (WRTE/returner, class-4) — confirm
  status and whether he was graded.

## Screen status

Both rule-doc gates now satisfied (sweep integrated; UNLV/Miami-OH re-reads done).
Screen can run on the rebuilt board any time; final qualification requires owner's
current line capture.
