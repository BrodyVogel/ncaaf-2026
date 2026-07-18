# Sun Belt (SBC) Round — magazine page map (2026)

Magazines: "Athlon 2026 - SBC.pdf", "Phil Steele 2026 - SBC (searchable).pdf"
(both in /mnt/user-data/uploads/NCAAF Data 2026/).
G5 = TWO-SOURCE build (Athlon + Phil Steele). NO Pick Six for the Sun Belt (Pick Six covers only
the P4 conferences + Notre Dame). R16's required-3rd-source rule is P4-only.

## MEMBERSHIP NOTE (2026 realignment)
This 2026 dataset's Sun Belt = 14 teams. Texas State LEFT for the Pac-12 (already built in the Pac-12
round). Louisiana Tech JOINED the Sun Belt West (Athlon SBC p12 header: "SUN BELT WEST PREDICTION: 3";
Athlon CUSA excludes it; PS SBC includes it). La Tech's 2025 tape was earned in CUSA (record "5-3
CUSA") -> its RETURNING production uses the CUSA cells (origin), even though 2026 home = Sun Belt.
=> CUSA round drops to 10 teams. Total unbuilt = 14 (SBC) + 10 (CUSA) + 2 (Independents) = 26.

## Athlon SBC (grouped East then West; NOT strictly alphabetical) — readable text layer
| Team | Athlon p | Div |
|------|:--------:|-----|
| Appalachian State | 3 | East |
| Coastal Carolina | 4 | East |
| Georgia Southern | 5 | East |
| Georgia State | 6 | East |
| James Madison | 7 | East |
| Marshall | 8 | East |
| Old Dominion | 9 | East |
| Arkansas State | 10 | West |
| Louisiana | 11 | West |
| Louisiana Tech | 12 | West (NEW - tape origin CUSA) |
| South Alabama | 13 | West |
| Southern Miss | 14 | West |
| Troy | 15 | West |
| UL Monroe (ULM) | 16 | West |

## Phil Steele SBC — non-sequential (15pp; team names in page margins; pin per-team)
Method (per SEC/ACC): grep the PS SBC PDF for the team's coach name / unique QB to locate its page,
then render via pdftoppm -r 200 -png and Read the image if the text layer is garbled.

## Batch plan (4 batches, alphabetical; checkpoint between each)
- Batch 1: Appalachian State, Arkansas State, Coastal Carolina, Georgia Southern
- Batch 2: Georgia State, James Madison, Louisiana, Louisiana Tech
- Batch 3: Marshall, Old Dominion, South Alabama, Southern Miss
- Batch 4: Troy, UL Monroe + full 14-team SBC round wrap

## SBC methodology note
The Sun Belt conference offsets are NEGATIVE/small (QB -1.01, RB -2.02, WRTE -0.74, OL -0.35,
DL -6.50, LB -8.20, DB -3.62). SBC teams' RETURNING tape uses the SBC cells at face value; arrivals
use their origin cells (FCS/JUCO = NO CELL, evidence-only). Watch for P4/G5-up transfers (common
landing spots) and heavy FCS-arrival rosters. La Tech returning tape = CUSA cells (origin).
