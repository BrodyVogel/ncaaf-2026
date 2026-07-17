# DISPOSITION RULES — the precedent book (v1.0, 2026-07-17)

Codified from 71 builds for the operator handoff. Every returns/leaves call
that the feeds cannot settle mechanically is governed by a NAMED RULE below.
Apply the rule, record the mechanism in META.json (bare-name key) + news.md
(rationale), and let `disposition_ledger.py` verify it. When a case fits no
rule, adjudicate conservatively, document a NEW named precedent here, and
tell the owner in the team summary.

"Both prints" = Athlon + Phil Steele 2026 editions (May-printed). "Print
conflict" = the two disagree. "Feed" = the frozen CFBD portal pulls
(data/cfbd/2026-07-12). "Tape row" = a PFF unit-csv row with 2025 volume.

---

## 1. Portal departures (out-feed)

**R1. Destination rule.** Out-feed WITH a destination = GONE, full stop.
Citing them as a returner is an error (the original Hopper error — Tulane's
best DL claimed as returning while his own team's out-feed showed Colorado;
DL was re-graded 50→38).

**R2. Rogers rule (no-dest + both prints start him = STAYS).** Out-feed with
destination None means "entered the portal" — the player may have withdrawn.
If BOTH prints carry him as a 2026 starter, he STAYS. Record in META
`portal_withdrawal_overrides` (bare name). Precedents: Rogers, the
Houston/Booth pair, and UTEP's Content + Coker (first double-STAYS build).

**R3. Flowe rule (withdrawn + single print = GONE).** A "withdrawn" report
or single-print appearance is NOT enough — no-dest + only one print = GONE.
Two-print anchoring is the bar (Gales/Cochnauer/Foster/Conti precedents).

**R4. No-dest + absent from both prints = GONE (adjudicated).** Record in
META `portal_departure_confirmed`. The commonest case (47 across the field).

**R5. Destination-resolution pattern.** A prior build's no-dest GONE stays
correct when the player later surfaces at another team — the RECEIVING build
resolves the destination and documents it; no retro change to the origin
build. Precedents: Givens→Nevada, Sibley→UNM, Louis-Nkuba→UNLV,
DeRosa→Hawai'i (SJSU's GONE stood).

## 2. Year-4 expirations (roster year fields)

**R6. Default.** CFBD roster year == 4 (or 5/6), not in the portal, absent
from both prints = EXPIRED(yr4). The feeds never see graduation.

**R7. May-print rule (two-print yr4 override = RETURNS).** yr4 player whom
BOTH prints carry as a 2026 starter RETURNS — the May prints trump the year
arithmetic (bonus/medical years are invisible to CFBD). Record bare name in
META `yr4_return_overrides_documented`. Precedents: Orji + D.Harris (UNLV),
Stuhlsatz (Wyoming — both prints' MLB1), McCoy (Hawai'i — PS's own "lose six
DL" count excluded him), Fiaseu/Kirkland/Finneseth (documented at build;
keys restored in the 2026-07-17 audit).

