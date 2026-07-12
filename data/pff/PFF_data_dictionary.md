# PFF NCAA 2025 Premium Stats — Data Dictionary

Machine-readable column definitions for the 27 PFF_*.csv player/team files. Built for agent lookup.

**How to use.** Look up a column under files[<csv>].columns[<column>].definition (unambiguous, in report context). Cross-tab columns are {bucket}_{base_metric}: resolve base under base_metrics and the qualifier under bucket_tokens. legends holds PFF's own verbatim abbreviation glossary per file.

**Sources.** Column names are ground-truth from CSV headers. Definitions compiled from the 27 PFF 'Key' images (OCR, verbatim in `legends`) plus standard definitions for export-only columns (EPA, snap counts, spikes, etc.).

**Grade scale.** All grades_* columns are PFF grades on a 0–100 scale (higher is better; ~60 average, 70+ good, 90+ elite).


## Common columns (in every player file)

- `player` — Player name
- `player_id` — PFF unique player identifier
- `position` — Player's listed position for the season (POS)
- `team_name` — Team the player played for
- `player_game_count` — Number of games in which the player appeared (#G)
- `franchise_id` — PFF unique team/franchise identifier

## Cross-tab bucket tokens

Cross-tab files name columns `{bucket}_{base_metric}` (e.g. `deep_btt_rate`). Bucket meanings:

- `left` — targeted to the left third of the field
- `center` — targeted to the center third of the field
- `right` — targeted to the right third of the field
- `behind_los` — thrown/caught behind the line of scrimmage
- `short` — thrown/caught 0–9 yards downfield
- `medium` — thrown/caught 10–19 yards downfield
- `deep` — thrown/caught 20+ yards downfield
- `man` — vs man coverage
- `zone` — vs zone coverage (or zone-scheme runs in run-blocking)
- `gap` — on gap/power-scheme run plays
- `true_pass_set` — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s)
- `lhs` — when rushing from the left side
- `rhs` — when rushing from the right side
- `no_screen` — on non-screen dropbacks
- `screen` — on screen passes
- `npa` — on non-play-action dropbacks
- `pa` — on play-action dropbacks
- `blitz` — vs a blitz (5+ rushers)
- `no_blitz` — vs no blitz
- `pressure` — on plays with pressure
- `no_pressure` — on plays with no pressure
- `less` — on dropbacks of 2.5 seconds or less in the pocket
- `more` — on dropbacks longer than 2.5 seconds in the pocket
- `base` — season total for this metric

## Files


### `PFF_2025_team_grades.csv` — Team Summaries (17 cols)

| column | definition |
|---|---|
| `TEAM` | Team name |
| `RECORD` | Win–loss record |
| `PF` | Points scored (PF) |
| `PA` | Points allowed (PA) |
| `OVER` | PFF grade, 0–100 (higher is better) — overall team performance (OVER) |
| `OFF` | PFF grade, 0–100 (higher is better) — offense (OFF) |
| `PASS` | PFF grade, 0–100 (higher is better) — passing (PASS) |
| `PBLK` | PFF grade, 0–100 (higher is better) — pass blocking (PBLK) |
| `RECV` | PFF grade, 0–100 (higher is better) — receiving (RECV) |
| `RUN` | PFF grade, 0–100 (higher is better) — rushing (RUN) |
| `RBLK` | PFF grade, 0–100 (higher is better) — run blocking (RBLK) |
| `DEF` | PFF grade, 0–100 (higher is better) — defense (DEF) |
| `RDEF` | PFF grade, 0–100 (higher is better) — run defense (RDEF) |
| `TACK` | PFF grade, 0–100 (higher is better) — tackling (TACK) |
| `PRSH` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) |
| `COV` | PFF grade, 0–100 (higher is better) — coverage (COV) |
| `SPEC` | PFF grade, 0–100 (higher is better) — special teams (SPEC) |

<details><summary>PFF key legend (verbatim)</summary>

- **PF**: Points Scored
- **OVER**: PFF Grade for Overall Performance (
- **PASS**: PFF Grade for Pass
- **RECV**: PFF Grade for Pass Routes
- **RBLK**: PFF Grade for Run Blocking
- **RDEF**: PFF Grade for Run Defense
- **PRSH**: PFF Grade for Pass Rush (
- **SPEC**: PFF Grade for Misc. Special Teams :
- **PA**: Points Allowed
- **OFF**: PFF Grade for Offense
- **PBLK**: PFF Grade for Pass Blocking
- **RUN**: PFF Grade for Rushing
- **DEF**: PFF Grade for Defense
- **TACK**: PFF Grade for Tackling
- **COV**: PFF Grade for Defensive Coverage against Receivers View offense, defense and special team reports

</details>

### `PFF_defense_coverage_scheme.csv` — Coverage Scheme (65 cols)

_Grades and coverage scheme stats_

Buckets: `man`, `zone`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `base_snap_counts_coverage` | Coverage snaps — season total |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `man_assists` | Assisted tackles (AST) — vs man coverage |
| `man_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — vs man coverage |
| `man_catch_rate` | Catch rate allowed — receptions/targets in coverage — vs man coverage |
| `man_coverage_percent` | Share of pass snaps spent in coverage (COV%) — vs man coverage |
| `man_coverage_snaps_per_reception` | Coverage snaps per reception allowed (S/REC) — vs man coverage |
| `man_coverage_snaps_per_target` | Coverage snaps per target (S/TGT) — vs man coverage |
| `man_dropped_ints` | Dropped interceptions (DRI) — vs man coverage |
| `man_forced_incompletes` | Forced incompletions (FI) — vs man coverage |
| `man_forced_incompletion_rate` | Forced incompletions per target (FI%) — vs man coverage |
| `man_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — vs man coverage |
| `man_interceptions` | Interceptions made in coverage (INT) — vs man coverage |
| `man_longest` | Longest reception allowed (LNG) — vs man coverage |
| `man_missed_tackle_rate` | Missed-tackle rate (MIS%) — vs man coverage |
| `man_missed_tackles` | Missed tackles (MIS) — vs man coverage |
| `man_pass_break_ups` | Pass breakups (PBU) — vs man coverage |
| `man_qb_rating_against` | Passer rating allowed in coverage (NFL) — vs man coverage |
| `man_receptions` | Receptions allowed (REC) — vs man coverage |
| `man_snap_counts_coverage` | Coverage snaps — vs man coverage |
| `man_snap_counts_coverage_percent` | Share of snaps in coverage — vs man coverage |
| `man_snap_counts_pass_play` | Snaps on pass plays (PASS) — vs man coverage |
| `man_stops` | Defensive stops — tackles constituting an offensive failure (STOP) — vs man coverage |
| `man_tackles` | Tackles, solo (TKL) — vs man coverage |
| `man_targets` | Targets into this player's coverage (TGT) — vs man coverage |
| `man_touchdowns` | Receiving touchdowns allowed (TD) — vs man coverage |
| `man_yards` | Receiving yards allowed (YDS) — vs man coverage |
| `man_yards_after_catch` | Yards after catch allowed (YAC) — vs man coverage |
| `man_yards_per_coverage_snap` | Yards allowed per coverage snap (Y/SNP) — vs man coverage |
| `man_yards_per_reception` | Yards per reception allowed (Y/REC) — vs man coverage |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `zone_assists` | Assisted tackles (AST) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_catch_rate` | Catch rate allowed — receptions/targets in coverage — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_coverage_percent` | Share of pass snaps spent in coverage (COV%) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_coverage_snaps_per_reception` | Coverage snaps per reception allowed (S/REC) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_coverage_snaps_per_target` | Coverage snaps per target (S/TGT) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_dropped_ints` | Dropped interceptions (DRI) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_forced_incompletes` | Forced incompletions (FI) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_forced_incompletion_rate` | Forced incompletions per target (FI%) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_interceptions` | Interceptions made in coverage (INT) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_longest` | Longest reception allowed (LNG) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_missed_tackle_rate` | Missed-tackle rate (MIS%) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_missed_tackles` | Missed tackles (MIS) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_pass_break_ups` | Pass breakups (PBU) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_qb_rating_against` | Passer rating allowed in coverage (NFL) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_receptions` | Receptions allowed (REC) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_snap_counts_coverage` | Coverage snaps — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_snap_counts_coverage_percent` | Share of snaps in coverage — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_snap_counts_pass_play` | Snaps on pass plays (PASS) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_stops` | Defensive stops — tackles constituting an offensive failure (STOP) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_tackles` | Tackles, solo (TKL) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_targets` | Targets into this player's coverage (TGT) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_touchdowns` | Receiving touchdowns allowed (TD) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_yards` | Receiving yards allowed (YDS) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_yards_after_catch` | Yards after catch allowed (YAC) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_yards_per_coverage_snap` | Yards allowed per coverage snap (Y/SNP) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_yards_per_reception` | Yards per reception allowed (Y/REC) — vs zone coverage (or zone-scheme runs in run-blocking) |

<details><summary>PFF key legend (verbatim)</summary>

- **MAN%**: Percentage of Snaps
- **COV**: Coverage Snaps
- **COV**: PFF Grade for Defensive Coverage against Receivers
- **REC**: Receptions
- **YDS**: Receiving Yards
- **YAC**: Yards After Catch
- **LNG**: Longest
- **FI%**: Forced Incompletions per Target
- **INT**: Receiving Interceptions
- **TD**: Receiving TD
- **S/TGT**: Coverage Snaps per Target
- **TKL**: Tackles
- **MIS**: Missed Tackles
- **STOP**: Defensive Stops - tackles that constitute a "failure" for the offense
- **PASS**: Snaps lined up on the field on pass plays
- **COV%**: The percentage of coverage snaps per passing snap played
- **TGT**: Receiving Targets
- **REC%**: Percentage of targets caught
- **Y/REC**: Yards per Reception
- **aDoT**: Average Depth of Target
- **FI**: Forced Incompletions
- **PBU**: Pass Breakups
- **DRI**: Dropped Interceptions
- **NFL**: NFL Passer Rating Against
- **S/REC**: Coverage Snaps per Reception
- **AST**: Assisted Tackles
- **MIS%**: Missed Tackle Rate

</details>

### `PFF_defense_coverage_summary.csv` — Coverage (40 cols)

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `assists` | Assisted tackles (AST) |
| `avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) |
| `catch_rate` | Catch rate allowed — receptions/targets in coverage |
| `coverage_percent` | Share of pass snaps spent in coverage (COV%) |
| `coverage_snaps_per_reception` | Coverage snaps per reception allowed (S/REC) |
| `coverage_snaps_per_target` | Coverage snaps per target (S/TGT) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `dropped_ints` | Dropped interceptions (DRI) |
| `forced_incompletes` | Forced incompletions (FI) |
| `forced_incompletion_rate` | Forced incompletions per target (FI%) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) |
| `grades_defense` | PFF grade, 0–100 (higher is better) — defense |
| `grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties |
| `grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) |
| `grades_run_defense` | PFF grade, 0–100 (higher is better) — run defense (RDEF) |
| `grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) |
| `interceptions` | Interceptions made in coverage (INT) |
| `longest` | Longest reception allowed (LNG) |
| `missed_tackle_rate` | Missed-tackle rate (MIS%) |
| `missed_tackles` | Missed tackles (MIS) |
| `pass_break_ups` | Pass breakups (PBU) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `qb_rating_against` | Passer rating allowed in coverage (NFL) |
| `receptions` | Receptions allowed (REC) |
| `snap_counts_coverage` | Coverage snaps |
| `snap_counts_pass_play` | Snaps on pass plays (PASS) |
| `stops` | Defensive stops — tackles constituting an offensive failure (STOP) |
| `tackles` | Tackles, solo (TKL) |
| `targets` | Targets into this player's coverage (TGT) |
| `touchdowns` | Receiving touchdowns allowed (TD) |
| `yards` | Receiving yards allowed (YDS) |
| `yards_after_catch` | Yards after catch allowed (YAC) |
| `yards_per_coverage_snap` | Yards allowed per coverage snap (Y/SNP) |
| `yards_per_reception` | Yards per reception allowed (Y/REC) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **COV**: Coverage Snaps
- **COV**: PFF Grade for Defensive Coverage against Receivers
- **TGT**: Receiving Targets
- **REC%**: Percentage of targets caught
- **Y/REC**: Yards per Reception
- **aDoT**: Average Depth of Target
- **FI**: Forced Incompletions
- **PBU**: Pass Breakups
- **DRI**: Dropped Interceptions
- **NFL**: NFL Passer Rating Against
- **S/REC**: Coverage Snaps per Reception
- **AST**: Assisted Tackles
- **MIS%**: Missed Tackle Rate
- **POS**: Season position
- **PASS**: Snaps lined up on the field on pass plays
- **COV%**: The percentage of coverage snaps per passing snap played
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties
- **REC**: Receptions
- **YDS**: Receiving Yards
- **YAC**: Yards After Catch
- **LNG**: Longest
- **FI%**: Forced Incompletions per Target
- **INT**: Receiving Interceptions
- **TD**: Receiving TD
- **S/TGT**: Coverage Snaps per Target
- **TKL**: Tackles
- **MIS**: Missed Tackles
- **STOP**: Defensive Stops - tackles that constitute a "failure" for the offense

</details>

### `PFF_defense_summary.csv` — Defense General (55 cols)

_Grades and base defense stats._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `assists` | Assisted tackles (AST) |
| `batted_passes` | Batted passes — deflected at the line (BAT) |
| `catch_rate` | Catch rate allowed — receptions/targets in coverage |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `forced_fumbles` | Forced fumbles (FFM) |
| `franchise_id` | PFF unique team/franchise identifier |
| `fumble_recoveries` | Fumble recoveries |
| `fumble_recovery_touchdowns` | Touchdowns scored on fumble recoveries |
| `grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) |
| `grades_defense` | PFF grade, 0–100 (higher is better) — defense |
| `grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties |
| `grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) |
| `grades_run_defense` | PFF grade, 0–100 (higher is better) — run defense (RDEF) |
| `grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) |
| `hits` | QB hits (HIT) |
| `hurries` | QB hurries (HUR) |
| `interception_touchdowns` | Interceptions returned for touchdowns |
| `interceptions` | Interceptions made (INT) |
| `longest` | Longest reception allowed (LNG) |
| `missed_tackle_rate` | Missed-tackle rate (MIS%) |
| `missed_tackles` | Missed tackles (MIS) |
| `pass_break_ups` | Pass breakups (PBU) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `qb_rating_against` | Passer rating allowed in coverage (NFL) |
| `receptions` | Receptions allowed (REC) |
| `sacks` | Sacks recorded (SK) |
| `safeties` | Safeties scored |
| `snap_counts_box` | Snaps aligned in the box |
| `snap_counts_corner` | Snaps aligned at cornerback |
| `snap_counts_coverage` | Coverage snaps |
| `snap_counts_defense` | Total defensive snaps |
| `snap_counts_dl` | Snaps on the defensive line |
| `snap_counts_dl_a_gap` | D-line snaps in the A-gap / as a nose tackle (AGP) |
| `snap_counts_dl_b_gap` | D-line snaps in the B-gap / as a DT (BGP) |
| `snap_counts_dl_outside_t` | D-line snaps outside the tackle (OUT) |
| `snap_counts_dl_over_t` | D-line snaps over the tackle (OVT) |
| `snap_counts_fs` | Snaps at free safety (FS) |
| `snap_counts_offball` | Off-ball (non-line) snaps |
| `snap_counts_pass_rush` | Pass-rush snaps (PRSH) |
| `snap_counts_run_defense` | Run-defense snaps (RDEF) |
| `snap_counts_slot` | Snaps in the slot (Slot) |
| `stops` | Defensive stops — tackles constituting an offensive failure (STOP) |
| `tackles` | Tackles, solo (TKL) |
| `tackles_for_loss` | Tackles for loss |
| `targets` | Targets into coverage (TGT) |
| `total_pressures` | Total pressures — sacks + QB hits + hurries (TOT) |
| `touchdowns` | Receiving touchdowns allowed (TD) |
| `yards` | Receiving yards allowed (YDS) |
| `yards_after_catch` | Yards after catch allowed (YAC) |
| `yards_per_reception` | Yards per reception allowed (Y/REC) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **RDEF**: Snaps in a run defense role
- **COV**: Coverage Snaps
- **RDEF**: PFF Grade for Run Defense
- **PRSH**: PFF Grade for Pass Rush
- **TOT**: Total pressures of the passer of any kind (generated by the defense)
- **HIT**: Hits - when the passer is hit by the defender
- **BAT**: Batted Passes - the number of passes batted or deflected at the line of scrimage
- **AST**: Assisted Tackles
- **MIS%**: Missed Tackle Rate
- **FFM**: Forced Fumbles
- **REC**: Receptions
- **YDS**: Receiving Yards
- **YAC**: Yards After Catch
- **TD**: Receiving TD
- **PBU**: Pass Breakups
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties
- **Box**: Number of player's snaps lined up in the Box
- **Slot**: Number of player's snaps lined up at Slot Corner
- **AGP**: Number of player's snaps lined up on DL as a NT
- **OVT**: Number of player's snaps lined up on DL over an OT
- **POS**: Season position
- **TOT**: Total Snaps
- **PRSH**: Pass Rush Snaps
- **DEF**: PFF Grade for Defense
- **TACK**: PFF Grade for Tackling
- **COV**: PFF Grade for Defensive Coverage against Receivers
- **SK**: Sacks
- **HUR**: Hurries - when the passer is hurried by the defender
- **TKL**: Tackles
- **MIS**: Missed Tackles
- **STOP**: Defensive Stops - tackles that constitute a "failure" for the offense
- **TGT**: Receiving Targets
- **REC%**: Percentage of targets caught
- **Y/REC**: Yards per Reception
- **LNG**: Longest
- **INT**: Receiving Interceptions
- **NFL**: NFL Passer Rating Against
- **DL**: Number of player's snaps lined up on the Line
- **FS**: Number of player's snaps lined up at Free Safety
- **Cnr**: Number of player's snaps lined up at Corner
- **BGP**: Number of player's snaps lined up on DL as a DT
- **OUT**: Number of player's snaps lined up on DL outside the OT

</details>

### `PFF_field_goal_summary.csv` — Field Goals (30 cols)

_Grades and base place kicking stats._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `fifty_attempts` | FG attempts from 50+ yards |
| `fifty_made` | FGs made from 50+ yards |
| `fifty_percent` | FG% from 50+ yards |
| `forty_attempts` | FG attempts from 40–49 yards |
| `forty_made` | FGs made from 40–49 yards |
| `forty_percent` | FG% from 40–49 yards |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_fgep_kicker` | PFF grade, 0–100 (higher is better) — field-goal/extra-point kicking (FG) |
| `one_attempts` | FG attempts from 1–19 yards |
| `one_made` | FGs made from 1–19 yards |
| `one_percent` | FG% from 1–19 yards |
| `pat_attempts` | Extra points (PAT) attempted (XPA) |
| `pat_made` | Extra points made (XP) |
| `pat_percent` | Extra-point % (XP%) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `thirty_attempts` | FG attempts from 30–39 yards |
| `thirty_made` | FGs made from 30–39 yards |
| `thirty_percent` | FG% from 30–39 yards |
| `total_attempts` | Total field goals attempted (FGA) |
| `total_made` | Total field goals made (FG) |
| `total_percent` | Field-goal percentage (FG%) |
| `twenty_attempts` | FG attempts from 20–29 yards |
| `twenty_made` | FGs made from 20–29 yards |
| `twenty_percent` | FG% from 20–29 yards |

<details><summary>PFF key legend (verbatim)</summary>

- **Note**: Field goal data currently only available since 2013.
- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **XP**: Points After Touchdown Made
- **XP%**: Percentage of Points After Touchdown made
- **FGA**: Field Goals Attempted
- **POS**: Season position
- **FG**: PFF Grade for Field Goals
- **XPA**: Points After Touchdown Attempted
- **FG**: Field Goals Made
- **FG%**: Percentage of Field Goals made

</details>

### `PFF_kickoff_summary.csv` — Kickoffs (23 cols)

_Grades and base kickoff stats._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `attempts` | Kickoff attempts (ATT) |
| `attempts_with_hangtime` | Attempts with hangtime recorded |
| `average_distance` | Average kickoff distance (yards) |
| `average_hangtime` | Average hangtime, seconds (AVG) |
| `average_starting_field_position` | Average opponent start field position after kickoff (AFP) |
| `average_yards_per_return` | Average return yards allowed per return (YPR) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `fair_catches` | Fair catches induced on kickoffs (FC) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_kickoff_kicker` | PFF grade, 0–100 (higher is better) — kickoffs (kicker) (KOFF) |
| `kicked_yards` | Total kicked yards |
| `kicks_returned` | Kicks returned (RET) |
| `onside_kicks` | Onside kicks (ONS) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `percent_returned` | Percentage of kickoffs returned (RET%) |
| `return_yards` | Return yards allowed on kickoffs |
| `total_hangtime` | Total hangtime, seconds |
| `touchbacks` | Touchbacks (TB) |

<details><summary>PFF key legend (verbatim)</summary>

- **Note**: Kickoff data currently only available since 2013.
- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **ATT**: Kickoff Attempts
- **AFP**: Average starting field position after kickoff
- **RET%**: Percentage of Kicks returned
- **YDS**: Return Yards
- **TB**: Touchbacks
- **ATT**: Attempts with Hangtime
- **POS**: Season position
- **KOFF**: PFF Grade for Kickoffs
- **YPA**: Yards per Kickoff Attempt
- **ONS**: Onside Kicks
- **RET**: # of Kicks returned
- **YPR**: Return Yards Per Return
- **FC**: Fair Catches
- **AVG**: Average Kick Hangtime (seconds)

</details>

### `PFF_offense_blocking.csv` — Blocking General (31 cols)

