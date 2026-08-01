# FCS opponent ratings — method & verification (2026)

FBS teams play 100 distinct FCS opponents across 127 games this season. Each needs a power
rating on our FBS scale (0 = average FBS, negative = weaker) so the win engine can price the
game. These are **not** graded with the full unit-by-unit machinery — that would be
disproportionate effort for games that are almost all layups. Instead:

## Tiering

Anchored to the **2026 Opta/consensus FCS preseason Top 25** plus program knowledge, mapped to
FBS-scale points:

| tier | rating range | band | examples |
|---|---|---|---|
| elite | −18 to −22 | 9 | Montana State −18, Montana −19, South Dakota State −20 |
| strong | −24 to −28 | 9 | Illinois State −24, Rhode Island −26, Tarleton −27 |
| good | −30 to −35 | 9 | Incarnate Word −30, Lamar −32, SE Louisiana −33 |
| mid | −37 to −42 | 10 | Stony Brook −37, Nicholls −38, Murray State −41 |
| low | −44 to −52 | 10–12 | Sacred Heart −45, Robert Morris −46, Alabama A&M −48 |

The elite band (−18 to −20 for the top three) matches where SP+ has historically graded peak
FCS programs (NDSU/SDSU/MSU in their primes: −14 to −20). Bands are wide (9–12 pts) because
FCS rating uncertainty is genuinely high; this correctly widens `sigma_eff` and pulls upset
probabilities toward the model's tails.

## The "within 10 points" verification (owner's instruction)

The owner asked: an FCS team within 10 points of its FBS host should be **rare — maybe a
couple per year — and verified before accepted.** The engine produces **exactly two**:

1. **Nevada (−12.6) vs Montana State (−18), margin 7.7, Nevada 68%.** Verified: SI's 2026
   preview calls MSU the national-title favorite (returning championship-game MVP QB Justin
   Lamson, All-American RB Adam Jones) and says they "may even be the betting favorite" at
   Nevada — against former MSU coach Jeff Choate. Our 68% Nevada is, if anything, slightly
   generous to the FBS side. **Accepted as a genuine near-tossup — the single closest game on
   the board and the one to watch for an actual market line.**

2. **Northern Illinois (−16.0) vs Illinois State (−24), margin 10.3, NIU 73.7%.** Verified:
   ISU was the 2025 FCS runner-up (beat Villanova in the semis) but must replace its 40-TD QB
   Rittenhouse (unsettled two-man battle), with All-American LB Tye Niekamp and a 1,377-yd RB
   back. Strong tier with a QB question → −24 is fair; 73.7% NIU is defensible. **Accepted.**

Both games confirmed real and correctly sited (FBS home, non-conference) against CFBD schedule
data. That the model independently surfaces ~2 close FCS games — matching the owner's prior —
is a calibration signal in its favor.

## Defaults

Three opponents defaulted to −41 (mid) for lack of a specific read: East Texas A&M, Eastern
Kentucky, UT Rio Grande Valley (UTRGV is a first-year program). All are heavy road underdogs
regardless; the default does not create any flagged close game.

## Addendum 2026-08-01 — market-calibration protocol + three re-rates

Owner flag (BGSU/Tarleton market capture) exposed a stale input: Tarleton at
-27 ("strong") despite a 2025 #6 final ranking / FCS quarterfinal (12-3) and
Opta preseason #8. Re-rates applied: **Tarleton -27 -> -14** (owner capture
BGSU -0.5/-1.5 at home implies ~-12..-16; tier -> elite), **Montana State
-18 -> -15** (defending national champion, Opta #1), **Montana -19 -> -16**
(Opta #2). Rest of the Opta top 10 checked: table-consistent, unchanged.

**Standing protocol:** as FBS-FCS lines post in August, back out each FCS
team's market-implied rating vs our rated FBS opponent; any |table - implied|
>= 6 triggers a research read + adjudicated re-rate. Owner book captures are
first-class inputs. Note the original "within 10 of FBS host" tripwire was
sound but ran on the stale input; under the new numbers BGSU-Tarleton (+3.1)
correctly enters the verified-close-game class.

Board impact (calibrated lens, tracker): BGSU O4.5 our_p .739 -> .703
(edge +14.8% -> +11.2%) — survives bars; Nevada O4.5 .619 -> .610; OSU O3.5
.730 -> .722. No other totals touched (only these three FBS teams play the
re-rated trio).