**R8. Jordon Thomas / Laubstein rule (single print + explicit mechanism =
RETURNS).** One print suffices ONLY when it states the mechanism in words —
a documented medical year, OFY, or waiver ("was OFY in July", "redshirted
2025"). Precedents: Jordon Thomas, Laubstein, Kam Thomas + Jaden Smith
(UTEP — OFY mechanisms printed).

**R9. Goodell/Hilty rule (single-print yr4 DEPTH = EXPIRED + note).** A yr4
player appearing in only one print, in a depth slot, with no stated
mechanism, EXPIRES — with the appearance noted in META
known_name_exceptions. Precedents: Goodell, Hilty, Robinson (Wyoming),
Adeyi (Northwestern — "feed governs"), Hook (Rice — enforced by the
2026-07-17 audit).

## 3. Departures the feeds cannot see

**R10. Spoth rule (research-GONE).** Feed-silent + absent from BOTH prints
= departure_confirmed_research (grad-transfer gaps, wrong feed year fields,
short-surname name forms). Strongest form adds print-explicit language
(NDSU's B.Kpeenu: "he departs"). Precedents: Spoth, Schuchts (UTEP).
NOTE: if the player has no roster/tape row at all, the entry is
documentation-only — put it in known_name_exceptions instead (Kpeenu final
form; the validator enforces this).

**R11. Fano/Lomu rule (early NFL declares).** Draft entries are invisible to
both portal and yr4 logic. Record in META `nfl_declare_confirmed` with the
print/draft evidence (Utah's Fano/Lomu; NDSU's Payton + Lance).

## 4. Arrivals

**R12. Strickland rule (feed-gap arrival).** An arrival in print(s) but
absent from the in-feed is documented in META `feed_gap_arrivals_documented`.
Two prints = full weight (DeRosa, Heil, C.Cheeks, Trapp); single print =
documented with modest/no grading weight (Strickland, Sims, Edmond,
Patterson, McCants).

**R13. Two-sided feed misses exist.** Six confirmed cases where BOTH teams'
feeds missed a real transfer (Anderson SacSt→SJSU, Turner-Gooden SJSU→Nevada,
Mathews Memphis→UNM, Walsh ISU→UNM, Epstein CMU→UNM, Helm TCU→UNLV). Prints
+ destination-side evidence govern. Feed absence is never proof of absence.

**R14. Offsets keyed to WHERE TAPE WAS EARNED.** Returning tape uses the
conference the snaps were played in (ex-conference rule: NIU returning tape
= MAC cells; UTEP = CUSA cells). Arrival tape uses the origin conference's
cells. FCS/D2/D3/NAIA/JC/Ivy = NO CELL — evidence-only, never invent an
adjustment. FBS newcomers (SacSt, NDSU) are evidence-only builds end to end.

## 5. Conflicts and name hygiene

**R15. Data-over-print precedence.** When a PFF tape row (with provenance)
contradicts BOTH prints on where a player played, the TAPE GOVERNS
(J.Brown-UTEP: both magazines said Michigan State '25; PFF shows 126 routes
at UTEP '25). Print asterisks/labels can simply be wrong (Lowe-UTEP's
phantom transfer asterisk).

**R16. Feed-over-print for identities.** The feed's name form settles
print-vs-print identity conflicts (Keith-not-Damian Williams at NDSU;
Anene-not-Akene). Watch name COLLISIONS (Kene Anene arrives while Toby Anene
departs; Jake Wilson TE returns while Brayden Wilson DE expires; two
Harrises at Hawai'i; Kpeenu brothers) and name VARIANTS (Ellijah/Elijah,
Drew/Andrew — the ledger's surname+first-prefix matcher handles most).

**R17. PFF-position convention (Hubert/Echoles).** A player is graded in the
room of his PFF tape position, whatever the prints slot him (Hubert ED→DL;
Vincent LB-tape counted LB though Athlon lists him at S). Note the print
usage.

**R18. Print conflicts on availability are graded as uncertainty.** PS "full
go" vs Athlon "unclear" (Otis-Hawai'i ACL) → cite both, grade the room, mark
the unit L. Never silently pick a side.

## 6. Mechanics (enforced by the gates)

- META override keys are BARE PLAYER NAMES. Rationale goes in
  known_name_exceptions / news.md. (Sentence-form keys silently match
  nothing — the Stuhlsatz slip; `disposition_ledger` now hard-errors.)
- Any GONE-class ledger name appearing in the two-deep player column is a
  hard error (`disposition_ledger` reconcile — the check that caught 5
  mis-graded units in the 2026-07-17 retro-audit).
- Departed players are described in the two-deep NOTE column, never the
  player column.
- Two-deep depth ≠ disposition: a returner absent from print two-deeps can
  still RETURN as depth (Geiger-Wyoming); the ledger's RETURNS is the
  default for non-yr4, non-portal roster players.
- Gates run with Team_Dir in UNDERSCORE form, exact accents/apostrophes
  (Hawai'i, San_José_State). A wrong form now FAILS loudly instead of
  silently skipping.
