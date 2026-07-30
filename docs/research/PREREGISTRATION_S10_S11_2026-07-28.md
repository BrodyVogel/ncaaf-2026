# Pre-registration — S10 (jump-term refinements) + S11 (dispersion-tilt persistence)
(2026-07-28, owner-authorized; committed before any fitting)

## S10 — jump term: position buckets and graded distance

Panel: data/research/pairs.csv, S1 VOLMIN filter, LOYO over transitions 2021→22 …
2024→25 (4 folds), movers-only evaluation — identical to Study 1's harness; the
pooled-jump S1 model is the incumbent baseline.

- **S10-A (position-bucket jump):** replace the 3 jump dummies with bucket×jump
  dummies, buckets QB / TRENCH (OL,DL) / OTHER (RB,WRTE,LB,DB). PASS iff (i) LOYO
  mover MAE improves ≥ 0.5% vs the pooled model, (ii) full-sample F-test for the
  split p < 0.05, and (iii) cross-class bucket coefficients are LOYO sign-stable.
  Ship rule: 2027 uses bucket constants only on PASS; else pooled stands.
- **S10-B (graded jump):** replace the two cross-class dummies with continuous
  up_gap = max(0, off_dest − off_orig) and down_gap = max(0, off_orig − off_dest),
  per-unit offsets (this also covers within-class moves — the owner's AAC≠MAC
  point). PASS iff LOYO mover MAE improves ≥ 0.5% vs binary AND both coefficients
  sign-stable 4/4 (expected: up negative, down positive).
- Report-only: effect sizes, bucket×graded combination, n per cell.

## S11 — dispersion tilt s*: is >1 persistent, or a 2025/26 artifact?

For y ∈ {2021..2024}: ratings = preseason SP+ vintage; stretch s applied as
r_s = mean + s·(sp − mean); expected wins via the probit engine (σ=13.5, HFA 2.3,
FCS=0.95, regular-season schedules). s*_y solves slope(EW_s − line ~ line) = 0
(the production criterion), bisection on [0.7, 1.7]; min-MSE s reported as
robustness. Lines: SBD DK openers (69–80 teams/yr). 2025 (owner near-closer
capture, median across books) reported alongside, vintage-flagged, excluded from
the bar. **Persistence bar: s*_y > 1.00 in ≥ 3 of 4 SBD years AND mean s* ≥ 1.05.**
Disclosures: production s* (1.1545) is fit on OUR calibrated ratings vs a
multi-book 2026 board; this test proxies with SP+ vs one book's openers — same
criterion, different rating set and vintage. K3 (settlement side) is independent
evidence and stands regardless.

## Also authorized, run alongside (descriptive, no bars)

dg cell-mean table: mean(formula v2 percentile − dossier grade) by conference-group ×
unit on the 2026 field (proforma_v2_2026.csv), n and SD per cell — the dossier-bias
screening table. Interpretation guardrail: uniform cell gaps are annihilated by the
rating-layer conference demeaning; the table hunts for outlier cells and
within-cell spread, not levels. Class-split k: DECLINED for now (owner's lowest
priority; S4-family evidence predicts null) — stays on the 2027 registry.
