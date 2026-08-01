#!/usr/bin/env python3
"""S15: level-conditioning of win-total error structure.
Per PREREGISTRATION_S15_2026-08-01.md."""
import csv, json, math, os, re, unicodedata
from collections import defaultdict
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


AL = {'connecticut': 'uconn'}


def rd(p, c):
    return {AL.get(r['norm_key'], r['norm_key']): float(r[c]) for r in csv.DictReader(open(p))}


P4C = ('SEC', 'Big Ten', 'Big 12', 'ACC')
conf_by = {}
for y in range(2021, 2026):
    for r in json.load(open(f'data/cfbd/2026-07-12/records_{y}.json')):
        if r.get('classification') == 'fbs':
            conf_by[(y, norm(r['team']))] = r.get('conference')


def is_g5(y, t):
    return int(not (conf_by.get((y, t)) in P4C or t == 'notredame'))


def ols(X, y):
    M = np.column_stack([np.ones(len(y))] + X)
    b, *_ = np.linalg.lstsq(M, y, rcond=None)
    r = y - M @ b
    dof = len(y) - M.shape[1]
    cov = (r @ r / dof) * np.linalg.pinv(M.T @ M)
    r2 = 1 - (r @ r) / ((y - y.mean()) @ (y - y.mean()))
    return b, b / np.sqrt(np.diag(cov)), r2


