# Full-stack audit — season win-total system (2026-08-02)

Owner-commissioned deep audit: assumptions AND construction, every layer. Run
as six parallel audit lanes (grading formula, adjudication data, anchor +
final_pass, win engine + bet math, repo hygiene, design assumptions), each
with independent recomputation; every action-driving finding re-verified by
hand afterward (code lines + numeric claims). Repo @ 0e96604 at audit start.

**Headline: the money path is internally consistent and reproducible** — the
board rebuilds from raw inputs to ≤0.005 on all 138 teams; the win engine's
correlation structure is exactly right (Gauss-Hermite shared-shock verified
against a 2M-season Monte Carlo to 4 decimals; Python/JS parity 1e-15); the
adjudication log replays 1,097/1,097 keys to the shipped grades; blends,
bands, camp rows, schedules, neutral sites, and FCS joins all verify. The
defects found are real but live at the edges: two were FIXED in this commit,
five need owner decisions, and the deepest findings are about how much of the
board's claimed edge rests on which evidence.

## Fixed in this commit (safe, provenance-clear)

- **F-1 Under-price inference produced invalid odds** for posted overs in
  (−129, −101): the naive mirror gave e.g. −105 → "+75", odds that don't
  exist (nothing between ±100). 187 of 785 posted offers (24%) sat in the
  broken zone; the correct crossing existed only in weekend_scan. Fixed in
  all three sites (win_engine.py, win_engine.js, bet_tracker.ufo); chain
  rebuilt. Effect: 12 of 24 tracked bets moved ≤0.6pp (overs down, unders
  up — the old bug flattered overs): UConn +20.0→+19.4, Tulsa +17.9→+17.4,
  Hawai'i +10.4→+10.7, Florida +7.0→+7.3. Zero qualification flips;
  market_stretch 1.1519→1.1516.
- **F-2 v1_grade lineage clobber guard** (regen_grades_v2.py setdefault):
  re-running regen after future adjudication rounds would have silently
  destroyed v1 lineage. Zero current-data change (all 360 v1_grades verified
  intact first).
- Hygiene: staleness register re-run (was 07-19, 83 stale finals), tracker
  ASOF, price_openers pointed at the committed lines probe.

## Owner decisions needed (board-affecting or convention choices)

- **D-1 Conference tilt from strip ordering (verified).** The level-strip
  runs AFTER conference demeaning and is fit on anchor level, re-inserting
  conference means the demeaning removed: post-strip residual × K averages
  CUSA −0.50 / MAC −0.49 / MW −0.31 vs B1G +0.44 / SEC +0.56 — a ~1.06-pt
  P4-vs-G5 tilt on a board whose class term was explicitly zeroed (+0.15,
  t 0.3). REFIT_DIAG's "≈0 by construction" claim is false. Fix = one joint
  projection (conference dummies + anchor level in a single OLS). Moves
  conference blocks ±0.3–0.5 pts; G5 overs (most of the book) would gain.
- **D-2 Junk-grade override teams still vote in the fits.** The 5 manual-
  override teams are excluded from demeaning pools but still enter the OLS
  conversion, un-shrink SDs, strip fit, and recenter mean — the exact
  contamination the 07-23 fix closed for pools. Field mean dragged −0.31;
  relative distortions ±0.3 (BYU −0.60, Tulsa −0.59, ECU −0.57 vs a clean
  fit). Fix = exclude the 5 from all four fits.
- **D-3 ST term is an undemeaned conference channel.** Conference ST means
  span 16 (MW) to 54 (SEC) — level judgment flowing through the one channel
  that bypasses both strips (P4−G5 +0.29 pts). Options: demean ST like
  everything else, or accept and document.
- **D-4 FCS lens convention split.** Tracker prices FCS opponents ×0.75;
  HTML uses raw; weekend_scan scaled BOTH lenses. The 0.75 constant was
  validated under the RAW convention (backtest harness), so the tracker is
  the deviant — but RIG_MANUAL documents the tracker's behavior. Unifying on
  raw (provenance-correct) raises tracked over probabilities: Nevada O4.5
  .610→.625, Buffalo O5.5 .656→.684, BGSU .703→.716, OSU .722→.736, UConn
  .679→.685. Recommend: unify on raw everywhere + fix the manual.
