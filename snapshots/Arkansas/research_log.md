# Arkansas — research log (2026)

## Build metadata
- Build date: 2026-07-18. Conference: SEC (P4). SEC Batch 1, team 2/4 (alphabetical).
- Anchor-blind build: assembler read NO rating/market/anchor values.

## Sources consulted (R16 — THREE-SOURCE for P4)
1. Athlon 2026 — SEC, p.4 (readable text layer). Header-verified "ARKANSAS RAZORBACKS."
   Full depth chart + Position Outlook + opposing-coach scouting.
2. Phil Steele 2026 — SEC, p.17 (page-image read via pdftoppm -r 150). Header-verified
   "ARKANSAS RAZORBACKS" (Russell photo, Silverfield "1st Year Here / 7th Overall," 2-10).
   Corroborated the QB battle, OL returners, DL transfer haul, and the K/P void.
3. Pick Six 2026 — SEC (Ciancia; extracted to /home/claude/p6_sec.txt, Arkansas editorial
   lines 1591-1665). Facts-only per R16: pulled went-pro/graduated/transfer/retention facts;
   rankings + Game-Grader NOT recorded into any grade.
- CFBD 2026-07-12 pull (roster + PFF '25 grades + portal feeds). yr4 adjudicated from
  roster_2025 class-year vs the three 2026 magazine charts.

## BLINDING DISCLOSURE
- During the P6 facts-only extraction, Arkansas' P6 ranking index line ("#16 ARKANSAS") was
  INCIDENTALLY VISIBLE. Disclosed here; NOT used. Grades were set by percentile-mapping the
  projected two-deep's PFF-adjusted grades against exemplars; full anchor values unconsulted.

## Adjudication notes
- Taylen Green (QB, the '25 offense engine) went pro — invisible to yr4 + portal feeds;
  added via nfl_declare_confirmed (P6 explicit + Athlon/PS chart-omission). GONE.
- Disposition gate conflicts resolved: Charlie Collins + Miguel Mitchell were portal-none in
  the feed but both named returning STARTERS by Athlon (and P6/PS) -> portal_withdrawal_overrides
  (R15). David Oke (yr4) named the NT starter in Athlon + PS -> yr4_return_override (R15).
  Danny Saili (portal-none, not named returning anywhere) -> portal_departure_confirmed (GONE,
  DL depth, grade-neutral).
- Disposition gate final: 35 rows, 0 to adjudicate, 0 errors.

## Grade rationale summary
- Planned: QB 42 L / RB 46 M / WRTE 44 M / OL 44 M / DL 48 M / LB 44 M / DB 48 M / ST 44 M
  (sum 360). A new-staff, near-total rebuild off a 2-10 base. The explosive '25 offense
  (RUN p99) is gutted (Green pro; Washington/Blake/Sharpe/Rohan Jones/Carmona graduated) and
  reloaded from LOWER tiers -> offense units 42-46. The historically bad defense (DEF p17,
  COV p7) gets a higher-upside portal transfusion -> DL 48 (All-SEC Rhodes anchor + KY edge
  Soles + 7 Top200 bodies) and DB 48 (All-AAC Johnson + Stoutmire + Mitchell). Wide band
  (coach change x1.13).
- SEC offsets applied to returning tape; big cells (OL/LB/RB) weighted down + small samples
  discounted; arrivals on origin cells (mostly G5/AAC/MWC = small-or-negative; FCS = no cell).