rows = []
for y in range(2021, 2026):
    pre = rd(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv', 'sp_plus_overall')
    fin = rd(f'data/backtest/sp_final/SP+_{y}_final.csv', 'final_overall')
    ranked = sorted(pre.values())
    for t in pre:
        if t not in fin:
            continue
        pct = np.searchsorted(ranked, pre[t]) / len(ranked)
        rows.append(dict(y=y, t=t, am=abs(fin[t] - pre[t]), pct=pct,
                         g5=is_g5(y, t), sp=pre[t]))
print(f'L1 panel n={len(rows)}')
Y = np.array([r['am'] for r in rows])
G = np.array([r['g5'] for r in rows], float)
P = np.array([r['pct'] for r in rows])
YR = np.array([r['y'] for r in rows])

print('\n===== S15-L1 |miss| ~ level =====')
b0, t0, r20 = ols([G], Y)
b1, t1, r21 = ols([G, P, P * P], Y)
print(f'binary:     G5 {b0[1]:+.3f} (t {t0[1]:+.2f})  R2 {r20:.4f}')
print(f'continuous: G5 {b1[1]:+.3f} (t {t1[1]:+.2f}) | pctl {b1[2]:+.3f} (t {t1[2]:+.2f}) | pctl^2 {b1[3]:+.3f} (t {t1[3]:+.2f})  R2 {r21:.4f}  dR2 {r21-r20:.4f}')
sig = [(i, tt) for i, tt in ((2, t1[2]), (3, t1[3])) if abs(tt) >= 2]
loyo_ok = 0
if sig:
    idx = sig[0][0]
    signs = []
    for yy in range(2021, 2026):
        m = YR != yy
        bb, _, _ = ols([G[m], P[m], P[m] * P[m]], Y[m])
        signs.append(np.sign(bb[idx]) == np.sign(b1[idx]))
    loyo_ok = sum(signs)
    print(f'LOYO on significant term: {loyo_ok}/5 same sign')
passL1 = bool(sig) and (r21 - r20) >= 0.01 and loyo_ok >= 4
print(f'S15-L1: {"PASS" if passL1 else "FAIL"} (bars: |t|>=2, dR2>=0.01, LOYO 4/5)')
m = G == 0
bp, tp, _ = ols([P[m], P[m] * P[m]], Y[m])
print(f'within-P4 slice (n={int(m.sum())}): pctl {bp[1]:+.3f} (t {tp[1]:+.2f}) | pctl^2 {bp[2]:+.3f} (t {tp[2]:+.2f})')
for lo, hi, lab in ((0, .2, 'bottom'), (.2, .4, ''), (.4, .6, 'middle'), (.6, .8, ''), (.8, 1.01, 'top')):
    mm = (P >= lo) & (P < hi)
    print(f'  pctl {lo:.1f}-{hi:.1f} {lab:6s}: mean|miss| {Y[mm].mean():.2f} (n={int(mm.sum())})')

# ---------- L2: zone bets by level ----------
games_cache = {}


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def sched_exp(tk, y, ratings):
    if y not in games_cache:
        games_cache[y] = json.load(open(f'data/cfbd/2026-07-12/games_{y}_regular.json'))
    ew = 0.0
    for g in games_cache[y]:
        h, a = norm(g['homeTeam']), norm(g['awayTeam'])
        if tk not in (h, a):
            continue
        opp = a if tk == h else h
        if opp not in ratings:
            ew += 0.95
            continue
        site = 0.0 if g.get('neutralSite') else (1.0 if tk == h else -1.0)
        ew += phi((ratings[tk] - ratings[opp] + 2.3 * site) / 13.5)
    return ew


def wins(tk, y):
    w = 0
    for g in games_cache[y]:
        h, a = norm(g['homeTeam']), norm(g['awayTeam'])
        if tk not in (h, a) or g.get('homePoints') is None:
            continue
        mine = g['homePoints'] if tk == h else g['awayPoints']
        their = g['awayPoints'] if tk == h else g['homePoints']
        w += int(mine > their)
    return w


bets = []
for y in (2022, 2023, 2024):
    pre = rd(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv', 'sp_plus_overall')
    ranked = sorted(pre.values())
    for r in csv.DictReader(open(f'data/win_totals/sbd_historical/sbd_{y}.csv')):
        tk = AL.get(norm(r['team']), norm(r['team']))
        if tk not in pre:
            continue
        line = float(r['line'])
        e = sched_exp(tk, y, pre)
        d = e - line
        if abs(d) < 1.0:
            continue
        W = wins(tk, y)
        if W == line:
            continue
        won = int((d > 0) == (W > line))
        bets.append(dict(y=y, t=tk, won=won, pct=np.searchsorted(ranked, pre[tk]) / len(ranked),
                         over=int(d > 0)))
print(f'\n===== S15-L2 zone bets by level (n={len(bets)}) =====')
BP = np.array([b['pct'] for b in bets])
BW = np.array([b['won'] for b in bets], float)
BY = np.array([b['y'] for b in bets])
terc = np.quantile(BP, [1 / 3, 2 / 3])
for lo, hi, lab in ((0, terc[0], 'low'), (terc[0], terc[1], 'mid'), (terc[1], 1.01, 'high')):
    mm = (BP >= lo) & (BP < hi)
    print(f'  {lab:4s} tercile: {100 * BW[mm].mean():.1f}% (n={int(mm.sum())})')


def logit_fit(X, y):
    b = np.zeros(X.shape[1] + 1)
    M = np.column_stack([np.ones(len(y)), X])
    for _ in range(50):
        p = 1 / (1 + np.exp(-M @ b))
        Wd = p * (1 - p)
        H = M.T @ (M * Wd[:, None]) + 1e-9 * np.eye(M.shape[1])
        b = b + np.linalg.solve(H, M.T @ (y - p))
    p = 1 / (1 + np.exp(-M @ b))
    Wd = p * (1 - p)
    cov = np.linalg.pinv(M.T @ (M * Wd[:, None]))
    return b, b / np.sqrt(np.diag(cov))


bl, tl = logit_fit(BP[:, None], BW)
print(f'logistic P(win) ~ pctl: slope {bl[1]:+.3f} (t {tl[1]:+.2f})')
signs = []
for yy in (2022, 2023, 2024):
    m = BY != yy
    bb, _ = logit_fit(BP[m][:, None], BW[m])
    signs.append(np.sign(bb[1]) == np.sign(bl[1]))
print(f'LOYO {sum(signs)}/3 same sign')
passL2 = abs(tl[1]) >= 2 and sum(signs) == 3
print(f'S15-L2: {"PASS" if passL2 else "FAIL"} (bars: |t|>=2, LOYO 3/3)')

print('\n===== S15-L3 overs/unders x tercile (report-only) =====')
for lo, hi, lab in ((0, terc[0], 'low'), (terc[0], terc[1], 'mid'), (terc[1], 1.01, 'high')):
    for ov, ovlab in ((1, 'overs'), (0, 'unders')):
        mm = (BP >= lo) & (BP < hi) & (np.array([b['over'] for b in bets]) == ov)
        if mm.sum():
            print(f'  {lab:4s} {ovlab:6s}: {100 * BW[mm].mean():.1f}% (n={int(mm.sum())})')
