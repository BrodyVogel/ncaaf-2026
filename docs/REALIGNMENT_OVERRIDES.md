# Realignment / reclassification rating overrides (2026-07-20)

## Problem
A cluster of realignment / recent-FCS-reclass teams had unreliable roster grades (no FBS track
record), because the grader had no FBS-level data. This produced grade-implied ratings that were
wildly wrong in both directions (e.g. North Dakota State graded **−27**, a pure no-data artifact,
for a 9-time FCS champion). The assembly's cap + orthogonalization neutralized most of these — for
Sam Houston, Delaware, UNLV, etc. the *final* landed on SP+/market despite a garbage grade. But a
handful still ended up well **below SP+ and the market**, generating false win-total edges. NDSU's
broken −7.0 was topping the board with a spurious Under 8.5.

## Diagnosis (final vs SP+ 2026 preseason)
Teams whose final sat meaningfully below SP+ (grade dragging them down, not real signal):

| team | our final (pre-fix) | SP+ | gap |
|---|---|---|---|
| North Dakota State | −7.0 | −1.4 | −5.7 |
| Colorado State | −13.4 | −8.3 | −5.1 |
| Kennesaw State | −13.5 | −9.3 | −4.2 |
| Jacksonville State | −10.5 | −7.7 | −2.8 |
| Boise State | +4.1 | +6.8 | −2.7 |

(The rest of the rebuilt Pac-12 — SDSU, Fresno, Wazzu, Utah State, Texas State — sat *at or above*
SP+, so their market unders are real edges, not errors, and were left alone.)

## Fix
Each was researched individually (web: returning production, departures, coaching, transfers,
reclassification comps) and given a fair value, logged with rationale in
`data/manual_overrides_2026.csv` and applied in `final_pass.py` (post-recenter; `--no-overrides`
reproduces the pure-model ratings):

| team | override | basis |
|---|---|---|
| North Dakota State | **+2.0** (band 8.0) | Research center +3.0, but market total (8.5–9.5) implies ~+1.5–2; set +2.0 to fairly-price a no-FBS-data team rather than flag an overconfident over. Wide band for reclass uncertainty; "FBS debut" flag warns in the UI. |
| Boise State | **+5.0** | Real WR/OL losses post-Jeanty (FPI +4.0 agrees with our grade); small nudge up from +4.1. Market +9.7 stays an over-hype → its under remains a real edge. |
| Colorado State | **−9.0** | New HC Mora + total roster reset; our −13.4 was an outlier below every public source. ≈ SP+ with slight QB-risk tilt. |
| Kennesaw State | **−10.5** | Defending CUSA champ; our −13.5 too low. ~1 below SP+ for the big offensive rebuild. |
| Jacksonville State | **−8.0** | 3 strong FBS years, returns dual-threat QB; our −10.5 too low. ≈ SP+. |

Note the four non-NDSU overrides all land *at or slightly below* SP+, so they don't overshoot into
spurious overs — they just stop dragging these teams below the market floor. NDSU is the only one
set above SP+, and deliberately kept near the market so it doesn't generate a high-conviction edge
on a team we can't confidently rate (it now ranks 116/138 by conviction, down from #1).

## Effect
NDSU's false Under 8.5 (was the board's top edge) is gone. Boise/SDSU/Wazzu unders remain (real:
market over-hypes the rebuilt Pac-12; we and SP+ agree they're lower). Field mean drifts +0.15
(immaterial). Ratings re-locked: `ASSEMBLY_LOCKED_2026-07-20.csv`.

## AUDIT CORRECTION (2026-07-20, Fable)
The "Effect" paragraph's market reads ("Boise/SDSU/Wazzu unders remain real edges") predate the discovery that all 8 Pac-12 schedules were missing the Week-13 flex game (see docs/AUDIT_2026-07-20_fable.md §1). With the 12th game restored, the Pac-12 unders largely evaporate (Boise flips to a modest over at 7.5). The rating overrides themselves are unaffected — they were and are correct.
