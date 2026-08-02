# Pre-registration — Study 18: FCS-influx as a market factor (+ cluster transfers) (2026-08-02)

Owner hunches: (1) attention to FCS→FBS movers is a real factor — consensus
anchors structurally miss it (FCS veterans carry zero returning production
and get no portal-pedigree credit) and the market may inherit the blindness;
(2) CLUSTER transfers — a unit imported together from one FCS program (the
Bailey Zappe / Houston Baptist→WKU archetype) — outperform an equal-graded
random mix (scheme/chemistry continuity).

**Peek disclosure:** S17 curve and B4 integration seen (they motivate the
metric; they claim nothing about consensus/market blindness — different
object). Miss panel = the S6–S13 reused panel, stated. No S18 statistic
computed. λ for the board leg is frozen from S18-A's point estimate
(sequential within-study, S13 convention, disclosed).

## Metrics (preseason-knowable; no look-ahead)

INTAKE: portal_{Y} entrants whose origin school classifies FCS (origin set
built from games files' fcs classifications, 2021–25). No survivorship —
rostered intent, not realized snaps.
- **N** = count of FCS intake for team-year (all intake).
- **Q (primary)** = Σ(curve_proj − 58) over TAPE-COVERED intake (≥4 FCS
  games year Y−1), curve = the S17 LEAVE-ORIGIN-YEAR-OUT fold fit (no
  in-sample leak). Sensitivity at replacement 55/61 reported.
- **CLUST** = size of the largest same-origin group in the team-year's FCS
  intake; clustered dummy = CLUST ≥ 2. QB+pass-catcher same-origin flavor
  reported as color (expect tiny n).

## Legs and bars

- **S18-A (panel integrity, make-or-break):** miss(final−pre SP+, 2022–25)
  ~ sp + rp + newHC + G5 + Q. PASS iff |t(Q)| ≥ 2, LOYO ≥3/4. Report
  G5×Q interaction (owner's G5 thesis) and N-variant.
- **S18-B (board / the market question):** rating′ = sp + λ_A·Q on SBD
  2022–24 (S13 conventions). PASS iff MAE improves AND |d|≥1 zone
  side-rate within 5pp of consensus-alone (strengthened if zone improves).
- **S18-C (report):** Q-vs-N horse race; position-mix gradient vs S17-L4.
- **S18-D (2026 freeze):** per-team Q/N/CLUST table frozen to
  data/research/s18_fcs2026.csv at registration+run; December scoring
  registered regardless of verdicts.
- **S18-E (cluster, panel):** A's regression + clustered dummy (and
  CLUST−1 count). Claim at |t| ≥ 2, LOYO ≥3/4.
- **S18-F (cluster, player level — the owner's phrasing exactly):** on the
  S17 1,035-pair panel, does having ≥1 same-origin companion (same FCS
  school → same FBS destination, same cycle) predict the realized FBS
  grade BEYOND the curve's expectation? resid_S17L1 ~ companion dummy.
  Claim at |t| ≥ 2 with LOYO ≥3/4; report companion-count dose curve.

## Decision rules

A+B PASS → **F5 factor candidate**: FCS-influx tie-breaker/sizing nudge in
the completion screen (Amendment-1 license shape), drafted for owner
sign-off; qualification bars untouched. E or F PASS → cluster flavor noted
inside F5 (or F5b if it passes where Q fails). All-null → hunch closed at
current power; December scores the frozen table anyway.

## Limitations

Panel reuse (S6–S13 lineage); Q tape coverage ~50–60% of intake (thin-tape
FCS adds invisible to Q, visible to N); rp collinearity may absorb the
effect (a legitimate outcome: exposure already carried by F3); origin-FCS
classification via games files misses FCS schools that never played FBS
that season (rare); staff-linkage (the Kittley half of the Zappe story)
unobservable in our data — same-origin player clustering is the proxy.
