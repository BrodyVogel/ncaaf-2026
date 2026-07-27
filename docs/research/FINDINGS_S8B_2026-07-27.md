# Study 8b findings — live-mirror re-test: PRIMARY FAILS BY 0.004, registered "underpowered small-positive" clause applies (2026-07-27)

Prereg: PREREGISTRATION_S8B_2026-07-27.md (bars fixed before any outcome regression;
post-hoc motivation disclosed there). Runner: pipeline/research/s8b_run.py; panel
data/research/s8b_panel.csv (n=516; debut seasons excluded per live override policy).
Chain verified against final_pass.py component-by-component (S8B audit doc).

## Primary — miss ~ sp_pre + R_pre: **FAIL** (t 1.94 vs bar 2.00)

**c = +0.120 pts drift per pt of live-style residual (t +1.94)**; LOYO signs 4/4
positive (PASS). Needed c ≥ 0.124 at this SE (0.062) to clear — missed by 0.004.
**λ\* = 0 per bars.** The registered power caveat applies VERBATIM: "if 0 < c < 0.2
with t < 2, the honest reading is 'small positive, underpowered,' not 'refuted.'"

## Secondary (G5, registered) — **FAIL**: c=+0.193, t=+1.54, LOYO 4/4

## Companion (measurement, no bar)

β on the applied-adjustment object (K·clip + ST): **+0.355, t +2.01, CI [+0.01, +0.70]**.
Same information as the primary at product scale (0.120/0.35 = 0.343 ≈ 0.355; the
clip/ST wiggle adds the rest) — NOT an independent significant finding, and it holds
no bar. Reading: point estimate says ~a third of every applied adjustment point
realizes in SP+ drift.

## Construction verdict on S8 (owner's smell test)

Direction confirmed. Live-faithful construction moved measured realization from
S8's 0.081 to 0.120/pt on the raw residual — and the product-scale realization to
~0.36 — i.e., S8's crude standalone score understated the arm by roughly 3× on the
number that matters. The fail margin went from clear (t 1.93 with ΔR² 0.006 against
0.02) to four-thousandths of a coefficient under honest bars.

## Slice reversal (report-only) — S8's G5 story was substantially artifact

P4: c=+0.268, **t=+2.67** (report-only). G5: +0.193, t 1.54. This REVERSES S8's
G5-strong/P4-weak pattern. Explanation: S8's D carried cross-conference level, which
the live rig's demeaning policy strips; once stripped, the within-pool signal sits in
P4. The 2027 registry's "G5-only primary" (inherited from S8-L6) is withdrawn and
replaced: pooled primary + P4 slice, both bar-fixed, on the 5-fold panel.

## Stability and fragility (report-only)

Per-year c: 2022 +0.258 (t 2.1), 2023 −0.088, 2024 +0.248 (t 2.1), 2025 +0.048.
2023 forensics: mega-portal year; big residuals split both ways (Kansas +12.3→+8.0,
Northwestern +10.8→+5.1 right; SMU −13.3→+4.1, Arkansas +12.5→−8.6, Vanderbilt
+11.5→−7.2 wrong). Jackknife: dropping the top-5 |R_pre| (Indiana'24, Vandy'24/'25,
Colorado'24, SMU'23) cuts c to +0.066 (t 1.04) — the effect leans on large residuals
(consistent with the large-|R| tercile carrying the signal: c +0.159, t +2.36).

## Decision (per registered matrix)

Both bars failed → **formula arm ships at λ\* = 0 for 2027**; the book is unchanged
(no leg of S8/S8b forces sizing action); the dossier layer's status is unchanged.
The effect is reclassified "small positive, underpowered" — not refuted, not shippable.

## The decisive next test (queued for owner)

Two things resolve this without any construction debate: (1) a fifth fold — if
c ≈ 0.12 holds, 2026's ~130 teams take expected t past 2; (2) **score the ACTUAL 2026
live arm**: the curated adjustments are frozen in the shipped board now; in December,
regress realized 2026 SP+ drift on them. That is the true out-of-sample test of the
rig as it actually bets — pre-registrable today with zero look-ahead risk (S8c).