_Blocking grades and allowed pressure stats for players who participated as run blockers or pass blockers._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `block_percent` | Share of snaps spent blocking (BLK%) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_offense` | PFF grade, 0–100 (higher is better) — offense |
| `grades_pass_block` | PFF grade, 0–100 (higher is better) — pass blocking (PBLK) |
| `grades_run_block` | PFF grade, 0–100 (higher is better) — run blocking (RBLK) |
| `hits_allowed` | QB hits allowed (HIT) |
| `hurries_allowed` | QB hurries allowed (HUR) |
| `non_spike_pass_block` | Allowed-pressure opportunities — non-spike, non-penalty pass-block snaps (OPP) |
| `non_spike_pass_block_percentage` | Share of pass-block snaps that were opportunities (OPP%) |
| `pass_block_percent` | Share of snaps pass blocking (PB%) |
| `pbe` | Pass-blocking efficiency — pressure allowed per snap, weighted to sacks (EFF) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `pressures_allowed` | QB pressures allowed (PR) |
| `sacks_allowed` | Sacks allowed (SK) |
| `snap_counts_block` | Total blocking snaps (BLK) |
| `snap_counts_ce` | Snaps aligned at center (C) |
| `snap_counts_lg` | Snaps at left guard (LG) |
| `snap_counts_lt` | Snaps at left tackle (LT) |
| `snap_counts_offense` | Total offensive snaps (OFF) |
| `snap_counts_pass_block` | Pass-block snaps (PBLK) |
| `snap_counts_pass_play` | Snaps on pass plays (PASS) |
| `snap_counts_rg` | Snaps at right guard (RG) |
| `snap_counts_rt` | Snaps at right tackle (RT) |
| `snap_counts_run_block` | Run-block snaps (RBLK) |
| `snap_counts_te` | Snaps aligned as inline TE (ITE) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **BLK**: Total Snaps
- **RBLK**: Snaps in a run blocking role
- **OFF**: PFF Grade for Offense
- **PBLK**: PFF Grade for Pass Blocking
- **OPP%**: Percentage of Non-Spike, non-penalty Passing Snaps with an opportunity to allow pressure
- **HIT**: QB Hits Allowed
- **PR**: QB Pressures Allowed
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties
- **LG**: Number of player's snaps lined up at Left Guard
- **RG**: Number of player's snaps lined up at Right Guard
- **ITE**: Number of player's snaps lined up as an inline Tight End
- **POS**: Season position
- **OFF**: Offensive Snaps
- **BLK%**: Percentage of snaps
- **PBLK**: Pass Block Snaps
- **RBLK**: PFF Grade for Run Blocking
- **OPP**: Allowed Pressure Opportunities - Non-spike, non-penalty Snaps when participating as a pass blocker
- **SK**: Sacks Allowed
- **HUR**: QB Hurries Allowed
- **EFF**: Pass Blocking Efficiency - A PFF Signature stat measuring pressure allowed on a per-snap basis with weighting toward sacks allowed.
- **LT**: Number of player's snaps lined up at Left Tackle
- **C**: Number of player's snaps lined up at Center
- **RT**: Number of player's snaps lined up at Right Tackle

</details>

### `PFF_offense_pass_blocking.csv` — Pass Block (30 cols)

_Blocking grades and allowed pressure stats for players who participated as pass blockers._

Buckets: `true_pass_set`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_pass_block` | PFF grade, 0–100 (higher is better) — pass blocking (PBLK) |
| `hits_allowed` | QB hits allowed (HIT) |
| `hurries_allowed` | QB hurries allowed (HUR) |
| `non_spike_pass_block` | Allowed-pressure opportunities — non-spike, non-penalty pass-block snaps (OPP) |
| `non_spike_pass_block_percentage` | Share of pass-block snaps that were opportunities (OPP%) |
| `pass_block_percent` | Share of snaps pass blocking (PB%) |
| `pbe` | Pass-blocking efficiency — pressure allowed per snap, weighted to sacks (EFF) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `pressures_allowed` | QB pressures allowed (PR) |
| `sacks_allowed` | Sacks allowed (SK) |
| `snap_counts_pass_block` | Pass-block snaps (PBLK) |
| `snap_counts_pass_play` | Snaps on pass plays (PASS) |
| `true_pass_set_grades_pass_block` | PFF grade, 0–100 (higher is better) — pass blocking (PBLK) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_hits_allowed` | QB hits allowed (HIT) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_hurries_allowed` | QB hurries allowed (HUR) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_non_spike_pass_block` | Allowed-pressure opportunities — non-spike, non-penalty pass-block snaps (OPP) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_non_spike_pass_block_percentage` | Share of pass-block snaps that were opportunities (OPP%) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_pass_block_percent` | Share of snaps pass blocking (PB%) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_pbe` | Pass-blocking efficiency — pressure allowed per snap, weighted to sacks (EFF) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_pressures_allowed` | QB pressures allowed (PR) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_sacks_allowed` | Sacks allowed (SK) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_snap_counts_pass_block` | Pass-block snaps (PBLK) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_snap_counts_pass_play` | Snaps on pass plays (PASS) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **PBLK**: Pass Block Snaps
- **PBLK**: PFF Grade for Pass Blocking
- **OPP**: Allowed Pressure Opportunities - Non-spike, non-penalty Snaps when participating as a pass blocker
- **SK**: Sacks Allowed
- **HUR**: QB Hurries Allowed
- **EFF**: Pass Blocking Efficiency - A PFF Signature stat measuring pressure allowed on a per-snap basis with weighting toward sacks allowed.
- **OPP%**: Percentage of Non-Spike, non-penalty Passing Snaps with an opportunity to allow pressure
- **HIT**: QB Hits Allowed
- **PR**: QB Pressures Allowed
- **POS**: Season position
- **PASS**: Snaps lined up on the field on pass plays
- **PB%**: Percentage of snaps
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties

</details>

### `PFF_offense_run_blockng.csv` — Run Block (22 cols)

_Blocking grades and allowed pressure stats for players who participated as run blockers._

Buckets: `gap`, `zone`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `gap_grades_run_block` | PFF grade, 0–100 (higher is better) — run blocking (RBLK) — on gap/power-scheme run plays |
| `gap_run_block_percent` | Share of snaps run blocking (RB%) — on gap/power-scheme run plays |
| `gap_snap_counts_run_block` | Run-block snaps (RBLK) — on gap/power-scheme run plays |
| `gap_snap_counts_run_block_percent` | Share of snaps run blocking (SNP%) — on gap/power-scheme run plays |
| `gap_snap_counts_run_play` | Snaps on run plays (RUN) — on gap/power-scheme run plays |
| `grades_run_block` | PFF grade, 0–100 (higher is better) — run blocking (RBLK) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `run_block_percent` | Share of snaps run blocking (RB%) |
| `snap_counts_run_block` | Run-block snaps (RBLK) |
| `snap_counts_run_play` | Snaps on run plays (RUN) |
| `zone_grades_run_block` | PFF grade, 0–100 (higher is better) — run blocking (RBLK) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_run_block_percent` | Share of snaps run blocking (RB%) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_snap_counts_run_block` | Run-block snaps (RBLK) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_snap_counts_run_block_percent` | Share of snaps run blocking (SNP%) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_snap_counts_run_play` | Snaps on run plays (RUN) — vs zone coverage (or zone-scheme runs in run-blocking) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **RBLK**: Snaps in a run blocking role
- **RBLK**: PFF Grade for Run Blocking
- **SNP%**: Percentage of snaps
- **POS**: Season position
- **RUN**: Snaps lined up on the field on run plays
- **RB%**: Percentage of snaps
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties

</details>

### `PFF_pass_rush_productivity.csv` — Pass Rush Productivity (40 cols)

_The PFF "Pass Rushing Productivity" rating measures pressure created on a per snap basis with weighting toward sacks._

Buckets: `lhs`, `rhs`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `assists` | Assisted tackles (AST) |
| `franchise_id` | PFF unique team/franchise identifier |
| `hits` | QB hits (HIT) |
| `hurries` | QB hurries (HUR) |
| `lhs_assists` | Assisted tackles (AST) — when rushing from the left side |
| `lhs_hits` | QB hits (HIT) — when rushing from the left side |
| `lhs_hurries` | QB hurries (HUR) — when rushing from the left side |
| `lhs_misses` | Missed tackles (as a pass rusher) — when rushing from the left side |
| `lhs_pass_rush_percent` | Share of pass snaps spent rushing (RSH%) — when rushing from the left side |
| `lhs_pass_rush_snaps` | Pass-rush snaps (PRSH) — when rushing from the left side |
| `lhs_pressures` | Total pressures generated (as a pass rusher) — when rushing from the left side |
| `lhs_prp` | Pass-Rush Productivity — pressure per snap, weighted to sacks (PRP) — when rushing from the left side |
| `lhs_sacks` | Sacks recorded (SK) — when rushing from the left side |
| `lhs_stops` | Defensive stops — tackles constituting an offensive failure (STOP) — when rushing from the left side |
| `lhs_tackles` | Tackles, solo (TKL) — when rushing from the left side |
| `misses` | Missed tackles (as a pass rusher) |
| `pass_rush_percent` | Share of pass snaps spent rushing (RSH%) |
| `pass_rush_snaps` | Pass-rush snaps (PRSH) |
| `pass_snaps` | Pass snaps (PASS) |
| `pressures` | Total pressures generated (as a pass rusher) |
| `prp` | Pass-Rush Productivity — pressure per snap, weighted to sacks (PRP) |
| `rhs_assists` | Assisted tackles (AST) — when rushing from the right side |
| `rhs_hits` | QB hits (HIT) — when rushing from the right side |
| `rhs_hurries` | QB hurries (HUR) — when rushing from the right side |
| `rhs_misses` | Missed tackles (as a pass rusher) — when rushing from the right side |
| `rhs_pass_rush_percent` | Share of pass snaps spent rushing (RSH%) — when rushing from the right side |
| `rhs_pass_rush_snaps` | Pass-rush snaps (PRSH) — when rushing from the right side |
| `rhs_pressures` | Total pressures generated (as a pass rusher) — when rushing from the right side |
| `rhs_prp` | Pass-Rush Productivity — pressure per snap, weighted to sacks (PRP) — when rushing from the right side |
| `rhs_sacks` | Sacks recorded (SK) — when rushing from the right side |
| `rhs_stops` | Defensive stops — tackles constituting an offensive failure (STOP) — when rushing from the right side |
| `rhs_tackles` | Tackles, solo (TKL) — when rushing from the right side |
| `sacks` | Sacks recorded (SK) |
| `stops` | Defensive stops — tackles constituting an offensive failure (STOP) |
| `tackles` | Tackles, solo (TKL) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **PRSH**: Pass Rush Snaps
- **SK**: Sacks
- **HUR**: Hurries - when the passer is hurried by the defender
- **PRP**: A formula that combines sacks, hits and hurries relative to how many times they rush the passer
- **RSH%**: The percentage of pass rush snaps per passing snap played
- **HIT**: Hits - when the passer is hit by the defender
- **DPR**: Total pressures of the passer of any kind (generated by the defense)
- **POS**: Season position
- **PASS**: Pass Snaps

</details>

### `PFF_pass_rush_summary.csv` — Pass Rush (34 cols)

_Grades and pass rush stats._

Buckets: `true_pass_set`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `batted_passes` | Batted passes — deflected at the line (BAT) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) |
| `hits` | QB hits (HIT) |
| `hurries` | QB hurries (HUR) |
| `pass_rush_opp` | Pass-rush opportunities (snaps rushing the passer) |
| `pass_rush_percent` | Share of pass snaps spent rushing (RSH%) |
| `pass_rush_win_rate` | Pass-rush win rate — % of rushes won vs the blocker (WIN%) |
| `pass_rush_wins` | Pass-rush wins |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `prp` | Pass-Rush Productivity — pressure per snap, weighted to sacks (PRP) |
| `sacks` | Sacks recorded (SK) |
| `snap_counts_pass_play` | Snaps on pass plays (PASS) |
| `snap_counts_pass_rush` | Pass-rush snaps (PRSH) |
| `total_pressures` | Total pressures — sacks + QB hits + hurries (TOT) |
| `true_pass_set_batted_passes` | Batted passes — deflected at the line (BAT) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_hits` | QB hits (HIT) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_hurries` | QB hurries (HUR) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_pass_rush_opp` | Pass-rush opportunities (snaps rushing the passer) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_pass_rush_percent` | Share of pass snaps spent rushing (RSH%) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_pass_rush_win_rate` | Pass-rush win rate — % of rushes won vs the blocker (WIN%) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_pass_rush_wins` | Pass-rush wins — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_prp` | Pass-Rush Productivity — pressure per snap, weighted to sacks (PRP) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_sacks` | Sacks recorded (SK) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_snap_counts_pass_play` | Snaps on pass plays (PASS) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_snap_counts_pass_rush` | Pass-rush snaps (PRSH) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |
| `true_pass_set_total_pressures` | Total pressures — sacks + QB hits + hurries (TOT) — on 'true pass sets' (excludes screens, play-action, short dropbacks, <4 rushers, and quick throws under ~2s) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **PRSH**: Pass Rush Snaps
- **PRSH**: PFF Grade for Pass Rush
- **TOT**: Total pressures of the passer of any kind (generated by the defense)
- **HIT**: Hits - when the passer is hit by the defender
- **PRP**: A formula that combines sacks, hits and hurries relative to how many times they rush the passer
- **BAT**: Batted Passes - the number of passes batted or deflected at the line of scrimage
- **SK**: Sacks
- **HUR**: Hurries - when the passer is hurried by the defender
- **WIN%**: Percentage of "wins" vs Blocking on non-penalty Pass Rush Snaps
- **POS**: Season position
- **PASS**: Snaps lined up on the field on pass plays
- **RSH%**: The percentage of pass rush snaps per passing snap played
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties

</details>

### `PFF_passing_allowed_pressure.csv` — Allowed Pressure (32 cols)

_Pressures are a stat a QB can own. This report considers plays where the offense allowed pressure._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `allowed_pressure_dropbacks` | Dropbacks while the offense was under pressure (APDB) |
| `ce_percent` | Share of the offense's allowed pressures charged to the center (C%) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `hits_allowed` | QB hits allowed (HIT) |
| `hurries_allowed` | QB hurries allowed (HUR) |
| `lg_percent` | Share of allowed pressures charged to the left guard (LG%) |
| `lt_percent` | Share charged to the left tackle (LT%) |
| `ol_te_percent` | Share charged to an OL/TE (OL%) |
| `other_percent` | Share charged to another player (OTH%) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `pressures_allowed` | QB pressures allowed (PR) |
| `pressures_ce` | Allowed pressures charged to the center |
| `pressures_lg` | Allowed pressures charged to the left guard |
| `pressures_lt` | Allowed pressures charged to the left tackle |
| `pressures_off` | Total allowed pressures charged to the offense |
| `pressures_ol_te` | Allowed pressures charged to an OL/TE |
| `pressures_other` | Allowed pressures charged to another player |
| `pressures_rg` | Allowed pressures charged to the right guard |
| `pressures_rt` | Allowed pressures charged to the right tackle |
| `pressures_self` | Allowed pressures charged to the QB himself |
| `pressures_te` | Allowed pressures charged to a tight end |
| `rg_percent` | Share charged to the right guard (RG%) |
| `rt_percent` | Share charged to the right tackle (RT%) |
| `sacks_allowed` | Sacks allowed (SK) |
| `self_percent` | Share charged to the QB himself (QB%) |
| `te_percent` | Share charged to a tight end (ITE%) |

<details><summary>PFF key legend (verbatim)</summary>

- **Note**: Offensive players may share responsibility for an allowed pressure (e.g. Defender splits a double-team).
- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **SK**: Sacks Allowed
- **HUR**: QB Hurries Allowed
- **QB%**: Percentage of Pressures Generated by the Defense charged to the Offense Player
- **LT%**: Percentage of Pressures Generated by the Defense charged to the Offense Player
- **C%**: Percentage of Pressures Generated by the Defense charged to the Offense Player
- **RT%**: Percentage of Pressures Generated by the Defense charged to the Offense Player
- **OTH%**: Percentage of Pressures Generated by the Defense charged to the Offense Player
- **POS**: Season position
- **APDB**: The number of Dropbacks when under pressure
- **HIT**: QB Hits Allowed
- **PR**: QB Pressures Allowed
- **OL%**: Percentage of Pressures Generated by the Defense charged to the Offense Player
- **LG%**: Percentage of Pressures Generated by the Defense charged to the Offense Player
- **RG%**: Percentage of Pressures Generated by the Defense charged to the Offense Player
- **ITE%**: Percentage of Pressures Generated by the Defense charged to the Offense Player

</details>

### `PFF_passing_concept.csv` — Passing Concept (199 cols)

_See how quarterbacks perform on Play Action and Screen passes and compare it to the times they do not use that pass conc_

