#!/usr/bin/env python3
"""Season-level validation of the win-total engine (intellectual audit, 2026-07-20).

The engine's job is a SEASON-WIN DISTRIBUTION, so validate at that level, not just per game:
run the full engine (probit + bands + shared shock + Poisson-Binomial + Gauss-Hermite) on
2021-25 with SP+ preseason ratings and each team's actual played schedule, then compare the
predicted distributions to actual win counts. Raw (shrink 1.0) vs calibrated (shrink 0.75).

Metrics:
  bias         mean(actual - E[W])            ~0 if centered
  disp ratio   SD(actual - E[W]) / mean model SD   ~1 if spread is right
  cover50/80   how often actual lands in the model's central 50% / 80% interval
  P(over) reliability   predicted P(W >= k) vs empirical frequency, bucketed
  six-win bump  actual freq of exactly 6 wins vs model (bowl-eligibility push)

FCS opponents rated -40 band 10 (engine default). Own/opp bands 6.0 (2026 base). HFA 2.3.
"""
import sys, os, json, csv, re, unicodedata, math, statistics as st
sys.path.insert(0, os.path.dirname(__file__))
import win_engine as E

YEARS = [2021, 2022, 2023, 2024, 2025]
BAND = 6.0


def nrm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def load_sp(year):
    n2c = {r['norm_key']: r['cfbd_school'] for r in csv.DictReader(open('data/anchors/team_name_map.csv'))}
    out = {}
    for r in csv.DictReader(open(f'data/backtest/sp_preseason/SP+_{year}_preseason.csv')):
        v = float(r['sp_plus_overall'])
        sc = n2c.get(r['norm_key'])
        if sc:
            out[sc] = v
        out[nrm(r['team_raw'])] = v
    return out


def team_seasons(shrink):
    rows = []
    for year in YEARS:
        sp = load_sp(year)
        mean_r = st.mean(v for k, v in sp.items())
        games = json.load(open(f'data/cfbd/2026-07-12/games_{year}_regular.json'))
        sched, wins = {}, {}
        for g in games:
            if g['homePoints'] is None or g['awayPoints'] is None:
                continue
            for side, opp in (('home', 'away'), ('away', 'home')):
                t = g[side + 'Team']
                if g[side + 'Classification'] != 'fbs':
                    continue
                rt = sp.get(t, sp.get(nrm(t)))
                if rt is None:
                    continue
                ocl = g[opp + 'Classification']
                oname = g[opp + 'Team']
                orat = sp.get(oname, sp.get(nrm(oname)))
                if ocl == 'fbs' and orat is None:
                    continue                      # unrated FBS opp: drop the game
                site = 0 if g['neutralSite'] else (1 if side == 'home' else -1)
                if ocl == 'fbs':
                    mu_o, band_o = mean_r + shrink * (orat - mean_r), BAND
                else:
                    mu_o, band_o = -40.0, 10.0
                sched.setdefault(t, []).append({'mu_opp': mu_o, 'site': site, 'band_opp': band_o})
                won = g[side + 'Points'] > g[opp + 'Points']
                wins[t] = wins.get(t, 0) + (1 if won else 0)
        for t, gl in sched.items():
            if len(gl) < 11:
                continue
            rt = sp.get(t, sp.get(nrm(t)))
            mu = mean_r + shrink * (rt - mean_r)
            d = E.win_distribution(mu, BAND, gl)['dist']
            rows.append({'year': year, 'team': t, 'dist': d, 'G': len(gl), 'w': wins.get(t, 0)})
    return rows


def metrics(rows, label):
    bias = st.mean(r['w'] - sum(k * p for k, p in enumerate(r['dist'])) for r in rows)
    errs = [r['w'] - sum(k * p for k, p in enumerate(r['dist'])) for r in rows]
    msd = st.mean(math.sqrt(sum(p * (k - sum(j * q for j, q in enumerate(r['dist']))) ** 2
                                for k, p in enumerate(r['dist']))) for r in rows)
    disp = st.pstdev(errs) / msd

    def central(r, mass):
        # smallest central interval via cumulative from the middle out
        d = r['dist']
        lo = hi = max(range(len(d)), key=lambda k: d[k])
        s = d[lo]
        while s < mass and (lo > 0 or hi < len(d) - 1):
            left = d[lo - 1] if lo > 0 else -1
            right = d[hi + 1] if hi < len(d) - 1 else -1
            if right >= left:
                hi += 1; s += d[hi]
            else:
                lo -= 1; s += d[lo]
        return lo, hi
    c50 = st.mean(1 if central(r, .5)[0] <= r['w'] <= central(r, .5)[1] else 0 for r in rows)
    c80 = st.mean(1 if central(r, .8)[0] <= r['w'] <= central(r, .8)[1] else 0 for r in rows)

    # P(over k-0.5) reliability across all team-seasons and k=3..10
    pairs = []
    for r in rows:
        for k in range(3, 11):
            if k <= r['G']:
                pairs.append((sum(r['dist'][k:]), 1 if r['w'] >= k else 0))
    buckets = []
    for lo, hi in [(0, .1), (.1, .25), (.25, .45), (.45, .55), (.55, .75), (.75, .9), (.9, 1.01)]:
        sel = [(p, y) for p, y in pairs if lo <= p < hi]
        if sel:
            buckets.append((f"{lo:.2f}-{hi:.2f}", len(sel),
                            st.mean(p for p, y in sel), st.mean(y for p, y in sel)))
    six_model = st.mean(r['dist'][6] if r['G'] >= 6 else 0 for r in rows)
    six_actual = st.mean(1 if r['w'] == 6 else 0 for r in rows)
    print(f"\n== {label} ==  (n={len(rows)} team-seasons)")
    print(f"  bias (actual-E[W]):  {bias:+.3f} wins")
    print(f"  dispersion ratio:    {disp:.3f}   (1.00 = spread exactly right)")
    print(f"  coverage central50:  {c50:.1%}   central80: {c80:.1%}")
    print(f"  P(over) reliability (pred -> actual):")
    for b, n, p, a in buckets:
        print(f"    {b}: n={n:>4}  pred {p:.3f}  actual {a:.3f}  gap {a-p:+.3f}")
    print(f"  P(exactly 6 wins): model {six_model:.3f}  actual {six_actual:.3f}  (bowl push)")


if __name__ == '__main__':
    for shrink, label in [(1.0, "RAW engine (shrink 1.0, band 6)"),
                          (0.75, "CALIBRATED engine (shrink 0.75, band 6)")]:
        metrics(team_seasons(shrink), label)
