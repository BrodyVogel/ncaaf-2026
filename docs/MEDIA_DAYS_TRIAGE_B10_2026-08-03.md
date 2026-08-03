# Big Ten media-days triage — 2026-08-03

Source: `data/media_days/B10_2026_media_days.md` (event July 28–30, Hilton Chicago —
post-dates our 2026-07-12 baseline, so podium content is genuinely new; the underlying
offseason facts largely are not). Method + decision rules R1–R4:
`docs/MEDIA_DAYS_TRIAGE_B12_2026-07-21.md`. Grader: Fable, per owner directive
("incorporate it the same way we did all the others").

**Outcome: 0 grade changes, 0 confidence changes, 0 schedule/data fixes,
3 digest-conflict resolutions from our own records, 5 watch-list notes.**
`final_pass` NOT run — no input changed, so boards/payload/artifact/tracker
remain current. All 19 open bets unchanged by this digest.

This is the B12 pattern repeating one level up: the event post-dates the baseline,
but every gradeable fact under it (coaching changes, portal moves, QB rooms) was
already in the snapshot layer. What the podium added was color, race timing, and
league business — none of it clears R1–R3.

## Digest conflicts RESOLVED by our records (feed back to source log)

1. **Michigan OL status (digest conflict #3).** Our dossier + META are unambiguous:
   Sprague (72.6/740, All-B10 soph) and Guarnera (71.3/710) carry documented
   **portal-withdrawal overrides** — they entered the portal and withdrew, which is
   exactly why one SI item shows "departed" and another shows the room intact.
   Babalola (5\*, back from injury, no tape) and Frazier also return. Five
   withdrawal overrides adjudicated in `snapshots/Michigan`. **All four on roster;
   graded room stands.**
2. **Illinois DC identity (digest gap).** Digest guessed "DC Aaron Henry comments"
   absent. Our META: **Henry left for Notre Dame; new DC is Hauck (Montana),
   installing the 3-3-5** the digest reports. The scheme note is confirmation; the
   digest's staffing premise was stale.
3. **Nebraska "three new coordinators" (single-source Yahoo [REPORTED]).** Our META:
   **DC Aurich new (4-2-5, as digest says); OC Holgorsen CONTINUES;** new OL coach
   Wade is position staff, not a coordinator. R3: single-source claim vs our
   documented continuity — our record stands. (Digest's 4-2-5/Aurich core is
   confirmation.)

## Per-team dispositions (18)

| Team | Digest highlight | Cross-check vs our files | Disposition |
|---|---|---|---|
| Illinois | Houser "locked in"; new 3-3-5; LB coverage SPARSE | QB 70 M has Houser w/ ECU tape (84.0/473); DC change in META (Hauck, not Henry); LB 'L' stays — digest itself reports nothing on the unit (R1: absence ≠ signal) | CONFIRMATION + resolution #2 |
| Indiana | Hoover named; "bigger gun"; Marsh ~6–7 mo into recovery | QB 74 M has Hoover (76.8/480 TCU, +6 B12 offset); Marsh in WRTE room (67.5/386 ex-MSU) | CONFIRMATION + **WATCH W1** (Marsh recovery timeline — single [REPORTED]; camp sweep 2 confirms availability) |
| Iowa | QB OPEN (Brown/Hecklinski), Aug resolution; DL lost 7 of 8; "new ST unit" | QB 32 **L** priced on exactly this race ("winner unnamed"); Bessinger already in graded depth ("true FR 4-star — no snaps") — the podium "just added" framing is relative, not new composition (R1); DL/LB/ST L's stand | CONFIRMATION — all four L's hold per R2 (races/tape unresolved) |
| Maryland | Washington returns; new OC Trickett; WR-room coverage SPARSE | QB 56 M priced on Washington's exact line (71.3/519); Trickett in META; WR gap honest in our grades | CONFIRMATION |
| Michigan | Whittingham/Beck; Underwood "cannon"; LB SPARSE; OL conflict | coach_change=True ×1.13 applied ("Moore FIRED (scandal); Whittingham hired pre-bowl"); QB 56 M priced; OL conflict resolved from our overrides (#1); LB thin per digest → no action | CONFIRMATION + resolution #1 |
| Michigan State | Fitzgerald; Milivojevic named; Chiles → NU | coach_change=True ×1.13 applied; QB 53 M priced on Milivojevic's 4-start line; Chiles exit priced (he's in NU's graded battle) | CONFIRMATION |
| Minnesota | Only full-continuity program; Lindsey returns | META documents exactly this (Fleck yr 10, Harbaugh yr 4, Collins yr 2); QB 58 M priced | CONFIRMATION |
| Nebraska | Colandrea front-runner, no QB in Chicago; Raiola → Oregon; Odem added | QB 62 M: Raiola GONE, Colandrea IN at 89.9/514 UNLV (MWC −7 → 82.9, ~p77), Lateef #2, Kaelin back — the podium confirmed our exact room; Odem priced ("only blue-chipper on the two-deep") | CONFIRMATION + resolution #3 + **WATCH W2** (open race formally; grade already assumes Colandrea — Rhule naming anyone else in camp would be news) |
| Northwestern | QB open (Chiles/Marchiol/Boe); Chip Kelly OC | QB 52 M priced on this exact battle incl. Kelly recruiting Chiles; McGarigle retained per META | CONFIRMATION + **WATCH W3** (camp naming) |
| Ohio State | Sayin; lost 12 starters, added 17 | QB 91 H; OC Arthur Smith change in META (digest missed it — we're ahead); portal ledger priced | CONFIRMATION |
| Oregon | Moore returned; Stein/Lupoi out; Raiola backup | QB 89 H; META has replacements (Mehringer int., DC Hampton) — consistent with digest's departures; Raiola cross-verified in dossier with the QB1-mixing mechanism note; $55M figure = headline color (R3) | CONFIRMATION |
| Penn State | Campbell era; Becht named; DC Lynn; ~40 transfers | coach_change=True ×1.13 applied (Franklin fired Oct 2025); QB 72 H priced Becht at 86.0 adj; Lynn cross-verified against USC's META (departure side) | CONFIRMATION |
| Purdue | Browne returns; DC Kane; STC Shibest; Carmicle limited | QB 46 M priced Browne's exact line incl. "dead last" rating; Kane in META; Shibest = STC color (no model input, HC-only ×1.13 rule); freshman DE availability immaterial | CONFIRMATION |
| Rutgers | QB OPEN (Lonergan/Surace), Schiano names late; DC Johansen; OL sparse | QB 55 M graded on the battle w/ Lonergan's BC tape (72.8 adj); Johansen in META (64-day search); UMass opener consistent with schedule data | CONFIRMATION + **WATCH W4** (Schiano's own timeline: naming expected ~post-first-scrimmage; camp sweep 2 catches it) |
| UCLA | Chesney; Iamaleava returned; 42+ transfers | coach_change=True ×1.13 applied (Foster fired 0-3, interim documented); QB 55 M priced incl. the concussion-context line | CONFIRMATION |
| USC | Maiava; 15 starters back; Patterson defense | QB 80 H priced; Patterson + STC Ekeler in META; Lynn→PSU consistent both directions | CONFIRMATION |
| Washington | Williams; zero staff departures; Manu back from ACL; Hatchett wrists | QB 72 H priced incl. the portal-attempt saga; Manu RETURNS with yr4 override + LB volume caution already in dossier; "58 returners" consistent | CONFIRMATION |
| Wisconsin | Joseph QB1, no QB brought; 33-transfer overhaul; Mateos OL | QB 57 M priced Joseph (SBC −1 → 77.9, ~p68) incl. OPOY honors; Mateos + first full-time STC in META; F3-relevant churn already in rp table | CONFIRMATION |

## Watch list

- **W1 (Indiana):** Marsh recovery "~6–7 months in" — availability for September
  unverified; single [REPORTED]. Camp sweep 2.
- **W2 (Nebraska):** QB formally open; our 62 M assumes Colandrea. Any non-Colandrea
  naming = revisit. (R3 note: no open bet touched.)
- **W3 (Northwestern):** QB naming during camp; grade already reflects the battle.
- **W4 (Rutgers):** Schiano's self-declared naming window (post-first-scrimmage,
  ~mid-Aug). We hold 0.80u Rutgers O4.5 — R3 motivated-reasoning guard applies to
  any bullish read of the race; the grade assumes the battle, not a winner.
- **W5 (poll):** Cleveland.com first-place split unresolved among aggregators. No
  model input either way (we do not consume polls); log-only.

## Impact

**None.** Zero input changes → no rebuild → zero movers. The tracker, payload,
artifact, and 2026-08-03 corrected screen all remain current. For the held B10
positions (Rutgers O4.5 0.80u, Illinois U7.5 0.65u, Wisconsin U6.5 0.60u) and the
active slate candidates (Maryland O4.5, Michigan U8.5), the digest is confirmation
throughout — nothing here changes a probability, band, tag, or size.

## Queue

- Pac-12 media-days digest (last outstanding conference) — will batch with any
  camp-sweep-2 deltas into the next `final_pass` rebuild.
- Camp sweep 2 (~mid-Aug): W1–W4 above + the 4 open QB races (Rutgers, Iowa,
  Northwestern, Nebraska) + the 13 open rooms carried from batch 1.
- Owner items standing: fresh prices before any new bet (stored lines are 07-19);
  Bet365 OSU-total-definition check.
