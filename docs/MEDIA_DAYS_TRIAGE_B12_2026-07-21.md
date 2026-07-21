# Big 12 media-days triage — 2026-07-21 (worked example)

Source: `data/media_days/B12_2026_media_days.md` (event July 7–8, Frisco TX — pre-dates our
2026-07-12 baseline; treated as un-ingested source + July 8→21 delta sweep).
Method: every team section cross-checked against `snapshots/<Team>/{unit_dossiers.md,
grades.json,news.md}`. Grader: Fable, per owner-approved plan (2026-07-21).

**Outcome: 0 grade changes, 0 confidence changes, 6 watch-list notes, 2 digest-flag
resolutions.** The Big 12 digest is confirmations of things our snapshot already priced.
That is the expected result for an event that happened *before* our baseline froze.

## Decision rules (conventions for all four conferences)

- **R1 — grade moves need new material facts** about talent, availability, or room
  composition, sourced `[QUOTE]`, multi-source, or corroborated by our own files.
  `[AGGREGATED]` and spring-dated beat *projections* never move a grade.
- **R2 — confidence L→M only when the dossier's own L rationale cites the uncertainty
  that media days resolved.** A presumed starter being confirmed does NOT flip L: our
  L usually flags tape/quality uncertainty, which survives a podium confirmation.
  (Canonical flip case: Hawai'i LB, where the dossier literally says "L: Otis
  availability" and media days resolved availability.) Confidence edits are
  **sim-affecting**: band = 1 + 0.03·min(L-count, 5) in final_pass.
- **R3 — single-source `[REPORTED]` injury/roster claims we cannot corroborate →
  watch-list, no action.** Apply extra suspicion when the move would *help* one of our
  open bets (motivated-reasoning guard; see ASU Gardner below).
- **R4 — provenance**: changes land in `grades.json` (units + grades_detail) with the
  unit named in `_meta.planned_vs_final_deviations` + a dated
  `snapshots/<Team>/media_days_addendum.md`; frozen dossier text is never edited.
  Gate with `pipeline/grades_check.py <Team_Dir>`, rebuild with `final_pass.py`.

## Per-team dispositions (16)

| Team | Digest highlight | Cross-check vs our files | Disposition |
|---|---|---|---|
| Arizona | Fifita confirmed; JUCO DB add 7/8; Brennan Heisman push | QB 88 H already prices it | CONFIRMATION |
| Arizona State | Dillingham: job "isn't locked up" (Boley presumed); Fite lone DL returner; **Gardner 2nd Achilles** (single src); Clayton Smith waiver return | QB 48 M consistent with open-ish race; Smith return in dossier as explicit override; DL 51 M rationale does NOT lean on Gardner (Fite+Smith+P4 restock, "8-man rotation") | CONFIRMATION + **WATCH W1** (Gardner: single unverified `[REPORTED]`; would *help* our ASU U6.5 → R3 bar applies doubly; revisit in camp) |
| Baylor | Lagway confirmed + "freedom" quotes; LB trio named (Reed/Burns/Barnes, player-sourced) | QB 52 M priced Lagway; LB trio matches our graded room 1:1 (Barnes yr-4 injury override, Reed, Burns; Thomas→Ole Miss gone) | CONFIRMATION. LB stays 38 **L** per R2 — our L is talent-signal-driven ("pedigree the only above-average signal"), and identity confirmation doesn't resolve tape |
| BYU | (not an open-question team) Bachmeier settled; Glasker health flagged | Not swept systematically by digest; no action | NOTE only |
| Cincinnati | French confirmed QB1; DC Woody scheme shift; Peek to SAM; WR1/TE1 beat-projected | QB 44 M priced French; WR names are `[AGGREGATED]` previews → R1 bars them | CONFIRMATION; WRTE stays 40 L |
| Colorado | Lewis confirmed starter; Scudero touted; 66 new players; OL beat-projected | Dossier header: "the job is his to lose" — priced; Scudero haul already keyed in WRTE 56 ("my 56 already credits the haul") | CONFIRMATION |
| Houston | Weigman "without question" + first healthy offseason; Henderson to play early | QB 62 M priced the room incl. Henderson packages | CONFIRMATION |
| Iowa State | Raynor "going into camp as the one"; WR/TE/OL/LB names are spring projections | QB 48 M priced Raynor winning the job in spring; rebuild units stay L (projections barred by R1) | CONFIRMATION; WRTE/OL/LB stay L |
| Kansas | Race open (Ballard vs Marshall); **Jenkins absent** from on-record contenders; Edwards (KSU) RB add | QB 42 M priced a 3-way; Edwards KSU→KU cross-ref already verified in BOTH dossiers | CONFIRMATION + **WATCH W2** (Jenkins not named at podium — if he's a non-factor by camp, the room is slightly thinner than graded; no move now) |
| Kansas State | Klein transition quotes; Jayce Brown→LSU; Edwards injury context | Brown→LSU in dossier ("GONE: J.Brown → LSU"); Klein-as-HC in dossier (QB rationale: Klein reunion) — digest's "flagged for verification" resolved by our files | CONFIRMATION + resolves digest flag |
| Oklahoma State | Mestemaker treated as starter, no lock quote; Morris "hard reset," 85+ new | Dossier priced Mestemaker + "HC Morris + OC Brophy ran the exact offense at North Texas." Digest's "SNAPSHOT ERROR: Gundy" was an error in **my prompt**, not our snapshot | CONFIRMATION + **WATCH W3** (no explicit lock; treat as named-in-practice) |
| TCU | Craig confirmed, no competition; OC Sammis run-more scheme note | QB 46 M priced Craig | CONFIRMATION + **WATCH W4** (Sammis scheme = beat-preview; verify in camp if TCU totals move) |
| Texas Tech | McGuire: Hammond "week one, if not week one for sure week two" | Dossier priced the ACL explicitly: "(ACL, August return)... 50, M = tape + pedigree + surroundings vs ACL timing" — podium timeline **consistent, slightly better** | CONFIRMATION (timeline validated; no move — 50 M already discounts ACL risk) |
| UCF | Frost: Barnett "the guy"; **spring injury, "full go" by camp** | Dossier has NO spring-injury mention (new fact), but resolution is positive and pre-camp | CONFIRMATION + **WATCH W5** (if camp reports contradict "full go," QB 52 M needs a look) |
| Utah | Scalley on Dampier: played >half 2025 hurt, Jan sports-hernia surgery, now healthy | QB 70 M priced the player; health arc is upside color; Scalley-as-HC consistent with our files | CONFIRMATION |
| West Virginia | Rodriguez declined to name QB1; Hawkins framed as ceiling vs Fox | QB 44 M priced exactly this open battle (Hawkins = Athlon's printed QB1) | CONFIRMATION |

**Digest-flag resolutions (our files answer their open flags):**
1. *Austin Romaine conflict* (KSU-outgoing vs TTU-LB): not a conflict — KSU dossier: "Romaine
   (76.5/517, 2x All-B12) → TT"; TTU dossier: "## LB — Roberts + Romaine." Transfer, both sides recorded.
2. *K-State HC identity*: Collin Klein is HC in our snapshot (QB rationale keys the Klein reunion).

**Poll note:** the unofficial beat-writer poll (TTU 1st/14 FP votes, BYU 2nd) and the coaches'
poll (BYU 1st) are consensus color only — grades are anchor-blind; no action. Preseason
All-B12 list ingested as context.

**Camp re-sweep queue (B12):** ASU/Kansas/WVU QB resolutions; W1–W5 above.
