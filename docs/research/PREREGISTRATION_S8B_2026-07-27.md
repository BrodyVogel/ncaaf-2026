# Pre-registration — Study 8b: live-mirror shadow-arm backtest (2026-07-27)

Committed BEFORE any S8b outcome regression. Spec is verbatim from the owner-reviewed
S8B_LIVE_MIRROR_AUDIT_2026-07-27.md (owner OK 2026-07-27). Honesty disclosure up
front: S8 outcomes on this panel have been seen (primary failed). S8b is a
post-hoc-motivated re-test whose construction was fixed by the live-mirror audit
BEFORE any re-look at outcomes. Whatever S8b shows, it is one test on a seen panel:
a PASS is labeled "post-hoc-motivated; 2026 live season is the confirmatory fold,"
never "pre-registered discovery."

## Regressor chain (per season y ∈ {2022..2025}, fixed)

1. Shadow unit VALUES (not percentiles): S8 engine (Mode B rosters, v2 constants,
   slot weights) with two corrections: per-team independent classing and offsets.
   Independent seasons classed: Notre Dame → P4 (all years), BYU 2021–22 → P4;
   Army ≤2023, Liberty ≤2022, New Mexico State ≤2022, UConn (all), UMass ≤2024 → G5.
   Applies to BOTH the jump term (player p4_from/p4_to) and the destination offset:
   ND → ACC offsets, BYU'21–22 → B12 offsets, G5-independents → per-unit mean of
   {AAC, CUSA, MAC, MWC, SBC} offsets.
2. Within-year conversion, mirroring final_pass exactly: OLS with intercept,
   off units {QB,RB,WRTE,OL} → preseason SP+ OFF split; def units {DL,LB,DB} →
   preseason SP+ DEF split (lower = better). Fit on non-debut FBS teams with
   complete data. match_spread un-shrink of each fitted side to the target side's SD.
3. resid = (impl_off − sp_off) − (impl_def − sp_def).
4. Conference demeaning within season: pools = conference of record; pseudo-pools
   P4-mean / G5-mean for independents per the classing above; 2024–25 Pac-12 (2 teams)
   pooled with MWC; FBS-debut seasons excluded from all pools.
5. Level-strip (decompress step 2): within-year OLS of resid on preseason SP+
   overall; keep the residual. Done BEFORE any clip.
6. **R_pre = resid after 4–5** (PRIMARY regressor — full variance).
   **R_adj = clip(0.35·R_pre, ±6) + ST term** (COMPANION — the applied-adjustment
   object). ST term = (pct−50)/50 where pct = y−1 PFF team SPEC percentile;
   unmapped teams → 0.
7. Panel: all FBS with SP+ preseason+final and a shadow build, MINUS FBS-debut
   seasons (2022 James Madison; 2023 Jacksonville State, Sam Houston; 2024 Kennesaw
   State; 2025 Delaware, Missouri State) — mirrors the live manual-override policy.
   Outcome: miss = final SP+ − preseason SP+. Covariate: preseason SP+ overall.

## Bars (fixed now)

- **Primary: miss ~ a + b·sp_pre + c·R_pre, pooled.** PASS iff **t(c) ≥ 2 AND
  LOYO sign-stable 4/4**. Materiality is c itself (pts realized per pt of live-style
  residual): **λ\* = clip(c, 0, 1) if PASS else 0.** No ΔR² bar (uninterpretable for
  a demeaned, level-stripped, bounded-family regressor; pre-stated in the audit).
- **Secondary (registered): G5-only slice**, same regression, same bars, own λ\*_G5.
- **Companion (measurement, no bar): β on R_adj with 95% CI** — the product-scale
  realization rate of the adjustment actually applied.
- **Report-only:** P4 slice; |R_pre| terciles; new-HC vs retained; per-year c's;
  2023 forensics (what flipped that year's sign in S8); influence/jackknife.
- NOT re-run: S8's L2a/L2b/L3 verdicts stand as issued (L2b never used D or the
  display weights; L2a/L3 carry S8's construction caveat in their findings text).

## Interpretation matrix (registered)

- Primary PASS → mechanical core movement-validated at measured λ\* (post-hoc-
  motivated label; 2026 live season = confirmatory fold). 2027 formula arm enters
  ratings at λ\* via the live chain (conversion→demean→strip→K·clip), owner approval
  required as always.
- Primary FAIL with G5 secondary PASS → arm validated for G5 only; 2027 arm is
  G5-scoped at λ\*_G5; P4 formula arm stays λ\*=0 (dossier-only).
- Both FAIL → the mechanical core's live-style adjustments do not detectably realize
  in consensus drift even under the faithful construction; formula arm stays λ\*=0
  for 2027; the 2026 dossier+arm live season becomes the sole forward test.
- Power caveat (pre-stated): SE(c) ≈ 0.10 expected on R_pre. If 0 < c < 0.2 with
  t < 2, the honest reading is "small positive, underpowered," not "refuted."

## Limitations (registered)

Single-system anchor proxy (SP+ splits, not the 6-system blend); formula-only unit
inputs (dossier unmirrorable); auto rosters (membership fidelity 0.958/0.972 from
Phase 1); pooled v2 constants (fold-stable); season-vintage rosters (small residual
channel); SP+ off/def splits are the same object family the conversion targets live,
but SP+'s own preseason projection already encodes returning production — c measures
value ADDED over that projection, the intended (hard) question.
