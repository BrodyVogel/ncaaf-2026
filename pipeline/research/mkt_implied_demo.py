#!/usr/bin/env python3
"""Demo (S16 scaffolding, not a registered study): market-implied ratings mechanics.

Shows (a) one week of closes alone is UNDERDETERMINED (disconnected graph,
fewer equations than unknowns, level unidentified); (b) the ridge-chained
solve — prior = last week's ratings, week-1 prior = preseason consensus —
is well-posed and recovers the market's cumulative team-strength drift.
Demo constants: HFA=2.3 fixed, lambda=0.5 (per-team ridge). S16 freezes real ones.
"""
import csv, json, os, re, unicodedata
from collections import defaultdict
from statistics import median
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


AL = {'connecticut': 'uconn'}
Y, HFA, LAM = 2024, 2.3, 0.5

pre = {}
for r in csv.DictReader(open(f'data/backtest/sp_preseason/SP+_{Y}_preseason.csv')):
    pre[AL.get(r['norm_key'], r['norm_key'])] = float(r['sp_plus_overall'])
neutral = {g['id']: bool(g.get('neutralSite'))
           for g in json.load(open(f'data/cfbd/2026-07-12/games_{Y}_regular.json'))}
by_week = defaultdict(list)
for g in json.load(open(f'data/cfbd/lines/lines_{Y}.json')):
    if g.get('homeClassification') != 'fbs' or g.get('awayClassification') != 'fbs':
        continue
    h, a = AL.get(norm(g['homeTeam']), norm(g['homeTeam'])), AL.get(norm(g['awayTeam']), norm(g['awayTeam']))
    sp = [l['spread'] for l in g.get('lines') or [] if l.get('spread') is not None and abs(l['spread']) <= 60]
    if h in pre and a in pre and sp:
        by_week[g['week']].append((h, a, median(sp), 0.0 if neutral.get(g['id']) else 1.0))

# (a) one week alone
wk = 5
games = by_week[wk]
teams_w = sorted({t for g in games for t in g[:2]})
parent = {t: t for t in teams_w}


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x


for h, a, *_ in games:
    parent[find(h)] = find(a)
comps = len({find(t) for t in teams_w})
print(f'week {wk} alone: {len(games)} equations, {len(teams_w)} teams appearing '
      f'({len(pre)} rated), {comps} disconnected islands -> underdetermined; '
      f'level unidentified (add c to every rating, all spreads unchanged)')

# (b) chained ridge weeks 1..5
teams = sorted(pre)
idx = {t: i for i, t in enumerate(teams)}
R = np.array([pre[t] for t in teams])
for w in range(1, 6):
    gs = by_week.get(w, [])
    if not gs:
        continue
    A = np.zeros((len(gs) + len(teams), len(teams)))
    b = np.zeros(len(gs) + len(teams))
    for k, (h, a, spr, site) in enumerate(gs):
        A[k, idx[h]], A[k, idx[a]] = 1, -1
        b[k] = -spr - HFA * site          # market home margin minus HFA
    for i in range(len(teams)):           # ridge to prior (= last week's R)
        A[len(gs) + i, i] = np.sqrt(LAM)
        b[len(gs) + i] = np.sqrt(LAM) * R[i]
    R, *_ = np.linalg.lstsq(A, b, rcond=None)
    R += np.mean([pre[t] for t in teams]) - np.mean(R)   # gauge: preserve level
d = R - np.array([pre[t] for t in teams])
print(f'\nchained ridge through week 5 ({Y}): mean |move| {np.mean(np.abs(d)):.2f}, '
      f'RMSE vs preseason {np.sqrt(np.mean(d**2)):.2f} (S14-C said ~6-7 by wk 4-5)')
order = np.argsort(d)
print("market's biggest risers wk1-5: " + ', '.join(f'{teams[i]} {d[i]:+.1f}' for i in order[::-1][:6]))
print('biggest fallers:              ' + ', '.join(f'{teams[i]} {d[i]:+.1f}' for i in order[:6]))