Buckets: `no_screen`, `screen`, `npa`, `pa`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `comp_pct_diff` | Completion-% difference between this report's splits (concept comparison) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `dropbacks` | Dropbacks — times the QB dropped back to pass (DB) |
| `franchise_id` | PFF unique team/franchise identifier |
| `no_screen_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — on non-screen dropbacks |
| `no_screen_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — on non-screen dropbacks |
| `no_screen_attempts` | Pass attempts (ATT) — on non-screen dropbacks |
| `no_screen_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — on non-screen dropbacks |
| `no_screen_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — on non-screen dropbacks |
| `no_screen_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — on non-screen dropbacks |
| `no_screen_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — on non-screen dropbacks |
| `no_screen_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — on non-screen dropbacks |
| `no_screen_completion_percent` | Completion percentage — completions/attempts (COM%) — on non-screen dropbacks |
| `no_screen_completions` | Completions (COM) — on non-screen dropbacks |
| `no_screen_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — on non-screen dropbacks |
| `no_screen_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — on non-screen dropbacks |
| `no_screen_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — on non-screen dropbacks |
| `no_screen_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — on non-screen dropbacks |
| `no_screen_drops` | Drops — on-target passes dropped by the receiver (DRP) — on non-screen dropbacks |
| `no_screen_epa` | Expected Points Added on the player's plays [standard/EPA] — on non-screen dropbacks |
| `no_screen_first_downs` | First downs gained (1st) — on non-screen dropbacks |
| `no_screen_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — on non-screen dropbacks |
| `no_screen_grades_defense` | PFF grade, 0–100 (higher is better) — defense — on non-screen dropbacks |
| `no_screen_grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties — on non-screen dropbacks |
| `no_screen_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — on non-screen dropbacks |
| `no_screen_grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) — on non-screen dropbacks |
| `no_screen_grades_offense` | PFF grade, 0–100 (higher is better) — offense — on non-screen dropbacks |
| `no_screen_grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties — on non-screen dropbacks |
| `no_screen_grades_overall_tackle` | PFF grade, 0–100 (higher is better) — overall tackling — on non-screen dropbacks |
| `no_screen_grades_pass` | PFF grade, 0–100 (higher is better) — passing — on non-screen dropbacks |
| `no_screen_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — on non-screen dropbacks |
| `no_screen_grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) — on non-screen dropbacks |
| `no_screen_grades_run` | PFF grade, 0–100 (higher is better) — rushing — on non-screen dropbacks |
| `no_screen_grades_run_defense` | PFF grade, 0–100 (higher is better) — run defense (RDEF) — on non-screen dropbacks |
| `no_screen_grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) — on non-screen dropbacks |
| `no_screen_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — on non-screen dropbacks |
| `no_screen_interceptions` | Interceptions thrown (INT) — on non-screen dropbacks |
| `no_screen_passing_snaps` | Passing snaps — snaps on pass plays — on non-screen dropbacks |
| `no_screen_positive_epa_percent` | Percentage of plays with positive EPA [standard] — on non-screen dropbacks |
| `no_screen_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — on non-screen dropbacks |
| `no_screen_qb_rating` | NFL passer rating (NFL) — on non-screen dropbacks |
| `no_screen_sack_percent` | Sack percentage — sacks per dropback [standard] — on non-screen dropbacks |
| `no_screen_sacks` | Sacks taken by the passer (SK) — on non-screen dropbacks |
| `no_screen_scrambles` | Scrambles — undesigned QB runs (SCR) — on non-screen dropbacks |
| `no_screen_spikes` | Spikes — QB clock-stopping spikes [standard] — on non-screen dropbacks |
| `no_screen_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — on non-screen dropbacks |
| `no_screen_touchdowns` | Passing touchdowns (TD) — on non-screen dropbacks |
| `no_screen_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — on non-screen dropbacks |
| `no_screen_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — on non-screen dropbacks |
| `no_screen_yards` | Passing yards (YDS) — on non-screen dropbacks |
| `no_screen_ypa` | Yards per pass attempt (YPA) — on non-screen dropbacks |
| `npa_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — on non-play-action dropbacks |
| `npa_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — on non-play-action dropbacks |
| `npa_attempts` | Pass attempts (ATT) — on non-play-action dropbacks |
| `npa_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — on non-play-action dropbacks |
| `npa_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — on non-play-action dropbacks |
| `npa_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — on non-play-action dropbacks |
| `npa_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — on non-play-action dropbacks |
| `npa_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — on non-play-action dropbacks |
| `npa_completion_percent` | Completion percentage — completions/attempts (COM%) — on non-play-action dropbacks |
| `npa_completions` | Completions (COM) — on non-play-action dropbacks |
| `npa_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — on non-play-action dropbacks |
| `npa_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — on non-play-action dropbacks |
| `npa_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — on non-play-action dropbacks |
| `npa_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — on non-play-action dropbacks |
| `npa_drops` | Drops — on-target passes dropped by the receiver (DRP) — on non-play-action dropbacks |
| `npa_epa` | Expected Points Added on the player's plays [standard/EPA] — on non-play-action dropbacks |
| `npa_first_downs` | First downs gained (1st) — on non-play-action dropbacks |
| `npa_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — on non-play-action dropbacks |
| `npa_grades_defense` | PFF grade, 0–100 (higher is better) — defense — on non-play-action dropbacks |
| `npa_grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties — on non-play-action dropbacks |
| `npa_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — on non-play-action dropbacks |
| `npa_grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) — on non-play-action dropbacks |
| `npa_grades_offense` | PFF grade, 0–100 (higher is better) — offense — on non-play-action dropbacks |
| `npa_grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties — on non-play-action dropbacks |
| `npa_grades_overall_tackle` | PFF grade, 0–100 (higher is better) — overall tackling — on non-play-action dropbacks |
| `npa_grades_pass` | PFF grade, 0–100 (higher is better) — passing — on non-play-action dropbacks |
| `npa_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — on non-play-action dropbacks |
| `npa_grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) — on non-play-action dropbacks |
| `npa_grades_run` | PFF grade, 0–100 (higher is better) — rushing — on non-play-action dropbacks |
| `npa_grades_run_defense` | PFF grade, 0–100 (higher is better) — run defense (RDEF) — on non-play-action dropbacks |
| `npa_grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) — on non-play-action dropbacks |
| `npa_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — on non-play-action dropbacks |
| `npa_interceptions` | Interceptions thrown (INT) — on non-play-action dropbacks |
| `npa_passing_snaps` | Passing snaps — snaps on pass plays — on non-play-action dropbacks |
| `npa_positive_epa_percent` | Percentage of plays with positive EPA [standard] — on non-play-action dropbacks |
| `npa_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — on non-play-action dropbacks |
| `npa_qb_rating` | NFL passer rating (NFL) — on non-play-action dropbacks |
| `npa_sack_percent` | Sack percentage — sacks per dropback [standard] — on non-play-action dropbacks |
| `npa_sacks` | Sacks taken by the passer (SK) — on non-play-action dropbacks |
| `npa_scrambles` | Scrambles — undesigned QB runs (SCR) — on non-play-action dropbacks |
| `npa_spikes` | Spikes — QB clock-stopping spikes [standard] — on non-play-action dropbacks |
| `npa_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — on non-play-action dropbacks |
| `npa_touchdowns` | Passing touchdowns (TD) — on non-play-action dropbacks |
| `npa_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — on non-play-action dropbacks |
| `npa_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — on non-play-action dropbacks |
| `npa_yards` | Passing yards (YDS) — on non-play-action dropbacks |
| `npa_ypa` | Yards per pass attempt (YPA) — on non-play-action dropbacks |
| `pa_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — on play-action dropbacks |
| `pa_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — on play-action dropbacks |
| `pa_attempts` | Pass attempts (ATT) — on play-action dropbacks |
| `pa_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — on play-action dropbacks |
| `pa_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — on play-action dropbacks |
| `pa_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — on play-action dropbacks |
| `pa_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — on play-action dropbacks |
| `pa_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — on play-action dropbacks |
| `pa_completion_percent` | Completion percentage — completions/attempts (COM%) — on play-action dropbacks |
| `pa_completions` | Completions (COM) — on play-action dropbacks |
| `pa_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — on play-action dropbacks |
| `pa_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — on play-action dropbacks |
| `pa_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — on play-action dropbacks |
| `pa_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — on play-action dropbacks |
| `pa_drops` | Drops — on-target passes dropped by the receiver (DRP) — on play-action dropbacks |
| `pa_epa` | Expected Points Added on the player's plays [standard/EPA] — on play-action dropbacks |
| `pa_first_downs` | First downs gained (1st) — on play-action dropbacks |
| `pa_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — on play-action dropbacks |
| `pa_grades_defense` | PFF grade, 0–100 (higher is better) — defense — on play-action dropbacks |
| `pa_grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties — on play-action dropbacks |
| `pa_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — on play-action dropbacks |
| `pa_grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) — on play-action dropbacks |
| `pa_grades_offense` | PFF grade, 0–100 (higher is better) — offense — on play-action dropbacks |
| `pa_grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties — on play-action dropbacks |
| `pa_grades_overall_tackle` | PFF grade, 0–100 (higher is better) — overall tackling — on play-action dropbacks |
| `pa_grades_pass` | PFF grade, 0–100 (higher is better) — passing — on play-action dropbacks |
| `pa_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — on play-action dropbacks |
| `pa_grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) — on play-action dropbacks |
| `pa_grades_run` | PFF grade, 0–100 (higher is better) — rushing — on play-action dropbacks |
| `pa_grades_run_defense` | PFF grade, 0–100 (higher is better) — run defense (RDEF) — on play-action dropbacks |
| `pa_grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) — on play-action dropbacks |
| `pa_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — on play-action dropbacks |
| `pa_interceptions` | Interceptions thrown (INT) — on play-action dropbacks |
| `pa_passing_snaps` | Passing snaps — snaps on pass plays — on play-action dropbacks |
| `pa_positive_epa_percent` | Percentage of plays with positive EPA [standard] — on play-action dropbacks |
| `pa_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — on play-action dropbacks |
| `pa_qb_rating` | NFL passer rating (NFL) — on play-action dropbacks |
| `pa_sack_percent` | Sack percentage — sacks per dropback [standard] — on play-action dropbacks |
| `pa_sacks` | Sacks taken by the passer (SK) — on play-action dropbacks |
| `pa_scrambles` | Scrambles — undesigned QB runs (SCR) — on play-action dropbacks |
| `pa_spikes` | Spikes — QB clock-stopping spikes [standard] — on play-action dropbacks |
| `pa_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — on play-action dropbacks |
| `pa_touchdowns` | Passing touchdowns (TD) — on play-action dropbacks |
| `pa_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — on play-action dropbacks |
| `pa_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — on play-action dropbacks |
| `pa_yards` | Passing yards (YDS) — on play-action dropbacks |
| `pa_ypa` | Yards per pass attempt (YPA) — on play-action dropbacks |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `screen_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — on screen passes |
| `screen_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — on screen passes |
| `screen_attempts` | Pass attempts (ATT) — on screen passes |
| `screen_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — on screen passes |
| `screen_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — on screen passes |
| `screen_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — on screen passes |
| `screen_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — on screen passes |
| `screen_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — on screen passes |
| `screen_completion_percent` | Completion percentage — completions/attempts (COM%) — on screen passes |
| `screen_completions` | Completions (COM) — on screen passes |
| `screen_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — on screen passes |
| `screen_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — on screen passes |
| `screen_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — on screen passes |
| `screen_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — on screen passes |
| `screen_drops` | Drops — on-target passes dropped by the receiver (DRP) — on screen passes |
| `screen_epa` | Expected Points Added on the player's plays [standard/EPA] — on screen passes |
| `screen_first_downs` | First downs gained (1st) — on screen passes |
| `screen_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — on screen passes |
| `screen_grades_defense` | PFF grade, 0–100 (higher is better) — defense — on screen passes |
| `screen_grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties — on screen passes |
| `screen_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — on screen passes |
| `screen_grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) — on screen passes |
| `screen_grades_offense` | PFF grade, 0–100 (higher is better) — offense — on screen passes |
| `screen_grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties — on screen passes |
| `screen_grades_overall_tackle` | PFF grade, 0–100 (higher is better) — overall tackling — on screen passes |
| `screen_grades_pass` | PFF grade, 0–100 (higher is better) — passing — on screen passes |
| `screen_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — on screen passes |
| `screen_grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) — on screen passes |
| `screen_grades_run` | PFF grade, 0–100 (higher is better) — rushing — on screen passes |
| `screen_grades_run_defense` | PFF grade, 0–100 (higher is better) — run defense (RDEF) — on screen passes |
| `screen_grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) — on screen passes |
| `screen_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — on screen passes |
| `screen_interceptions` | Interceptions thrown (INT) — on screen passes |
| `screen_passing_snaps` | Passing snaps — snaps on pass plays — on screen passes |
| `screen_positive_epa_percent` | Percentage of plays with positive EPA [standard] — on screen passes |
| `screen_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — on screen passes |
| `screen_qb_rating` | NFL passer rating (NFL) — on screen passes |
| `screen_sack_percent` | Sack percentage — sacks per dropback [standard] — on screen passes |
| `screen_sacks` | Sacks taken by the passer (SK) — on screen passes |
| `screen_scrambles` | Scrambles — undesigned QB runs (SCR) — on screen passes |
| `screen_spikes` | Spikes — QB clock-stopping spikes [standard] — on screen passes |
| `screen_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — on screen passes |
| `screen_touchdowns` | Passing touchdowns (TD) — on screen passes |
| `screen_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — on screen passes |
| `screen_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — on screen passes |
| `screen_yards` | Passing yards (YDS) — on screen passes |
| `screen_ypa` | Yards per pass attempt (YPA) — on screen passes |
| `ypa_diff` | Yards-per-attempt difference between this report's splits (concept comparison) |

<details><summary>PFF key legend (verbatim)</summary>

- **Note**: Play Action data currently only available since 2012.
- **COM%**: Completion Percentage - the percentage of completions to pass attempts
- **DB%**: The percentage of dropbacks in the passing split
- **ATT**: Attempts - the number of times the passer threw the ball
- **YPA**: Yards per Attempt - the average number of passing yards gained per passing attempt
- **INT**: Interceptions - the number of interceptions thrown by the passer
- **PASS**: PFF Grade for Pass
- **FUM**: PFF Grade for HandsFumble
- **BTT%**: Big Time Throw Rate - the % of attempts that are BTTs
- **TWP%**: Turnover Worthy Play Rate - the % of attempts that are TWP
- **ADJ%**: Adjusted Completion Percentage - the % of aimed passes thrown on target (completions + drops / aimed)
- **DRP%**: Drops - on-target passes dropped by the receiver
- **HAT**: Hit As Thrown - the passer is hit by a defender while a pass is being thrown
- **DPR**: Total pressures of the passer of any kind (generated by the defense)
- **P2S%**: Percentage of Pressures Turned into Sacks
- **SCR**: Scrambles - undesigned runs by the QB
- **NFL**: NFL Passer Rating
- **DB**: Dropbacks - the number of times the QB dropped back to pass
- **COM**: Completions - the number of times the passer completed a pass
- **YDS**: Yards - the number of yards gained passing
- **TD**: Touchdowns - the number of touchdowns thrown by the passer
- **OFF**: PFF Grade for Offense
- **RUN**: PFF Grade for Rushing
- **BTT**: Big Time Throws - a pass with excellent ball location and timing, generally thrown further down the field and/or into a tighter window
- **TWP**: Turnover Worthy Plays - a pass that has a high percentage chance to be intercepted or a poor job of taking care of the ball and fumbling
- **aDoT**: Average Depth of Target
- **DRP**: Drops - on-target passes dropped by the receiver
- **BAT**: Batted Passes - the number of passes batted or deflected at the line of scrimage
- **TA**: Thrown Away - passes intentionally thrown out of play
- **SK**: Sacks - The number of times the passer was sacked
- **TTT**: Average Time to Throw on all dropbacks
- **1st**: First Downs

</details>

### `PFF_passing_depth.csv` — Passing Depth (554 cols)

_The ability to successfully throw the deep ball is one that not all quarterbacks possess. This report shows only passing attem_

