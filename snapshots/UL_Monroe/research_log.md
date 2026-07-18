# UL Monroe — research log (process + exposure disclosures)

## Sources consulted
- Athlon 2026 SBC p16 (readable text layer): full depth chart + prose + scout quote (PRIMARY).
- Phil Steele 2026 SBC (searchable): SBC dedicated-page text layer GARBLED - conference-level cross-check only.
- CFBD pulls: roster_2025 (102), portal in/out (20/17), PFF unit tables (under the alias 'LA MONROE').

## DATA GAP (flagged for FORWARD_FLAGS)
- The PFF TEAM-PERCENTILE row did NOT match: ULM's PFF data is under 'LA MONROE' while the roster feed uses
  'UL Monroe', so team_dump reported 'NO ROW' and the shadow proxy is all-None. The PER-PLAYER PFF grades ARE
  present (under LA MONROE) and were used for grading; only the team-level percentile CONTEXT is unavailable.
  FIX: add 'LA MONROE' -> 'UL Monroe' to the PFF alias map (a name_map task, not re-grade-blocking here).

## Blinding (v2)
- Assembler read no rating/market/anchor data. Magazines.md facts-only.
- DISCLOSED: Athlon NF131 / Sun Belt West 7 incidentally visible - logged, NOT used.
- G5 2-source; PS unusable at name level -> Athlon depth chart + scout + the PFF player grades are load-bearing.

## Disposition (heavy churn; a bottom-tier rebuild)
- Grade-critical: ALL the top graders left - RB McReynolds (87.6 -> UAB) + Palmer-Smith (83.6, yr4); DL Howell
  (81.4, yr4); CB Godsey (76.9, yr4). The returning core is the LB room (Flemmings 77.9 + Ross 71.4) + Armenta
  + Trujillo + Vinson + a couple DL.
- yr4 RETURN overrides: Cliff Mosley + Levontae Jacobs (Athlon-named DL). departure_confirmed_research: the yr4
  top-graders (Palmer-Smith, Howell, Godsey, Pullen, Ester). portal_departure_confirmed: McBroom, Wells,
  Hamlin, Canterbury (portal->None). feed-gap arrival: Chaney Jr. (Louisville/Miami RB).
- Established SBC team -> returning tape on SBC cells. Arrivals on origin (Chaney Louisville/Miami-P4; Anderson
  Memphis-AAC; Rue UTEP-CUSA; Murray Cal-P4; the juco adds = no cell).

## Grade calibration note
- No as-played percentile line, so grading leaned on the per-player PFF grades + Athlon detail. ULM is a
  bottom-tier SBC team (Athlon's lowest NF): a game-manager QB + a decent returning LB core, but heavy rebuilds
  at RB/OL/DL/DB. DB marked LOW-confidence (four new faces).
