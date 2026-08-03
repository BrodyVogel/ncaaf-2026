# Rejoin findings — canonical-key repair across validation + screen (2026-08-03)

Owner directive 2026-08-03: "Fix it. Fix all of it. The FCS garbage, the UConn
screwup, the S7/S8 disaster." Scripts: `team_alias.py` (bridge),
`s7s8_rejoin_2026-08-03.py` (before/after harness), fixed `s8_run_panel.py`,
fixed `s18_fcs_factor.py` (+ regenerated `s18_fcs2026.csv`), and
`portfolio_screen_2026-08-03.py` (corrected live screen).

## Root cause

No canonical name bridge. SP+ vintages/anchors key on canonical `norm_key`
(`miamifl`, `appalachianstate`, `connecticut`, `louisianamonroe`); CFBD game
JSON and board captures norm to CFBD spellings (`miami`, `appstate`, `uconn`,
`ulmonroe`). Every bare `norm()`-vs-`norm()` join across that boundary silently
dropped or misclassified those teams. Two independent manifestations:

- **Backtests (S7/S8/S13/S18):** games vs the unmatched teams fell into the
  `opp not in ratings` branch and were priced at the 0.95 FCS constant —
  61 real-FBS games inside the S7 panel EWs (`miami` 37, `ulmonroe` 14,
  `appstate` 10; `uconn` was patched ad hoc via SP_ALIAS) — and the teams'
  own board rows dropped (4 Miami rows). Worse: in seasons where the board
  spelled "Appalachian State" (matching the vintage), the team keyed into the
  panel but matched ZERO games — **App State 2021 and 2022 entered the panel
  with expected wins 0.00 and recorded wins 0**, a −9.0 "gap" scored as a
  winning under call both years. Two fabricated rows inside the flagship
  bucket, both counted as hits.
- **Live screen (2026-08-02):** `sp` built in CFBD-name space, read back with
  canonical keys — App State / UConn / UL Monroe / Miami-FL structurally
  unrecommendable (gap=None), and `HELD` keyed `'uconn'` never matched the
  payload, so the book's largest position (1.07u) was absent from every
  section of the screen.

## S7 re-derivation (K1/K2), old join vs fixed join

Bar years 2021–24 (replication first: old-join harness reproduces
FINDINGS_S7 within row provenance — n=294 vs 296, ≥1.0 bucket 42 @ 78.6%
vs documented 44 @ 77.3%):

|                      | OLD join      | FIXED join    |
|----------------------|---------------|---------------|
| board rows joined    | 294 (4 dropped) | **298 (0 dropped)** |
| K1 consensus MAE     | 1.767         | 1.783         |
| K1 market MAE        | 1.857         | 1.810         |
| gap <0.5 side rate   | 47.4% (154)   | 47.6% (168)   |
| gap 0.5–1.0          | 48.8% (80)    | 51.2% (82)    |
| **gap ≥1.0**         | **78.6% (42)**| **76.7% (30)**|
| per-year ≥1.0        | 13/14, 13/16, 3/5, 4/7 | 8/8, 11/13, 2/4, 2/5 |
| 2025 (peeked) ≥1.0   | 69.6% (23)    | 70.0% (20)    |
| **pooled 2021–25 ≥1.0** | **75.4% (49/65)** | **74.0% (37/50)** |

Reading: **the F1 mechanism survives the repair.** K1 (consensus beats market
openers outright) holds in every variant. The ≥1.0 bucket's hit rate is
essentially unchanged — but the bucket itself shrinks ~25%: five of 2021's
fourteen "wins" were join artifacts (two fabricated App State unders + three
rows whose EW deflates out of the bucket once games at Miami/ULM/App State are
priced properly), and zero side calls flip. The five-season evidence base for
F1 is now n=50 at 74.0% (Wilson 95% ≈ 60–84%), not n=65 at 75.4%. The
2023–24 thinness (2/4, 2/5) is unchanged and remains the honest caveat.
All four recovered Miami rows land in the <0.5 no-bet zone.

## S8 rerun under fixed joins (panel 522 → 534 team-seasons)

Registered verdicts all stand; nothing flips in either direction.

