#!/usr/bin/env python3
"""S14: preseason consensus vs the early-season spread market.
Per PREREGISTRATION_S14_2026-07-31.md — bars fixed before any outcome computed."""
import csv, json, os, re, unicodedata
from collections import defaultdict
from statistics import median
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


AL = {'connecticut': 'uconn'}


def rd(p, c):
    return {AL.get(norm(r['team_name' if 'team_name' in r else 'team']), norm(r['team_name' if 'team_name' in r else 'team'])): float(r[c])
            for r in csv.DictReader(open(p))}


HFA = 2.3
rows = []
for y in range(2021, 2026):
    f = f'data/backtest/sp_preseason/SP+_{y}_preseason.csv'
    sp = {}
    for r in csv.DictReader(open(f)):
        k = AL.get(r['norm_key'], r['norm_key'])
        sp[k] = float(r['sp_plus_overall'])
    neutral = {}
    for g in json.load(open(f'data/cfbd/2026-07-12/games_{y}_regular.json')):
        neutral[g['id']] = bool(g.get('neutralSite'))
    for g in json.load(open(f'data/cfbd/lines/lines_{y}.json')):
        if g.get('homeClassification') != 'fbs' or g.get('awayClassification') != 'fbs':
            continue
        h, a = AL.get(norm(g['homeTeam']), norm(g['homeTeam'])), AL.get(norm(g['awayTeam']), norm(g['awayTeam']))
        if h not in sp or a not in sp or g.get('homeScore') is None or g.get('awayScore') is None:
            continue
        closes = [l['spread'] for l in g.get('lines') or [] if l.get('spread') is not None and abs(l['spread']) <= 60]
        opens = [l['spreadOpen'] for l in g.get('lines') or [] if l.get('spreadOpen') is not None and abs(l['spreadOpen']) <= 60]
        if not closes:
            continue
        site = 0.0 if neutral.get(g['id'], False) else HFA
        M = sp[h] - sp[a] + site
        margin = g['homeScore'] - g['awayScore']
        rows.append(dict(y=y, wk=g['week'], M=M, close=median(closes),
                         open=median(opens) if opens else None, margin=margin))

print(f'panel: {len(rows)} FBS-vs-FBS games with close, both SP+-rated, scored')
print('by year:', {y: sum(1 for r in rows if r['y'] == y) for y in range(2021, 2026)})
print('with opener:', sum(1 for r in rows if r['open'] is not None))


def ats(sub, line_key):
    """cover-1/push-0.5-excluded record for the consensus side vs given line."""
    w = l = 0
    for r in sub:
        line = r[line_key]
        D = r['M'] + line
        if D == 0:
            continue
        side_home = D > 0
        cover_margin = r['margin'] + line          # >0 home covers
        if cover_margin == 0:
            continue
        won = (cover_margin > 0) == side_home
        w += int(won); l += int(not won)
    return w, l, (w / (w + l) if w + l else float('nan'))


def leg(title, wk_lo, wk_hi, thresh, line_key):
    sub = [r for r in rows if wk_lo <= r['wk'] <= wk_hi and r[line_key] is not None
           and abs(r['M'] + r[line_key]) >= thresh]
    w, l, p = ats(sub, line_key)
    print(f'\n{title}: n={w+l}, cover {100*p:.1f}%')
    ok_years = 0
    for y in range(2021, 2026):
        wy, ly, py = ats([r for r in sub if r['y'] == y], line_key)
        flag = 'ok' if py >= 0.524 else '  '
        ok_years += int(py >= 0.524)
        print(f'  {y}: {wy}-{ly}  {100*py:.1f}% {flag}')
    return p, ok_years, w + l


print('\n===== S14-A PRIMARY: weeks 0-3, |D|>=3, vs CLOSE =====')
pA, okA, nA = leg('A', 0, 3, 3.0, 'close')
print(f'S14-A: {"PASS" if pA >= 0.55 and okA >= 4 else "FAIL"} (bars: pooled>=55%, >=4/5 years >=52.4%)')
w, l, p5 = ats([r for r in rows if r['wk'] <= 3 and abs(r['M'] + r['close']) >= 5], 'close')
print(f'  report |D|>=5: n={w+l}, {100*p5:.1f}%')

print('\n===== S14-B OPENERS: weeks 0-3, |D|>=3, vs OPEN =====')
pB, okB, nB = leg('B', 0, 3, 3.0, 'open')
print(f'S14-B: {"PASS" if pB >= 0.55 and okB >= 4 else "FAIL"}')

print('\n===== S14-C DECAY (report-only) =====')
print('week |   n | slope market~M    R2 | RMSE(M-mkt) | MAE mkt | MAE consensus')
for wk in range(0, 15):
    sub = [r for r in rows if r['wk'] == wk]
    if len(sub) < 30:
        continue
    Mv = np.array([r['M'] for r in sub])
    mk = np.array([-r['close'] for r in sub])
    mg = np.array([r['margin'] for r in sub])
    b = np.polyfit(Mv, mk, 1)
    r2 = np.corrcoef(Mv, mk)[0, 1] ** 2
    print(f'  {wk:2d} | {len(sub):3d} |  {b[0]:+.3f}        {r2:.3f} |   {np.sqrt(np.mean((Mv-mk)**2)):5.2f}     |  {np.mean(np.abs(mg-mk)):5.2f}  |  {np.mean(np.abs(mg-Mv)):5.2f}')

print('\n===== S14-D SHAPE (report-only, vs close) =====')
print(f'{"":12s}' + ''.join(f'|D| {lo}-{hi if hi<99 else "+"}   ' for lo, hi in ((1, 3), (3, 5), (5, 8), (8, 99))))
for wlab, wlo, whi in (('wk 0-1', 0, 1), ('wk 2-3', 2, 3), ('wk 4-8', 4, 8), ('wk 9+', 9, 20)):
    cells = []
    for dlo, dhi in ((1, 3), (3, 5), (5, 8), (8, 99)):
        sub = [r for r in rows if wlo <= r['wk'] <= whi and dlo <= abs(r['M'] + r['close']) < dhi]
        w, l, p = ats(sub, 'close')
        cells.append(f'{100*p:4.1f}% n={w+l:<4d}')
    print(f'{wlab:12s}' + ' '.join(cells))
