# Audit round 1 — 2026-07-14 (pre-pilot, full-system review against the betting goal)

Verdict: architecture sound; parameters evidence-sourced; no fatal flaws found.
Findings ranked below. New tests run for this audit: new-QB multiplier (closed, flat).

## A. Real recommendations (additive QA, build into compute phase)

1. SHADOW MECHANICAL GRADE on every build sheet. The single largest unvalidated leap in
   the system is the k-transfer assumption: gamma was measured on PFF-proxy grades, and
   we apply it to LLM grades whose noise profile is unknown. Un-testable directly
   (cannot re-LLM-grade history). Mitigation: compute the 2026 PFF-returning proxy unit
   grades (mechanical, deterministic) alongside the LLM grades for every team; print
   both on the build sheet. Expected correlation ~0.7-0.85; large per-unit divergences
   = review flags; systematic divergence = k re-examination trigger.

2. ANCHORING TRIPWIRE on the league-wide fit. The grader (the assistant) has seen the
   2026 SP+ table in-session (verified it row-by-row) - memory contamination is real
   and non-erasable. Blinding v2's defenses (evidence citations, bracketing exemplars)
   are process-level; add a measurement: the SS3 cross-sectional fit R2 from proxy
   grades runs 0.46-0.68. If the LLM grades fit the anchor at R2 >~0.75, that is
   evidence of consensus-parroting, not independent grading -> warning + review before
   the blend is trusted.

3. TEST-RETEST RE-GRADES at scale. The founding complaint was ~6-pt run-to-run grade
   swings. Fixed template/exemplars/integer-grades address it by design, but nothing
   MEASURES it. After scale-out: re-grade a random ~5% of units (fresh call, same
   frozen snapshot), report |delta| distribution. Typical |delta| > ~8 percentile pts
   -> tighten template before finalizing.

## B. Item closed by this audit

4. NEW-QB VARIANCE MULTIPLIER (brief SS3 candidate, dropped without test): now tested
   on real misses 2022-2025. Teams with no returning 100-dropback QB (n=165): miss SD
   7.99 vs 7.90 (ratio 1.01, bootstrap 90% CI [0.90, 1.12]) - decisively flat; anchors
   already price QB uncertainty. Drop is now evidence-based. (Side note: new-QB teams'
   mean miss +0.98, t~1.6 - weakly suggestive the market over-fears new QBs; not
   actionable at this significance; logged for post-2026 retest.)

## C. Honest structural risks (accepted, monitored - no engineering fix exists)

5. k-transfer (see #1) - mitigated, not eliminated.
6. Band decomposition: sigma=6.0 rests on an ASSUMED in-season noise (~4.5) and treats
   final SP+ as truth (which has its own error). Downstream check at pilot: feed the
   band through the user's sim and compare win-total spread vs market spreads - wins-
   space calibration is the real test of 6.0.
7. Class term (+-1.68) is a portal-era estimate (4 of 5 years); if NIL/rev-share
   concentration reverses the G5 edge, it goes stale. Small magnitude; monitor yearly.
8. Winsorize guard uses median of ~4 other sources - noisy at this n; acceptable as a
   data-error guard, not a precision instrument.

## D. Registered disagreements (mild, on record per user request)

9. SP+ 2x / KFord 2x weights are user preference, not evidence (no accuracy basis for
   any weighting; sources correlate 0.95+ so impact is small). Harmless; noted.
10. Dispersion band multiplier x1.10 is uncalibrated judgment - correctly labeled as
    such in PARAMETERS; keep small until history allows calibration.

## E. Checked and clean (no findings forced)

- Backtest/calibration leakage: LOYO offsets guard the adjustment; SP+ files verified
  preseason-vintage; miss panels use only preseason-known features. Clean.
- Name-map joins: 138/138 validated; PFF alias table hand-verified; no ad-hoc matching.
- Parameters: every number in PARAMETERS.json traces to a committed script + run.
- Blinding tooling: lint tested in both directions (legal citations pass, violations flag).
- Repo durability/secrets hygiene: clean (secrets gitignored, never printed).
- Anchor captures: SP+ human-verified; Pick Six 68/68 parsed; dispersion policy set.