- **L1 main effect: FAIL (unchanged).** c=+1.092, t=+1.96 (was +1.095/+1.93);
  ΔR²=0.0064 (unchanged). The drop-2022 LOYO fold moves +0.03 → **−0.02**:
  L1-B sign stability, previously a "technical PASS" with a flagged
  2022-carried effect, now fails formally. Cleaner version of the same story.
- L2a trench: FAIL (c_t +0.82 t 0.84). L2b OL persistence: r=+0.115 t=+2.27,
  byte-identical (internal to shadow space — expected invariance, and a good
  integrity check on the repair).
- L3 money leg: consensus zone 25 @ 68.2% (was 30 @ 70.4%); λ=1 still
  dilutes (128 @ 55.9%); soft-(i) still FAIL, soft-(ii) still PASS.
- L4: β=+0.081 (t 1.90). **λ\* = 0 for 2027, unchanged.**
- L6 (report-only): G5 c=+3.19 t=+2.76 (was +3.54/+2.94) — the 2027 retry
  hypothesis survives, slightly attenuated.

## S18 regeneration

`s18_fcs2026.csv` 127 → 130 rows: gains **App State Q=82.18 N=12 (3rd-highest
on the board)**, Miami-FL (2.77), UL Monroe (6.5); `uconn` re-keyed
`connecticut`; **zero existing values changed**. Drop census now prints
`dropped-but-FBS-aliasable: {}`. S18-B under fixed joins: MAE 1.774 → 1.763,
zone 68.2% (n=22) → 73.9% (n=23) — same caveat as before: the two zones are
different bet sets (independent denominators), so treat as descriptive.

## Empirical check on the 0.95 FCS constant

Realized FBS win rate in true FBS-vs-FCS games (classification fields),
2021–25 pooled: **568/602 = 0.944**; hosts with market total ≤5.5: 65/70 =
0.929. The constant was empirically sound in-sample. The 2026 failure mode is
regime-specific: the rerate places Tarleton (−14), Montana State (−15) and
Montana (−16) at FBS-fringe strength, visiting exactly the low-total hosts
F2o selects. The corrected screen prices FCS opponents from the payload
rerate; the backtests keep 0.95 for genuinely non-FBS historical opponents
(now correctly scoped to them).

## Corrected screen (portfolio_screen_2026-08-03.py) — board deltas

Guards: 19/19 held rows priced; 126 FCS games from payload; zero fallbacks;
zero gap=None. Rule set unchanged from the 2026-08-02 screen (Amendments
1+2+3); every delta below is pure plumbing.

- **UConn O5.5 (1.07u, largest position) prices for the first time:
  minE +14.1%, calE +14.5%, gap −0.29, tags [ARM].** The anchor lens sits
  0.29 wins *below* the market on the over side: the position is carried
  entirely by the model/grade layer against the consensus — the unvalidated
  disagreement category identified in AUDIT_2026-08-03 §3.
- **Nevada O4.5 (0.75u): gap +0.76 → +0.46, loses F2o — its only tag.**
  The position keeps +10.9% min-lens model edge but has no factor
  justification under the committed rules.
- Bowling Green +1.43 → +1.06 and Oregon State +1.45 → +1.31: both keep F1.
  Buffalo +1.53 → +1.61, Wisconsin +1.23 → +1.18, Tulsa +0.79 → +0.83: hold.
- **Vanderbilt O5.5 +0.96 → +1.01: gains F1, PRIORITY, 0.25u (was 0.15u).**
- North Carolina O4.5 enters E at gap +0.75 (rule-blocked, mid-band).
- All other held positions move ≤ ±0.05; no other tag changes.

## Fixed vs still open

Fixed: alias bridge; S18 generator + table; S7/S8 joins + re-derived numbers;
live screen keys, FCS pricing, HELD coverage, join guards; FINDINGS_S7/S8
corrections appended.

Open (owner decisions / data needed): real under-price capture (all under
prices remain synthesized from the 30-cent convention — 8 of 19 held
positions); F5 functional form (binary dummy t≈1.85 deployed vs continuous
t=+2.83 validated); correlation control not wired into the live screen path
(`portfolio_mc.py`); legacy research scripts (s9/s11/s12/s13_rp_board/s15/
weekend_scan) retain local alias maps — superseded or rerun-on-demand, not
edited retroactively; `s13_*_proxy.csv` still has no generator;
STALENESS_REGISTER refresh.
