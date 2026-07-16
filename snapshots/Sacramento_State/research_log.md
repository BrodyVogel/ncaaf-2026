# Sacramento State — research log

- 2026-07-16 snapshot_build "Sacramento State": pulls=10, pff=4 unit files
  (7 arrival rows TOTAL - no FCS tape in the FBS dataset), roster25=112,
  portal 25 in / 22 out. FBS NEWCOMER: not in the 136-team league percentile
  file; ledger universe nearly empty; proxy ALL-VOID (8/8 None - project
  first, artifact #43).
- 2026-07-16 magazines: Athlon MAC p.12 (header-verified), PS MAC pdf p.14
  LEFT PANEL (banner visually verified; right panel = North Dakota State).
  Blinding v2 (Athlon FORECAST 136 + PS "rebuilding year" call retained as
  prose-only where factual).
- 2026-07-16 COACH MULTIPLIER: coach_change=TRUE (x1.13) - Alonzo Carter yr
  1 (first career HC job; Marion one-and-done; 2nd HC change in 2 yrs).
  Timing trap documented: FBS invite came after signing day + portal close;
  13+ JC adds post-spring.
- 2026-07-16 adjudications: HOUSTON portal-return override STAYS
  (Immediate/no-dest vs BOTH prints - he is the Athlon page photo); CURTIS
  Withdrawn override STAYS (both prints RB1; injury monitor); THORNTON
  resolved as 2026 arrival from Portland State (Athlon* right, PS caps
  misled); no-dest GONE x2 (Burkart, Johnson-Burrell); 29 feed-yr4 names
  checked against the two-deep (no conflicts; Mullican clean); name
  variants logged (Ellijah/Elijah Washington, Matt/Matthew Coleman).
- 2026-07-16 cross-refs: CLOSED against frozen snapshots - Watts->Washington
  (their two-deep; UW flag), Blank<-UCLA (out-feed), Howard<-Wisconsin
  (out-feed + arrival row; Athlon spring-starter), Robinson->Central
  Michigan (two-deep + META; CMU flag), C.Williams->Maryland (in-feed;
  Maryland now has TWO MAC-adjacent QB pickups incl. Kargman),
  Akui->Rice (in-feed), Henderson II + Campbell + J.Smith + Soto ->
  COLORADO (Henderson in their two-deep; four-player pipeline). Forward
  flags (unbuilt): Oliver->San Diego State, Lee->Middle Tennessee,
  Mosley+Hampsten->Fresno State, McGlothen->San Jose State, McKenzie->UAB,
  Tenney->New Mexico, Gillespie->Nevada, Rashada->Mississippi State; in:
  Klemm<-Arizona State (built B12! zero tape - no retro), King<-Colorado
  (built - zero tape RS, no retro), Turner<-Illinois (built - DNP, no
  retro), Wallace<-Miami FL (unbuilt ACC), Moore<-Northern Illinois (fwd
  MWC), Chala+Thomas<-Fresno State (fwd), Godley+Soifua<-Weber State (FCS),
  Jeanty<-Lafayette (FCS), Washington<-Oregon State (fwd Pac-12; zero
  tape).
- 2026-07-16 offsets: only 7 FBS arrival rows carry cells (Conklin-Fresno,
  Howard-Wisc, Chala-Fresno, Moore-NIU, Silvera-USF, Thomas-Fresno,
  Rhaney-SDSU); ALL FCS/D2/JC production no-cell.
- 2026-07-16 planned grades: THREE project floors set on evidence (OL 8 new
  OL floor; WRTE 10 new WRTE floor; DB 10 near the FAU-6 global floor);
  4 L-units (QB/RB/DL/DB) -> conf x1.12 stacking with coach x1.13.
- 2026-07-16 gates: disposition_ledger --write, departure_check,
  blinding_check — results below.
- 2026-07-16 grades.json written + schema-validated (8/8); departure_check
  caught the Matt/Matthew Coleman cited-name form (Funk precedent) - fixed
  via known_name_exceptions; gates re-run clean.
- 2026-07-16 pilot_readout: FINAL -19.61 (r135/138), band ±7.59 = WIDEST OF
  THE PROJECT (coach 1.13 x conf 1.12 [4 L-units] stack). FPI winsorized
  AGAIN (-12.6 -> -15.3; FPI systematically kind to bad teams - 3rd FPI
  event). Dispersion 10.1 just under the flag. resid +1.42 = level +10.88 +
  shape -9.47. First build this round where grades are cooler than anchors
  on OFFENSE too (-0.74).