Buckets: `left_behind_los`, `left_short`, `left_medium`, `left_deep`, `center_behind_los`, `center_short`, `center_medium`, `center_deep`, `right_behind_los`, `right_short`, `right_medium`, `right_deep`, `behind_los`, `short`, `medium`, `deep`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `base_attempts` | Pass attempts (ATT) — season total |
| `base_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — season total |
| `behind_los_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — thrown/caught behind the line of scrimmage |
| `behind_los_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — thrown/caught behind the line of scrimmage |
| `behind_los_attempts` | Pass attempts (ATT) — thrown/caught behind the line of scrimmage |
| `behind_los_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — thrown/caught behind the line of scrimmage |
| `behind_los_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — thrown/caught behind the line of scrimmage |
| `behind_los_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — thrown/caught behind the line of scrimmage |
| `behind_los_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — thrown/caught behind the line of scrimmage |
| `behind_los_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — thrown/caught behind the line of scrimmage |
| `behind_los_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — thrown/caught behind the line of scrimmage |
| `behind_los_completion_percent` | Completion percentage — completions/attempts (COM%) — thrown/caught behind the line of scrimmage |
| `behind_los_completions` | Completions (COM) — thrown/caught behind the line of scrimmage |
| `behind_los_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — thrown/caught behind the line of scrimmage |
| `behind_los_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — thrown/caught behind the line of scrimmage |
| `behind_los_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — thrown/caught behind the line of scrimmage |
| `behind_los_drops` | Drops — on-target passes dropped by the receiver (DRP) — thrown/caught behind the line of scrimmage |
| `behind_los_epa` | Expected Points Added on the player's plays [standard/EPA] — thrown/caught behind the line of scrimmage |
| `behind_los_first_downs` | First downs gained (1st) — thrown/caught behind the line of scrimmage |
| `behind_los_grades_pass` | PFF grade, 0–100 (higher is better) — passing — thrown/caught behind the line of scrimmage |
| `behind_los_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — thrown/caught behind the line of scrimmage |
| `behind_los_interceptions` | Interceptions thrown (INT) — thrown/caught behind the line of scrimmage |
| `behind_los_passing_snaps` | Passing snaps — snaps on pass plays — thrown/caught behind the line of scrimmage |
| `behind_los_positive_epa_percent` | Percentage of plays with positive EPA [standard] — thrown/caught behind the line of scrimmage |
| `behind_los_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — thrown/caught behind the line of scrimmage |
| `behind_los_qb_rating` | NFL passer rating (NFL) — thrown/caught behind the line of scrimmage |
| `behind_los_sack_percent` | Sack percentage — sacks per dropback [standard] — thrown/caught behind the line of scrimmage |
| `behind_los_sacks` | Sacks taken by the passer (SK) — thrown/caught behind the line of scrimmage |
| `behind_los_scrambles` | Scrambles — undesigned QB runs (SCR) — thrown/caught behind the line of scrimmage |
| `behind_los_spikes` | Spikes — QB clock-stopping spikes [standard] — thrown/caught behind the line of scrimmage |
| `behind_los_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — thrown/caught behind the line of scrimmage |
| `behind_los_touchdowns` | Passing touchdowns (TD) — thrown/caught behind the line of scrimmage |
| `behind_los_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — thrown/caught behind the line of scrimmage |
| `behind_los_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — thrown/caught behind the line of scrimmage |
| `behind_los_yards` | Passing yards (YDS) — thrown/caught behind the line of scrimmage |
| `behind_los_ypa` | Yards per pass attempt (YPA) — thrown/caught behind the line of scrimmage |
| `center_behind_los_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_attempts` | Pass attempts (ATT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_completions` | Completions (COM) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_first_downs` | First downs gained (1st) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_interceptions` | Interceptions thrown (INT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_qb_rating` | NFL passer rating (NFL) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_sacks` | Sacks taken by the passer (SK) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_touchdowns` | Passing touchdowns (TD) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_yards` | Passing yards (YDS) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_ypa` | Yards per pass attempt (YPA) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_deep_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_attempts` | Pass attempts (ATT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_completions` | Completions (COM) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_first_downs` | First downs gained (1st) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_interceptions` | Interceptions thrown (INT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_qb_rating` | NFL passer rating (NFL) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_sacks` | Sacks taken by the passer (SK) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_touchdowns` | Passing touchdowns (TD) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_yards` | Passing yards (YDS) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_ypa` | Yards per pass attempt (YPA) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_medium_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_attempts` | Pass attempts (ATT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_completions` | Completions (COM) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_first_downs` | First downs gained (1st) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_interceptions` | Interceptions thrown (INT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_qb_rating` | NFL passer rating (NFL) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_sacks` | Sacks taken by the passer (SK) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_touchdowns` | Passing touchdowns (TD) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_yards` | Passing yards (YDS) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_ypa` | Yards per pass attempt (YPA) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_short_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_attempts` | Pass attempts (ATT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_completions` | Completions (COM) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_first_downs` | First downs gained (1st) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_interceptions` | Interceptions thrown (INT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_qb_rating` | NFL passer rating (NFL) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_sacks` | Sacks taken by the passer (SK) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_touchdowns` | Passing touchdowns (TD) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_yards` | Passing yards (YDS) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_ypa` | Yards per pass attempt (YPA) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `deep_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — thrown/caught 20+ yards downfield |
| `deep_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — thrown/caught 20+ yards downfield |
| `deep_attempts` | Pass attempts (ATT) — thrown/caught 20+ yards downfield |
| `deep_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — thrown/caught 20+ yards downfield |
| `deep_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — thrown/caught 20+ yards downfield |
| `deep_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — thrown/caught 20+ yards downfield |
| `deep_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — thrown/caught 20+ yards downfield |
| `deep_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — thrown/caught 20+ yards downfield |
| `deep_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — thrown/caught 20+ yards downfield |
| `deep_completion_percent` | Completion percentage — completions/attempts (COM%) — thrown/caught 20+ yards downfield |
| `deep_completions` | Completions (COM) — thrown/caught 20+ yards downfield |
| `deep_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — thrown/caught 20+ yards downfield |
| `deep_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — thrown/caught 20+ yards downfield |
| `deep_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — thrown/caught 20+ yards downfield |
| `deep_drops` | Drops — on-target passes dropped by the receiver (DRP) — thrown/caught 20+ yards downfield |
| `deep_epa` | Expected Points Added on the player's plays [standard/EPA] — thrown/caught 20+ yards downfield |
| `deep_first_downs` | First downs gained (1st) — thrown/caught 20+ yards downfield |
| `deep_grades_pass` | PFF grade, 0–100 (higher is better) — passing — thrown/caught 20+ yards downfield |
| `deep_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — thrown/caught 20+ yards downfield |
| `deep_interceptions` | Interceptions thrown (INT) — thrown/caught 20+ yards downfield |
| `deep_passing_snaps` | Passing snaps — snaps on pass plays — thrown/caught 20+ yards downfield |
| `deep_positive_epa_percent` | Percentage of plays with positive EPA [standard] — thrown/caught 20+ yards downfield |
| `deep_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — thrown/caught 20+ yards downfield |
| `deep_qb_rating` | NFL passer rating (NFL) — thrown/caught 20+ yards downfield |
| `deep_sack_percent` | Sack percentage — sacks per dropback [standard] — thrown/caught 20+ yards downfield |
| `deep_sacks` | Sacks taken by the passer (SK) — thrown/caught 20+ yards downfield |
| `deep_scrambles` | Scrambles — undesigned QB runs (SCR) — thrown/caught 20+ yards downfield |
| `deep_spikes` | Spikes — QB clock-stopping spikes [standard] — thrown/caught 20+ yards downfield |
| `deep_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — thrown/caught 20+ yards downfield |
| `deep_touchdowns` | Passing touchdowns (TD) — thrown/caught 20+ yards downfield |
| `deep_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — thrown/caught 20+ yards downfield |
| `deep_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — thrown/caught 20+ yards downfield |
| `deep_yards` | Passing yards (YDS) — thrown/caught 20+ yards downfield |
| `deep_ypa` | Yards per pass attempt (YPA) — thrown/caught 20+ yards downfield |
| `franchise_id` | PFF unique team/franchise identifier |
| `left_behind_los_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_attempts` | Pass attempts (ATT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_completions` | Completions (COM) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_first_downs` | First downs gained (1st) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_interceptions` | Interceptions thrown (INT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_qb_rating` | NFL passer rating (NFL) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_sacks` | Sacks taken by the passer (SK) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_touchdowns` | Passing touchdowns (TD) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_yards` | Passing yards (YDS) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_ypa` | Yards per pass attempt (YPA) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_deep_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_attempts` | Pass attempts (ATT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_completions` | Completions (COM) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_first_downs` | First downs gained (1st) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_interceptions` | Interceptions thrown (INT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_qb_rating` | NFL passer rating (NFL) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_sacks` | Sacks taken by the passer (SK) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_touchdowns` | Passing touchdowns (TD) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_yards` | Passing yards (YDS) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_ypa` | Yards per pass attempt (YPA) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_medium_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_attempts` | Pass attempts (ATT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_completions` | Completions (COM) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_first_downs` | First downs gained (1st) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_interceptions` | Interceptions thrown (INT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_qb_rating` | NFL passer rating (NFL) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_sacks` | Sacks taken by the passer (SK) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_touchdowns` | Passing touchdowns (TD) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_yards` | Passing yards (YDS) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_ypa` | Yards per pass attempt (YPA) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_short_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_attempts` | Pass attempts (ATT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_completions` | Completions (COM) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_first_downs` | First downs gained (1st) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_interceptions` | Interceptions thrown (INT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_qb_rating` | NFL passer rating (NFL) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_sacks` | Sacks taken by the passer (SK) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_touchdowns` | Passing touchdowns (TD) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_yards` | Passing yards (YDS) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_ypa` | Yards per pass attempt (YPA) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `medium_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — thrown/caught 10–19 yards downfield |
| `medium_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — thrown/caught 10–19 yards downfield |
| `medium_attempts` | Pass attempts (ATT) — thrown/caught 10–19 yards downfield |
| `medium_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — thrown/caught 10–19 yards downfield |
| `medium_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — thrown/caught 10–19 yards downfield |
| `medium_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — thrown/caught 10–19 yards downfield |
| `medium_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — thrown/caught 10–19 yards downfield |
| `medium_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — thrown/caught 10–19 yards downfield |
| `medium_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — thrown/caught 10–19 yards downfield |
| `medium_completion_percent` | Completion percentage — completions/attempts (COM%) — thrown/caught 10–19 yards downfield |
| `medium_completions` | Completions (COM) — thrown/caught 10–19 yards downfield |
| `medium_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — thrown/caught 10–19 yards downfield |
| `medium_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — thrown/caught 10–19 yards downfield |
| `medium_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — thrown/caught 10–19 yards downfield |
| `medium_drops` | Drops — on-target passes dropped by the receiver (DRP) — thrown/caught 10–19 yards downfield |
| `medium_epa` | Expected Points Added on the player's plays [standard/EPA] — thrown/caught 10–19 yards downfield |
| `medium_first_downs` | First downs gained (1st) — thrown/caught 10–19 yards downfield |
| `medium_grades_pass` | PFF grade, 0–100 (higher is better) — passing — thrown/caught 10–19 yards downfield |
| `medium_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — thrown/caught 10–19 yards downfield |
| `medium_interceptions` | Interceptions thrown (INT) — thrown/caught 10–19 yards downfield |
| `medium_passing_snaps` | Passing snaps — snaps on pass plays — thrown/caught 10–19 yards downfield |
| `medium_positive_epa_percent` | Percentage of plays with positive EPA [standard] — thrown/caught 10–19 yards downfield |
| `medium_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — thrown/caught 10–19 yards downfield |
| `medium_qb_rating` | NFL passer rating (NFL) — thrown/caught 10–19 yards downfield |
| `medium_sack_percent` | Sack percentage — sacks per dropback [standard] — thrown/caught 10–19 yards downfield |
| `medium_sacks` | Sacks taken by the passer (SK) — thrown/caught 10–19 yards downfield |
| `medium_scrambles` | Scrambles — undesigned QB runs (SCR) — thrown/caught 10–19 yards downfield |
| `medium_spikes` | Spikes — QB clock-stopping spikes [standard] — thrown/caught 10–19 yards downfield |
| `medium_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — thrown/caught 10–19 yards downfield |
| `medium_touchdowns` | Passing touchdowns (TD) — thrown/caught 10–19 yards downfield |
| `medium_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — thrown/caught 10–19 yards downfield |
| `medium_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — thrown/caught 10–19 yards downfield |
| `medium_yards` | Passing yards (YDS) — thrown/caught 10–19 yards downfield |
| `medium_ypa` | Yards per pass attempt (YPA) — thrown/caught 10–19 yards downfield |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `right_behind_los_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_attempts` | Pass attempts (ATT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_completions` | Completions (COM) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_first_downs` | First downs gained (1st) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_interceptions` | Interceptions thrown (INT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_qb_rating` | NFL passer rating (NFL) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_sacks` | Sacks taken by the passer (SK) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_touchdowns` | Passing touchdowns (TD) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_yards` | Passing yards (YDS) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_ypa` | Yards per pass attempt (YPA) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_deep_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_attempts` | Pass attempts (ATT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_completions` | Completions (COM) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_first_downs` | First downs gained (1st) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_interceptions` | Interceptions thrown (INT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_qb_rating` | NFL passer rating (NFL) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_sacks` | Sacks taken by the passer (SK) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_touchdowns` | Passing touchdowns (TD) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_yards` | Passing yards (YDS) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_ypa` | Yards per pass attempt (YPA) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_medium_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_attempts` | Pass attempts (ATT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_completions` | Completions (COM) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_first_downs` | First downs gained (1st) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_interceptions` | Interceptions thrown (INT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_qb_rating` | NFL passer rating (NFL) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_sacks` | Sacks taken by the passer (SK) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_touchdowns` | Passing touchdowns (TD) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_yards` | Passing yards (YDS) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_ypa` | Yards per pass attempt (YPA) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_short_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_attempts` | Pass attempts (ATT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_completion_percent` | Completion percentage — completions/attempts (COM%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_completions` | Completions (COM) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_first_downs` | First downs gained (1st) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_grades_pass` | PFF grade, 0–100 (higher is better) — passing — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_interceptions` | Interceptions thrown (INT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_passing_snaps` | Passing snaps — snaps on pass plays — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_qb_rating` | NFL passer rating (NFL) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_sack_percent` | Sack percentage — sacks per dropback [standard] — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_sacks` | Sacks taken by the passer (SK) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_scrambles` | Scrambles — undesigned QB runs (SCR) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_spikes` | Spikes — QB clock-stopping spikes [standard] — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_touchdowns` | Passing touchdowns (TD) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_yards` | Passing yards (YDS) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_ypa` | Yards per pass attempt (YPA) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `short_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — thrown/caught 0–9 yards downfield |
| `short_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — thrown/caught 0–9 yards downfield |
| `short_attempts` | Pass attempts (ATT) — thrown/caught 0–9 yards downfield |
| `short_attempts_percent` | Percentage of the player's attempts in this split (ATT%) — thrown/caught 0–9 yards downfield |
| `short_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — thrown/caught 0–9 yards downfield |
| `short_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — thrown/caught 0–9 yards downfield |
| `short_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — thrown/caught 0–9 yards downfield |
| `short_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — thrown/caught 0–9 yards downfield |
| `short_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — thrown/caught 0–9 yards downfield |
| `short_completion_percent` | Completion percentage — completions/attempts (COM%) — thrown/caught 0–9 yards downfield |
| `short_completions` | Completions (COM) — thrown/caught 0–9 yards downfield |
| `short_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — thrown/caught 0–9 yards downfield |
| `short_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — thrown/caught 0–9 yards downfield |
| `short_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — thrown/caught 0–9 yards downfield |
| `short_drops` | Drops — on-target passes dropped by the receiver (DRP) — thrown/caught 0–9 yards downfield |
| `short_epa` | Expected Points Added on the player's plays [standard/EPA] — thrown/caught 0–9 yards downfield |
| `short_first_downs` | First downs gained (1st) — thrown/caught 0–9 yards downfield |
| `short_grades_pass` | PFF grade, 0–100 (higher is better) — passing — thrown/caught 0–9 yards downfield |
| `short_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — thrown/caught 0–9 yards downfield |
| `short_interceptions` | Interceptions thrown (INT) — thrown/caught 0–9 yards downfield |
| `short_passing_snaps` | Passing snaps — snaps on pass plays — thrown/caught 0–9 yards downfield |
| `short_positive_epa_percent` | Percentage of plays with positive EPA [standard] — thrown/caught 0–9 yards downfield |
| `short_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — thrown/caught 0–9 yards downfield |
| `short_qb_rating` | NFL passer rating (NFL) — thrown/caught 0–9 yards downfield |
| `short_sack_percent` | Sack percentage — sacks per dropback [standard] — thrown/caught 0–9 yards downfield |
| `short_sacks` | Sacks taken by the passer (SK) — thrown/caught 0–9 yards downfield |
| `short_scrambles` | Scrambles — undesigned QB runs (SCR) — thrown/caught 0–9 yards downfield |
| `short_spikes` | Spikes — QB clock-stopping spikes [standard] — thrown/caught 0–9 yards downfield |
| `short_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — thrown/caught 0–9 yards downfield |
| `short_touchdowns` | Passing touchdowns (TD) — thrown/caught 0–9 yards downfield |
| `short_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — thrown/caught 0–9 yards downfield |
| `short_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — thrown/caught 0–9 yards downfield |
| `short_yards` | Passing yards (YDS) — thrown/caught 0–9 yards downfield |
| `short_ypa` | Yards per pass attempt (YPA) — thrown/caught 0–9 yards downfield |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **ATT**: Attempts - the number of times the passer threw the ball
- **COM%**: Completion Percentage - the percentage of completions to pass attempts
- **YPA**: Yards per Attempt - the average number of passing yards gained per passing attempt
- **INT**: Interceptions - the number of interceptions thrown by the passer
- **BTT**: Big Time Throws - a pass with excellent ball location and timing, generally thrown further down the field and/or into a tighter window
- **TWP**: Turnover Worthy Plays - a pass that has a high percentage chance to be intercepted or a poor job of taking care of the ball and fumbling
- **aDoT**: Average Depth of Target
- **DRP**: Drops - on-target passes dropped by the receiver
- **BAT**: Batted Passes - the number of passes batted or deflected at the line of scrimage
- **DPR**: Total pressures of the passer of any kind (generated by the defense)
- **1st**: First Downs
- **POS**: Season position
- **DB**: Dropbacks - the number of times the QB dropped back to pass
- **ATT%**: The percentage of attempts
- **COM**: Completions - the number of times the passer completed a pass
- **YDS**: Yards - the number of yards gained passing
- **TD**: Touchdowns - the number of touchdowns thrown by the passer
- **PASS**: PFF Grade for Pass
- **BTT%**: Big Time Throw Rate - the % of attempts that are BTTs
- **TWP%**: Turnover Worthy Play Rate - the % of attempts that are TWP
- **ADJ%**: Adjusted Completion Percentage - the % of aimed passes thrown on target (completions + drops / aimed)
- **DRP%**: Drops - on-target passes dropped by the receiver
- **HAT**: Hit As Thrown - the passer is hit by a defender while a pass is being thrown
- **TTT**: Average Time to Throw on all dropbacks
- **NFL**: NFL Passer Rating

</details>

### `PFF_passing_pressure.csv` — Passing Pressure (197 cols)

_Dealing with pressure is a huge part of playing quarterback in the NFL. This report reflects performance on plays with the sele_

Buckets: `no_blitz`, `blitz`, `no_pressure`, `pressure`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `base_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — season total |
| `blitz_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — vs a blitz (5+ rushers) |
| `blitz_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — vs a blitz (5+ rushers) |
| `blitz_attempts` | Pass attempts (ATT) — vs a blitz (5+ rushers) |
| `blitz_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — vs a blitz (5+ rushers) |
| `blitz_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — vs a blitz (5+ rushers) |
| `blitz_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — vs a blitz (5+ rushers) |
| `blitz_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — vs a blitz (5+ rushers) |
| `blitz_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — vs a blitz (5+ rushers) |
| `blitz_completion_percent` | Completion percentage — completions/attempts (COM%) — vs a blitz (5+ rushers) |
| `blitz_completions` | Completions (COM) — vs a blitz (5+ rushers) |
| `blitz_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — vs a blitz (5+ rushers) |
| `blitz_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — vs a blitz (5+ rushers) |
| `blitz_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — vs a blitz (5+ rushers) |
| `blitz_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — vs a blitz (5+ rushers) |
| `blitz_drops` | Drops — on-target passes dropped by the receiver (DRP) — vs a blitz (5+ rushers) |
| `blitz_epa` | Expected Points Added on the player's plays [standard/EPA] — vs a blitz (5+ rushers) |
| `blitz_first_downs` | First downs gained (1st) — vs a blitz (5+ rushers) |
| `blitz_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — vs a blitz (5+ rushers) |
| `blitz_grades_defense` | PFF grade, 0–100 (higher is better) — defense — vs a blitz (5+ rushers) |
| `blitz_grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties — vs a blitz (5+ rushers) |
| `blitz_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — vs a blitz (5+ rushers) |
| `blitz_grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) — vs a blitz (5+ rushers) |
| `blitz_grades_offense` | PFF grade, 0–100 (higher is better) — offense — vs a blitz (5+ rushers) |
| `blitz_grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties — vs a blitz (5+ rushers) |
| `blitz_grades_overall_tackle` | PFF grade, 0–100 (higher is better) — overall tackling — vs a blitz (5+ rushers) |
| `blitz_grades_pass` | PFF grade, 0–100 (higher is better) — passing — vs a blitz (5+ rushers) |
| `blitz_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — vs a blitz (5+ rushers) |
| `blitz_grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) — vs a blitz (5+ rushers) |
| `blitz_grades_run` | PFF grade, 0–100 (higher is better) — rushing — vs a blitz (5+ rushers) |
| `blitz_grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) — vs a blitz (5+ rushers) |
| `blitz_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — vs a blitz (5+ rushers) |
| `blitz_interceptions` | Interceptions thrown (INT) — vs a blitz (5+ rushers) |
| `blitz_passing_snaps` | Passing snaps — snaps on pass plays — vs a blitz (5+ rushers) |
| `blitz_positive_epa_percent` | Percentage of plays with positive EPA [standard] — vs a blitz (5+ rushers) |
| `blitz_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — vs a blitz (5+ rushers) |
| `blitz_qb_rating` | NFL passer rating (NFL) — vs a blitz (5+ rushers) |
| `blitz_sack_percent` | Sack percentage — sacks per dropback [standard] — vs a blitz (5+ rushers) |
| `blitz_sacks` | Sacks taken by the passer (SK) — vs a blitz (5+ rushers) |
| `blitz_scrambles` | Scrambles — undesigned QB runs (SCR) — vs a blitz (5+ rushers) |
| `blitz_spikes` | Spikes — QB clock-stopping spikes [standard] — vs a blitz (5+ rushers) |
| `blitz_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — vs a blitz (5+ rushers) |
| `blitz_touchdowns` | Passing touchdowns (TD) — vs a blitz (5+ rushers) |
| `blitz_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — vs a blitz (5+ rushers) |
| `blitz_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — vs a blitz (5+ rushers) |
| `blitz_yards` | Passing yards (YDS) — vs a blitz (5+ rushers) |
| `blitz_ypa` | Yards per pass attempt (YPA) — vs a blitz (5+ rushers) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) |
| `grades_offense` | PFF grade, 0–100 (higher is better) — offense |
| `grades_pass` | PFF grade, 0–100 (higher is better) — passing |
| `grades_run` | PFF grade, 0–100 (higher is better) — rushing |
| `no_blitz_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — vs no blitz |
| `no_blitz_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — vs no blitz |
| `no_blitz_attempts` | Pass attempts (ATT) — vs no blitz |
| `no_blitz_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — vs no blitz |
| `no_blitz_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — vs no blitz |
| `no_blitz_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — vs no blitz |
| `no_blitz_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — vs no blitz |
| `no_blitz_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — vs no blitz |
| `no_blitz_completion_percent` | Completion percentage — completions/attempts (COM%) — vs no blitz |
| `no_blitz_completions` | Completions (COM) — vs no blitz |
| `no_blitz_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — vs no blitz |
| `no_blitz_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — vs no blitz |
| `no_blitz_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — vs no blitz |
| `no_blitz_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — vs no blitz |
| `no_blitz_drops` | Drops — on-target passes dropped by the receiver (DRP) — vs no blitz |
| `no_blitz_epa` | Expected Points Added on the player's plays [standard/EPA] — vs no blitz |
| `no_blitz_first_downs` | First downs gained (1st) — vs no blitz |
| `no_blitz_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — vs no blitz |
| `no_blitz_grades_defense` | PFF grade, 0–100 (higher is better) — defense — vs no blitz |
| `no_blitz_grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties — vs no blitz |
| `no_blitz_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — vs no blitz |
| `no_blitz_grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) — vs no blitz |
| `no_blitz_grades_offense` | PFF grade, 0–100 (higher is better) — offense — vs no blitz |
| `no_blitz_grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties — vs no blitz |
| `no_blitz_grades_overall_tackle` | PFF grade, 0–100 (higher is better) — overall tackling — vs no blitz |
| `no_blitz_grades_pass` | PFF grade, 0–100 (higher is better) — passing — vs no blitz |
| `no_blitz_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — vs no blitz |
| `no_blitz_grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) — vs no blitz |
| `no_blitz_grades_run` | PFF grade, 0–100 (higher is better) — rushing — vs no blitz |
| `no_blitz_grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) — vs no blitz |
| `no_blitz_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — vs no blitz |
| `no_blitz_interceptions` | Interceptions thrown (INT) — vs no blitz |
| `no_blitz_passing_snaps` | Passing snaps — snaps on pass plays — vs no blitz |
| `no_blitz_positive_epa_percent` | Percentage of plays with positive EPA [standard] — vs no blitz |
| `no_blitz_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — vs no blitz |
| `no_blitz_qb_rating` | NFL passer rating (NFL) — vs no blitz |
| `no_blitz_sack_percent` | Sack percentage — sacks per dropback [standard] — vs no blitz |
| `no_blitz_sacks` | Sacks taken by the passer (SK) — vs no blitz |
| `no_blitz_scrambles` | Scrambles — undesigned QB runs (SCR) — vs no blitz |
| `no_blitz_spikes` | Spikes — QB clock-stopping spikes [standard] — vs no blitz |
| `no_blitz_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — vs no blitz |
| `no_blitz_touchdowns` | Passing touchdowns (TD) — vs no blitz |
| `no_blitz_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — vs no blitz |
| `no_blitz_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — vs no blitz |
| `no_blitz_yards` | Passing yards (YDS) — vs no blitz |
| `no_blitz_ypa` | Yards per pass attempt (YPA) — vs no blitz |
| `no_pressure_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — on plays with no pressure |
| `no_pressure_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — on plays with no pressure |
| `no_pressure_attempts` | Pass attempts (ATT) — on plays with no pressure |
| `no_pressure_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — on plays with no pressure |
| `no_pressure_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — on plays with no pressure |
| `no_pressure_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — on plays with no pressure |
| `no_pressure_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — on plays with no pressure |
| `no_pressure_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — on plays with no pressure |
| `no_pressure_completion_percent` | Completion percentage — completions/attempts (COM%) — on plays with no pressure |
| `no_pressure_completions` | Completions (COM) — on plays with no pressure |
| `no_pressure_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — on plays with no pressure |
| `no_pressure_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — on plays with no pressure |
| `no_pressure_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — on plays with no pressure |
| `no_pressure_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — on plays with no pressure |
| `no_pressure_drops` | Drops — on-target passes dropped by the receiver (DRP) — on plays with no pressure |
| `no_pressure_epa` | Expected Points Added on the player's plays [standard/EPA] — on plays with no pressure |
| `no_pressure_first_downs` | First downs gained (1st) — on plays with no pressure |
| `no_pressure_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — on plays with no pressure |
| `no_pressure_grades_defense` | PFF grade, 0–100 (higher is better) — defense — on plays with no pressure |
| `no_pressure_grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties — on plays with no pressure |
| `no_pressure_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — on plays with no pressure |
| `no_pressure_grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) — on plays with no pressure |
| `no_pressure_grades_offense` | PFF grade, 0–100 (higher is better) — offense — on plays with no pressure |
| `no_pressure_grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties — on plays with no pressure |
| `no_pressure_grades_overall_tackle` | PFF grade, 0–100 (higher is better) — overall tackling — on plays with no pressure |
| `no_pressure_grades_pass` | PFF grade, 0–100 (higher is better) — passing — on plays with no pressure |
| `no_pressure_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — on plays with no pressure |
| `no_pressure_grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) — on plays with no pressure |
| `no_pressure_grades_run` | PFF grade, 0–100 (higher is better) — rushing — on plays with no pressure |
| `no_pressure_grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) — on plays with no pressure |
| `no_pressure_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — on plays with no pressure |
| `no_pressure_interceptions` | Interceptions thrown (INT) — on plays with no pressure |
| `no_pressure_passing_snaps` | Passing snaps — snaps on pass plays — on plays with no pressure |
| `no_pressure_positive_epa_percent` | Percentage of plays with positive EPA [standard] — on plays with no pressure |
| `no_pressure_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — on plays with no pressure |
| `no_pressure_qb_rating` | NFL passer rating (NFL) — on plays with no pressure |
| `no_pressure_sack_percent` | Sack percentage — sacks per dropback [standard] — on plays with no pressure |
| `no_pressure_sacks` | Sacks taken by the passer (SK) — on plays with no pressure |
| `no_pressure_scrambles` | Scrambles — undesigned QB runs (SCR) — on plays with no pressure |
| `no_pressure_spikes` | Spikes — QB clock-stopping spikes [standard] — on plays with no pressure |
| `no_pressure_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — on plays with no pressure |
| `no_pressure_touchdowns` | Passing touchdowns (TD) — on plays with no pressure |
| `no_pressure_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — on plays with no pressure |
| `no_pressure_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — on plays with no pressure |
| `no_pressure_yards` | Passing yards (YDS) — on plays with no pressure |
| `no_pressure_ypa` | Yards per pass attempt (YPA) — on plays with no pressure |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `pressure_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — on plays with pressure |
| `pressure_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — on plays with pressure |
| `pressure_attempts` | Pass attempts (ATT) — on plays with pressure |
| `pressure_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — on plays with pressure |
| `pressure_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — on plays with pressure |
| `pressure_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — on plays with pressure |
| `pressure_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — on plays with pressure |
| `pressure_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — on plays with pressure |
| `pressure_completion_percent` | Completion percentage — completions/attempts (COM%) — on plays with pressure |
| `pressure_completions` | Completions (COM) — on plays with pressure |
| `pressure_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — on plays with pressure |
| `pressure_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — on plays with pressure |
| `pressure_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — on plays with pressure |
| `pressure_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — on plays with pressure |
| `pressure_drops` | Drops — on-target passes dropped by the receiver (DRP) — on plays with pressure |
| `pressure_epa` | Expected Points Added on the player's plays [standard/EPA] — on plays with pressure |
| `pressure_first_downs` | First downs gained (1st) — on plays with pressure |
| `pressure_grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) — on plays with pressure |
| `pressure_grades_defense` | PFF grade, 0–100 (higher is better) — defense — on plays with pressure |
| `pressure_grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties — on plays with pressure |
| `pressure_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — on plays with pressure |
| `pressure_grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) — on plays with pressure |
| `pressure_grades_offense` | PFF grade, 0–100 (higher is better) — offense — on plays with pressure |
| `pressure_grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties — on plays with pressure |
| `pressure_grades_overall_tackle` | PFF grade, 0–100 (higher is better) — overall tackling — on plays with pressure |
| `pressure_grades_pass` | PFF grade, 0–100 (higher is better) — passing — on plays with pressure |
| `pressure_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — on plays with pressure |
| `pressure_grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) — on plays with pressure |
| `pressure_grades_run` | PFF grade, 0–100 (higher is better) — rushing — on plays with pressure |
| `pressure_grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) — on plays with pressure |
| `pressure_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — on plays with pressure |
| `pressure_interceptions` | Interceptions thrown (INT) — on plays with pressure |
| `pressure_passing_snaps` | Passing snaps — snaps on pass plays — on plays with pressure |
| `pressure_positive_epa_percent` | Percentage of plays with positive EPA [standard] — on plays with pressure |
| `pressure_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — on plays with pressure |
| `pressure_qb_rating` | NFL passer rating (NFL) — on plays with pressure |
| `pressure_sack_percent` | Sack percentage — sacks per dropback [standard] — on plays with pressure |
| `pressure_sacks` | Sacks taken by the passer (SK) — on plays with pressure |
| `pressure_scrambles` | Scrambles — undesigned QB runs (SCR) — on plays with pressure |
| `pressure_spikes` | Spikes — QB clock-stopping spikes [standard] — on plays with pressure |
| `pressure_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — on plays with pressure |
| `pressure_touchdowns` | Passing touchdowns (TD) — on plays with pressure |
| `pressure_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — on plays with pressure |
| `pressure_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — on plays with pressure |
| `pressure_yards` | Passing yards (YDS) — on plays with pressure |
| `pressure_ypa` | Yards per pass attempt (YPA) — on plays with pressure |

<details><summary>PFF key legend (verbatim)</summary>

- **DB**: Dropbacks - the number of times the QB dropped back to pass
- **COM**: Completions - the number of times the passer completed a pass
- **YDS**: Yards - the number of yards gained passing
- **TD**: Touchdowns - the number of touchdowns thrown by the passer
- **OFF**: PFF Grade for Offense
- **RUN**: PFF Grade for Rushing
- **BTT**: Big Time Throws - a pass with excellent ball location and timing, generally thrown further down the field and/or into a tighter window
- **TWP**: Turnover Worthy Plays - a pass that has a high percentage chance to be intercepted or a poor job of taking care of the ball and fumbling
- **aDoT**: Average Depth of Target
- **DRP**: Drops - on-target passes dropped by the receiver
- **BAT**: Batted Passes - the number of passes batted or deflected at the line of scrimage
- **TA**: Thrown Away - passes intentionally thrown out of play
- **SK**: Sacks - The number of times the passer was sacked
- **TTT**: Average Time to Throw on all dropbacks
- **1st**: First Downs -cted pressure level.
- **DB%**: The percentage of dropbacks in the passing split
- **ATT**: Attempts - the number of times the passer threw the ball
- **COM%**: Completion Percentage - the percentage of completions to pass attempts
- **YPA**: Yards per Attempt - the average number of passing yards gained per passing attempt
- **INT**: Interceptions - the number of interceptions thrown by the passer
- **PASS**: PFF Grade for Pass
- **FUM**: PFF Grade for HandsFumble
- **BTT%**: Big Time Throw Rate - the % of attempts that are BTTs
- **TWP%**: Turnover Worthy Play Rate - the % of attempts that are TWP
- **ADJ%**: Adjusted Completion Percentage - the % of aimed passes thrown on target (completions + drops / aimed)
- **DRP%**: Drops - on-target passes dropped by the receiver
- **HAT**: Hit As Thrown - the passer is hit by a defender while a pass is being thrown
- **DPR**: Total pressures of the passer of any kind (generated by the defense)
- **P2S%**: Percentage of Pressures Turned into Sacks
- **SCR**: Scrambles - undesigned runs by the QB
- **NFL**: NFL Passer Rating

</details>

### `PFF_passing_summary.csv` — Passing General (44 cols)

_Grades and base passing stats._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) |
| `aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) |
| `attempts` | Pass attempts (ATT) |
| `avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) |
| `avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) |
| `bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) |
| `big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) |
| `btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) |
| `completion_percent` | Completion percentage — completions/attempts (COM%) |
| `completions` | Completions (COM) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) |
| `drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) |
| `dropbacks` | Dropbacks — times the QB dropped back to pass (DB) |
| `drops` | Drops — on-target passes dropped by the receiver (DRP) |
| `epa` | Expected Points Added on the player's plays [standard/EPA] |
| `first_downs` | First downs gained (1st) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) |
| `grades_offense` | PFF grade, 0–100 (higher is better) — offense |
| `grades_pass` | PFF grade, 0–100 (higher is better) — passing |
| `grades_run` | PFF grade, 0–100 (higher is better) — rushing |
| `hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) |
| `interceptions` | Interceptions thrown (INT) |
| `passing_snaps` | Passing snaps — snaps on pass plays |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `positive_epa_percent` | Percentage of plays with positive EPA [standard] |
| `pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) |
| `qb_rating` | NFL passer rating (NFL) |
| `sack_percent` | Sack percentage — sacks per dropback [standard] |
| `sacks` | Sacks taken by the passer (SK) |
| `scrambles` | Scrambles — undesigned QB runs (SCR) |
| `spikes` | Spikes — QB clock-stopping spikes [standard] |
| `thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) |
| `touchdowns` | Passing touchdowns (TD) |
| `turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) |
| `twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) |
| `yards` | Passing yards (YDS) |
| `ypa` | Yards per pass attempt (YPA) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **ATT**: Attempts - the number of times the passer threw the ball
- **COM%**: Completion Percentage - the percentage of completions to pass attempts
- **YPA**: Yards per Attempt - the average number of passing yards gained per passing attempt
- **INT**: Interceptions - the number of interceptions thrown by the passer
- **PASS**: PFF Grade for Pass
- **FUM**: PFF Grade for HandsFumble
- **BTT%**: Big Time Throw Rate - the % of attempts that are BTTs
- **TWP%**: Turnover Worthy Play Rate - the % of attempts that are TWP
- **ADJ%**: Adjusted Completion Percentage - the % of aimed passes thrown on target (completions + drops / aimed)
- **DRP%**: Drops - on-target passes dropped by the receiver
- **HAT**: Hit As Thrown - the passer is hit by a defender while a pass is being thrown
- **DPR**: Total pressures of the passer of any kind (generated by the defense)
- **P2S%**: Percentage of Pressures Turned into Sacks
- **SCR**: Scrambles - undesigned runs by the QB
- **NFL**: NFL Passer Rating
- **POS**: Season position
- **DB**: Dropbacks - the number of times the QB dropped back to pass
- **COM**: Completions - the number of times the passer completed a pass
- **YDS**: Yards - the number of yards gained passing
- **TD**: Touchdowns - the number of touchdowns thrown by the passer
- **OFF**: PFF Grade for Offense
- **RUN**: PFF Grade for Rushing
- **BTT**: Big Time Throws - a pass with excellent ball location and timing, generally thrown further down the field and/or into a tighter window
- **TWP**: Turnover Worthy Plays - a pass that has a high percentage chance to be intercepted or a poor job of taking care of the ball and fumbling
- **aDoT**: Average Depth of Target
- **DRP**: Drops - on-target passes dropped by the receiver
- **BAT**: Batted Passes - the number of passes batted or deflected at the line of scrimage
- **TA**: Thrown Away - passes intentionally thrown out of play
- **SK**: Sacks - The number of times the passer was sacked
- **TTT**: Average Time to Throw on all dropbacks
- **1st**: First Downs
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties

