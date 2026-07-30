#!/usr/bin/env python3
"""S11: dispersion-tilt persistence per PREREGISTRATION_S10_S11_2026-07-28.md.
s*_y = stretch on preseason SP+ deviations solving slope(EW_s - line ~ line)=0,
vs SBD DK openers 2021-24 (+2025 owner near-closers, report-only)."""
import csv, json, math, os, re, unicodedata
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


ALIAS = {'connecticut': 'uconn', 'appstate': 'appalachianstate', 'olemiss': 'olemiss',
         'sanjosest': 'sanjosestate', 'umass': 'massachusetts'}


def sp_pre(year):
    out = {}
    for r in csv.DictReader(open(f'data/backtest/sp_preseason/SP+_{year}_preseason.csv')):
        k = r['norm_key']; out[ALIAS.get(k, k)] = float(r['sp_plus_overall'])
    return out


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def sched(year):
    games = json.load(open(f'data/cfbd/2026-07-12/games_{year}_regular.json'))
    out = {}
    for g in games:
        h, a = norm(g['homeTeam']), norm(g['awayTeam'])
        site0 = 0.0 if g.get('neutralSite') else 1.0
        out.setdefault(h, []).append((a, site0))
        out.setdefault(a, []).append((h, -site0))
    return out


def ew(team, year_sched, ratings):
    tot = 0.0
    for opp, site in year_sched.get(team, []):
        if opp not in ratings:
            tot += 0.95
            continue
        tot += phi((ratings[team] - ratings[opp] + 2.3 * site) / 13.5)
    return tot


def lines_for(year):
    if year <= 2024:
        return {norm(r['team']): float(r['line'])
                for r in csv.DictReader(open(f'data/win_totals/sbd_historical/sbd_{year}.csv'))}
    out = {}
    for r in csv.DictReader(open('data/win_totals/Win Totals from 2025.csv')):
        vals = []
        for c in ('Bet365 Win Total', 'FanDuel Win Total', 'DraftKings Win Total',
                  'Caesars Win Total', 'BetRivers Win Total'):
            m = re.match(r'\s*([0-9.]+)', r.get(c) or '')
            if m:
                vals.append(float(m.group(1)))
        if vals:
            out[norm(r['TEAM'])] = float(np.median(vals))
    return {ALIAS.get(k, k): v for k, v in out.items()}


def slope_at(s, teams, sp, sc, lines):
    mu = np.mean([sp[t] for t in teams])
    rt = {t: mu + s * (v - mu) for t, v in sp.items()}
    edges = np.array([ew(t, sc, rt) - lines[t] for t in teams])
    L = np.array([lines[t] for t in teams])
    A = np.column_stack([np.ones(len(L)), L])
    b, *_ = np.linalg.lstsq(A, edges, rcond=None)
    return float(b[1]), float(np.mean(edges ** 2))


print('year   n   s*(slope=0)   s(min-MSE)   note')
results = {}
for y in [2021, 2022, 2023, 2024, 2025]:
    sp = sp_pre(y); sc = sched(y); ln = lines_for(y)
    teams = sorted(set(sp) & set(ln))
    lo, hi = 0.7, 1.7
    flo, _ = slope_at(lo, teams, sp, sc, ln)
    fhi, _ = slope_at(hi, teams, sp, sc, ln)
    star = None
    if flo * fhi < 0:
        for _ in range(40):
            mid = (lo + hi) / 2
            fm, _ = slope_at(mid, teams, sp, sc, ln)
            if flo * fm <= 0:
                hi = mid; fhi = fm
            else:
                lo = mid; flo = fm
        star = (lo + hi) / 2
    grid = np.arange(0.7, 1.71, 0.02)
    mses = [slope_at(s, teams, sp, sc, ln)[1] for s in grid]
    smse = float(grid[int(np.argmin(mses))])
    note = '2025 = owner near-closers, report-only' if y == 2025 else 'SBD DK openers'
    results[y] = star
    print(f'{y}  {len(teams):3d}   {star if star else "no-root":>10}   {smse:9.2f}   {note}'
          if star is None else
          f'{y}  {len(teams):3d}   {star:10.3f}   {smse:9.2f}   {note}')
bar_years = [y for y in [2021, 2022, 2023, 2024] if results[y] is not None]
above = sum(1 for y in bar_years if results[y] > 1.0)
mean_s = np.mean([results[y] for y in bar_years]) if bar_years else float('nan')
print(f'\nbar: s*>1 in >=3 of 4 SBD years: {above}/4 | mean s* {mean_s:.3f} (bar >=1.05)')
print('PASS' if above >= 3 and mean_s >= 1.05 else 'FAIL')
