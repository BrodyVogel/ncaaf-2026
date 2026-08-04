# Deep-dive procedure — season QB props (for the reviewing model, 2026-08-04)

You are reviewing ONE proposed prop bet in depth. Your job is not to
confirm it — it is to try to kill it, and to report what survives. The
candidate list and all quantitative context live in:
`docs/research/FINDINGS_S20_2026-08-03.md` (read fully first),
`docs/research/PREREGISTRATION_S20_2026-08-03.md` (the rules you inherit),
`data/cfbd/qb_props/` (panel, per-game flat file, pricer v0/v1 JSONs).
House context: this repo's audit history (AUDIT_2026-08-03_FULL_STACK.md)
is the cautionary tale — name-join bugs, silent data loss, and motivated
reasoning are the recurring failure modes here. Check joins before
trusting any number, including ours.

Work the steps IN ORDER. Each produces a written subsection. If any step
returns a kill, say so immediately at the top of your report and finish
the remaining steps anyway (the post-mortem value is the point).

## Step 0 — Rules gate (kill switch, needs live web)

Pull FanDuel's actual house rules text for "Regular Season passing yards":
does "regular season" include conference championship games? All-action or
void-if-doesn't-play? Dead-heat rules? Any start-requirement? If CCGs are
INCLUDED, the availability math shifts for CCG-likely teams and the v1
number for this QB must be recomputed before proceeding — flag and stop.
Confirm the line/juice still stand (−113/−113 baseline; if the line moved
≥100 yards toward us since 2026-08-03, ask what the market learned).

## Step 1 — Re-derive the number (local data only)

Rebuild the QB's 2025 per-game reg-season pace from
`data/cfbd/qb_props/player_games_flat.csv` yourself. Verify: name variants
(suffixes!), team assignment, game count, no missing weeks. Recompute
ratio = line / (12 × pace) and the v1 probability from the ladder in the
findings doc. If your number differs from pricer_v1 JSON by >0.01, stop
and reconcile before anything else. Data hygiene IS the edge here.

## Step 2 — Availability audit (the whole thesis; needs live web)

The v1 edge is ~entirely an availability bet: P(12 meaningful games) ≈
40–46% in every historical cell. For THIS QB, gather with dated sources:
injury history (all seasons, soft-tissue vs structural), current camp
health, playing style (sack/scramble exposure — pull his pressure/rush
numbers from the PFF files), the backup situation (our snapshots grades:
a touted QB2 raises pull risk in blowouts AND bench risk; an empty room
lowers both), and any redshirt/draft-preservation chatter. Deliverable: a
game-count distribution for this QB — your honest P(12), P(10–11), P(≤9)
— vs the panel's 45/15/40 shape, with reasons. If you conclude P(12) ≥
65%, the bet likely dies; say so with the arithmetic.

## Step 3 — Volume audit (needs live web + repo)

Scheme continuity: same OC/system as 2025? (Check snapshots/<team>/META
coach_note first — it is usually ahead of press coverage — then verify
nothing changed since 2026-07-12.) New-OC air-raid hire = volume-up risk
for an under. Team pace and pass-rate history; OL pass-pro grade from our
files (a collapsing OL cuts BOTH ways: more dropback yards needed, more
hits taken). WR room per our unit grades. State a per-game pace estimate
with a range, and whether it moves the v1 number.

## Step 4 — Schedule walk (repo only)

Walk all 12 games from `outputs/win_totals_payload.json` schedules: our
win prob and expected margin per game, opponent pass-defense from the
anchor off/def splits. Count: projected blowout LOSSES (the only script
state that suppressed pace historically: −51 yd/g; blowout WINS do NOT —
H9), likely backup-mop-up spots, bye placement, late-season weather sites.
Note games vs teams we hold positions on (correlation with the existing
book).

## Step 5 — Market context (needs live web)

Has any other book posted this market? If so: line comparison — are we
betting INTO a consensus or against one book's number? Check for steam
since posting. Note limits and whether the account matters (props get
profiled fast). If the number moved toward our side ≥100 yards: what did
the market learn that we haven't? Answer it, don't wave at it.

## Step 6 — Adversarial pass (mandatory)

Write the strongest OVER case in ≥150 words as if you were betting it:
development curve (year-2 starters held pace flat historically — that was
the OWNER's confirmed intuition), award/draft volume incentives, schedule
softness, scheme upgrade, the desk's information advantage on their own
marquee names. Then list the 2–3 observable kill criteria that would
flip this bet dead (e.g., "named QB2 transfers out," "OC announces tempo
increase," "line moves to X"). These go in the tracker note.

## Step 7 — Verdict + sizing

Template: BET / PASS / WATCH(trigger). If BET: 0.10–0.15u per the S20
pilot lane, ≤5 props total across the board, and the bet is NOT placed by
you — it returns to the owner with this report. Include: final p(under),
edge vs .5305, the three numbers that carry the conclusion, and the
tracker-ready entry line (date, market, line, odds, book, stake, note
with kill criteria). Log CLV plan: re-check the line at Week 0 and at
season close.

## Reporting format

One markdown file per QB: `docs/research/deep_dives/DD_<qb>_<date>.md`,
sections 0–7, every external claim dated and sourced, every internal
number reproducible from a named repo file. Verdict in the first line.
No grades or ratings changes from this process — findings that implicate
the main model go to the owner as flags, not edits.

## CORRECTIONS (2026-08-04, append-only — apply to all subsequent dives)

1. **Step 0 kill switch as written is WRONG — do not follow it.** It assumes
   the historical panel is a strict-12 basis. It is not: the S20 panel used
   CFBD seasonType=regular, which INCLUDES conference championship games.
   Therefore: FD-includes-CCGs = matches panel basis (approximately neutral;
   for CCG-LIKELY teams it is mildly ANTI-under, since their true P(13th
   game) far exceeds the panel's ~6% — quantify per team); FD-excludes-CCGs
   = under bonus (use the strict-12 column in pricer_v2 JSON). Neither
   branch is a stop. The FD text itself is still unverified for this market
   — owner verification remains a pre-stake gate.
2. **Step 1 basis:** prior pace = total yards / games with ≥10 attempts
   (panel-consistent, confirmed 181/181). Do NOT divide by all games played;
   relief cameos corrupt the anchor (Carr, Sellers, Chambliss cases). Strip
   generational suffixes before joining (the "Demond Williams Jr." case —
   the Step 1 warning about suffixes was vindicated in practice).
3. **Benchmark pricer is now v2** (pricer_v2_2026-08-04.json, spec in
   PRICER_V2_SPEC_2026-08-04.md). Step 1's reconcile-within-0.01 check runs
   against v2's p_raw/p_v2, and Step 1 must quote BOTH the v1 and v2 numbers
   so drift stays visible. The DD's job is the judgment layer ON TOP of v2's
   mechanical price: availability vs the hazard base rate, CCG probability,
   scheme/destination context the transfer shift can't see, benching risk.