</details>

### `PFF_punting_summary.csv` — Punting (29 cols)

_Grades and base punting stats._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `attempts` | Punt attempts (ATT) |
| `attempts_with_hangtime` | Attempts with hangtime recorded |
| `average_hangtime` | Average hangtime, seconds (AVG) |
| `average_net_yards` | Average net yards per punt (NET) |
| `average_yards_per_attempt` | Average gross yards per punt (YPA) |
| `average_yards_per_return` | Average return yards allowed per return (YPR) |
| `blocks` | Punts blocked (BLK) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `downeds` | Punts downed by the kicking team (DWN) |
| `fair_catches` | Fair catches induced on punts (FC) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_punter` | PFF grade, 0–100 (higher is better) — punting (PUNT) |
| `inside_twenties` | Punts inside the 20-yard line (I20) |
| `long` | Longest punt, yards (LNG) |
| `out_of_bounds` | Punts out of bounds (OOB) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `percent_returned` | Percentage of punts returned (RET%) |
| `return_yards` | Return yards allowed on punts |
| `returns` | Returns (RET) |
| `snaps` | Snaps |
| `total_hangtime` | Total hangtime, seconds |
| `total_net_yards` | Total net punting yards |
| `touchbacks` | Touchbacks (TB) |
| `yards` | Gross punt yardage (YDS) |

<details><summary>PFF key legend (verbatim)</summary>

- **Note**: Punting data currently only available since 2013.
- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **ATT**: Punt Attempts
- **YPA**: Average Yards per Punt Attempt
- **LNG**: Longest
- **BLK**: Punts Blocked
- **RET**: # of Kicks returned
- **YPR**: Return Yards Per Return
- **OOB**: Kicks out of bounds
- **FC**: Fair Catches
- **AVG**: Average Kick Hangtime (seconds)
- **POS**: Season position
- **PUNT**: PFF Grade for Punts
- **YDS**: Punt Yardage
- **NET**: Average Net Yards per Punt Attempt
- **120**: Kicks inside the 20 yard line
- **RET%**: Percentage of Kicks returned
- **YDS**: Return Yards
- **TB**: Touchbacks
- **DWN**: Kick downed by the kicking team
- **ATT**: Attempts with Hangtime

</details>

### `PFF_receiving_concept.csv` — Receiving Concept (71 cols)

_Grades and receiving stats when in the slot or on screens_

Buckets: `screen`, `slot`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `base_targets` | Targets (TGT) — season total |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `screen_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — on screen passes |
| `screen_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — on screen passes |
| `screen_caught_percent` | Catch rate — receptions/targets (REC%) — on screen passes |
| `screen_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — on screen passes |
| `screen_contested_receptions` | Contested catches made in tight coverage (CTC) — on screen passes |
| `screen_contested_targets` | Contested targets (CTT) — on screen passes |
| `screen_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — on screen passes |
| `screen_drops` | Drops — on-target passes dropped by the receiver (DRP) — on screen passes |
| `screen_epa` | Expected Points Added on the player's plays [standard/EPA] — on screen passes |
| `screen_first_downs` | First downs gained (1st) — on screen passes |
| `screen_fumbles` | Fumbles — on screen passes |
| `screen_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — on screen passes |
| `screen_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — on screen passes |
| `screen_interceptions` | Interceptions on targets to this receiver (INT) — on screen passes |
| `screen_longest` | Longest reception (LNG) — on screen passes |
| `screen_pass_block_rate` | Share of pass plays the player spent pass blocking — on screen passes |
| `screen_pass_blocks` | Pass-block snaps — on screen passes |
| `screen_pass_plays` | Pass plays the player was on the field for — on screen passes |
| `screen_positive_epa_percent` | Percentage of plays with positive EPA [standard] — on screen passes |
| `screen_receptions` | Receptions (REC) — on screen passes |
| `screen_route_rate` | Share of pass plays on which the player ran a route — on screen passes |
| `screen_routes` | Routes run — on screen passes |
| `screen_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — on screen passes |
| `screen_targets` | Targets (TGT) — on screen passes |
| `screen_targets_percent` | Target rate — targets per snap (TGT%) — on screen passes |
| `screen_touchdowns` | Receiving touchdowns (TD) — on screen passes |
| `screen_yards` | Receiving yards (YDS) — on screen passes |
| `screen_yards_after_catch` | Yards after catch (YAC) — on screen passes |
| `screen_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — on screen passes |
| `screen_yards_per_reception` | Yards per reception (Y/REC) — on screen passes |
| `screen_yprr` | Yards per route run (Y/RR) — on screen passes |
| `slot_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) |
| `slot_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) |
| `slot_caught_percent` | Catch rate — receptions/targets (REC%) |
| `slot_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) |
| `slot_contested_receptions` | Contested catches made in tight coverage (CTC) |
| `slot_contested_targets` | Contested targets (CTT) |
| `slot_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) |
| `slot_drops` | Drops — on-target passes dropped by the receiver (DRP) |
| `slot_epa` | Expected Points Added on the player's plays [standard/EPA] |
| `slot_first_downs` | First downs gained (1st) |
| `slot_fumbles` | Fumbles |
| `slot_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) |
| `slot_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) |
| `slot_interceptions` | Interceptions on targets to this receiver (INT) |
| `slot_longest` | Longest reception (LNG) |
| `slot_pass_block_rate` | Share of pass plays the player spent pass blocking |
| `slot_pass_blocks` | Pass-block snaps |
| `slot_pass_plays` | Pass plays the player was on the field for |
| `slot_positive_epa_percent` | Percentage of plays with positive EPA [standard] |
| `slot_receptions` | Receptions (REC) |
| `slot_route_rate` | Share of pass plays on which the player ran a route |
| `slot_routes` | Routes run |
| `slot_targeted_qb_rating` | Passer rating when this player is targeted (RTG) |
| `slot_targets` | Targets (TGT) |
| `slot_targets_percent` | Target rate — targets per snap (TGT%) |
| `slot_touchdowns` | Receiving touchdowns (TD) |
| `slot_yards` | Receiving yards (YDS) |
| `slot_yards_after_catch` | Yards after catch (YAC) |
| `slot_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) |
| `slot_yards_per_reception` | Yards per reception (Y/REC) |
| `slot_yprr` | Yards per route run (Y/RR) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **TGT%**: The percentage of targets to snaps
- **REC**: Receptions
- **YDS**: Receiving Yards
- **TD**: Receiving TD
- **DROP**: PFF Grade for HandsDrop
- **YAC/REC**: Yards After Catch per Reception
- **aDoT**: Average Depth of Target
- **DRP%**: Drops - on-target passes dropped by the receiver
- **CTC**: Contested Catches
- **INT**: Receiving Interceptions
- **MTF**: Missed Tackles Forced after a Reception
- **RTG**: NFL Passer Rating when targeted
- **POS**: Season position
- **TGT**: Receiving Targets
- **REC%**: Percentage of targets caught
- **Y/REC**: Yards per Reception
- **RECV**: PFF Grade for Pass Routes
- **YAC**: Yards After Catch
- **Y/RR**: Yards per Route Run
- **DRP**: Drops - on-target passes dropped by the receiver
- **CTT**: Contested Targets
- **CTC%**: Contested Catch Rate
- **FUM**: Fumbles
- **1st**: First Downs

</details>

### `PFF_receiving_depth.csv` — Receiving Depth (505 cols)

_Who's doing damage downfield? This report shows only receiving targets at the selected distances._

