# The four rating sets in the win-totals engine — definitions, intuition, justification

*(2026-07-22. Code: `anchor_loader.py`, `final_pass.py`, `win_totals_compute.py`,
`build_win_totals_artifact.py` `ratingFn()`. Every formula below is transcribed from
source, not memory.)*

## 0. The common object

Every set expresses the same thing: a **neutral-field point margin vs an average FBS
team**. Ohio State ≈ +32 means "favored by ~32 over a dead-average team on a neutral
field." One engine consumes all four sets identically:

```
expected_margin = μ_S − μ_O + 2.3·site            site ∈ {+1 home, −1 away, 0 neutral}
P(S wins)       = Φ( (μ_S + δ − μ_O + 2.3·site) / σ_eff )
σ_eff           = sqrt( 13.5² + band_O² )          per-game noise + opponent uncertainty
δ ~ N(0, band_S²)                                  OUR uncertainty about S — one draw
                                                   shared across the whole season
wins ~ Poisson-Binomial({p_g(δ)}), δ integrated out by 21-node Gauss-Hermite (exact)
```

The shared shock δ is the engine's most consequential choice: if we're 2 points wrong
about a team, we're wrong in *every* game, which fattens the season-win tails exactly the
way real seasons do. So the sets differ **only in which μ they feed the engine**.

---

## 1. Consensus (anchor) — "what the analytics world believes"

**Formula** (`anchor_loader.py`): a weighted blend of six public systems, z-normalized
onto SP+'s scale — SP+ (weight 2), FEI, Massey, FPI, TeamRankings, Pick Six (1 each).
Any source more than 5 points from the median of the others is winsorized to that
boundary (63 team-sources were). The offense/defense split borrows SP+'s shape.

```
anchor_T = Σ_i w_i · z_i(T) / Σ_i w_i     (z = source normalized to SP+ scale, winsorized)
```

**Intuition.** A robust average of every serious public measurement of team strength.
No opinion of ours is in it.

**Justification.** Single systems have house quirks; a weighted, winsorized blend keeps
the shared signal and clips the quirks. Its spread (SD ≈ 13) matches what true team
strength actually spreads to (SP+/KFord finals 2021–25: SD 12.3–13.7) — evidence the
scale is "fair." Role in the product: the stabilizer our grades are blended against, and
a sanity column ("edge (consensus)") showing whether a bet needs our private opinion or
is visible even to public numbers.

---

## 2. Power (ours) — "consensus + bounded roster-scouting disagreement"

**Formula** (`final_pass.py`, frozen constants):

```
1. implied_off = OLS(QB, RB, WRTE, OL → anchor offenses)      R² ≈ 0.67
   implied_def = OLS(DL, LB, DB → anchor defenses)             R² ≈ 0.49
2. un-shrink: rescale each implied side to the anchor's spread (OLS fits are
   compressed toward the mean by ~√R²; this restores a fair SD)
3. resid = (implied_off − anchor_off) − (implied_def − anchor_def)
   a. conference-demeaned (each league's mean residual removed — owner policy:
      no cross-conference level claims without direct evidence)
   b. level-orthogonalized (the component linear in team strength removed —
      that component was measured to be grade compression, not signal)
4. adj  = clip( 0.35 · resid, ±6 )
5. ours = anchor_blend + adj + (ST−50)/50 + recenter-to-mean-0
6. a handful of manual overrides for grade-unreliable reclass teams (e.g. NDSU),
   logged in data/manual_overrides_2026.csv
```

**Intuition.** Start from the consensus, then let our anchor-blind unit grades move a team
by at most ±6 points, at 35% weight, and only on the component of disagreement that is
*within-conference roster shape* — the thing our film/roster work can actually know.

**Justification.** The grades were built blind to the anchors, so the residual is genuine
independent information; validation showed the within-conference shape signal is real
(Spearman ~0.94 in the diagnostic) while the level and cross-conference components were
noise or double-counting, so they're stripped. K=0.35/±6 encodes "our scouting gets a
vote, not a veto." The result spreads at SD 13.2 — the fair, true-strength scale.
**This is the set the UI calls "Power (ours)"; it drives the editable team pages and
best-bet EV/$1.**

---

## 3. Market-matched (×1.1475) — "our opinions wearing the market's dispersion"

