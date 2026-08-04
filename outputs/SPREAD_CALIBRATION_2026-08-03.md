# Spread calibration vs posted Week 0 / Week 1 / GoTY lines — 2026-08-03

Input: owner capture `NCAAF_2026_all_posted_lines.xlsx` (snapshot Aug 3 8:33 PM
ET; Kambi + Action Network, 195 book ids, best price per market; 117 games).
Parsed to `data/market/spreads_wk01_goty_2026-08-03.csv` (canonical keys,
site from the audited payload schedule; 5 neutral games detected). 113/117
joined; 4 FCS name variants unmatched (UAlbany/LIU/Nicholls/SE Louisiana
spellings — FCSR alias additions queued, not blocking).

Model spread = −(rating_home − rating_away + 2.3·site), three lenses:
calibrated (0.75 shrink), market_matched (1.15 stretch), raw (unshrunk).
This is a DIAGNOSTIC — nothing here refits anything.

## 1. Scale validation — the headline clean bill

FBS-vs-FBS (n=62): **raw lens MAE 2.75, slope 1.022, corr 0.964, mean error
−0.84.** The unshrunk rating scale IS the spread market's scale, within noise,
against the sharpest numbers on the board (openers on marquee + wk0/1). The
lens family behaves exactly as designed: calibrated under-disperses (slope
1.25 ≈ 1/0.75), market_matched slightly over-disperses (0.89 ≈ 1/1.15). Many
games land essentially exact (UMass@Rutgers −30.5 vs −30.8; Bama@LSU −3.5 vs
−3.5; WKU@Nevada +3.0 vs +3.2; ASU@A&M −14.5 vs −15.1).

## 2. HFA reads light

True-home FBS-FBS games: mean error −0.95 ⇒ market-implied HFA ≈ **3.3** vs
our 2.3. Registered follow-up, not a constant change: early-season openers may
carry their own home lean; test on the full 2021–25 games archive before
touching HFA (it propagates everywhere).

## 3. The FCS tier is generically too deep in the payload

FCS-at-FBS (n=44): mean error ≈ **+9 points** in every lens — the market
prices FBS hosts ~9 weaker vs FCS visitors than the payload does (payload FCS
median −41). Win-total impact is minimal for cupcakes (P(win) saturates near
1.0 either way), which is why the totals engine passed its checks; the error
concentrates where probabilities are sensitive — the top tier:

- **Tarleton @ Bowling Green (wk1): posted −2.5** (FanDuel) vs our calibrated
  −6.8 / raw −4.6 / mm −2.9. The market sits at/below our most
  market-friendly lens. At the posted number, P(BGSU win) ≈ 0.57 vs the 0.661
  the corrected screen uses ⇒ BGSU's F1 gap +1.06 → ≈ +0.97 under
  market-implied FCS pricing. **The 1.05u BGSU position's F1 tag is at the
  bar on market evidence.** No action forced (procedure uses payload
  numbers); logged as a live watch item.
- MSU@Nevada, Montana@OSU, IllState@NIU: not posted in this capture — the
  Nevada re-entry trigger is still pending.

## 4. The NDSU outlier — payload review recommended

**Jacksonville State @ North Dakota State (wk0): posted +7.5 — Jax State
favored by a TD on the road.** Payload says NDSU −11.5 (raw). That is a
19-point disagreement, the largest in the file, and SP+ (−1.4) is on OUR side
of it. The market is fading the FBS transition hard. NDSU is bet-blocked
(reclass) but appears on ten FBS schedules incl. **Hawai'i (U7.5 held —
market-NDSU weakens the under)** and Nevada's wk7 trip (market-NDSU
strengthens any Nevada-over re-entry). Recommended: review the reclass-team
grade provenance (NDSU cal +1.46) against this line before trusting either
number. Sacramento State's wk0 line (EMU −8 vs our −10.9) leans the same
direction, milder.

## 5. Clean per-team reads (FBS-FBS games only)

Attribution caveat: one game carries both teams' errors plus market noise —
reads under ±3 are noise; FCS-hosting games are excluded (they measure the
FCS tier, not the host — the first pass that included them produced fake
−10/−22 "reads" on UConn/Kennesaw/UCF/Vandy, none of which have any clean
FBS-FBS read in this window).

Against our positions: **East Carolina −10.4** (ECU@Bama −28.5 vs −18.1;
Bama's other game is priced exactly, so the miss likely sits on ECU's side —
ECU O 0.55u), **West Virginia +6.5** (vs our U 0.50u), **Tulsa −4.2** (O
1.10u), **Liberty +4.0** (vs U 0.60u), **Illinois +3.7** (vs U 0.65u),
**Texas +6.0 on n=2** incl. OSU@Texas posted −1.5 vs our raw +6.4 (cools the
Texas U9.5 watch item). Supporting: **Duke +3.6** (O rec), FSU +2.9,
Wisconsin +2.6 (mildly against U), Michigan +1.5 (neutral-ish). Dead-on:
Rutgers, UMass, Nevada, ASU, Oregon State, Wake, Pitt, Florida, Hawai'i
(FBS games).

## Queue

FCSR spelling aliases (UAlbany etc.); HFA study on the games archive; NDSU
reclass grade review; re-pull this capture near close for CLV once bets are
graded; MSU@Nevada line watch (re-entry trigger).

## CORRECTION (2026-08-03, owner-reported transcription error, append-only)

The JaxState@NDSU row was transcribed with the wrong sign in the source sheet:
Jacksonville State is CATCHING 7.5, i.e. posted NDSU −7.5 (not +7.5). §4 is
retracted as written: the "19-point outlier" is a data-entry artifact. The
corrected read is posted −7.5 vs payload raw −11.5 — market rates NDSU ~4 pts
below payload, a mild lean inside the single-game noise band, same direction
and size as the Sacramento State wk0 read (~3). Transition-team payload review
downgraded from "recommended" to watch-list; the Hawai'i-U/Nevada-re-entry
implications shrink to noise. Corrected aggregates (FBS-FBS n=62): raw MAE
2.50 (was 2.75), slope 1.020, corr 0.978, mean −1.08; HFA read firms slightly
to ~3.5 implied vs our 2.3. Dataset CSV corrected in place; owner may want to
fix the source xlsx cell for his own records.
