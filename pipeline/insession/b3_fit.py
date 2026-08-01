#!/usr/bin/env python3
"""B3: week-indexed observation weights. Per REGISTRATION_B3_WEEK_WEIGHTS.
Reuses B2 loaders by exec-ing its definitions with stages skipped."""
import csv, json, os, re, unicodedata
from collections import defaultdict
from statistics import median
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


AL = {'connecticut': 'uconn'}
TUNE = [2021, 2022, 2023, 2024]
panel = defaultdict(list)
for r in csv.DictReader(open('data/research/insession_panel_2016_2025.csv')):
    y = int(r['year'])
    if y in TUNE and r['fcs_opp'] == '0':
        panel[y].append(r)
MAP_OLD = (17.97, 0.950)


def season_games(y):
    rows = {(r['game_id'], r['team']): r for r in panel[y]}

    def conv(r):
        if not r['off_ppa'] or not r['off_plays']:
            return None
        return MAP_OLD[0] + MAP_OLD[1] * float(r['off_ppa']) * float(r['off_plays'])
    out = []
    for (gid, t), r in rows.items():
        if r['home'] != '1' and r['neutral'] != '1':
            continue
        opp = rows.get((gid, r['opp']))
        if opp is None or (r['home'] != '1' and norm(opp['team']) < norm(t)):
            continue
        out.append(dict(w=int(r['week']), i=t, j=r['opp'], gid=gid,
                        site=0.0 if r['neutral'] == '1' else 1.0,
                        margin=float(r['margin']), effi=conv(r), effj=conv(opp)))
    return sorted(out, key=lambda g: g['w'])


