# Iowa — research log (all sources, incl. dead ends) — 2026-07-14

## Magazines (staged device files, extracted to /tmp workspace, distilled into magazines.md)
1. Phil Steele 2026 — Iowa section (B10 pp. 10–16 of extract). OCR noisy; load-bearing numbers
   (returning-starters box, portal box, QB career lines, Hecklinski PS#51) VERIFIED against rendered
   page images (ps_iowa_p10-10.png, ps_retbox-10.png, ps_lineup-10.png).
2. Athlon 2026 — Iowa page (clean text): full unit write-ups, depth chart, opposing-coach scouting quote.
3. Pick Six 2026 — Iowa section pp. 16–19 (verbatim): unit assessments incl. opponent-adjusted defense
   context (#7/68 P4; #1 pass D). Team-level outlook sentence + its team-level number EXCLUDED (blinding v2).
   NOTE: raw magazine extracts kept OUT of snapshot (contain forbidden forecast numbers); only distilled,
   blinding-compliant facts recorded here.

## Authoritative depth chart
4. OurLads Iowa two-deep, dated 06/15/2026 — full starter/backup capture; cross-checked vs Athlon depth
   chart + spring reports. Five open battles flagged: QB, RG, WLB, CB2, P. OurLads "TR" tag on Van Kekerix
   determined ERRONEOUS (2022 HS signee — official roster + 4 signing-day articles).

## News/beat sweep (fetched OK)
5. KCRG 4/9/26 (Collin Davies) — spring practice: QB reps even; Pieper→C w/ teammate quotes; Diaz praise.
6. The Gazette 4/26/26 (Madison Hricik) — spring game QB numbers (Hecklinski 10-22, Brown 3-10), Ferentz
   timeline quotes, WR injury list.
7. Dear Old Gold 4/27/26 (Jordan Underwood) — final-practice takeaways: QB battle detail, KJ Parker
   breakout, DL interior "problematic," Hawthorne MCL.
8. Dear Old Gold 5/11/26 — Klatt unit-level OL concern (his team rank NOT recorded).
9. SI 4/29/26 (Mitchell Corcoran) — NFL-departure replacement map w/ 2025 stats.
10. SI 1/16/26 (Jordon Lawrenz) — portal-add valuations (T.Brown #1 w/ P4 offer list; Styles PFF 89.1;
    Phillips PFF 92.8).
11. Hawk Fanatic 1/28/26 (Pat Harty) — all-16 portal bios w/ stats.
12. Hawkeyes Wire 6/1/26 (Zach Hiney) — QB room preview (Hecklinski projected starter, sizes, depth).
13. SI 6/10/26 (Riley Donald) — ST overhaul detail (Ozick career numbers, Buhr, P battle, Polizzi).
14. SI 7/7/26 (Riley Donald) — position-group strength ranking (attributed unit-level; legal).
15. hawkeyesports.com official roster — Van Kekerix class/origin verification.
16. Signing-day coverage (Sioux City Journal etc.) — Van Kekerix 2022 HS signee confirmation.

## Dead ends (logged per procedure §7)
- hawkcentral.com robots-disallowed (www + eu): Leistikow spring-scrimmage "8 thoughts" (4/25),
  practice notes (4/9), portal evaluation (1/13), secondary progress (5/26) — headlines only.
- blackheartgoldpants.com robots-disallowed: QB position preview; spring takeaways. Yahoo syndication 404.
- dailyiowan.com 403 (x2): spring takeaways (4/26); Lester QB-battle piece (4/26).
- 247sports post-spring depth-chart article: VIP paywall.
- thegazette.com Ferentz-spring-thoughts URL: 429 throttled (other Gazette URL fetched OK).
- Sideline player valuations: no Iowa QB/RB/WR entries surfaced in accessible sweeps — mosaic built from
  SI portal ranking + Hawk Fanatic bios + magazine assessments instead (procedure fallback).

## Corrections made during research
- snapshot pff arrivals name-collision: dropped Clemson WR "Tyler Brown," Colorado G "Tyler Brown,"
  Oklahoma DI "Trent Wilson" (kept JMU rows). Builder patched to require name+origin match
  (pipeline/snapshot_build.py, 2026-07-14) and to refuse re-running over an existing snapshot.
- Olagbaju origin discrepancy noted (CFBD: North Dakota vs Hawk Fanatic: St. Thomas) — depth player, confidence L.
- CFBD portal-in = 15 vs program "record 16": Everitt (Australia) is an international signee, not portal. Resolved.
- Phil Steele portal box (17 in/13 out) counts non-scholarship moves; CFBD/beat consensus = 16 adds. Noted.

## Loop-until-dry status
QB/OL/DL/DB/ST: 3+ consecutive searches returned no new load-bearing facts (final sweeps 7/14). DRY.
RB/WRTE/LB: coverage saturated across 6+ sources; remaining unknowns are battles that resolve in August
(QB1, RG, WLB, CB2, P) — flagged in two-deep, not researchable further today. DRY.
