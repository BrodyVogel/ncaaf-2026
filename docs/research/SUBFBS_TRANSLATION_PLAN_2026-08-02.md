# Sub-FBS translation program — data migration + research plan (2026-08-02)

Owner supplied PFF player-level grades for FCS (2021–2025, complete: 30
files) and D2/D3 (2021–2025; 4 of 30 staged before the device bridge
dropped — remainder queued for next desktop connection). Migrated to
data/pff_history/fcs/ and data/pff_history/d2d3/. Schema matches the FBS
files exactly (player, team_name, position, player_game_count,
grades_offense/defense) — every existing loader works unmodified.

## Feasibility census (run at migration)

- **Historical translation panel: 1,035 FCS→FBS pairs** with ≥6 games of
  tape on both sides (2021→22: 151; 2022→23: 235; 2023→24: 240; **2024→25:
  409** — the owner's "more than ever" is literally true; the class nearly
  doubled last cycle). Larger than S16's entire 790-pair panel.
- **2026 coverage: 220 of 427 flagged sub-FBS two-deep entrants (52%) have
  ≥4 games of 2025 FCS tape**, including **88 projected starters** (e.g.
  App State WR Lofton 87.3/12gm, Boise S Tillmon 79.5/15, BGSU CB Braxton
  73.8/12, Buffalo LB Cheshire 67.6/10). The uncovered 48% = D2/D3 (files
  partially staged), JuCo/NAIA (no PFF), name-mismatches, and <4-game
  seasons.
- FCS coverage: ~129 teams/yr, ~5,200 defense rows/yr — full-population,
  not a sample.

## Phase A — S17: the FCS→FBS translation study (registered before fitting)

Panel: the 1,035 pairs (fold = origin year). Target: FBS-year PFF grade.
Design mirrors S16 with the lessons applied up front:
- **L1 baseline:** grade_FBS ~ grade_FCS + position-group. The raw
  translation curve (expect: slope <1, large level drop — context
  inflation at maximum gap).
- **L2 origin-strength within FCS (the S16 within-class lesson):** origin
  proxy = FCS team-mean grade (computable from these files; no SP+ exists
  for FCS). S16 found within-class origin strength matters MOST where the
  quality range is widest — FCS spans NDSU-to-MVSU, the widest range in
  the sport. Expect this to be the largest term.
- **L3 position groups:** S16 predicts trench/back-7 carry the context
  discount and skill travels; QB handled separately (S10 prior).
- **L4 destination class:** G5 vs P4 landing spots (most 2026 exposure is
  G5 — the owner's edge thesis).
- Bars: house standard (|t|≥2, ΔR², LOYO by origin year). December scores
  the 2026 cohort as the out-of-sample fold.

## Phase B — 2026 integration (the owner's ask: improve THESE grades)

On S17 passing bars: compute model projections for the 220 matched
players; diff vs the current v1 qualitative brackets inside their unit
grades; **targeted adjudication of material disagreements** (TE-sweep /
S16-audit pattern — case reads, normal adjudication rows, regen,
repopulate under the owner's accuracy waiver). Priority order: held teams
first (Buffalo has multiple matched contributors; BGSU, Nevada, ECU
likely), then heaviest-exposure G5 (UTEP 16, UMass 14, Wyoming 14), then
field. The 88 matched projected starters are the material core.

## Phase C — bonus integration: tape-based FCS opponent ratings

These files price the OTHER side of FCS games too: team-mean grades per
FCS team-year → a data-driven replacement for the tier-guess FCS table
(the Tarleton class of error, killed at the source). Cross-validated
against the August market-calibration protocol (two independent
instruments). Also gives the win engine real ratings for all ~100 FCS
opponents instead of five tiers.

## Phase D — remainder

D2/D3: stage the 26 remaining files at next connection; same pipeline;
expect thinner coverage (D2/D3 rosters are smaller PFF footprint). JuCo/
NAIA stay dossier-bracketed (no tape exists); their brackets get the
December calibration scoring like everything else.

## Sequencing

S17 registration+run fits one session block. Phase B sizing depends on
S17's disagreement count (expect 15–30 case reads). Phase C is a
half-block, independent of S17. Recommended order: S17 → Phase C →
Phase B — the translation evidence should exist before any grade moves,
and the FCS table upgrade helps every FBS-FCS game immediately.
