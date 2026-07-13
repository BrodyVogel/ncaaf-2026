#!/usr/bin/env python3
"""§7 enrichment: benchmark the anchor against the 2025 win-totals market.

Per team: market expected wins (median book total, de-juiced toward the favored side),
SP+-implied expected wins (TRUE preseason SP+ 2025 + actual 2025 regular schedule,
P(win) = Phi((dSP + 2.0*home)/13.5), FCS opponents = -22), realized regular-season wins.
Compares MAE/RMSE/correlation of misses. COMPUTE-PHASE data (blinding-safe here: backtest).

The listed price is the OVER price (standard convention). De-juice: shift the total by
0.25 wins in the direction the juice leans, scaled by |implied prob - 50%| — crude but
unbiased enough for a benchmark.

Usage: python3 market_check_2025.py
"""
import csv, json, math, re
import numpy as np

D = "data/cfbd/2026-07-12"

def name_map_cols():
    rows = list(csv.DictReader(open("data/anchors/team_name_map.csv")))
    return rows

def implied_prob(american):
    a = float(american)
    return 100 / (a + 100) if a > 0 else -a / (-a + 100)

def parse_cell(cell):
    m = re.match(r"^\s*([\d.]+)\s*\(([-+]\d+)\)\s*$", cell or "")
    if not m:
        return None
    total, price = float(m.group(1)), m.group(2)
    p_over = implied_prob(price)
    return total + (p_over - 0.5) * 1.0  # de-juiced expected wins (0.5 win per 100% prob tilt)

def main():
    # --- market
    nm = name_map_cols()
    # win-totals TEAM spellings: try match against every known spelling column
    spell2cfbd = {}
    for r in nm:
        for col in ("cfbd_school", "sp_plus_espn", "fei_bcftoys", "massey", "espn_fpi", "teamrankings", "pff_2025"):
            spell2cfbd.setdefault(r[col], r["cfbd_school"])
    spell2cfbd.update({"FAU": "Florida Atlantic", "Louisiana Lafayette": "Louisiana",
                       "Louisiana Monroe": "UL Monroe"})  # win-totals file spellings
    market, unmatched = {}, []
    for r in csv.DictReader(open("data/win_totals/Win Totals from 2025.csv")):
        team = spell2cfbd.get(r["TEAM"].strip())
        if not team:
            unmatched.append(r["TEAM"]); continue
        vals = [parse_cell(r[c]) for c in ("Bet365 Win Total", "FanDuel Win Total", "DraftKings Win Total",
                                           "Caesars Win Total", "BetRivers Win Total")]
        vals = [v for v in vals if v is not None]
        if vals:
            market[team] = float(np.median(vals))
    print(f"market teams parsed: {len(market)}; unmatched spellings: {unmatched or 'none'}")

    # --- SP+ implied wins
    n2c = {r["norm_key"]: r["cfbd_school"] for r in nm}
    pre = {n2c[r["norm_key"]]: float(r["sp_plus_overall"])
           for r in csv.DictReader(open("data/backtest/sp_preseason/SP+_2025_preseason.csv"))}
    FCS = -22.0
    exp_wins = {t: 0.0 for t in pre}
    n_games = {t: 0 for t in pre}
    for g in json.load(open(f"{D}/games_2025_regular.json")):
        h, a = g.get("homeTeam"), g.get("awayTeam")
        neutral = g.get("neutralSite") or False
        for me, opp, home in ((h, a, not neutral), (a, h, False)):
            if me in pre:
                d = pre[me] - pre.get(opp, FCS) + (2.0 if home else 0.0)
                exp_wins[me] += 0.5 * (1 + math.erf(d / (13.5 * math.sqrt(2))))
                n_games[me] += 1
    # --- realized regular-season wins
    real = {}
    for r in json.load(open(f"{D}/records_2025.json")):
        if r.get("classification") == "fbs":
            rs = r.get("regularSeason") or {}
            real[r["team"]] = rs.get("wins")

    rows = [(t, market[t], exp_wins[t], real[t]) for t in market
            if t in exp_wins and n_games.get(t, 0) >= 10 and real.get(t) is not None]
    mk = np.array([r[1] for r in rows]); sp = np.array([r[2] for r in rows]); rl = np.array([r[3] for r in rows], float)
    print(f"benchmark teams: {len(rows)} (FBS with market + schedule + record)")
    for nm_, pred in (("market", mk), ("SP+raw", sp)):
        e = rl - pred
        print(f"  {nm_:8s} MAE={np.abs(e).mean():.2f}  RMSE={np.sqrt((e**2).mean()):.2f}  mean err={e.mean():+.2f}  SD={e.std():.2f}")
    print(f"  corr(market miss, SP+ miss) = {np.corrcoef(rl-mk, rl-sp)[0,1]:.3f}")
    print(f"  corr(market total, SP+ exp wins) = {np.corrcoef(mk, sp)[0,1]:.3f}")
    # where they disagreed, who was right?
    dis = np.abs(mk - sp) >= 1.0
    if dis.sum() >= 10:
        closer_mkt = (np.abs(rl - mk) < np.abs(rl - sp))[dis]
        print(f"  disagreements >=1 win: n={dis.sum()}, market closer {closer_mkt.mean()*100:.0f}% of the time")

if __name__ == "__main__":
    main()