- **D-5 Restore 46 overwritten confidence letters.** Mechanically-filled
  conf columns on re-read/reconciliation rows silently flipped 38 L→M and
  8 H→M (regen applies row conf unconditionally on grade-changing rows —
  guard only covers no-change rows). 32 teams' bands are 3–6pp narrower
  than the dossier record supports (incl. Nevada, Oregon State, Wake
  Forest). Fix = restore letters from the pre-overwrite record + patch the
  regen guard to regex-only conf application. Widens those distributions
  slightly (longer tails).

## Registered/structural findings (no immediate action; scheduled homes)

- **S-1 Slot-weight schema bug in the mechanical sweep arm (verified
  premise).** Two roster schemas (80 'depth' teams / 58 'slot' teams);
  `r.get('slot','1')` defaults every depth-schema row to weight 1.0
  (backups at starter weight), while slot-schema teams give 1.0 to only ONE
  player (other starters 0.33). Neither matches intent; the dual-aggregation
  reconciliation was a silent no-op for the 80 depth teams. Counterfactual:
  ~105–164 units' mechanical dg would shift ≥2 pts. MITIGATION: every
  triggered unit got a human case read, and the damping chain (percentile →
  OLS → K → clip) shrinks residual impact; the shipped grades are
  adjudicated, not mechanical. DISPOSITION: fix belongs in the 2027 formula
  rebuild (with S16's continuous jumps); a 2026 hot-fix would re-open the
  whole adjudication vintage for sub-0.1-win team effects.
- **S-2 Spine classes FBS Independents as P4** → UConn/UMass-origin players
  carried wrong jump terms (24 current players; Colorado State's 13-player
  UConn bloc +1.45 each). Same home: 2027 formula rebuild; the affected
  units passed adjudication.
- **S-3 Three false-identity name matches** (Kent State RB inherits a
  Hawaii RB's 341-carry tape; 2 trivial). Add identity guard (team/class
  check) to the matcher at next regen; no shipped flip found.
- **S-4 WRTE and LB slopes are statistically zero** in the conversion
  (t +0.49 / −0.47) — those unit grades are nearly inert in ratings (98
  grade pts ≈ 0.9 final pts). Known-ish (S8's LB/RB persistence notes);
  now quantified. 2027: consider pooling or informative priors.
- **S-5 grades_check red field-wide** (502 errors, 125 teams): verified
  PURE metadata desync — 360 grades_detail entries + 142 planned-line
  declarations all equal v1_grade exactly; ZERO real drift. The per-team
  gate is dead until resynced. One-time resync spec'd in lane report;
  scheduled as next hygiene block.
- **S-6 Integer-line push handling** treats P(W=L) as full loss for overs
  (all current lines are X.5 — latent). Fix with a push-aware EV at next
  engine touch.
- **S-7 Sacramento State** (FBS newcomer) lacks the NDSU-style reclass
  guard; band already elevated. Add flag at next payload build.
- **S-8 price_game.py "calibrated" label** uses shrink-toward-anchor, not
  the board lens. Relabel at next touch.
- **S-9 portfolio_enumerate.py** still contains both pre-fix devig bugs —
  stale tool, retire or backport (portfolio work now lives elsewhere).

## The assumption verdicts (design lane, verified where checkable)

- **A-1 The book vs its evidence base (the deepest finding).** The betting
  number is 98.6% consensus by variance; the validated S7 mechanism (77–79%)
  lives only at ≥1.0-win consensus-vs-market gaps — and ~1 of 21 held
  positions sits in that zone (consistent with S15's finding that the zone
  is ~9 bets/season field-wide). ~40% of model EV rides on the roster arm
  (S8b: suggestive, λ*=0) and the compression/macro factor (K3/stretch:
  validated as a class). The cal lens prices residuals at 0.2625
  pass-through vs S8b's measured ~0.12 average realization (≈2.2×
  generous), though about right in the top-|R| decile. Claimed per-leg
  edges (+7–20%) are therefore evidence-implied high by ~3–5× ON AVERAGE.
  This does NOT say the book is wrong — it says its EV is carried by the
  factor evidence (F1/F2/F3 sleeves, sized small) rather than by the
  displayed per-leg numbers, which is exactly how the owner already treats
  it. ACTION: December S8c is the arbiter; evidence-class tags on future
  legs; treat displayed EV as a rank, not a magnitude.
- **A-2 σ=13.5 is really ~15.3** (margin-vs-close SD, n=3,730, flat across
  spread sizes — heteroskedasticity refuted) but the COMPOSITION
  compensates: bands + shared shock + 0.75 shrink reproduce correct total
  dispersion and calibrated coverage (80.8%). A compensating-errors
  equilibrium: safe until someone tunes one layer alone. Big-favorite tails
  are fat (4.6% upsets vs 2.2% modeled) — matters for G5 near-lock slates.
  ACTION: registered joint re-derivation (σ, band scale, shrink together)
  before ANY solo retune; fat-tail patch as part of it. 2027.
- **A-3 s* is ~57% self-generated.** Market-vs-consensus stretch is only
  ~1.065; our own adjustments (corr −0.448 with lines, verified) manufacture
  the rest of 1.152. The "market over-disperses 15%" narrative overstates
  the market-vs-consensus tilt ~2×; the F2 premise survives (K3 settlement
  evidence stands) but the mm lens quietly re-shrinks the line-correlated
  part of our arm. ACTION: log s*_anchor alongside s* each build (one
  line); interpret F2 sizing off K3 evidence, not off s* magnitude.
- **A-4 HFA flat 2.3 is fine for the field** (home-vs-close +0.06) but
  Hawai'i U7.5 loses ~3.2pp of edge under realistic venue/travel premiums
  (the effect points AGAINST the held side); UConn −1.9, KSU −1.2 (KSU
  pinned anyway). ACTION: 6-venue HFA table (Hawai'i, Laramie, AFA, UNM,
  CSU + travel legs) — bounded lookup, no study needed; Hawai'i conviction
  gets a manual haircut meanwhile.
- **A-5 Portfolio correlation is a non-issue** (verified MC: variance ratio
  1.30, driven by same-team duplicates the team cap already governs;
  dispersion shocks net ~zero settlement exposure). The one undiversifiable
  factor is shared arm error: arm-zero stress = book EV −40%. ACTION:
  standing arm-stress column in the tracker.
- **A-6 ×0.75 static is selection-safe** (no position crosses any bar
  across 0.70–0.85) but stale-anchor risk is real: the rig's max response
  to a camp catastrophe is ~25% of true impact (anchor frozen 07-14).
  The ≤7-day-news exclusion + delta-card doctrine are the mitigations.
- **A-7 Conference demeaning VALIDATED with new evidence:** raw conference-
  level residuals are ANTI-signal (slope −0.57, t −3.68 predicting drift);
  demeaning protects against exactly that. A small orthogonal conference
  component (+1.18, t +2.26) is real and discarded — 2027 candidate.
- **A-8 Good news:** QB formula input is grades_offense (INCLUDES rushing)
  — the "passing-facet-only dual-threat blind spot" in the docs is wrong;
  the real gap is volume=dropbacks only (milder). Docs corrected reading;
  2027 rushing-value term should NOT double-count.

## Hygiene actions (from lane 5's checklist, sequenced)

Done now: staleness re-run, ASOF, price_openers path. Next block: grades
gate resync (S-5); frozen-comparison set regenerate-or-expire; delete
orphaned win_totals_calibration.json; archive portfolio v1–v4; doc updates
(market_stretch → pointer, WIN_ENGINE_METHOD banner + NDSU passage, row
counts, parity claim). Longer-term: git-lfs the ~358MB of magazine PDFs;
stop re-committing rebuilt HTML/payload every build.

## Lane reports

Full lane outputs (with all recomputations) are preserved in the session
transcript; this doc is the verified synthesis. Findings were accepted only
after (a) the lane showed its arithmetic and (b) spot re-verification of
code lines and key numbers (slot-weight line, regen conf guard, FCS lens
sites, under-inference arithmetic, spine IND class, QB grade column,
conference tilt table, adj-vs-line correlation) reproduced exactly.
