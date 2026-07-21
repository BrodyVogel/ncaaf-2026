# Mountain West media-days triage — 2026-07-21

Source: `data/media_days/MWC_2026_media_days.md` (July 15–16, Palms, Las Vegas — post-dates
our 2026-07-12 baseline, so podium content is genuinely new). Method + decision rules
R1–R4: `docs/MEDIA_DAYS_TRIAGE_B12_2026-07-21.md`. Grader: Fable.

**Outcome: 2 grade changes (Hawai'i LB 12L→14M, NIU QB 18L→20L), 1 schedule-data fix
(NDSU–SJSU is_conf), 2 digest-flag resolutions, 3 watch-list notes.** `final_pass` has NOT
been run — boards/payload are stale until the step-4 rebuild (Opus).

## Grade changes (full detail in the per-team addenda)

1. **Hawai'i LB 12 (L) → 14 (M)** — `snapshots/Hawai'i/media_days_addendum.md`. The
   canonical R2 case: dossier says "L: Otis availability"; media days resolved it (player
   rep, preseason All-MW, "fully healthy ahead of camp," MIKE→dime). +2 only — "tape
   modest even healthy" survives; exemplar ceiling (< FIU QB 15) holds. L-count 4→3
   (band ×1.12→×1.09 at rebuild). **Moves against our open Hawai'i U7.5 — quantify in the
   step-5 memo.**
2. **NIU QB 18 (L) → 20 (L)** — `snapshots/Northern_Illinois/media_days_addendum.md`.
   R1 room-composition change: Dickens (WCU, SoCon OPOY) signed ~July 3, absent from the
   graded room. +2 to the SacSt/Wyoming FCS-transfer 20-tier; July arrival + academics
   wrinkle + open battle cap it. Confidence stays L. (NIU is a Hawai'i opponent —
   partial offset for the U7.5.)

## Schedule-data fix

**NDSU–SJSU 2026 flagged non-conference** (edit in `pipeline/win_totals_data.py`,
takes effect at rebuild). CFBD marks it `conferenceGame=True`, which gave both teams 9
conference games — the only census outliers in a league whose slate is a balanced 8
(CBS Sports; NDSU's stated composition "8 MW + 3 non-conf FBS + 1 FCS" per
ESPN/Sportico/NDSU; SJSU's 13th game rides the Hawai'i exemption, customarily non-conf).
Zero live-market impact (neither team has posted conference totals); fixes the artifact's
conference-tab distributions. **Step-4 check: post-build MW census must be {8: 10}.**

## Per-team dispositions (10)

| Team | Digest highlight | Cross-check | Disposition |
|---|---|---|---|
| Air Force | Szarka confirmed (1 of 3 returning MW starters); DL rebuild spring-sourced | QB 32 M priced; digest couldn't confirm our Adams/Grobe departure premise — our dossier is the primary source, stands | CONFIRMATION |
| Hawai'i | Otis resolved healthy; K Olvera-Harle named, P = intl TBD; DL/OL preview-only; Alejado preseason OPOY | LB regrade above; ST 12 L stays (quality-driven, R2); QB 38 M graded on tape, honors are color | **REGRADE (LB)** |
| Nevada | QB open into camp, contender sets conflict across sources; WR adds; EJ Smith returns | QB 18 L consistent; Smith RETURNS already in dossier (65.4/280, 8 st); WR names preview-sourced (R1) | CONFIRMATION + **WATCH W1** (contender-set conflict — camp re-sweep) |
| New Mexico | Layne confirmed; Eck preseason DPOY; most returning production in MW | QB 34 M priced; all consistent | CONFIRMATION |
| NDSU | Membership + attendance CONFIRMED; Hayes named starter; Woolen returns; preseason honors ×4 | Model's MW treatment validated; QB 14 L stays per R2 (the L is zero-starts evidence, not identity); Woolen RETURNS as graded (our prompt's open question mis-framed him as a loss — digest handled it; 41-vs-86 tkl = solo-vs-total noise) | CONFIRMATION + **SCHEDULE FIX** |
| NIU | Dickens expected to lead; play-caller "conflict" (Petersen vs Sanders); DL/LB April projections | QB regrade above; conflict RESOLVED by our META (co-OCs Sanders + Petersen — each outlet named one); HC change priced (coach_change ×1.13); DL/LB 10 L stand (R1) | **REGRADE (QB)** + resolves digest flag |
| SJSU | QB 3-way "close," early-camp decision; WR replacements = genuine gap | QB 20 L consistent; WRTE 16 L stands (gap honest) | CONFIRMATION + **SCHEDULE FIX** |
| UNLV | Arnold presumptive, Mullen slightly open (Orji); Lyons preseason All-MW; Conti lone DL returner | QB 36 M priced exactly this; Lyons RETURNS in dossier (62.4/114, outside the departed top-4); DL 18 L consistent | CONFIRMATION + **WATCH W2** (Lyons honors vs our WRTE 16 L — if camp corroborates, revisit) |
| UTEP | Colson named QB1 in early May ("clear cut"); OL five + DL rotation = genuine gaps; staff answered | Colson already in dossier w/ exact UIW line; QB 16 L stays per R2 (tape/projection-driven); OL 8 L / DL 10 L stand | CONFIRMATION |
| Wyoming | Hughes presumptive, officially open until camp; WR/DL name lists (official site) | QB 20 L consistent (the rail NIU now joins); names ≠ tape (R1) | CONFIRMATION + **WATCH W3** (if Sawvel names Hughes early in camp, no action needed — grade already assumes him) |

**Digest-flag resolutions:** NIU play-caller (our META: co-OCs, both real); NDSU
membership/eligibility question (validated; postseason ineligibility is irrelevant to
regular-season totals).

**League notes:** no preseason media poll (realignment) — preseason All-MW ingested as
color only (R1: honors ≠ tape); 8-game schedule validated after our fix; HQ move,
expansion pause, UNLV grant-of-rights — no model relevance.

**Camp re-sweep queue (MWC):** Nevada/SJSU/Wyoming/NIU QB resolutions; Hawai'i P;
W1–W3; Dickens eligibility confirmation.