Buckets: `left_behind_los`, `left_short`, `left_medium`, `left_deep`, `center_behind_los`, `center_short`, `center_medium`, `center_deep`, `right_behind_los`, `right_short`, `right_medium`, `right_deep`, `behind_los`, `short`, `medium`, `deep`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `base_targets` | Targets (TGT) — season total |
| `behind_los_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — thrown/caught behind the line of scrimmage |
| `behind_los_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — thrown/caught behind the line of scrimmage |
| `behind_los_caught_percent` | Catch rate — receptions/targets (REC%) — thrown/caught behind the line of scrimmage |
| `behind_los_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — thrown/caught behind the line of scrimmage |
| `behind_los_contested_receptions` | Contested catches made in tight coverage (CTC) — thrown/caught behind the line of scrimmage |
| `behind_los_contested_targets` | Contested targets (CTT) — thrown/caught behind the line of scrimmage |
| `behind_los_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — thrown/caught behind the line of scrimmage |
| `behind_los_drops` | Drops — on-target passes dropped by the receiver (DRP) — thrown/caught behind the line of scrimmage |
| `behind_los_epa` | Expected Points Added on the player's plays [standard/EPA] — thrown/caught behind the line of scrimmage |
| `behind_los_first_downs` | First downs gained (1st) — thrown/caught behind the line of scrimmage |
| `behind_los_fumbles` | Fumbles — thrown/caught behind the line of scrimmage |
| `behind_los_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — thrown/caught behind the line of scrimmage |
| `behind_los_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — thrown/caught behind the line of scrimmage |
| `behind_los_interceptions` | Interceptions on targets to this receiver (INT) — thrown/caught behind the line of scrimmage |
| `behind_los_longest` | Longest reception (LNG) — thrown/caught behind the line of scrimmage |
| `behind_los_pass_block_rate` | Share of pass plays the player spent pass blocking — thrown/caught behind the line of scrimmage |
| `behind_los_pass_blocks` | Pass-block snaps — thrown/caught behind the line of scrimmage |
| `behind_los_pass_plays` | Pass plays the player was on the field for — thrown/caught behind the line of scrimmage |
| `behind_los_positive_epa_percent` | Percentage of plays with positive EPA [standard] — thrown/caught behind the line of scrimmage |
| `behind_los_receptions` | Receptions (REC) — thrown/caught behind the line of scrimmage |
| `behind_los_route_rate` | Share of pass plays on which the player ran a route — thrown/caught behind the line of scrimmage |
| `behind_los_routes` | Routes run — thrown/caught behind the line of scrimmage |
| `behind_los_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — thrown/caught behind the line of scrimmage |
| `behind_los_targets` | Targets (TGT) — thrown/caught behind the line of scrimmage |
| `behind_los_targets_percent` | Target rate — targets per snap (TGT%) — thrown/caught behind the line of scrimmage |
| `behind_los_touchdowns` | Receiving touchdowns (TD) — thrown/caught behind the line of scrimmage |
| `behind_los_yards` | Receiving yards (YDS) — thrown/caught behind the line of scrimmage |
| `behind_los_yards_after_catch` | Yards after catch (YAC) — thrown/caught behind the line of scrimmage |
| `behind_los_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — thrown/caught behind the line of scrimmage |
| `behind_los_yards_per_reception` | Yards per reception (Y/REC) — thrown/caught behind the line of scrimmage |
| `behind_los_yprr` | Yards per route run (Y/RR) — thrown/caught behind the line of scrimmage |
| `center_behind_los_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_contested_targets` | Contested targets (CTT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_first_downs` | First downs gained (1st) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_fumbles` | Fumbles — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_longest` | Longest reception (LNG) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_pass_blocks` | Pass-block snaps — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_pass_plays` | Pass plays the player was on the field for — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_receptions` | Receptions (REC) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_route_rate` | Share of pass plays on which the player ran a route — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_routes` | Routes run — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_targets` | Targets (TGT) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_touchdowns` | Receiving touchdowns (TD) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_yards` | Receiving yards (YDS) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_yards_after_catch` | Yards after catch (YAC) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_yards_per_reception` | Yards per reception (Y/REC) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_behind_los_yprr` | Yards per route run (Y/RR) — targeted to the center third of the field, thrown/caught behind the line of scrimmage |
| `center_deep_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_contested_targets` | Contested targets (CTT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_first_downs` | First downs gained (1st) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_fumbles` | Fumbles — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_longest` | Longest reception (LNG) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_pass_blocks` | Pass-block snaps — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_pass_plays` | Pass plays the player was on the field for — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_receptions` | Receptions (REC) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_route_rate` | Share of pass plays on which the player ran a route — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_routes` | Routes run — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_targets` | Targets (TGT) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_touchdowns` | Receiving touchdowns (TD) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_yards` | Receiving yards (YDS) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_yards_after_catch` | Yards after catch (YAC) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_yards_per_reception` | Yards per reception (Y/REC) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_deep_yprr` | Yards per route run (Y/RR) — targeted to the center third of the field, thrown/caught 20+ yards downfield |
| `center_medium_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_contested_targets` | Contested targets (CTT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_first_downs` | First downs gained (1st) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_fumbles` | Fumbles — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_longest` | Longest reception (LNG) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_pass_blocks` | Pass-block snaps — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_pass_plays` | Pass plays the player was on the field for — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_receptions` | Receptions (REC) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_route_rate` | Share of pass plays on which the player ran a route — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_routes` | Routes run — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_targets` | Targets (TGT) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_touchdowns` | Receiving touchdowns (TD) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_yards` | Receiving yards (YDS) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_yards_after_catch` | Yards after catch (YAC) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_yards_per_reception` | Yards per reception (Y/REC) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_medium_yprr` | Yards per route run (Y/RR) — targeted to the center third of the field, thrown/caught 10–19 yards downfield |
| `center_short_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_contested_targets` | Contested targets (CTT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_first_downs` | First downs gained (1st) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_fumbles` | Fumbles — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_longest` | Longest reception (LNG) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_pass_blocks` | Pass-block snaps — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_pass_plays` | Pass plays the player was on the field for — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_receptions` | Receptions (REC) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_route_rate` | Share of pass plays on which the player ran a route — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_routes` | Routes run — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_targets` | Targets (TGT) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_touchdowns` | Receiving touchdowns (TD) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_yards` | Receiving yards (YDS) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_yards_after_catch` | Yards after catch (YAC) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_yards_per_reception` | Yards per reception (Y/REC) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `center_short_yprr` | Yards per route run (Y/RR) — targeted to the center third of the field, thrown/caught 0–9 yards downfield |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `deep_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — thrown/caught 20+ yards downfield |
| `deep_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — thrown/caught 20+ yards downfield |
| `deep_caught_percent` | Catch rate — receptions/targets (REC%) — thrown/caught 20+ yards downfield |
| `deep_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — thrown/caught 20+ yards downfield |
| `deep_contested_receptions` | Contested catches made in tight coverage (CTC) — thrown/caught 20+ yards downfield |
| `deep_contested_targets` | Contested targets (CTT) — thrown/caught 20+ yards downfield |
| `deep_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — thrown/caught 20+ yards downfield |
| `deep_drops` | Drops — on-target passes dropped by the receiver (DRP) — thrown/caught 20+ yards downfield |
| `deep_epa` | Expected Points Added on the player's plays [standard/EPA] — thrown/caught 20+ yards downfield |
| `deep_first_downs` | First downs gained (1st) — thrown/caught 20+ yards downfield |
| `deep_fumbles` | Fumbles — thrown/caught 20+ yards downfield |
| `deep_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — thrown/caught 20+ yards downfield |
| `deep_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — thrown/caught 20+ yards downfield |
| `deep_interceptions` | Interceptions on targets to this receiver (INT) — thrown/caught 20+ yards downfield |
| `deep_longest` | Longest reception (LNG) — thrown/caught 20+ yards downfield |
| `deep_pass_block_rate` | Share of pass plays the player spent pass blocking — thrown/caught 20+ yards downfield |
| `deep_pass_blocks` | Pass-block snaps — thrown/caught 20+ yards downfield |
| `deep_pass_plays` | Pass plays the player was on the field for — thrown/caught 20+ yards downfield |
| `deep_positive_epa_percent` | Percentage of plays with positive EPA [standard] — thrown/caught 20+ yards downfield |
| `deep_receptions` | Receptions (REC) — thrown/caught 20+ yards downfield |
| `deep_route_rate` | Share of pass plays on which the player ran a route — thrown/caught 20+ yards downfield |
| `deep_routes` | Routes run — thrown/caught 20+ yards downfield |
| `deep_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — thrown/caught 20+ yards downfield |
| `deep_targets` | Targets (TGT) — thrown/caught 20+ yards downfield |
| `deep_targets_percent` | Target rate — targets per snap (TGT%) — thrown/caught 20+ yards downfield |
| `deep_touchdowns` | Receiving touchdowns (TD) — thrown/caught 20+ yards downfield |
| `deep_yards` | Receiving yards (YDS) — thrown/caught 20+ yards downfield |
| `deep_yards_after_catch` | Yards after catch (YAC) — thrown/caught 20+ yards downfield |
| `deep_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — thrown/caught 20+ yards downfield |
| `deep_yards_per_reception` | Yards per reception (Y/REC) — thrown/caught 20+ yards downfield |
| `deep_yprr` | Yards per route run (Y/RR) — thrown/caught 20+ yards downfield |
| `franchise_id` | PFF unique team/franchise identifier |
| `left_behind_los_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_contested_targets` | Contested targets (CTT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_first_downs` | First downs gained (1st) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_fumbles` | Fumbles — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_longest` | Longest reception (LNG) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_pass_blocks` | Pass-block snaps — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_pass_plays` | Pass plays the player was on the field for — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_receptions` | Receptions (REC) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_route_rate` | Share of pass plays on which the player ran a route — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_routes` | Routes run — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_targets` | Targets (TGT) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_touchdowns` | Receiving touchdowns (TD) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_yards` | Receiving yards (YDS) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_yards_after_catch` | Yards after catch (YAC) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_yards_per_reception` | Yards per reception (Y/REC) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_behind_los_yprr` | Yards per route run (Y/RR) — targeted to the left third of the field, thrown/caught behind the line of scrimmage |
| `left_deep_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_contested_targets` | Contested targets (CTT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_first_downs` | First downs gained (1st) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_fumbles` | Fumbles — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_longest` | Longest reception (LNG) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_pass_blocks` | Pass-block snaps — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_pass_plays` | Pass plays the player was on the field for — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_receptions` | Receptions (REC) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_route_rate` | Share of pass plays on which the player ran a route — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_routes` | Routes run — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_targets` | Targets (TGT) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_touchdowns` | Receiving touchdowns (TD) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_yards` | Receiving yards (YDS) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_yards_after_catch` | Yards after catch (YAC) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_yards_per_reception` | Yards per reception (Y/REC) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_deep_yprr` | Yards per route run (Y/RR) — targeted to the left third of the field, thrown/caught 20+ yards downfield |
| `left_medium_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_contested_targets` | Contested targets (CTT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_first_downs` | First downs gained (1st) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_fumbles` | Fumbles — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_longest` | Longest reception (LNG) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_pass_blocks` | Pass-block snaps — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_pass_plays` | Pass plays the player was on the field for — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_receptions` | Receptions (REC) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_route_rate` | Share of pass plays on which the player ran a route — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_routes` | Routes run — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_targets` | Targets (TGT) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_touchdowns` | Receiving touchdowns (TD) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_yards` | Receiving yards (YDS) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_yards_after_catch` | Yards after catch (YAC) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_yards_per_reception` | Yards per reception (Y/REC) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_medium_yprr` | Yards per route run (Y/RR) — targeted to the left third of the field, thrown/caught 10–19 yards downfield |
| `left_short_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_contested_targets` | Contested targets (CTT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_first_downs` | First downs gained (1st) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_fumbles` | Fumbles — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_longest` | Longest reception (LNG) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_pass_blocks` | Pass-block snaps — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_pass_plays` | Pass plays the player was on the field for — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_receptions` | Receptions (REC) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_route_rate` | Share of pass plays on which the player ran a route — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_routes` | Routes run — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_targets` | Targets (TGT) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_touchdowns` | Receiving touchdowns (TD) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_yards` | Receiving yards (YDS) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_yards_after_catch` | Yards after catch (YAC) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_yards_per_reception` | Yards per reception (Y/REC) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `left_short_yprr` | Yards per route run (Y/RR) — targeted to the left third of the field, thrown/caught 0–9 yards downfield |
| `medium_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — thrown/caught 10–19 yards downfield |
| `medium_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — thrown/caught 10–19 yards downfield |
| `medium_caught_percent` | Catch rate — receptions/targets (REC%) — thrown/caught 10–19 yards downfield |
| `medium_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — thrown/caught 10–19 yards downfield |
| `medium_contested_receptions` | Contested catches made in tight coverage (CTC) — thrown/caught 10–19 yards downfield |
| `medium_contested_targets` | Contested targets (CTT) — thrown/caught 10–19 yards downfield |
| `medium_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — thrown/caught 10–19 yards downfield |
| `medium_drops` | Drops — on-target passes dropped by the receiver (DRP) — thrown/caught 10–19 yards downfield |
| `medium_epa` | Expected Points Added on the player's plays [standard/EPA] — thrown/caught 10–19 yards downfield |
| `medium_first_downs` | First downs gained (1st) — thrown/caught 10–19 yards downfield |
| `medium_fumbles` | Fumbles — thrown/caught 10–19 yards downfield |
| `medium_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — thrown/caught 10–19 yards downfield |
| `medium_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — thrown/caught 10–19 yards downfield |
| `medium_interceptions` | Interceptions on targets to this receiver (INT) — thrown/caught 10–19 yards downfield |
| `medium_longest` | Longest reception (LNG) — thrown/caught 10–19 yards downfield |
| `medium_pass_block_rate` | Share of pass plays the player spent pass blocking — thrown/caught 10–19 yards downfield |
| `medium_pass_blocks` | Pass-block snaps — thrown/caught 10–19 yards downfield |
| `medium_pass_plays` | Pass plays the player was on the field for — thrown/caught 10–19 yards downfield |
| `medium_positive_epa_percent` | Percentage of plays with positive EPA [standard] — thrown/caught 10–19 yards downfield |
| `medium_receptions` | Receptions (REC) — thrown/caught 10–19 yards downfield |
| `medium_route_rate` | Share of pass plays on which the player ran a route — thrown/caught 10–19 yards downfield |
| `medium_routes` | Routes run — thrown/caught 10–19 yards downfield |
| `medium_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — thrown/caught 10–19 yards downfield |
| `medium_targets` | Targets (TGT) — thrown/caught 10–19 yards downfield |
| `medium_targets_percent` | Target rate — targets per snap (TGT%) — thrown/caught 10–19 yards downfield |
| `medium_touchdowns` | Receiving touchdowns (TD) — thrown/caught 10–19 yards downfield |
| `medium_yards` | Receiving yards (YDS) — thrown/caught 10–19 yards downfield |
| `medium_yards_after_catch` | Yards after catch (YAC) — thrown/caught 10–19 yards downfield |
| `medium_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — thrown/caught 10–19 yards downfield |
| `medium_yards_per_reception` | Yards per reception (Y/REC) — thrown/caught 10–19 yards downfield |
| `medium_yprr` | Yards per route run (Y/RR) — thrown/caught 10–19 yards downfield |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `right_behind_los_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_contested_targets` | Contested targets (CTT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_first_downs` | First downs gained (1st) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_fumbles` | Fumbles — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_longest` | Longest reception (LNG) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_pass_blocks` | Pass-block snaps — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_pass_plays` | Pass plays the player was on the field for — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_receptions` | Receptions (REC) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_route_rate` | Share of pass plays on which the player ran a route — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_routes` | Routes run — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_targets` | Targets (TGT) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_touchdowns` | Receiving touchdowns (TD) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_yards` | Receiving yards (YDS) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_yards_after_catch` | Yards after catch (YAC) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_yards_per_reception` | Yards per reception (Y/REC) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_behind_los_yprr` | Yards per route run (Y/RR) — targeted to the right third of the field, thrown/caught behind the line of scrimmage |
| `right_deep_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_contested_targets` | Contested targets (CTT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_first_downs` | First downs gained (1st) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_fumbles` | Fumbles — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_longest` | Longest reception (LNG) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_pass_blocks` | Pass-block snaps — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_pass_plays` | Pass plays the player was on the field for — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_receptions` | Receptions (REC) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_route_rate` | Share of pass plays on which the player ran a route — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_routes` | Routes run — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_targets` | Targets (TGT) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_touchdowns` | Receiving touchdowns (TD) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_yards` | Receiving yards (YDS) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_yards_after_catch` | Yards after catch (YAC) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_yards_per_reception` | Yards per reception (Y/REC) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_deep_yprr` | Yards per route run (Y/RR) — targeted to the right third of the field, thrown/caught 20+ yards downfield |
| `right_medium_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_contested_targets` | Contested targets (CTT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_first_downs` | First downs gained (1st) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_fumbles` | Fumbles — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_longest` | Longest reception (LNG) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_pass_blocks` | Pass-block snaps — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_pass_plays` | Pass plays the player was on the field for — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_receptions` | Receptions (REC) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_route_rate` | Share of pass plays on which the player ran a route — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_routes` | Routes run — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_targets` | Targets (TGT) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_touchdowns` | Receiving touchdowns (TD) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_yards` | Receiving yards (YDS) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_yards_after_catch` | Yards after catch (YAC) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_yards_per_reception` | Yards per reception (Y/REC) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_medium_yprr` | Yards per route run (Y/RR) — targeted to the right third of the field, thrown/caught 10–19 yards downfield |
| `right_short_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_caught_percent` | Catch rate — receptions/targets (REC%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_contested_receptions` | Contested catches made in tight coverage (CTC) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_contested_targets` | Contested targets (CTT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_drops` | Drops — on-target passes dropped by the receiver (DRP) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_epa` | Expected Points Added on the player's plays [standard/EPA] — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_first_downs` | First downs gained (1st) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_fumbles` | Fumbles — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_interceptions` | Interceptions on targets to this receiver (INT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_longest` | Longest reception (LNG) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_pass_block_rate` | Share of pass plays the player spent pass blocking — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_pass_blocks` | Pass-block snaps — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_pass_plays` | Pass plays the player was on the field for — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_positive_epa_percent` | Percentage of plays with positive EPA [standard] — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_receptions` | Receptions (REC) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_route_rate` | Share of pass plays on which the player ran a route — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_routes` | Routes run — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_targets` | Targets (TGT) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_targets_percent` | Target rate — targets per snap (TGT%) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_touchdowns` | Receiving touchdowns (TD) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_yards` | Receiving yards (YDS) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_yards_after_catch` | Yards after catch (YAC) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_yards_per_reception` | Yards per reception (Y/REC) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `right_short_yprr` | Yards per route run (Y/RR) — targeted to the right third of the field, thrown/caught 0–9 yards downfield |
| `short_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — thrown/caught 0–9 yards downfield |
| `short_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — thrown/caught 0–9 yards downfield |
| `short_caught_percent` | Catch rate — receptions/targets (REC%) — thrown/caught 0–9 yards downfield |
| `short_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — thrown/caught 0–9 yards downfield |
| `short_contested_receptions` | Contested catches made in tight coverage (CTC) — thrown/caught 0–9 yards downfield |
| `short_contested_targets` | Contested targets (CTT) — thrown/caught 0–9 yards downfield |
| `short_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — thrown/caught 0–9 yards downfield |
| `short_drops` | Drops — on-target passes dropped by the receiver (DRP) — thrown/caught 0–9 yards downfield |
| `short_epa` | Expected Points Added on the player's plays [standard/EPA] — thrown/caught 0–9 yards downfield |
| `short_first_downs` | First downs gained (1st) — thrown/caught 0–9 yards downfield |
| `short_fumbles` | Fumbles — thrown/caught 0–9 yards downfield |
| `short_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — thrown/caught 0–9 yards downfield |
| `short_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — thrown/caught 0–9 yards downfield |
| `short_interceptions` | Interceptions on targets to this receiver (INT) — thrown/caught 0–9 yards downfield |
| `short_longest` | Longest reception (LNG) — thrown/caught 0–9 yards downfield |
| `short_pass_block_rate` | Share of pass plays the player spent pass blocking — thrown/caught 0–9 yards downfield |
| `short_pass_blocks` | Pass-block snaps — thrown/caught 0–9 yards downfield |
| `short_pass_plays` | Pass plays the player was on the field for — thrown/caught 0–9 yards downfield |
| `short_positive_epa_percent` | Percentage of plays with positive EPA [standard] — thrown/caught 0–9 yards downfield |
| `short_receptions` | Receptions (REC) — thrown/caught 0–9 yards downfield |
| `short_route_rate` | Share of pass plays on which the player ran a route — thrown/caught 0–9 yards downfield |
| `short_routes` | Routes run — thrown/caught 0–9 yards downfield |
| `short_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — thrown/caught 0–9 yards downfield |
| `short_targets` | Targets (TGT) — thrown/caught 0–9 yards downfield |
| `short_targets_percent` | Target rate — targets per snap (TGT%) — thrown/caught 0–9 yards downfield |
| `short_touchdowns` | Receiving touchdowns (TD) — thrown/caught 0–9 yards downfield |
| `short_yards` | Receiving yards (YDS) — thrown/caught 0–9 yards downfield |
| `short_yards_after_catch` | Yards after catch (YAC) — thrown/caught 0–9 yards downfield |
| `short_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — thrown/caught 0–9 yards downfield |
| `short_yards_per_reception` | Yards per reception (Y/REC) — thrown/caught 0–9 yards downfield |
| `short_yprr` | Yards per route run (Y/RR) — thrown/caught 0–9 yards downfield |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **TGT%**: The percentage of targets to snaps
- **REC**: Receptions
- **YDS**: Receiving Yards
- **TD**: Receiving TD
- **DROP**: PFF Grade for HandsDrop
- **YAC/REC**: Yards After Catch per Reception
- **aDoT**: Average Depth of Target
- **DRP%**: Drops - on-target passes dropped by the receiver
- **CTC**: Contested Catches
- **INT**: Receiving Interceptions
- **MTF**: Missed Tackles Forced after a Reception
- **RTG**: NFL Passer Rating when targeted
- **POS**: Season position
- **TGT**: Receiving Targets
- **REC%**: Percentage of targets caught
- **Y/REC**: Yards per Reception
- **RECV**: PFF Grade for Pass Routes
- **YAC**: Yards After Catch
- **Y/RR**: Yards per Route Run
- **DRP**: Drops - on-target passes dropped by the receiver
- **CTT**: Contested Targets
- **CTC%**: Contested Catch Rate
- **FUM**: Fumbles
- **1st**: First Downs

</details>

### `PFF_receiving_scheme.csv` — Receiving vs Scheme (71 cols)

_Grades and receiving stats vs Man and Zone coverage schemes_

Buckets: `man`, `zone`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `base_targets` | Targets (TGT) — season total |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `man_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — vs man coverage |
| `man_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — vs man coverage |
| `man_caught_percent` | Catch rate — receptions/targets (REC%) — vs man coverage |
| `man_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — vs man coverage |
| `man_contested_receptions` | Contested catches made in tight coverage (CTC) — vs man coverage |
| `man_contested_targets` | Contested targets (CTT) — vs man coverage |
| `man_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — vs man coverage |
| `man_drops` | Drops — on-target passes dropped by the receiver (DRP) — vs man coverage |
| `man_epa` | Expected Points Added on the player's plays [standard/EPA] — vs man coverage |
| `man_first_downs` | First downs gained (1st) — vs man coverage |
| `man_fumbles` | Fumbles — vs man coverage |
| `man_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — vs man coverage |
| `man_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — vs man coverage |
| `man_interceptions` | Interceptions on targets to this receiver (INT) — vs man coverage |
| `man_longest` | Longest reception (LNG) — vs man coverage |
| `man_pass_block_rate` | Share of pass plays the player spent pass blocking — vs man coverage |
| `man_pass_blocks` | Pass-block snaps — vs man coverage |
| `man_pass_plays` | Pass plays the player was on the field for — vs man coverage |
| `man_positive_epa_percent` | Percentage of plays with positive EPA [standard] — vs man coverage |
| `man_receptions` | Receptions (REC) — vs man coverage |
| `man_route_rate` | Share of pass plays on which the player ran a route — vs man coverage |
| `man_routes` | Routes run — vs man coverage |
| `man_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — vs man coverage |
| `man_targets` | Targets (TGT) — vs man coverage |
| `man_targets_percent` | Target rate — targets per snap (TGT%) — vs man coverage |
| `man_touchdowns` | Receiving touchdowns (TD) — vs man coverage |
| `man_yards` | Receiving yards (YDS) — vs man coverage |
| `man_yards_after_catch` | Yards after catch (YAC) — vs man coverage |
| `man_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — vs man coverage |
| `man_yards_per_reception` | Yards per reception (Y/REC) — vs man coverage |
| `man_yprr` | Yards per route run (Y/RR) — vs man coverage |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `zone_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_caught_percent` | Catch rate — receptions/targets (REC%) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_contested_receptions` | Contested catches made in tight coverage (CTC) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_contested_targets` | Contested targets (CTT) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_drops` | Drops — on-target passes dropped by the receiver (DRP) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_epa` | Expected Points Added on the player's plays [standard/EPA] — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_first_downs` | First downs gained (1st) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_fumbles` | Fumbles — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_interceptions` | Interceptions on targets to this receiver (INT) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_longest` | Longest reception (LNG) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_pass_block_rate` | Share of pass plays the player spent pass blocking — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_pass_blocks` | Pass-block snaps — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_pass_plays` | Pass plays the player was on the field for — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_positive_epa_percent` | Percentage of plays with positive EPA [standard] — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_receptions` | Receptions (REC) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_route_rate` | Share of pass plays on which the player ran a route — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_routes` | Routes run — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_targeted_qb_rating` | Passer rating when this player is targeted (RTG) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_targets` | Targets (TGT) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_targets_percent` | Target rate — targets per snap (TGT%) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_touchdowns` | Receiving touchdowns (TD) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_yards` | Receiving yards (YDS) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_yards_after_catch` | Yards after catch (YAC) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_yards_per_reception` | Yards per reception (Y/REC) — vs zone coverage (or zone-scheme runs in run-blocking) |
| `zone_yprr` | Yards per route run (Y/RR) — vs zone coverage (or zone-scheme runs in run-blocking) |

<details><summary>PFF key legend (verbatim)</summary>

- **TGT%**: The percentage of targets to snaps
- **REC**: Receptions
- **YDS**: Receiving Yards
- **TD**: Receiving TD
- **DROP**: PFF Grade for HandsDrop
- **YAC/REC**: Yards After Catch per Reception
- **aDoT**: Average Depth of Target
- **DRP%**: Drops - on-target passes dropped by the receiver
- **CTC**: Contested Catches
- **INT**: Receiving Interceptions
- **MTF**: Missed Tackles Forced after a Reception
- **RTG**: NFL Passer Rating when targeted
- **TGT**: Receiving Targets
- **REC%**: Percentage of targets caught
- **Y/REC**: Yards per Reception
- **RECV**: PFF Grade for Pass Routes
- **YAC**: Yards After Catch
- **Y/RR**: Yards per Route Run
- **DRP**: Drops - on-target passes dropped by the receiver
- **CTT**: Contested Targets
- **CTC%**: Contested Catch Rate
- **FUM**: Fumbles
- **1st**: First Downs

</details>

### `PFF_receiving_summary.csv` — Receiving General (47 cols)

_Grades and most receiving stats, including passer rating when targeted._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) |
| `avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) |
| `caught_percent` | Catch rate — receptions/targets (REC%) |
| `contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) |
| `contested_receptions` | Contested catches made in tight coverage (CTC) |
| `contested_targets` | Contested targets (CTT) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) |
| `drops` | Drops — on-target passes dropped by the receiver (DRP) |
| `epa` | Expected Points Added on the player's plays [standard/EPA] |
| `first_downs` | First downs gained (1st) |
| `franchise_id` | PFF unique team/franchise identifier |
| `fumbles` | Fumbles |
| `grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) |
| `grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) |
| `grades_offense` | PFF grade, 0–100 (higher is better) — offense |
| `grades_pass_block` | PFF grade, 0–100 (higher is better) — pass blocking (PBLK) |
| `grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) |
| `inline_rate` | Share of snaps aligned inline as a TE (INL%) |
| `inline_snaps` | Snaps aligned inline (INL) |
| `interceptions` | Interceptions on targets to this receiver (INT) |
| `longest` | Longest reception (LNG) |
| `pass_block_rate` | Share of pass plays the player spent pass blocking |
| `pass_blocks` | Pass-block snaps |
| `pass_plays` | Pass plays the player was on the field for |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `positive_epa_percent` | Percentage of plays with positive EPA [standard] |
| `receptions` | Receptions (REC) |
| `route_rate` | Share of pass plays on which the player ran a route |
| `routes` | Routes run |
| `slot_rate` | Share of snaps in the slot (SLT%) |
| `slot_snaps` | Snaps in the slot (SLOT) |
| `targeted_qb_rating` | Passer rating when this player is targeted (RTG) |
| `targets` | Targets (TGT) |
| `touchdowns` | Receiving touchdowns (TD) |
| `wide_rate` | Share of snaps out wide (WID%) |
| `wide_snaps` | Snaps out wide (WIDE) |
| `yards` | Receiving yards (YDS) |
| `yards_after_catch` | Yards after catch (YAC) |
| `yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) |
| `yards_per_reception` | Yards per reception (Y/REC) |
| `yprr` | Yards per route run (Y/RR) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **REC**: Receptions
- **YDS**: Receiving Yards
- **TD**: Receiving TD
- **RECV**: PFF Grade for Pass Routes
- **FUM**: PFF Grade for HandsFumble
- **PASS**: Snaps lined up on the field on pass plays
- **RT%**: Percentage of snaps
- **PB%**: Percentage of pass block snaps per passing snap played
- **SLT%**: Percentage of snaps
- **WID%**: Percentage of snaps
- **INL%**: Percentage of snaps
- **YAC/REC**: Yards After Catch per Reception
- **aDoT**: Average Depth of Target
- **DRP**: Drops - on-target passes dropped by the receiver
- **CTT**: Contested Targets
- **CTC%**: Contested Catch Rate
- **FUM**: Fumbles
- **1st**: First Downs
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties
- **POS**: Season position
- **TGT**: Receiving Targets
- **REC%**: Percentage of targets caught
- **Y/REC**: Yards per Reception
- **OFF**: PFF Grade for Offense
- **DROP**: PFF Grade for HandsDrop
- **PBLK**: PFF Grade for Pass Blocking
- **RECV**: Snaps where running a receiving route
- **PBLK**: Pass Block Snaps
- **SLOT**: Slot Snaps
- **WIDE**: Wide Snaps
- **INL**: Inline Snaps
- **YAC**: Yards After Catch
- **Y/RR**: Yards per Route Run
- **LNG**: Longest
- **DRP%**: Drops - on-target passes dropped by the receiver
- **CTC**: Contested Catches
- **INT**: Receiving Interceptions
- **MTF**: Missed Tackles Forced after a Reception
- **RTG**: NFL Passer Rating when targeted

</details>

### `PFF_return_summary.csv` — Kick Returns (26 cols)

_Grades and base kick returning stats._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_kick_return` | PFF grade, 0–100 (higher is better) — kickoff returns (KRTN) |
| `grades_punt_return` | PFF grade, 0–100 (higher is better) — punt returns (PRTN) |
| `grades_return` | PFF grade, 0–100 (higher is better) — overall returns (kick & punt) (RETN) |
| `kickoff_attempts` | Kickoff-return attempts |
| `kickoff_fair_catches` | Fair catches on kickoffs (FC) |
| `kickoff_long` | Longest kickoff return (LNG) |
| `kickoff_muffed_returns` | Muffed kickoff returns (MUF) |
| `kickoff_touchdowns` | Kickoff returns for TD (TD) |
| `kickoff_yards` | Kickoff-return yards (YDS) |
| `kickoff_ypa` | Kickoff-return yards per attempt (YPA) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `punt_attempts` | Punt-return attempts |
| `punt_fair_catches` | Fair catches on punts (FC) |
| `punt_long` | Longest punt return (LNG) |
| `punt_muffed_returns` | Muffed punt returns (MUF) |
| `punt_touchdowns` | Punt returns for TD (TD) |
| `punt_yards` | Punt-return yards (YDS) |
| `punt_ypa` | Punt-return yards per attempt (YPA) |
| `total_attempts` | Total return attempts (kickoff + punt) |

<details><summary>PFF key legend (verbatim)</summary>

- **Note**: Kick return data currently only available since 2013.
- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **RTN**: Return Attempts
- **YDS**: Return Yards
- **YPA**: Return Yards Per Attempt
- **FC**: Fair Catches
- **PRTN**: PFF Grade for Punt Returns
- **MUF**: Muffed Returns
- **POS**: Season position
- **RETN**: PFF Grade for Kickoff and Punt Returns
- **KRTN**: PFF Grade for Kickoff Returns
- **LNG**: Longest
- **TD**: # of Kicks returned for a Touchdown

</details>

### `PFF_run_defense_summary.csv` — Run Defense (24 cols)

_2025 NCAA Run Defense Grades — Player Rankin_

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `assists` | Assisted tackles (AST) |
| `avg_depth_of_tackle` | Average depth of tackle — avg yards downfield of run tackles (AVDT) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `forced_fumbles` | Forced fumbles (FFM) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) |
| `grades_defense` | PFF grade, 0–100 (higher is better) — defense |
| `grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties |
| `grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) |
| `grades_run_defense` | PFF grade, 0–100 (higher is better) — run defense (RDEF) |
| `grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) |
| `missed_tackle_rate` | Missed-tackle rate (MIS%) |
| `missed_tackles` | Missed tackles (MIS) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `run_stop_opp` | Run-stop opportunities — run snaps where a stop was possible |
| `snap_counts_run` | Run-defense snaps |
| `stop_percent` | Stop % — share of run-defense snaps producing a stop (STOP%) |
| `stops` | Defensive stops — tackles constituting an offensive failure (STOP) |
| `tackles` | Tackles, solo (TKL) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **RDEF**: PFF Grade for Run Defense
- **AST**: Assisted Tackles
- **MIS%**: Missed Tackle Rate
- **STOP%**: The percentage of a player's run defense snaps where he was responsible for a stop
- **AVDT**: Average Depth of Tackle
- **POS**: Season position
- **RDEF**: Snaps in a run defense role
- **TKL**: Tackles
- **MIS**: Missed Tackles
- **STOP**: Defensive Stops - tackles that constitute a "failure" for the offense
- **FFM**: Forced Fumbles
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties

</details>

### `PFF_rushing_summary.csv` — Rushing (47 cols)

_Grades and base rushing stats._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `attempts` | Designed rushing attempts / carries (ATT) |
| `avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) |
| `breakaway_attempts` | Designed rush attempts of 15+ yards (D15+) |
| `breakaway_percent` | Breakaway % — share of rushing yards on 15+ yard runs (BAY%) |
| `breakaway_yards` | Breakaway yards — rushing yards on designed runs over 15 yards (BAY) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `designed_yards` | Yardage on designed runs (DYDS) |
| `drops` | Drops — on-target passes dropped by the receiver (DRP) |
| `elu_recv_mtf` | Missed tackles forced as a receiver (Elusive Rating input) |
| `elu_rush_mtf` | Missed tackles forced as a rusher (Elusive Rating input) |
| `elu_yco` | Yards after contact (Elusive Rating input) |
| `elusive_rating` | Elusive Rating — PFF signature stat: runner success/impact independent of blocking (ELU) |
| `explosive` | Explosive runs — designed runs over 10 yards (10+) |
| `first_downs` | First downs gained (1st) |
| `franchise_id` | PFF unique team/franchise identifier |
| `fumbles` | Fumbles |
| `gap_attempts` | Designed rush attempts on gap-scheme runs (GAP) |
| `grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) |
| `grades_offense` | PFF grade, 0–100 (higher is better) — offense |
| `grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties |
| `grades_pass` | PFF grade, 0–100 (higher is better) — passing |
| `grades_pass_block` | PFF grade, 0–100 (higher is better) — pass blocking (PBLK) |
| `grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) |
| `grades_run` | PFF grade, 0–100 (higher is better) — rushing |
| `grades_run_block` | PFF grade, 0–100 (higher is better) — run blocking (RBLK) |
| `longest` | Longest rush (LNG) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `rec_yards` | Receiving yards (for this rusher) |
| `receptions` | Receptions (REC) — caught, or allowed on defense (see report) |
| `routes` | Routes run |
| `run_plays` | Run plays the player was on the field for |
| `scramble_yards` | Yardage on scrambles (SYDS) |
| `scrambles` | Scrambles — undesigned QB runs (SCR) |
| `targets` | Targets (TGT) — thrown to receiver, or into coverage on defense |
| `total_touches` | Total touches (carries + receptions) |
| `touchdowns` | Rushing touchdowns (TD) |
| `yards` | Rushing yards (YDS) |
| `yards_after_contact` | Yards after contact (YCO) |
| `yco_attempt` | Yards after contact per attempt (YCO/A) |
| `ypa` | Rushing yards per attempt (YPA) |
| `yprr` | Yards per route run (Y/RR) |
| `zone_attempts` | Designed rush attempts on zone-scheme runs (ZONE) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **ATT**: Designed Rushing Attempts
- **YPA**: Rushing Yards per Attempt
- **FUM**: Fumbles
- **RUN**: PFF Grade for Rushing
- **RBLK**: PFF Grade for Run Blocking
- **YCO/A**: Yards After Contact per Attempt
- **LNG**: Longest
- **ZONE**: Designed Rushing Attempts
- **SCR**: Scrambles - undesigned runs by the QB
- **DYDS**: Yardage accumulated on designed runs
- **BAY**: Rushing yardage on designed attempts more than 15 yards
- **1st**: First Downs
- **RECV**: PFF Grade for Pass Routes
- **TGT**: Receiving Targets
- **YDS**: Receiving Yards
- **Y/RR**: Yards per Route Run
- **ELU**: Elusive Rating - A PFF Signature stat measuring success and impact of a runner with the ball independently of the blocking
- **POS**: Season position
- **SNP**: Snaps lined up on the field on run plays
- **YDS**: Rushing Yards
- **TD**: Rushing Touchdowns
- **OFF**: PFF Grade for Offense
- **FUM**: PFF Grade for HandsFumble
- **YCO**: Yards After Contact
- **MTF**: Missed Tackles Forced after a Rush
- **10+**: Explosive Runs - runs over 10 yards
- **GAP**: Designed Rushing Attempts
- **SYDS**: Yardage accumulated on scrambles
- **D15+**: Designed Rushing Attempts more than 15 yards
- **BAY%**: Breakaway Percentage
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties
- **PBLK**: PFF Grade for Pass Blocking
- **REC**: Receptions
- **RSNP**: Snaps where running a receiving route
- **DRP**: Drops - on-target passes dropped by the receiver

</details>

### `PFF_slot_coverage.csv` — Slot Coverage (17 cols)

_Taking into account the number of snaps a defender spends in coverage is key to understandin_

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `coverage_snaps` | Coverage snaps (COV) |
| `coverage_snaps_per_reception` | Coverage snaps per reception allowed (S/REC) |
| `coverage_snaps_per_target` | Coverage snaps per target (S/TGT) |
| `franchise_id` | PFF unique team/franchise identifier |
| `interceptions` | Interceptions made in coverage (INT) |
| `qb_rating_against` | Passer rating allowed in coverage (NFL) |
| `receptions` | Receptions allowed (REC) |
| `targets` | Targets into this player's coverage (TGT) |
| `touchdowns` | Receiving touchdowns allowed (TD) |
| `yards` | Receiving yards allowed (YDS) |
| `yards_after_catch` | Yards after catch allowed (YAC) |
| `yards_per_coverage_snap` | Yards allowed per coverage snap (Y/SNP) |

<details><summary>PFF key legend (verbatim)</summary>

- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **TGT**: Receiving Targets
- **YDS**: Receiving Yards
- **TD**: Receiving TD
- **NFL**: NFL Passer Rating
- **S/TGT**: Coverage Snaps per Target
- **POS**: Season position
- **COV**: Coverage Snaps
- **REC**: Receptions
- **YAC**: Yards After Catch
- **INT**: Interceptions
- **Y/SNP**: Yards per coverage snap
- **S/REC**: Coverage Snaps per Reception

</details>

### `PFF_special_teams_summary.csv` — Special Teams General (27 cols)

_Grades and base special teaming stats._

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `assists` | Assisted tackles (AST) |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) |
| `franchise_id` | PFF unique team/franchise identifier |
| `grades_fgep_defense` | PFF grade, 0–100 (higher is better) — FG/XP block unit (defense) |
| `grades_fgep_kicker` | PFF grade, 0–100 (higher is better) — field-goal/extra-point kicking (FG) |
| `grades_fgep_offense` | PFF grade, 0–100 (higher is better) — FG/XP protection unit (offense) |
| `grades_kick_return` | PFF grade, 0–100 (higher is better) — kickoff returns (KRTN) |
| `grades_kickoff_kicker` | PFF grade, 0–100 (higher is better) — kickoffs (kicker) (KOFF) |
| `grades_long_snap` | PFF grade, 0–100 (higher is better) — long snapping |
| `grades_misc_st` | PFF grade, 0–100 (higher is better) — miscellaneous special teams (SPEC) |
| `grades_punt_return` | PFF grade, 0–100 (higher is better) — punt returns (PRTN) |
| `grades_punter` | PFF grade, 0–100 (higher is better) — punting (PUNT) |
| `grades_special_teams_penalty` | PFF grade, 0–100 (higher is better) — special-teams penalties |
| `missed_tackles` | Missed tackles (MIS) |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' |
| `snap_counts_field_goal` | FG/PAT kicking snaps (FGK) |
| `snap_counts_field_goal_blocking` | FG/PAT block-unit snaps (FGBLK) |
| `snap_counts_kickoff` | Kickoff-coverage snaps (KCOV) |
| `snap_counts_kickoff_return` | Kickoff-return snaps (KRET) |
| `snap_counts_punt_coverage` | Punt-coverage snaps (PCOV) |
| `snap_counts_punt_return` | Punt-return snaps (PRET) |
| `tackles` | Tackles, solo (TKL) |

