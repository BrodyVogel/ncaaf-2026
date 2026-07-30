# Pre-registration — Study 12: coach track-record persistence (2026-07-31)

Owner-commissioned deep dig. **Peek disclosure:** the pooled effect is SEEN
(2026-07-31 diagnostic: miss ~ sp + coach prior-mean-miss, coef +0.164, t +2.82,
LOYO 4/4; horse race vs rp/newHC survived; ledger inspected). S12 therefore
registers bars ONLY on unseen questions. Panel = the S6/S8/S9 outcome panel
(2022–25 misses, n≈411 with ≥1 prior coach season 2021+) — heavily reused, stated.
Selection: first-time HCs excluded by construction; fired coaches exit the panel.
~10 registered looks below → expect ~0.5 false |t|≥2 by chance; claims are made
leg-by-leg at the stated bars, and the December fold is the arbiter.

Definitions: PM = mean of the coach's prior misses (final−preseason SP+, 2021+
window, any school, seasons before y). team_prior = the TEAM's year-(y−1) miss.
R_pre = S8b live-mirror mechanical-arm residual (merge on team-year).

## Registered legs and bars

- **S12-A — INTEGRITY (the make-or-break):** miss ~ sp + rp + newHC + **team_prior**
  + PM. PASS iff t(PM) ≥ 2 AND LOYO sign 4/4. team_prior is the dangerous control:
  for stayers PM ≈ team momentum; if PM dies here, the "coach" framing is just
  ascending-program drift we could capture without coach identity. Robustness
  (report): + thin-tape, luck, G5; and + R_pre (registered question: is PM
  independent of the mechanical arm? both-survive = independent).
- **S12-B — SHAPE:** (i) asymmetry: PM⁺=max(PM,0), PM⁻=min(PM,0) separately —
  claim "overperformers persist" / "underperformers persist" per side at t ≥ 2;
  (ii) tails: PM×|PM| interaction — claim "tail-concentrated" iff t ≥ 2 and the
  implied slope at |PM|=10 ≥ 2× the slope at |PM|=3.
- **S12-C — ONSET (owner Q5):** slice coefficients by history depth: n_prior=1;
  n_prior=2 same-signed; n_prior=2 mixed; n_prior≥3. Claim "one year is signal"
  iff the n=1 slice alone has t ≥ 2. Claim "consistency matters" iff same-signed-2+
  beats mixed with the difference at t ≥ 2. Otherwise: report, no claim.
- **S12-D — NUANCE (owner Q3):** (i) switcher survival: new-to-team with ported
  history (seen partially: +0.24, t 0.96, n=27) — extend with 2021-era moves where
  data allows; claim only at t ≥ 2, expect underpowered → honest "insufficient n"
  is the likely verdict; (ii) class interaction PM×G5(current team); (iii) move
  direction (stepped down P4→G5 vs up) — report-only, n will be tiny.
- **S12-E — WIN-TOTAL IMPACT (owner Q4):** translate: rating' = sp + 0.164·PM
  (coefficient FROZEN from the seen pooled fit; no refit on boards). On SBD DK
  openers 2022–24 (n≈219): (i) MAE vs actual regular-season wins must IMPROVE vs
  consensus-alone; (ii) the |d|≥1.0 zone side-rate must stay within 5pp of
  consensus-alone's (non-dilution). PASS = both. Also report: per-team wins shift
  at PM = ±5/±10 via schedule sensitivity, and the shift for every held position.
- **S12-F — FORWARD FOLD (frozen today, scored in December):** the 2026 PM table
  is committed alongside this registration (data/research/s12_pm2026.csv; rule:
  continuing coaches = 2025 mapping; 2026 new hires included ONLY where identity
  is documented in-repo, else PM null and the team is excluded). December scoring:
  2026 miss ~ sp + PM on that frozen table; PASS = t ≥ 2, sign +.

## Decision rules (registered)

S12-A PASS + S12-E PASS → coach-prior becomes a registered 2027 build candidate
(additive term 0.164·PM, capped ±3 pts, entering at the consensus-lens stage) and
remains a 2026 SIZING/tie-breaker overlay only — the frozen 2026 board does not
change. S12-A FAIL → the overlay is withdrawn from weekend use and the ledger is
demoted to color. S12-E FAIL (zone dilution) → factor confined to team-total
sizing, never to side selection. S12-F in December is confirmatory either way.

## Limitations (registered)

Five seasons of vintages; PM windows 1–4 years; coach ≈ program confound only
partially separable (S12-A's team_prior control + S12-D switchers are the
instruments, both power-limited); 2021 preseason ratings carry COVID-2020 inputs;
SBD boards P4-heavy for S12-E; the pooled coefficient reused in E/F was fit
in-sample (disclosed; frozen to avoid board-fitting).
