# Ole Miss — research log (2026)

## Build metadata
- Build date: 2026-07-18. Conference: SEC (P4). SEC Batch 3, team 3/4 (alphabetical).
- Anchor-blind build: assembler read NO rating/market/anchor values.

## Sources consulted (R16 — THREE-SOURCE for P4)
1. Athlon 2026 — SEC, p.13 (readable text layer). Header-verified "OLE MISS REBELS."
2. Phil Steele 2026 — SEC, p.6 (page-image read via pdftoppm -r 150). Header-verified "MISSISSIPPI
   REBELS" (QB Chambliss + RB Lacy photos; Golding "1st Year / 1st Overall FBS"; 13-2). Corroborated
   the Chambliss return, the tackle losses, and the reloaded defense.
3. Pick Six 2026 — SEC (Ciancia; extracted to /home/claude/p6_sec.txt, Ole Miss editorial lines
   336-442). Facts-only per R16. Decisive on the Golding promotion + Baker OC hire, the WR reload,
   the 8-four-star D haul, and Chambliss's bonus-year context. Rankings NOT recorded.
- CFBD 2026-07-12 pull (roster + PFF '25 grades + portal feeds).

## DATA NOTE
- The team-level as-played percentile row is UNAVAILABLE for Ole Miss in this pull (a name-map quirk,
  the SacSt/NDSU pattern). The per-player PFF grades ARE present (the shadow proxy computed), so the
  unit grades use those + the magazine context. Documented in META known_gaps + the dossier.

## BLINDING NOTE
- Standard blinding v2. Ole Miss is NOT among the six teams flagged in SEC_PAGE_MAP.md for an
  incidental P6-ranking glimpse, and no Ole Miss ranking was seen during extraction.

## Adjudication notes
- Golding is a NEW HC (Kiffin -> LSU) -> coach_change TRUE, band x1.13 (internal-continuity + the
  "80% same scheme" OC are mitigants, but the rule is binary on HC changes).
- Trinidad Chambliss (QB, yr4) - RETURNS via a court-won bonus year; named returning by all three
  sources -> yr4_return_override (R15). Grade-critical (the elite QB). Delano Townsend (G) - portal-
  none but named a returning interior starter -> portal_withdrawal_override (R15).
- CROSS-BUILD ties (extensive, all consistent): Umanmielen + Dottery -> LSU; Simmons + Lee -> Missouri;
  Renaud (Alabama) + Curne (LSU) + Fields/Crawford (Auburn) -> Ole Miss.
- Disposition gate: 36 rows, 0 to adjudicate, 0 errors.

## Grade rationale summary
- Planned: QB 70 M / RB 68 M / WRTE 56 M / OL 54 M / DL 60 M / LB 58 M / DB 56 M / ST 62 M
  (sum 484). An AP-#3 team that retained an ELITE spine through the Kiffin upheaval - a Heisman-favorite
  QB (Chambliss) + an All-America RB (Lacy) + a strong reloaded D (Echoles/Perkins + 8 four-star
  transfers) + an elite kicker - with the WR room + both OL tackles as the reloads under a first-year
  (internal) staff. Calibrated vs the board's elite tier. Band x1.13 (HC change).
- SEC offsets on returning tape (big cells weighted down); the #2 transfer haul on origin cells
  (Auburn/SEC, Michigan State/B10, Syracuse/ACC, LSU/SEC, Oregon/B10, Colorado/B12, Baylor/B12, etc.).