def sp_prior(y):
    off, dfn = {}, {}
    for r in csv.DictReader(open(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv')):
        k = AL.get(r['norm_key'], r['norm_key'])
        off[k], dfn[k] = float(r['sp_plus_off']), float(r['sp_plus_def'])
    mo, md = np.mean(list(off.values())), np.mean(list(dfn.values()))
    return {t: (off[t] - mo, md - dfn[t]) for t in off}


def market_chain(y, prior, hfa):
    gp = (f'data/cfbd/insession/games_{y}_regular.json'
          if os.path.exists(f'data/cfbd/insession/games_{y}_regular.json')
          else f'data/cfbd/2026-07-12/games_{y}_regular.json')
    neutral = {g['id']: bool(g.get('neutralSite')) for g in json.load(open(gp))}
    by_week = defaultdict(list)
    for g in json.load(open(f'data/cfbd/lines/lines_{y}.json')):
        if g.get('homeClassification') != 'fbs' or g.get('awayClassification') != 'fbs':
            continue
        h, a = AL.get(norm(g['homeTeam']), norm(g['homeTeam'])), AL.get(norm(g['awayTeam']), norm(g['awayTeam']))
        cl = [l['spread'] for l in g.get('lines') or [] if l.get('spread') is not None and abs(l['spread']) <= 60]
        if cl:
            by_week[g['week']].append((h, a, median(cl), 0.0 if neutral.get(g['id']) else 1.0))
    teams = sorted(prior)
    idx = {t: i for i, t in enumerate(teams)}
    R = np.array([prior[t][0] + prior[t][1] for t in teams])
    out = {}
    for w in range(1, 16):
        gs = [g for g in by_week.get(w, []) if g[0] in idx and g[1] in idx]
        if gs:
            A = np.zeros((len(gs) + len(teams), len(teams)))
            b = np.zeros(len(gs) + len(teams))
            for k, (h, a, spr, site) in enumerate(gs):
                A[k, idx[h]], A[k, idx[a]] = 1, -1
                b[k] = -spr - hfa * site
            for i in range(len(teams)):
                A[len(gs) + i, i] = np.sqrt(0.5)
                b[len(gs) + i] = np.sqrt(0.5) * R[i]
            R, *_ = np.linalg.lstsq(A, b, rcond=None)
            R += -np.mean(R)
        out[w] = {t: R[idx[t]] for t in teams}
    return out


def wk_mult(w, cfg):
    if w == 1:
        return cfg.get('m1', 1.0)
    if 2 <= w <= 4:
        return cfg.get('m24', 1.0)
    return 1.0


def run_season(games, prior, cfg, mkt=None, track=None):
    teams = sorted(prior)
    idx = {t: k for k, t in enumerate(teams)}
    N = len(teams)
    x0 = np.zeros(2 * N)
    for t in teams:
        x0[idx[t]], x0[N + idx[t]] = prior[t]
    x = x0.copy()
    preds, hist = [], []
    prev_overall = None
    for w in range(1, 16):
        wk = [g for g in games if g['w'] == w and g['i'] in idx and g['j'] in idx]
        for g in wk:
            m = (x[idx[g['i']]] + x[N + idx[g['i']]]) - (x[idx[g['j']]] + x[N + idx[g['j']]]) \
                + cfg['hfa'] * g['site']
            preds.append((w, m, g['margin']))
        hist.extend(wk)
        rows, rhs, wts = [], [], []
        for g in hist:
            aw = cfg['rho'] ** (w - g['w'])
            se = (cfg['sig_eff'] * wk_mult(g['w'], cfg)) ** 2
            ii, jj = idx[g['i']], idx[g['j']]
            if g['effi'] is not None:
                r1 = np.zeros(2 * N); r1[ii], r1[N + jj] = 1, -1
                rows.append(r1); rhs.append(g['effi']); wts.append(aw / se)
            if g['effj'] is not None:
                r2 = np.zeros(2 * N); r2[jj], r2[N + ii] = 1, -1
                rows.append(r2); rhs.append(g['effj']); wts.append(aw / se)
            r3 = np.zeros(2 * N)
            r3[ii], r3[N + ii], r3[jj], r3[N + jj] = 1, 1, -1, -1
            rows.append(r3); rhs.append(g['margin'] - cfg['hfa'] * g['site'])
            wts.append(aw / (cfg['sig_m'] ** 2 * se))
        if mkt is not None and w - 1 >= 1:
            for t, rv in mkt.get(w - 1, {}).items():
                if t in idx:
                    r4 = np.zeros(2 * N); r4[idx[t]], r4[N + idx[t]] = 1, 1
                    rows.append(r4); rhs.append(rv); wts.append(1 / cfg['sig_mkt'] ** 2)
        for t in teams:
            for od in (0, N):
                rp = np.zeros(2 * N); rp[idx[t] + od] = 1
                rows.append(rp); rhs.append(x0[idx[t] + od]); wts.append(1 / cfg['sig_prior'] ** 2)
        A = np.array(rows); b = np.array(rhs); sw = np.sqrt(np.array(wts))
        x, *_ = np.linalg.lstsq(A * sw[:, None], b * sw, rcond=None)
        x[:N] -= x[:N].mean(); x[N:] -= x[N:].mean()
        if track is not None:
            ov = x[:N] + x[N:]
            if prev_overall is not None:
                track.append((w, float(np.mean(np.abs(ov - prev_overall)))))
            prev_overall = ov.copy()
    return preds


V2 = json.load(open('data/research/insession_v2_constants.json'))
PRIORS = {y: sp_prior(y) for y in TUNE}
GAMES = {y: season_games(y) for y in TUNE}
MKT = {y: market_chain(y, PRIORS[y], V2['hfa']) for y in TUNE}


def evaluate(cfg):
    per = {}
    for y in TUNE:
        p = run_season(GAMES[y], PRIORS[y], cfg, mkt=MKT[y])
        per[y] = np.mean([abs(a - b) for (w, a, b) in p if w >= 2])
    return np.mean(list(per.values())), per


base_v, base_per = evaluate(V2)
print(f'v2 baseline: {base_v:.3f}')
best, bestv, bestper = None, base_v, None
for m1 in (0.8, 1.0, 1.25):
    for m24 in (0.9, 1.0, 1.15):
        if m1 == 1.0 and m24 == 1.0:
            continue
        v, per = evaluate(dict(V2, m1=m1, m24=m24))
        tag = f'm1={m1} m24={m24}: {v:.3f}'
        if v < bestv:
            best, bestv, bestper = dict(m1=m1, m24=m24), v, per
            tag += '  <-- best'
        print(tag)
if best and base_v - bestv >= 0.02 and sum(1 for y in TUNE if bestper[y] < base_per[y]) >= 3:
    print(f'ADOPT {best} ({bestv:.3f})')
else:
    print(f'NO ADOPTION — v2 stands (best {bestv:.3f} vs {base_v:.3f}); '
          f'endogenous schedule adequate at current power')

track = []
run_season(GAMES[2023], PRIORS[2023], V2, mkt=MKT[2023], track=track)
print('\nrealized aggressiveness (2023, mean |weekly overall change| per team):')
print('  ' + ' '.join(f'wk{w}:{d:.2f}' for w, d in track))
