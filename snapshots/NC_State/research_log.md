# NC State — research log

- 2026-07-18 snapshot_build "NC State" (dir NC_State): ACC Batch 3 team 4/4. pulls=10,
  pff=8, roster25=126, portal 20 in / 22 out, games=12. 8-5 (4-4 ACC).
- 2026-07-18 magazines: Athlon ACC p.12 (header-verified, readable) + PS ACC p.10
  (coach + roster + departures page-image read). Blinding v2.
- 2026-07-18 DATA NOTE: no percentile row for 'NC State' (pff key 'North Carolina
  State' mismatch) -> EVIDENCE-ONLY build off raw PFF unit tape + magazines; shadow
  proxy miscomputed (ignored).
- 2026-07-18 COACH: FALSE. Dave Doeren - PS "14th Year Here / 16th Overall." Band
  x1.00. Verified BOTH. OC Roper (2nd yr) + DC Eliot (2nd yr) return.
- 2026-07-18 OFFSET: ACC positive on returning tape; arrivals on origin cells. G5/
  inflated arrivals (Snow MAC, Dyson AAC, Nelson B10 +16.10, King Mack B10) weighted.
- 2026-07-18 DISPOSITION GATE - heavy talent drain:
  * PROVEN QB Bailey RETURNS (3,105 yds/25 TD, 3rd-yr starter).
  * yr4 elite GONE: Marshall (CB 89.8), Fordham (LB AA), Joly (TE), Grant (OL),
    Slone/Cleveland (DL).
  * RESEARCH-GONE: Sabastian Harsh (DE 86.7, best edge) - both mags omit; PS 'rebuilt
    unit, lose 4 starters'; not in feed/not yr4 -> departure_confirmed_research.
  * Portal out: Smothers (Texas), Rogers (Bama), Anderson (USC), Peak (SC), Soares (MSU).
  * GATE CATCH: Sean Brown (I'd listed returning) yr4-GONE (PS 'lose Brown') - removed.
  * 3 Miami FWD FLAGS CLOSED (Trader/Robinson/Aguirre - in-feed + Athlon verified).
  * ledger --check: 39 rows, 0 to adjudicate, 0 errors. departure_check: clean.
- 2026-07-18 grades (EVIDENCE-ONLY, off raw PFF tape; proven QB Bailey graded M;
  everything else modest-returning or transfer-reload; the two elite defenders
  [Marshall, Harsh] gone -> DL/LB graded L, WRTE gutted L): QB 54 | RB 56 | WRTE 42 L |
  OL 46 | DL 40 L | LB 42 L | DB 46 | ST 48. Sum 374.
- 2026-07-18 gates: disposition_ledger --write + --check, departure_check,
  blinding_check, grades_check, post-grades departure_check - below.
