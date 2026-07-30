#!/usr/bin/env python3
"""S12: coach track-record persistence — all registered legs.
Per PREREGISTRATION_S12_2026-07-31.md (bars on unseen legs only)."""
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


miss, spp = {}, {}
for y in range(2021, 2026):
    pre = rd(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv', 'sp_plus_overall')
    fin = rd(f'data/backtest/sp_final/SP+_{y}_final.csv', 'final_overall')
    for t in pre:
        if t in fin:
            miss[(y, t)] = fin[t] - pre[t]; spp[(y, t)] = pre[t]
hc = {}
for y in range(2021, 2026):
    for c in json.load(open(f'data/cfbd/2026-07-12/coaches_{y}.json')):
        nm = (c.get('firstName', '') + ' ' + c.get('lastName', '')).strip()
        for s in c.get('seasons', []):
            hc[(s.get('year'), norm(s['school']))] = nm
cm = defaultdict(list)   # coach -> [(y, t, miss)]
for (y, t), m in sorted(miss.items()):
    co = hc.get((y, t))
    if co:
        cm[co].append((y, t, m))
rp = {}
for y in range(2022, 2026):
    for e in json.load(open(f'data/cfbd/2026-07-12/returning_{y}.json')):
        ks = [k for k in e if 'percent' in k.lower()]
        v = e.get('percentPPA', e.get(ks[0]) if ks else None)
        if v is not None:
            rp[(y, norm(e['team']))] = float(v)
P4C = ('SEC', 'Big Ten', 'Big 12', 'ACC')
conf_by = {}
for y in range(2021, 2026):
    for r in json.load(open(f'data/cfbd/2026-07-12/records_{y}.json')):
        if r.get('classification') == 'fbs':
            conf_by[(y, norm(r['team']))] = r.get('conference')
rpre = {(int(r['year']), r['team']): float(r['R_pre'])
        for r in csv.DictReader(open('data/research/s8b_panel.csv'))}

rows = []
for (y, t), m in miss.items():
    if y < 2022:
        continue
    co = hc.get((y, t))
    if not co or (y, t) not in rp:
        continue
    hist = [(yy, tt, mm) for (yy, tt, mm) in cm[co] if yy < y]
    if not hist:
        continue
    pms = [mm for _, _, mm in hist]
    newteam = int(not any(tt == t for _, tt, _ in hist))
    prev_class_p4 = None
    if newteam:
        last = max(hist)
        prev_class_p4 = int(conf_by.get((last[0], last[1])) in P4C or last[1] == 'notredame')
    rows.append(dict(
        y=y, t=t, coach=co, miss=m, sp=spp[(y, t)], pm=float(np.mean(pms)),
        n_prior=len(pms), samesign=int(len(pms) >= 2 and (all(x > 0 for x in pms) or all(x < 0 for x in pms))),
        newteam=newteam, prev_p4=prev_class_p4,
        cur_g5=int(not (conf_by.get((y, t)) in P4C or t == 'notredame')),
        team_prior=miss.get((y - 1, t), np.nan),
        newhc=int(hc.get((y - 1, t)) != co), rp=rp[(y, t)],
        rpre=rpre.get((y, t), np.nan)))
print(f'panel n={len(rows)}')


def ols(X, y):
    M = np.column_stack([np.ones(len(y))] + X)
    b, *_ = np.linalg.lstsq(M, y, rcond=None)
    r = y - M @ b
    cov = (r @ r / (len(y) - M.shape[1])) * np.linalg.pinv(M.T @ M)
    return b, b / np.sqrt(np.diag(cov))


def col(k):
    return np.array([r[k] for r in rows], float)


Y, SP, PM, RP_, NH, TP = col('miss'), col('sp'), col('pm'), col('rp'), col('newhc'), col('team_prior')
YR = col('y')

print('\n===== S12-A INTEGRITY: miss ~ sp + rp + newHC + team_prior + PM =====')
m = ~np.isnan(TP)
b, t = ols([SP[m], RP_[m], NH[m], TP[m], PM[m]], Y[m])
print(f'n={int(m.sum())}  PM {b[5]:+.3f} (t {t[5]:+.2f}) | team_prior {b[4]:+.3f} (t {t[4]:+.2f}) | rp {b[2]:+.2f} (t {t[2]:+.2f})')
signs = []
for y in (2022, 2023, 2024, 2025):
    mm = m & (YR != y)
    bb, tt = ols([SP[mm], RP_[mm], NH[mm], TP[mm], PM[mm]], Y[mm])
    signs.append(bb[5] > 0)
    print(f'  LOYO drop {int(y)}: PM {bb[5]:+.3f} (t {tt[5]:+.2f})')
passA = t[5] >= 2 and all(signs)
print(f'S12-A: {"PASS" if passA else "FAIL"}')
RB = col('rpre')
m2 = m & ~np.isnan(RB)
b2, t2 = ols([SP[m2], RP_[m2], NH[m2], TP[m2], RB[m2], PM[m2]], Y[m2])
print(f'robustness +R_pre (n={int(m2.sum())}): PM {b2[6]:+.3f} (t {t2[6]:+.2f}) | R_pre {b2[5]:+.3f} (t {t2[5]:+.2f})')

print('\n===== S12-B SHAPE =====')
PMp, PMn = np.maximum(PM, 0), np.minimum(PM, 0)
b, t = ols([SP, PMp, PMn], Y)
print(f'asymmetry: PM+ {b[2]:+.3f} (t {t[2]:+.2f}) | PM- {b[3]:+.3f} (t {t[3]:+.2f})')
b, t = ols([SP, PM, PM * np.abs(PM)], Y)
s3, s10 = b[2] + b[3] * 3, b[2] + b[3] * 10
print(f'tails: PM {b[2]:+.3f} (t {t[2]:+.2f}) + PM|PM| {b[3]:+.4f} (t {t[3]:+.2f}) -> slope@|3| {s3:+.3f}, @|10| {s10:+.3f}')

print('\n===== S12-C ONSET =====')
NP, SS = col('n_prior'), col('samesign')
for lab, msk in (('n=1', NP == 1), ('n=2 same-sign', (NP == 2) & (SS == 1)),
                 ('n=2 mixed', (NP == 2) & (SS == 0)), ('n>=3', NP >= 3)):
    if msk.sum() < 25:
        print(f'  {lab:14s} n={int(msk.sum())} (too thin)')
        continue
    bb, tt = ols([SP[msk], PM[msk]], Y[msk])
    print(f'  {lab:14s} n={int(msk.sum()):3d}  PM {bb[2]:+.3f} (t {tt[2]:+.2f})')

print('\n===== S12-D NUANCE =====')
NT = col('newteam').astype(bool)
bb, tt = ols([SP[NT], PM[NT]], Y[NT])
print(f'switchers (n={int(NT.sum())}): PM {bb[2]:+.3f} (t {tt[2]:+.2f})')
G5 = col('cur_g5')
b, t = ols([SP, PM, PM * G5], Y)
print(f'PM x G5(current): base {b[2]:+.3f} (t {t[2]:+.2f}) | xG5 {b[3]:+.3f} (t {t[3]:+.2f})')
dn = NT & (col('prev_p4') == 1) & (G5 == 1)
if dn.sum() >= 10:
    bb, tt = ols([SP[dn], PM[dn]], Y[dn])
    print(f'stepped DOWN P4->G5 (n={int(dn.sum())}): PM {bb[2]:+.3f} (t {tt[2]:+.2f})')
else:
    print(f'stepped DOWN P4->G5: n={int(dn.sum())} — insufficient')

print('\n===== S12-E WIN-TOTAL IMPACT (SBD 2022-24, lambda=0.164 frozen) =====')
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
    if y not in games_cache:
        games_cache[y] = json.load(open(f'data/cfbd/2026-07-12/games_{y}_regular.json'))
    w = 0
    for g in games_cache[y]:
        h, a = norm(g['homeTeam']), norm(g['awayTeam'])
        if tk not in (h, a) or g.get('homePoints') is None:
            continue
        mine = g['homePoints'] if tk == h else g['awayPoints']
        their = g['awayPoints'] if tk == h else g['homePoints']
        w += int(mine > their)
    return w


pm_by = {(r['y'], r['t']): r['pm'] for r in rows}
res = {'c': [], 'k': []}
zone = {'c': [0, 0], 'k': [0, 0]}
for y in (2022, 2023, 2024):
    pre = rd(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv', 'sp_plus_overall')
    adj = {t: pre[t] + 0.164 * pm_by.get((y, t), 0.0) for t in pre}
    for r in csv.DictReader(open(f'data/win_totals/sbd_historical/sbd_{y}.csv')):
        tk = AL.get(norm(r['team']), norm(r['team']))
        if tk not in pre:
            continue
        line = float(r['line']); W = wins(tk, y)
        for key, rat in (('c', pre), ('k', adj)):
            e = sched_exp(tk, y, rat)
            res[key].append(abs(e - W))
            if abs(e - line) >= 1.0 and W != line:
                zone[key][0] += int((e > line) == (W > line)); zone[key][1] += 1
mc, mk = np.mean(res['c']), np.mean(res['k'])
zc = zone['c'][0] / zone['c'][1] if zone['c'][1] else float('nan')
zk = zone['k'][0] / zone['k'][1] if zone['k'][1] else float('nan')
print(f'MAE consensus {mc:.3f} -> +coach {mk:.3f}  ({"improves" if mk < mc else "WORSE"})')
print(f'|d|>=1 zone: consensus {100*zc:.1f}% (n={zone["c"][1]}) -> +coach {100*zk:.1f}% (n={zone["k"][1]})')
print(f'S12-E: {"PASS" if (mk < mc and zk >= zc - 0.05) else "FAIL"}')
