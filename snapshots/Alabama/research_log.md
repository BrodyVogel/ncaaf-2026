# Alabama — research log (2026)

## Build metadata
- Build date: 2026-07-18. Assembler: pipeline v (see META assembler_git_rev).
- Conference: SEC (P4). SEC Batch 1, team 1/4 (alphabetical).
- Anchor-blind build: assembler read NO rating/market/anchor values.

## Sources consulted (R16 — THREE-SOURCE for P4)
1. Athlon 2026 — SEC, p.3 (readable text layer via `pdftotext -layout`). Header-verified
   "ALABAMA CRIMSON TIDE." Full depth chart + Final Analysis + opposing-coach scouting.
2. Phil Steele 2026 — SEC, p.4 (page-image read via `pdftoppm -r 200 -png`; text layer
   jumbled). Cross-verified the declare list + OL/DL exodus + secondary retention.
3. Pick Six 2026 — SEC (Ciancia; extracted to /home/claude/p6_sec.txt, Alabama editorial
   lines 763-866). Facts-only per R16: pulled went-pro/declares/transfers/retentions/
   injuries; rankings + Game-Grader NOT recorded into any grade.
- CFBD 2026-07-12 pull (roster + PFF '25 grades + portal feeds). 2026 CFBD feeds not yet
  published — yr4 adjudicated from roster_2025 class-year vs the three 2026 magazine charts.

## BLINDING DISCLOSURE (important — honesty over convenience)
- During the P6 facts-only extraction, Alabama's P6 ranking header was INCIDENTALLY
  VISIBLE at the top of its editorial ("ALABAMA #7(TIE) #16"). This exposure is disclosed
  here. It was NOT used: grades were set by percentile-mapping the projected two-deep's
  PFF-adjusted grades against exemplars, and the full anchor values remain unconsulted.
  Alabama is not among the six teams flagged in SEC_PAGE_MAP.md for the incidental
  ordering glimpse (Georgia/Oklahoma/Texas/Auburn/Missouri/S. Carolina); this is a
  separate, team-local ranking exposure logged for completeness.

## Adjudication notes
- Three junior NFL declares (Simpson/Proctor/Brailsford) are invisible to both the yr4
  class-year list and the portal feed — added via nfl_declare_confirmed, each print-verified
  (Simpson 3-source; Proctor/Brailsford Athlon+P6). See META known_name_exceptions.
- yr4 gate: Jah-Marien Latham resolved as a RETURN (7th season) ONLY on P6's explicit
  "hopes to get Jah-Marien Latham back" naming (R15 satisfied). All other yr4 conflicts
  (Miller/Cuevas/Overton/Keenan/Bernard/Jefferson/Lawson/Hill-Green/Jackson) resolved as
  EXPIRED/GONE — none named returning; several print-confirmed departed.
- Rico Scott (WR): portal-out feed w/ NO destination → withdrawal override on Athlon's
  WR7 depth-chart listing (R15: named-in-chart return). Grade-neutral (below two-deep).
- Disposition gate: 40 rows, 0 to adjudicate, 0 errors after the Rico Scott resolution.

## Grade rationale summary
- Planned: QB 48 L / RB 48 M / WRTE 54 M / OL 46 L / DL 46 M / LB 48 M / DB 76 H / ST 48 M
  (sum 414). The secondary (DB 76) is the lone carry-over of '25's ceiling (COV p95, four
  returning starters incl. All-American Hubbard). Everything else is reset to a '26
  projection after historic NFL/portal attrition — matching the 3-source narrative of "a
  downgrade in every position room aside from the elite secondary" (P6).
- SEC offsets applied to returning tape at face on modest cells (QB/WRTE/DB) and WEIGHTED
  DOWN on the large over-inflating cells (OL +13.45 / LB +14.01 / RB +10.17) and on
  small-sample producers; arrivals use their origin-league cells (B10 DL weighted down).