**Formula** (`win_totals_compute.compute_market_stretch`):

```
mm_T = field_mean + s* · (ours_T − field_mean)        s* = 1.1475 (refit each build)
```

s\* is fitted so that the win-total edge-vs-line slope is **exactly zero**: the unique
stretch at which our edges stop correlating with how good the market thinks a team is.

**Intuition.** The market prices totals as if team strength spread ~15% wider than our
scale. This set adopts that spread while keeping our team *ordering* — our opinions
re-expressed in the market's own accent.

**Justification.** Against the raw board, most totals show the same systematic tilt
(fade high totals, back low totals) — one macro disagreement expressed 130 times. By
construction, that tilt is zero on this set, so **any edge that survives here is
team-specific**: a disagreement about *that roster*, not about dispersion. This is the
"idiosyncratic edge" screen used for portfolio building. It is *not* a probability lens —
we don't believe the market's spread — it's an isolation device.

---

## 4. Calibrated (×0.75) — "the honest probability lens"

**Formula**:

```
cal_T = field_mean + 0.75 · (ours_T − field_mean)
```

**Intuition.** A July rating is an *estimate* of a quantity that (a) mean-reverts by
season's end and (b) carries estimation error. Before an estimate becomes a probability
it must be shrunk toward the mean. December ratings need no shrink; July ratings do.

**Justification — the most-tested number in the project.** Game-level: probit fit of
preseason ratings on 2021–25 games gives slope **0.624** (a preseason "93% favorite" wins
81.5%), while *final* ratings give slope 0.983 ≈ 1 — the machinery is right; July
information is the problem. Season-level: running the full engine over 663 team-seasons,
the raw set is overconfident (dispersion ratio 1.18; 65% claims hit 60%) while ×0.75 is
near-textbook (central-80% coverage 80.8%, tail buckets within 0.3 pts). The 0.75 (not
0.62) is because the band terms already absorb part of the uncertainty. **All bet
probabilities, EVs, sizing, and the tracker's Model P use this set.** Note what it is
NOT: it does not "remove our biases vs the market" — being furthest from the market's
spread, it expresses the dispersion disagreement *most*.

---

## 5. The band (per-team uncertainty, ± points)

```
band_T = 6.0 · [×1.13 if new HC] · [×1.10 if anchor-sources disagree top-decile]
             · [1 + 0.03·min(#low-confidence units, 5)]
```

Feeds the engine twice: as opponent noise (σ_eff) and as the subject's shared shock (δ).
Justification: coach changes and source disagreement are the two measurable flags of
"this rating could be well off," and unit-grade confidence adds roster-level uncertainty.
This is why confidence flips in grading (L→M) are sim-affecting even when the grade
barely moves.

---

## 6. How the board combines them

Each total shows four edges (our P(side) minus the de-vigged market probability, computed
under each set). The reading:

| column | question it answers |
|---|---|
| Edge (calibr.) | "What's the honest-probability edge?" — but includes the macro dispersion bet |
| Edge (ours) | same question on the un-shrunk scale (optimistic) |
| Edge (consensus) | "Would public numbers alone see this?" |
| Edge (mkt-match) | "Does the edge survive with the dispersion story removed?" = team-specific |

**Conviction** (default sort) = the edge on the *weaker* of the two bracket endpoints,
calibrated (×0.75) and market-matched (×1.1475). Since edges are monotone in the
dispersion factor, clearing both endpoints certifies the edge under **every** dispersion
hypothesis in between — ✓✓ marks totals clearing +4% on both. That min() is the board's
defense against counting one macro opinion 50 times.

**Worked example.** Field mean ≈ 0. A team we rate +8 with the market's line implying
+11: cal = +6, mm = +9.2. The under might show +14% calibrated (mostly "the market
over-spreads good teams") but only +3% market-matched (little team-specific case) → high
calibrated edge, no ✓✓ — the board is telling you it's the macro trade. Flip case: UConn
shows ~+20% on *both* — a genuine disagreement about the roster that no dispersion story
explains. Those are the bets worth owning.

**The one-line summary of the ladder:** reality calibrates at 0.75× our scale, our board
sits at 1.0×, the market prices at ~1.15× — and every edge is some mix of "the market
spreads too wide" (the macro bet) and "we disagree about this team" (the idiosyncratic
bet). The four columns exist to tell you the mix.