<details><summary>PFF key legend (verbatim)</summary>

- **Note**: Special teams data currently only available since 2013.
- **#**: Jersey Number
- **#G**: Number of games in which the player appeared
- **KRET**: Snaps where returning the ball on a kickoff
- **PRET**: Snaps where returning the ball on a punt
- **FGBLK**: Snaps where rushing/blocking a field goal or PAT
- **SPEC**: PFF Grade for Misc. Special Teams
- **PUNT**: PFF Grade for the Punter or Returner
- **PEN**: Total (Declined+Offset): Total and (declined or offsetting) penalties
- **AST**: Assisted Tackles
- **POS**: Season position
- **TOT**: Total Snaps
- **KCOV**: Snaps where hunting down those kickoff returners
- **PCOV**: Snaps where hunting down those punt returners
- **FGK**: Snaps where kicking a field goal or PAT
- **KOFF**: PFF Grade for the Kicker or Returner
- **FG**: PFF Grade for the Kicker
- **TKL**: Tackles
- **MIS**: Missed Tackles

</details>

### `PFF_time_in_pocket.csv` — Time in Pocket (77 cols)

_The Time In The Pocket report lets you find out which quarterbacks are holding onto the ball the most and how it impacts pel_

Buckets: `less`, `more`

| column | definition |
|---|---|
| `player` | Player name |
| `player_id` | PFF unique player identifier |
| `position` | Player's listed position for the season (POS) |
| `team_name` | Team the player played for |
| `player_game_count` | Number of games in which the player appeared (#G) |
| `avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) |
| `avg_ttt_attempts` | Average time to throw on dropbacks ending in a pass attempt, seconds |
| `avg_ttt_sacks` | Average time to throw on dropbacks ending in a sack, seconds |
| `avg_ttt_scrambles` | Average time to throw on dropbacks ending in a scramble, seconds |
| `dropbacks` | Dropbacks — times the QB dropped back to pass (DB) |
| `franchise_id` | PFF unique team/franchise identifier |
| `less_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_attempts` | Pass attempts (ATT) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_completion_percent` | Completion percentage — completions/attempts (COM%) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_completions` | Completions (COM) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_drops` | Drops — on-target passes dropped by the receiver (DRP) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_epa` | Expected Points Added on the player's plays [standard/EPA] — on dropbacks of 2.5 seconds or less in the pocket |
| `less_first_downs` | First downs gained (1st) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_interceptions` | Interceptions thrown (INT) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_passing_snaps` | Passing snaps — snaps on pass plays — on dropbacks of 2.5 seconds or less in the pocket |
| `less_positive_epa_percent` | Percentage of plays with positive EPA [standard] — on dropbacks of 2.5 seconds or less in the pocket |
| `less_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_qb_rating` | NFL passer rating (NFL) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_sack_percent` | Sack percentage — sacks per dropback [standard] — on dropbacks of 2.5 seconds or less in the pocket |
| `less_sacks` | Sacks taken by the passer (SK) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_scrambles` | Scrambles — undesigned QB runs (SCR) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_spikes` | Spikes — QB clock-stopping spikes [standard] — on dropbacks of 2.5 seconds or less in the pocket |
| `less_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_touchdowns` | Passing touchdowns (TD) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_yards` | Passing yards (YDS) — on dropbacks of 2.5 seconds or less in the pocket |
| `less_ypa` | Yards per pass attempt (YPA) — on dropbacks of 2.5 seconds or less in the pocket |
| `more_accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_attempts` | Pass attempts (ATT) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_completion_percent` | Completion percentage — completions/attempts (COM%) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_completions` | Completions (COM) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_dropbacks` | Dropbacks — times the QB dropped back to pass (DB) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_drops` | Drops — on-target passes dropped by the receiver (DRP) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_epa` | Expected Points Added on the player's plays [standard/EPA] — on dropbacks longer than 2.5 seconds in the pocket |
| `more_first_downs` | First downs gained (1st) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_interceptions` | Interceptions thrown (INT) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_passing_snaps` | Passing snaps — snaps on pass plays — on dropbacks longer than 2.5 seconds in the pocket |
| `more_positive_epa_percent` | Percentage of plays with positive EPA [standard] — on dropbacks longer than 2.5 seconds in the pocket |
| `more_pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_qb_rating` | NFL passer rating (NFL) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_sack_percent` | Sack percentage — sacks per dropback [standard] — on dropbacks longer than 2.5 seconds in the pocket |
| `more_sacks` | Sacks taken by the passer (SK) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_scrambles` | Scrambles — undesigned QB runs (SCR) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_spikes` | Spikes — QB clock-stopping spikes [standard] — on dropbacks longer than 2.5 seconds in the pocket |
| `more_thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_touchdowns` | Passing touchdowns (TD) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_yards` | Passing yards (YDS) — on dropbacks longer than 2.5 seconds in the pocket |
| `more_ypa` | Yards per pass attempt (YPA) — on dropbacks longer than 2.5 seconds in the pocket |

<details><summary>PFF key legend (verbatim)</summary>

- **Note**: Pocket Timing data only available since 2011.
- **ALL**: Average Time to Throw on all dropbacks
- **SK**: Average Time to Throw on dropbacks with a sack
- **DB%**: The percentage of dropbacks in the passing split
- **ATT**: Attempts - the number of times the passer threw the ball
- **COM%**: Completion Percentage - the percentage of completions to pass attempts
- **YPA**: Yards per Attempt - the average number of passing yards gained per passing attempt
- **INT**: Interceptions - the number of interceptions thrown by the passer
- **PASS**: PFF Grade for Pass
- **FUM**: PFF Grade for HandsFumble
- **BTT%**: Big Time Throw Rate - the % of attempts that are BTTs
- **TWP%**: Turnover Worthy Play Rate - the % of attempts that are TWP
- **ADJ%**: Adjusted Completion Percentage - the % of aimed passes thrown on target (completions + drops / aimed)
- **DRP%**: Drops - on-target passes dropped by the receiver
- **HAT**: Hit As Thrown - the passer is hit by a defender while a pass is being thrown
- **DPR**: Total pressures of the passer of any kind (generated by the defense)
- **P2S%**: Percentage of Pressures Turned into Sacks
- **SCR**: Scrambles - undesigned runs by the QB
- **NFL**: NFL Passer Rating ‘formance.
- **ATT**: Average Time to Thow on dropbacks with a pass attempt
- **SCR**: Average Time to Throws on dropbacks with a scrambles
- **DB**: Dropbacks - the number of times the QB dropped back to pass
- **COM**: Completions - the number of times the passer completed a pass
- **YDS**: Yards - the number of yards gained passing
- **TD**: Touchdowns - the number of touchdowns thrown by the passer
- **OFF**: PFF Grade for Offense
- **RUN**: PFF Grade for Rushing
- **BTT**: Big Time Throws - a pass with excellent ball location and timing, generally thrown further down the field and/or into a tighter window
- **TWP**: Turnover Worthy Plays - a pass that has a high percentage chance to be intercepted or a poor job of taking care of the ball and fumbling
- **aDoT**: Average Depth of Target
- **DRP**: Drops - on-target passes dropped by the receiver
- **BAT**: Batted Passes - the number of passes batted or deflected at the line of scrimage
- **TA**: Thrown Away - passes intentionally thrown out of play
- **SK**: Sacks - The number of times the passer was sacked
- **TTT**: Average Time to Throw on all dropbacks
- **1st**: First Downs

</details>

## Base metric glossary (deduplicated)

| base metric | definition | # files |
|---|---|---|
| `accuracy_percent` | Adjusted completion % — aimed passes thrown on target, (completions+drops)/aimed (ADJ%) | 5 |
| `aimed_passes` | Aimed passes — attempts aimed at a receiver (excludes throwaways, spikes, batted & hit-as-thrown) | 5 |
| `allowed_pressure_dropbacks` | Dropbacks while the offense was under pressure (APDB) | 1 |
| `assists` | Assisted tackles (AST) | 6 |
| `attempts` | Attempts (ATT) — pass attempts (see report context for rushing/kicking variants) | 8 |
| `attempts_percent` | Percentage of the player's attempts in this split (ATT%) | 1 |
| `attempts_with_hangtime` | Attempts with hangtime recorded | 2 |
| `average_distance` | Average kickoff distance (yards) | 1 |
| `average_hangtime` | Average hangtime, seconds (AVG) | 2 |
| `average_net_yards` | Average net yards per punt (NET) | 1 |
| `average_starting_field_position` | Average opponent start field position after kickoff (AFP) | 1 |
| `average_yards_per_attempt` | Average gross yards per punt (YPA) | 1 |
| `average_yards_per_return` | Average return yards allowed per return (YPR) | 2 |
| `avg_depth_of_tackle` | Average depth of tackle — avg yards downfield of run tackles (AVDT) | 1 |
| `avg_depth_of_target` | Average depth of target — avg yards downfield of the throw target (aDoT) | 11 |
| `avg_time_to_throw` | Average time to throw on all dropbacks, seconds (TTT) | 5 |
| `avg_ttt_attempts` | Average time to throw on dropbacks ending in a pass attempt, seconds | 1 |
| `avg_ttt_sacks` | Average time to throw on dropbacks ending in a sack, seconds | 1 |
| `avg_ttt_scrambles` | Average time to throw on dropbacks ending in a scramble, seconds | 1 |
| `avoided_tackles` | Missed/avoided tackles forced after the catch or rush (MTF) | 5 |
| `bats` | Batted passes — passes batted/deflected at the line of scrimmage (BAT) | 5 |
| `batted_passes` | Batted passes — deflected at the line (BAT) | 2 |
| `big_time_throws` | Big-time throws — passes with excellent location/timing, usually deep and/or tight-window (BTT) | 5 |
| `block_percent` | Share of snaps spent blocking (BLK%) | 1 |
| `blocks` | Punts blocked (BLK) | 1 |
| `breakaway_attempts` | Designed rush attempts of 15+ yards (D15+) | 1 |
| `breakaway_percent` | Breakaway % — share of rushing yards on 15+ yard runs (BAY%) | 1 |
| `breakaway_yards` | Breakaway yards — rushing yards on designed runs over 15 yards (BAY) | 1 |
| `btt_rate` | Big-time throw rate — % of attempts that are BTTs (BTT%) | 5 |
| `catch_rate` | Catch rate allowed — receptions/targets in coverage | 3 |
| `caught_percent` | Catch rate — receptions/targets (REC%) | 4 |
| `ce_percent` | Share of the offense's allowed pressures charged to the center (C%) | 1 |
| `comp_pct_diff` | Completion-% difference between this report's splits (concept comparison) | 1 |
| `completion_percent` | Completion percentage — completions/attempts (COM%) | 5 |
| `completions` | Completions (COM) | 5 |
| `contested_catch_rate` | Contested-catch rate — contested receptions/contested targets (CTC%) | 4 |
| `contested_receptions` | Contested catches made in tight coverage (CTC) | 4 |
| `contested_targets` | Contested targets (CTT) | 4 |
| `coverage_percent` | Share of pass snaps spent in coverage (COV%) | 2 |
| `coverage_snaps` | Coverage snaps (COV) | 1 |
| `coverage_snaps_per_reception` | Coverage snaps per reception allowed (S/REC) | 3 |
| `coverage_snaps_per_target` | Coverage snaps per target (S/TGT) | 3 |
| `declined_penalties` | Penalties on the player that were declined or offset (not enforced) | 23 |
| `def_gen_pressures` | Defense-generated pressures faced by the passer, any kind (DPR) | 5 |
| `designed_yards` | Yardage on designed runs (DYDS) | 1 |
| `downeds` | Punts downed by the kicking team (DWN) | 1 |
| `drop_rate` | Drop rate — on-target passes dropped as a share of catchable throws (DRP%) | 9 |
| `dropbacks` | Dropbacks — times the QB dropped back to pass (DB) | 5 |
| `dropbacks_percent` | Percentage of the QB's dropbacks in this split (DB%) | 3 |
| `dropped_ints` | Dropped interceptions (DRI) | 2 |
| `drops` | Drops — on-target passes dropped by the receiver (DRP) | 10 |
| `elu_recv_mtf` | Missed tackles forced as a receiver (Elusive Rating input) | 1 |
| `elu_rush_mtf` | Missed tackles forced as a rusher (Elusive Rating input) | 1 |
| `elu_yco` | Yards after contact (Elusive Rating input) | 1 |
| `elusive_rating` | Elusive Rating — PFF signature stat: runner success/impact independent of blocking (ELU) | 1 |
| `epa` | Expected Points Added on the player's plays [standard/EPA] | 9 |
| `explosive` | Explosive runs — designed runs over 10 yards (10+) | 1 |
| `fair_catches` | Fair catches (FC) | 2 |
| `fifty_attempts` | FG attempts from 50+ yards | 1 |
| `fifty_made` | FGs made from 50+ yards | 1 |
| `fifty_percent` | FG% from 50+ yards | 1 |
| `first_downs` | First downs gained (1st) | 10 |
| `forced_fumbles` | Forced fumbles (FFM) | 2 |
| `forced_incompletes` | Forced incompletions (FI) | 2 |
| `forced_incompletion_rate` | Forced incompletions per target (FI%) | 2 |
| `forty_attempts` | FG attempts from 40–49 yards | 1 |
| `forty_made` | FGs made from 40–49 yards | 1 |
| `forty_percent` | FG% from 40–49 yards | 1 |
| `fumble_recoveries` | Fumble recoveries | 1 |
| `fumble_recovery_touchdowns` | Touchdowns scored on fumble recoveries | 1 |
| `fumbles` | Fumbles | 5 |
| `gap_attempts` | Designed rush attempts on gap-scheme runs (GAP) | 1 |
| `grades_coverage_defense` | PFF grade, 0–100 (higher is better) — coverage defense (COV) | 6 |
| `grades_defense` | PFF grade, 0–100 (higher is better) — defense | 5 |
| `grades_defense_penalty` | PFF grade, 0–100 (higher is better) — defensive penalties | 5 |
| `grades_fgep_defense` | PFF grade, 0–100 (higher is better) — FG/XP block unit (defense) | 1 |
| `grades_fgep_kicker` | PFF grade, 0–100 (higher is better) — field-goal/extra-point kicking (FG) | 2 |
| `grades_fgep_offense` | PFF grade, 0–100 (higher is better) — FG/XP protection unit (offense) | 1 |
| `grades_hands_drop` | PFF grade, 0–100 (higher is better) — receiver hands / drops (DROP) | 6 |
| `grades_hands_fumble` | PFF grade, 0–100 (higher is better) — ball security / fumbles (FUM) | 5 |
| `grades_kick_return` | PFF grade, 0–100 (higher is better) — kickoff returns (KRTN) | 2 |
| `grades_kickoff_kicker` | PFF grade, 0–100 (higher is better) — kickoffs (kicker) (KOFF) | 2 |
| `grades_long_snap` | PFF grade, 0–100 (higher is better) — long snapping | 1 |
| `grades_misc_st` | PFF grade, 0–100 (higher is better) — miscellaneous special teams (SPEC) | 1 |
| `grades_offense` | PFF grade, 0–100 (higher is better) — offense | 6 |
| `grades_offense_penalty` | PFF grade, 0–100 (higher is better) — offensive penalties | 3 |
| `grades_overall_tackle` | PFF grade, 0–100 (higher is better) — overall tackling | 2 |
| `grades_pass` | PFF grade, 0–100 (higher is better) — passing | 5 |
| `grades_pass_block` | PFF grade, 0–100 (higher is better) — pass blocking (PBLK) | 4 |
| `grades_pass_route` | PFF grade, 0–100 (higher is better) — receiving / route running (RECV) | 7 |
| `grades_pass_rush_defense` | PFF grade, 0–100 (higher is better) — pass rush (PRSH) | 6 |
| `grades_punt_return` | PFF grade, 0–100 (higher is better) — punt returns (PRTN) | 2 |
| `grades_punter` | PFF grade, 0–100 (higher is better) — punting (PUNT) | 2 |
| `grades_return` | PFF grade, 0–100 (higher is better) — overall returns (kick & punt) (RETN) | 1 |
| `grades_run` | PFF grade, 0–100 (higher is better) — rushing | 4 |
| `grades_run_block` | PFF grade, 0–100 (higher is better) — run blocking (RBLK) | 3 |
| `grades_run_defense` | PFF grade, 0–100 (higher is better) — run defense (RDEF) | 4 |
| `grades_special_teams_penalty` | PFF grade, 0–100 (higher is better) — special-teams penalties | 1 |
| `grades_tackle` | PFF grade, 0–100 (higher is better) — tackling (TACK) | 5 |
| `hit_as_threw` | Hit as thrown — passer hit by a defender while throwing (HAT) | 5 |
| `hits` | QB hits — passer hit by the defender (HIT) | 3 |
| `hits_allowed` | QB hits allowed (HIT) | 3 |
| `hurries` | QB hurries (HUR) | 3 |
| `hurries_allowed` | QB hurries allowed (HUR) | 3 |
| `inline_rate` | Share of snaps aligned inline as a TE (INL%) | 1 |
| `inline_snaps` | Snaps aligned inline (INL) | 1 |
| `inside_twenties` | Punts inside the 20-yard line (I20) | 1 |
| `interception_touchdowns` | Interceptions returned for touchdowns | 1 |
| `interceptions` | Interceptions (INT) — thrown, if a passer; made/allowed on defense (see report) | 13 |
| `kicked_yards` | Total kicked yards | 1 |
| `kickoff_attempts` | Kickoff-return attempts | 1 |
| `kickoff_fair_catches` | Fair catches on kickoffs (FC) | 1 |
| `kickoff_long` | Longest kickoff return (LNG) | 1 |
| `kickoff_muffed_returns` | Muffed kickoff returns (MUF) | 1 |
| `kickoff_touchdowns` | Kickoff returns for TD (TD) | 1 |
| `kickoff_yards` | Kickoff-return yards (YDS) | 1 |
| `kickoff_ypa` | Kickoff-return yards per attempt (YPA) | 1 |
| `kicks_returned` | Kicks returned (RET) | 1 |
| `lg_percent` | Share of allowed pressures charged to the left guard (LG%) | 1 |
| `long` | Longest punt, yards (LNG) | 1 |
| `longest` | Longest single play, yards (LNG) — per report context | 8 |
| `lt_percent` | Share charged to the left tackle (LT%) | 1 |
| `missed_tackle_rate` | Missed-tackle rate (MIS%) | 4 |
| `missed_tackles` | Missed tackles (MIS) | 5 |
| `misses` | Missed tackles (as a pass rusher) | 1 |
| `non_spike_pass_block` | Allowed-pressure opportunities — non-spike, non-penalty pass-block snaps (OPP) | 2 |
| `non_spike_pass_block_percentage` | Share of pass-block snaps that were opportunities (OPP%) | 2 |
| `ol_te_percent` | Share charged to an OL/TE (OL%) | 1 |
| `one_attempts` | FG attempts from 1–19 yards | 1 |
| `one_made` | FGs made from 1–19 yards | 1 |
| `one_percent` | FG% from 1–19 yards | 1 |
| `onside_kicks` | Onside kicks (ONS) | 1 |
| `other_percent` | Share charged to another player (OTH%) | 1 |
| `out_of_bounds` | Punts out of bounds (OOB) | 1 |
| `pass_block_percent` | Share of snaps pass blocking (PB%) | 2 |
| `pass_block_rate` | Share of pass plays the player spent pass blocking | 4 |
| `pass_blocks` | Pass-block snaps | 4 |
| `pass_break_ups` | Pass breakups (PBU) | 3 |
| `pass_plays` | Pass plays the player was on the field for | 4 |
| `pass_rush_opp` | Pass-rush opportunities (snaps rushing the passer) | 1 |
| `pass_rush_percent` | Share of pass snaps spent rushing (RSH%) | 2 |
| `pass_rush_snaps` | Pass-rush snaps (PRSH) | 1 |
| `pass_rush_win_rate` | Pass-rush win rate — % of rushes won vs the blocker (WIN%) | 1 |
| `pass_rush_wins` | Pass-rush wins | 1 |
| `pass_snaps` | Pass snaps (PASS) | 1 |
| `passing_snaps` | Passing snaps — snaps on pass plays | 5 |
| `pat_attempts` | Extra points (PAT) attempted (XPA) | 1 |
| `pat_made` | Extra points made (XP) | 1 |
| `pat_percent` | Extra-point % (XP%) | 1 |
| `pbe` | Pass-blocking efficiency — pressure allowed per snap, weighted to sacks (EFF) | 2 |
| `penalties` | Total penalties charged to the player, PFF 'PEN: Total (Declined+Offset)' | 23 |
| `percent_returned` | Percentage of kicks returned (RET%) | 2 |
| `positive_epa_percent` | Percentage of plays with positive EPA [standard] | 9 |
| `pressure_to_sack_rate` | Pressure-to-sack rate — % of pressures that became sacks (P2S%) | 5 |
| `pressures` | Total pressures generated (as a pass rusher) | 1 |
| `pressures_allowed` | QB pressures allowed (PR) | 3 |
| `pressures_ce` | Allowed pressures charged to the center | 1 |
| `pressures_lg` | Allowed pressures charged to the left guard | 1 |
| `pressures_lt` | Allowed pressures charged to the left tackle | 1 |
| `pressures_off` | Total allowed pressures charged to the offense | 1 |
| `pressures_ol_te` | Allowed pressures charged to an OL/TE | 1 |
| `pressures_other` | Allowed pressures charged to another player | 1 |
| `pressures_rg` | Allowed pressures charged to the right guard | 1 |
| `pressures_rt` | Allowed pressures charged to the right tackle | 1 |
| `pressures_self` | Allowed pressures charged to the QB himself | 1 |
| `pressures_te` | Allowed pressures charged to a tight end | 1 |
| `prp` | Pass-Rush Productivity — pressure per snap, weighted to sacks (PRP) | 2 |
| `punt_attempts` | Punt-return attempts | 1 |
| `punt_fair_catches` | Fair catches on punts (FC) | 1 |
| `punt_long` | Longest punt return (LNG) | 1 |
| `punt_muffed_returns` | Muffed punt returns (MUF) | 1 |
| `punt_touchdowns` | Punt returns for TD (TD) | 1 |
| `punt_yards` | Punt-return yards (YDS) | 1 |
| `punt_ypa` | Punt-return yards per attempt (YPA) | 1 |
| `qb_rating` | NFL passer rating (NFL) | 5 |
| `qb_rating_against` | Passer rating allowed in coverage (NFL) | 4 |
| `rec_yards` | Receiving yards (for this rusher) | 1 |
| `receptions` | Receptions (REC) — caught, or allowed on defense (see report) | 9 |
| `return_yards` | Return yards (allowed by the kicking team) | 2 |
| `returns` | Returns (RET) | 1 |
| `rg_percent` | Share charged to the right guard (RG%) | 1 |
| `route_rate` | Share of pass plays on which the player ran a route | 4 |
| `routes` | Routes run | 5 |
| `rt_percent` | Share charged to the right tackle (RT%) | 1 |
| `run_block_percent` | Share of snaps run blocking (RB%) | 1 |
| `run_plays` | Run plays the player was on the field for | 1 |
| `run_stop_opp` | Run-stop opportunities — run snaps where a stop was possible | 1 |
| `sack_percent` | Sack percentage — sacks per dropback [standard] | 5 |
| `sacks` | Sacks (SK) — taken by the passer, or recorded by a defender (see report) | 8 |
| `sacks_allowed` | Sacks allowed (SK) | 3 |
| `safeties` | Safeties scored | 1 |
| `scramble_yards` | Yardage on scrambles (SYDS) | 1 |
| `scrambles` | Scrambles — undesigned QB runs (SCR) | 6 |
| `self_percent` | Share charged to the QB himself (QB%) | 1 |
| `slot_rate` | Share of snaps in the slot (SLT%) | 1 |
| `slot_snaps` | Snaps in the slot (SLOT) | 1 |
| `snap_counts_block` | Total blocking snaps (BLK) | 1 |
| `snap_counts_box` | Snaps aligned in the box | 1 |
| `snap_counts_ce` | Snaps aligned at center (C) | 1 |
| `snap_counts_corner` | Snaps aligned at cornerback | 1 |
| `snap_counts_coverage` | Coverage snaps | 3 |
| `snap_counts_coverage_percent` | Share of snaps in coverage | 1 |
| `snap_counts_defense` | Total defensive snaps | 1 |
| `snap_counts_dl` | Snaps on the defensive line | 1 |
| `snap_counts_dl_a_gap` | D-line snaps in the A-gap / as a nose tackle (AGP) | 1 |
| `snap_counts_dl_b_gap` | D-line snaps in the B-gap / as a DT (BGP) | 1 |
| `snap_counts_dl_outside_t` | D-line snaps outside the tackle (OUT) | 1 |
| `snap_counts_dl_over_t` | D-line snaps over the tackle (OVT) | 1 |
| `snap_counts_field_goal` | FG/PAT kicking snaps (FGK) | 1 |
| `snap_counts_field_goal_blocking` | FG/PAT block-unit snaps (FGBLK) | 1 |
| `snap_counts_fs` | Snaps at free safety (FS) | 1 |
| `snap_counts_kickoff` | Kickoff-coverage snaps (KCOV) | 1 |
| `snap_counts_kickoff_return` | Kickoff-return snaps (KRET) | 1 |
| `snap_counts_lg` | Snaps at left guard (LG) | 1 |
| `snap_counts_lt` | Snaps at left tackle (LT) | 1 |
| `snap_counts_offball` | Off-ball (non-line) snaps | 1 |
| `snap_counts_offense` | Total offensive snaps (OFF) | 1 |
| `snap_counts_pass_block` | Pass-block snaps (PBLK) | 2 |
| `snap_counts_pass_play` | Snaps on pass plays (PASS) | 5 |
| `snap_counts_pass_rush` | Pass-rush snaps (PRSH) | 2 |
| `snap_counts_punt_coverage` | Punt-coverage snaps (PCOV) | 1 |
| `snap_counts_punt_return` | Punt-return snaps (PRET) | 1 |
| `snap_counts_rg` | Snaps at right guard (RG) | 1 |
| `snap_counts_rt` | Snaps at right tackle (RT) | 1 |
| `snap_counts_run` | Run-defense snaps | 1 |
| `snap_counts_run_block` | Run-block snaps (RBLK) | 2 |
| `snap_counts_run_block_percent` | Share of snaps run blocking (SNP%) | 1 |
| `snap_counts_run_defense` | Run-defense snaps (RDEF) | 1 |
| `snap_counts_run_play` | Snaps on run plays (RUN) | 1 |
| `snap_counts_slot` | Snaps in the slot (Slot) | 1 |
| `snap_counts_te` | Snaps aligned as inline TE (ITE) | 1 |
| `snaps` | Snaps | 1 |
| `spikes` | Spikes — QB clock-stopping spikes [standard] | 5 |
| `stop_percent` | Stop % — share of run-defense snaps producing a stop (STOP%) | 1 |
| `stops` | Defensive stops — tackles constituting an offensive failure (STOP) | 5 |
| `tackles` | Tackles, solo (TKL) | 6 |
| `tackles_for_loss` | Tackles for loss | 1 |
| `targeted_qb_rating` | Passer rating when this player is targeted (RTG) | 4 |
| `targets` | Targets (TGT) — thrown to receiver, or into coverage on defense | 9 |
| `targets_percent` | Target rate — targets per snap (TGT%) | 3 |
| `te_percent` | Share charged to a tight end (ITE%) | 1 |
| `thirty_attempts` | FG attempts from 30–39 yards | 1 |
| `thirty_made` | FGs made from 30–39 yards | 1 |
| `thirty_percent` | FG% from 30–39 yards | 1 |
| `thrown_aways` | Throwaways — passes intentionally thrown out of play (TA) | 5 |
| `total_attempts` | Total attempts (FGs if kicking; kick+punt returns if a returner) — see report | 2 |
| `total_hangtime` | Total hangtime, seconds | 2 |
| `total_made` | Total field goals made (FG) | 1 |
| `total_net_yards` | Total net punting yards | 1 |
| `total_percent` | Field-goal percentage (FG%) | 1 |
| `total_pressures` | Total pressures — sacks + QB hits + hurries (TOT) | 2 |
| `total_touches` | Total touches (carries + receptions) | 1 |
| `touchbacks` | Touchbacks (TB) | 2 |
| `touchdowns` | Touchdowns (TD) — passing/rushing/receiving/allowed per report context | 14 |
| `turnover_worthy_plays` | Turnover-worthy plays — high INT-chance throws or poor ball security (TWP) | 5 |
| `twenty_attempts` | FG attempts from 20–29 yards | 1 |
| `twenty_made` | FGs made from 20–29 yards | 1 |
| `twenty_percent` | FG% from 20–29 yards | 1 |
| `twp_rate` | Turnover-worthy play rate — % of attempts that are TWPs (TWP%) | 5 |
| `wide_rate` | Share of snaps out wide (WID%) | 1 |
| `wide_snaps` | Snaps out wide (WIDE) | 1 |
| `yards` | Yards (YDS) — passing/rushing/receiving/punt per report context | 15 |
| `yards_after_catch` | Yards after catch (YAC) | 8 |
| `yards_after_catch_per_reception` | Yards after catch per reception (YAC/REC) | 4 |
| `yards_after_contact` | Yards after contact (YCO) | 1 |
| `yards_per_coverage_snap` | Yards allowed per coverage snap (Y/SNP) | 3 |
| `yards_per_reception` | Yards per reception (Y/REC) | 7 |
| `yco_attempt` | Yards after contact per attempt (YCO/A) | 1 |
| `ypa` | Yards per attempt (YPA) — per report context | 6 |
| `ypa_diff` | Yards-per-attempt difference between this report's splits (concept comparison) | 1 |
| `yprr` | Yards per route run (Y/RR) | 5 |
| `zone_attempts` | Designed rush attempts on zone-scheme runs (ZONE) | 1 |
