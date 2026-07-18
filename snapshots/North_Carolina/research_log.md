# North Carolina — research log

- 2026-07-18 snapshot_build "North Carolina": ACC Batch 4 team 1/4. pulls=10, pff=8,
  roster25=109, portal 20 in / 31 out (MASSIVE), games=12. 4-8 (2-6 ACC).
- 2026-07-18 magazines: Athlon ACC p.11 (header-verified, readable) + PS ACC p.14
  (coach + roster + departures page-image read). Blinding v2.
- 2026-07-18 COACH: FALSE. Bill Belichick Year 2 (PS "2nd Yr Here"; coached '25). Band
  x1.00. Verified BOTH. NEW OC Bobby Petrino ('26); DC Steve Belichick returns.
- 2026-07-18 OFFSET: ACC positive on returning tape; arrivals on origin cells. B10/SEC/
  FCS arrivals handled per cell / evidence-only.
- 2026-07-18 DISPOSITION GATE - massive churn:
  * QB Lopez ('25 starter) -> Wake; rebuilt with Edwards Jr (Wisconsin/Maryland) + O'Neill (A&M).
  * DL anchor Abou Jaoude (10.5 sk) RETURNS; lost Thompson (-> Louisville), Mims (-> A&M).
  * LB GUTTED: House (-> Ark), Simpson (yr4), Gbayor (-> FSU) all gone.
  * OL: all 5 starters gone -> FCS/transfer rebuild.
  * DB: deep veteran corps returns.
  * yr4 KEPT (veteran returners): Hall/Lindberg (OL), Allen/Gibson/Dixon (DB), Vilbert (DL).
  * GATE: Vilbert + Dixon flagged yr4-conflict -> added to yr4 overrides (veteran returners
    per both mags' 'returning core' framing).
  * Cross-build confirmed: Thompson->Louisville, Gbayor->FSU, Gause+White->NC State, Lopez->Wake.
  * ledger --check: 37 rows, 0 to adjudicate, 0 errors. departure_check: clean.
- 2026-07-18 grades (percentile-mapped; DEF the relative strength [Abou Jaoude anchor +
  deep DB] graded M; OFFENSE rebuilt [QB unsettled, OL all-new, LB gutted] graded L/low):
  QB 48 L | RB 50 | WRTE 48 | OL 44 | DL 54 | LB 40 L | DB 54 | ST 46. Sum 384.
- 2026-07-18 gates: disposition_ledger --write + --check, departure_check, blinding_check,
  grades_check, post-grades departure_check - below.
- 2026-07-18 P6 RETRO-QA (post-freeze correction): Pick Six ACC cross-check. CATCH:
  Allen + Gibson + Dixon (DB) + Vilbert (DL) yr4 overrides were WRONG - my "both list
  as returning" claims were false (the Athlon defense chart, re-read, lists Patterson/
  Willie/Cost/Bryson/Smith - none of the four; P6: "four starters are gone from the
  secondary... Cost is the only full-time starter back" + "end Smith Vilbert graduated").
  All four removed; Willie (chart CB) + Hoilette (chart DE, was mis-attributed as OL at
  build) added. DL 54->52, DB 54->48. Rating +1.84 -> +1.58 (rank 58->59). Gates clean.
  P6 CORROBORATED: Abou Jaoude "retained its top star... poised for All-ACC run," LB
  gutting (House/Gbayor 4-star transfers out), Seelman/McDonald arrivals, QB battle.
