#!/usr/bin/env python3
"""S18: FCS-influx as a market factor + cluster transfers.
Per PREREGISTRATION_S18_2026-08-02.md."""
import csv, glob, json, math, os, re, unicodedata
from collections import defaultdict
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


AL = {'connecticut': 'uconn'}
POSGRP = {'QB': 'QB', 'HB': 'skill', 'FB': 'skill', 'WR': 'skill', 'TE': 'skill',
          'T': 'trench', 'G': 'trench', 'C': 'trench', 'DI': 'trench', 'ED': 'trench',
          'LB': 'back7', 'CB': 'back7', 'S': 'back7'}

# ---- FCS school set from games files (classification == 'fcs') ----
FCS_SCHOOLS = set()
for y in range(2021, 2026):
    for g in json.load(open(f'data/cfbd/2026-07-12/games_{y}_regular.json')):
        for side in ('home', 'away'):
            if g.get(f'{side}Classification') == 'fcs':
                FCS_SCHOOLS.add(norm(g[f'{side}Team']))
print(f'FCS school set: {len(FCS_SCHOOLS)}')

# ---- FCS tape loader (grades + games + position + team) ----
def load_fcs(y):
    out = {}
    for fn in sorted(glob.glob(f'data/pff_history/fcs/*_{y}.csv')):
        if 'special_teams' in fn:
            continue
        for r in csv.DictReader(open(fn)):
            nm = norm(r.get('player') or '')
            g = r.get('grades_defense') if 'defense' in fn else r.get('grades_offense')
            try:
                g = float(g); gc = float(r.get('player_game_count') or 0)
            except (TypeError, ValueError):
                continue
            pos = (r.get('position') or '').upper()
            if nm and (nm not in out or gc > out[nm][1]):
                out[nm] = (g, gc, pos)
    return out


def load_fbs(y):
    if y < 2025:
        base, files = f'data/pff_history/{y}', [f'defense_summary_{y}.csv', f'offense_blocking_{y}.csv', f'passing_summary_{y}.csv', f'receiving_summary_{y}.csv', f'rushing_summary_{y}.csv']
    else:
        base, files = 'data/pff', ['PFF_defense_summary.csv', 'PFF_offense_blocking.csv', 'PFF_passing_summary.csv', 'PFF_receiving_summary.csv', 'PFF_rushing_summary.csv']
    out = {}
    for fn in files:
        p = os.path.join(base, fn)
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(open(p)):
            nm = norm(r.get('player') or '')
            g = r.get('grades_defense') if 'defense' in fn else r.get('grades_offense')
            try:
                g = float(g); gc = float(r.get('player_game_count') or 0)
            except (TypeError, ValueError):
                continue
            if nm and (nm not in out or gc > out[nm][1]):
                out[nm] = (g, gc)
    return out


# ---- S17 pair panel + LOYO fold curves (leave ORIGIN year out) ----
FCS_Y = {y: load_fcs(y) for y in range(2021, 2026)}
FBS_Y = {y: load_fbs(y) for y in range(2021, 2026)}
pairs = []
for y in (2021, 2022, 2023, 2024):
    for nm, (g, gc, pos) in FCS_Y[y].items():
        if gc < 6 or nm in FBS_Y[y] or nm not in FBS_Y[y + 1]:
            continue
        g2, gc2 = FBS_Y[y + 1][nm]
        if gc2 < 6:
            continue
        pairs.append(dict(y=y, nm=nm, gp=g, gn=g2, grp=POSGRP.get(pos, 'other')))
print(f'S17 pair panel rebuilt: n={len(pairs)}')


def fit_curve(excl_year):
    sub = [p for p in pairs if p['y'] != excl_year]
    GN = np.array([p['gn'] for p in sub]); GP = np.array([p['gp'] for p in sub])
    dums = [np.array([float(p['grp'] == g) for p in sub]) for g in ('skill', 'trench', 'back7')]
    M = np.column_stack([np.ones(len(sub)), GP] + dums)
    b, *_ = np.linalg.lstsq(M, GN, rcond=None)
    return b


CURVES = {y: fit_curve(y) for y in (2021, 2022, 2023, 2024)}
CURVES[2025] = fit_curve(None)   # full fit for the 2026 freeze


def curve_proj(b, g, grp):
    d = [float(grp == 'skill'), float(grp == 'trench'), float(grp == 'back7')]
    return b[0] + b[1] * g + b[2] * d[0] + b[3] * d[1] + b[4] * d[2]


# ---- team-year intake metrics from portal files ----
def rdmap(path, col):
    return {AL.get(r['norm_key'], r['norm_key']): float(r[col]) for r in csv.DictReader(open(path))}


FBS_TEAMS = {}
for y in range(2022, 2026):
    FBS_TEAMS[y] = set(rdmap(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv', 'sp_plus_overall'))

metrics = defaultdict(lambda: dict(N=0, Q=0.0, Q55=0.0, Q61=0.0, groups=defaultdict(int)))
for y in range(2022, 2026):
    fcs_prev = FCS_Y[y - 1]
    b = CURVES[y - 1]
    for e in json.load(open(f'data/cfbd/2026-07-12/portal_{y}.json')):
        o = norm(e.get('origin')); d = AL.get(norm(e.get('destination')), norm(e.get('destination')))
        if o not in FCS_SCHOOLS or d not in FBS_TEAMS[y]:
            continue
        m = metrics[(y, d)]
        m['N'] += 1
        m['groups'][o] += 1
        nm = norm((e.get('firstName') or '') + (e.get('lastName') or ''))
        if nm in fcs_prev and fcs_prev[nm][1] >= 4:
            g, gc, pos = fcs_prev[nm]
            cp = curve_proj(b, g, POSGRP.get(pos, 'other'))
            m['Q'] += cp - 58
            m['Q55'] += cp - 55
            m['Q61'] += cp - 61

nz = sum(1 for v in metrics.values() if v['N'] > 0)
tape = sum(1 for v in metrics.values() if abs(v['Q']) > 0)
print(f'team-years with FCS intake: {nz} | with tape-covered Q: {tape}')

# ---- panel assembly ----
P4C = ('SEC', 'Big Ten', 'Big 12', 'ACC')
conf_by = {}
for y in range(2021, 2026):
    for r in json.load(open(f'data/cfbd/2026-07-12/records_{y}.json')):
        if r.get('classification') == 'fbs':
            conf_by[(y, norm(r['team']))] = r.get('conference')
hc = {}
for y in range(2021, 2026):
    for c in json.load(open(f'data/cfbd/2026-07-12/coaches_{y}.json')):
        nmc = (c.get('firstName', '') + ' ' + c.get('lastName', '')).strip()
        for s in c.get('seasons', []):
            hc[(s.get('year'), norm(s['school']))] = nmc
rp = {}
for y in range(2022, 2026):
    for e in json.load(open(f'data/cfbd/2026-07-12/returning_{y}.json')):
        v = e.get('percentPPA')
        if v is not None:
            rp[(y, norm(e['team']))] = float(v)

rows = []
for y in range(2022, 2026):
    pre = rdmap(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv', 'sp_plus_overall')
    fin = rdmap(f'data/backtest/sp_final/SP+_{y}_final.csv', 'final_overall')
    for t in pre:
        if t not in fin or (y, t) not in rp:
            continue
        m = metrics.get((y, t), dict(N=0, Q=0.0, Q55=0.0, Q61=0.0, groups={}))
        clust = max(m['groups'].values()) if m['groups'] else 0
        rows.append(dict(y=y, t=t, miss=fin[t] - pre[t], sp=pre[t], rp=rp[(y, t)],
                         nh=int(hc.get((y - 1, t)) != hc.get((y, t))),
                         g5=int(not (conf_by.get((y, t)) in P4C or t == 'notredame')),
                         N=m['N'], Q=m['Q'], Q55=m['Q55'], Q61=m['Q61'],
                         clust2=int(clust >= 2), clustn=max(0, clust - 1)))
print(f'panel n={len(rows)}')


def ols(X, y):
    M = np.column_stack([np.ones(len(y))] + X)
    b, *_ = np.linalg.lstsq(M, y, rcond=None)
    r = y - M @ b
    cov = (r @ r / (len(y) - M.shape[1])) * np.linalg.pinv(M.T @ M)
    return b, b / np.sqrt(np.diag(cov))


def col(k):
    return np.array([r[k] for r in rows], float)


Y, SP, RP_, NH, G5 = col('miss'), col('sp'), col('rp'), col('nh'), col('g5')
Q, N_, YR = col('Q'), col('N'), col('y')
C2, CN = col('clust2'), col('clustn')

print('\n===== S18-A: miss ~ sp + rp + newHC + G5 + Q =====')
b, t = ols([SP, RP_, NH, G5, Q], Y)
print(f'Q {b[5]:+.4f} (t {t[5]:+.2f}) | rp {b[2]:+.2f} (t {t[2]:+.2f}) | newHC {b[3]:+.2f} | G5 {b[4]:+.2f}')
signs = []
for yy in (2022, 2023, 2024, 2025):
    m = YR != yy
    bb, tt = ols([SP[m], RP_[m], NH[m], G5[m], Q[m]], Y[m])
    signs.append(np.sign(bb[5]) == np.sign(b[5]))
    print(f'  LOYO drop {yy}: Q {bb[5]:+.4f} (t {tt[5]:+.2f})')
passA = abs(t[5]) >= 2 and sum(signs) >= 3
print(f'S18-A: {"PASS" if passA else "FAIL"}')
lamA = b[5]
for lab, qq in (('Q55', col('Q55')), ('Q61', col('Q61'))):
    bb, tt = ols([SP, RP_, NH, G5, qq], Y)
    print(f'  sensitivity {lab}: {bb[5]:+.4f} (t {tt[5]:+.2f})')
b2, t2 = ols([SP, RP_, NH, G5, Q, Q * G5], Y)
print(f'  G5 x Q interaction: base {b2[5]:+.4f} (t {t2[5]:+.2f}) | xG5 {b2[6]:+.4f} (t {t2[6]:+.2f})')
bn, tn = ols([SP, RP_, NH, G5, N_], Y)
print(f'  N-variant: {bn[5]:+.4f} (t {tn[5]:+.2f})')

print('\n===== S18-C: Q vs N horse race =====')
bh, th = ols([SP, RP_, NH, G5, Q, N_], Y)
print(f'jointly: Q {bh[5]:+.4f} (t {th[5]:+.2f}) | N {bh[6]:+.4f} (t {th[6]:+.2f})')

print('\n===== S18-E: cluster (panel) =====')
be, te = ols([SP, RP_, NH, G5, Q, C2], Y)
print(f'clustered dummy {be[6]:+.3f} (t {te[6]:+.2f})')
signsE = []
for yy in (2022, 2023, 2024, 2025):
    m = YR != yy
    bb, tt = ols([SP[m], RP_[m], NH[m], G5[m], Q[m], C2[m]], Y[m])
    signsE.append(np.sign(bb[6]) == np.sign(be[6]))
be2, te2 = ols([SP, RP_, NH, G5, Q, CN], Y)
print(f'cluster count (CLUST-1) {be2[6]:+.3f} (t {te2[6]:+.2f}) | dummy LOYO {sum(signsE)}/4')
passE = abs(te[6]) >= 2 and sum(signsE) >= 3
print(f'S18-E: {"PASS" if passE else "FAIL"}')

print('\n===== S18-F: cluster (player level) =====')
# companions: same origin -> same destination, same cycle, among ALL portal FCS intake
port_groups = defaultdict(int)
for y in range(2022, 2026):
    for e in json.load(open(f'data/cfbd/2026-07-12/portal_{y}.json')):
        o = norm(e.get('origin')); d = AL.get(norm(e.get('destination')), norm(e.get('destination')))
        if o in FCS_SCHOOLS:
            port_groups[(y, o, d)] += 1
# map each pair to its portal record (origin/destination) via name
port_by_name = {}
for y in range(2022, 2026):
    for e in json.load(open(f'data/cfbd/2026-07-12/portal_{y}.json')):
        nm = norm((e.get('firstName') or '') + (e.get('lastName') or ''))
        port_by_name[(y, nm)] = (norm(e.get('origin')), AL.get(norm(e.get('destination')), norm(e.get('destination'))))
resid, comp, pyr = [], [], []
for p in pairs:
    yy = p['y'] + 1
    pr = port_by_name.get((yy, p['nm']))
    if pr is None or pr[0] not in FCS_SCHOOLS:
        continue
    b = CURVES[p['y']]
    r = p['gn'] - curve_proj(b, p['gp'], p['grp'])
    resid.append(r); comp.append(int(port_groups[(yy, pr[0], pr[1])] >= 2)); pyr.append(p['y'])
resid, comp, pyr = np.array(resid), np.array(comp, float), np.array(pyr)
print(f'player-level n={len(resid)} | with companion: {int(comp.sum())}')
bf, tf = ols([comp], resid)
print(f'companion effect on realized-vs-curve: {bf[1]:+.2f} grade pts (t {tf[1]:+.2f})')
signsF = []
for yy in (2021, 2022, 2023, 2024):
    m = pyr != yy
    bb, tt = ols([comp[m]], resid[m])
    signsF.append(np.sign(bb[1]) == np.sign(bf[1]))
passF = abs(tf[1]) >= 2 and sum(signsF) >= 3
print(f'LOYO {sum(signsF)}/4 -> S18-F: {"PASS" if passF else "FAIL"}')
# dose curve
for k in (1, 2, 3):
    mk = np.array([port_groups[(p['y'] + 1, port_by_name[(p['y'] + 1, p['nm'])][0], port_by_name[(p['y'] + 1, p['nm'])][1])] if (p['y'] + 1, p['nm']) in port_by_name else 0 for p in pairs])
# simpler dose report on the resid subset
sizes = np.array([port_groups[(int(y) + 1, port_by_name[(int(y) + 1, nm)][0], port_by_name[(int(y) + 1, nm)][1])]
                  for y, nm in zip(pyr, [p['nm'] for p in pairs if (p['y'] + 1, p['nm']) in port_by_name and port_by_name[(p['y'] + 1, p['nm'])][0] in FCS_SCHOOLS])])
for lo, hi, lab in ((1, 1, 'solo'), (2, 2, 'pair'), (3, 99, '3+')):
    mk = (sizes >= lo) & (sizes <= hi)
    if mk.sum():
        print(f'  {lab:5s}: n={int(mk.sum()):3d} mean resid {resid[mk].mean():+.2f}')

print('\n===== S18-B: board test (SBD 2022-24, lambda from A frozen) =====')
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


qmap = {(r['y'], r['t']): r['Q'] for r in rows}
res = {'c': [], 'k': []}
zone = {'c': [0, 0], 'k': [0, 0]}
for y in (2022, 2023, 2024):
    pre = rdmap(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv', 'sp_plus_overall')
    adj = {t: pre[t] + lamA * qmap.get((y, t), 0.0) for t in pre}
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
mc, mk_ = np.mean(res['c']), np.mean(res['k'])
zc = zone['c'][0] / zone['c'][1] if zone['c'][1] else float('nan')
zk = zone['k'][0] / zone['k'][1] if zone['k'][1] else float('nan')
print(f'MAE {mc:.3f} -> {mk_:.3f} ({"improves" if mk_ < mc else "WORSE"}) | zone {100*zc:.1f}% (n={zone["c"][1]}) -> {100*zk:.1f}% (n={zone["k"][1]})')
print(f'S18-B: {"PASS" if (mk_ < mc and zk >= zc - 0.05) else "FAIL"}')

# ===== S18-D: 2026 freeze =====
m26 = defaultdict(lambda: dict(N=0, Q=0.0, groups=defaultdict(int)))
fcs25 = FCS_Y[2025]
b26 = CURVES[2025]
teams26 = set(rdmap('data/anchors/SP+_2026preseason_2026-07-12.csv', 'sp_plus_overall'))
for e in json.load(open('data/cfbd/2026-07-12/portal_2026.json')):
    o = norm(e.get('origin')); d = AL.get(norm(e.get('destination')), norm(e.get('destination')))
    if o not in FCS_SCHOOLS or d not in teams26:
        continue
    mm = m26[d]
    mm['N'] += 1
    mm['groups'][o] += 1
    nm = norm((e.get('firstName') or '') + (e.get('lastName') or ''))
    if nm in fcs25 and fcs25[nm][1] >= 4:
        g, gc, pos = fcs25[nm]
        mm['Q'] += curve_proj(b26, g, POSGRP.get(pos, 'other')) - 58
with open('data/research/s18_fcs2026.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['team', 'N', 'Q', 'clust_max'])
    for d in sorted(m26):
        mm = m26[d]
        w.writerow([d, mm['N'], round(mm['Q'], 2), max(mm['groups'].values()) if mm['groups'] else 0])
qs = sorted(((mm['Q'], d, mm['N']) for d, mm in m26.items()), reverse=True)
print(f'\n2026 freeze: {len(m26)} teams -> s18_fcs2026.csv | top Q: ' + ', '.join(f'{d}({q:+.0f},N{n})' for q, d, n in qs[:8]))
print('bottom Q:', ', '.join(f'{d}({q:+.0f})' for q, d, n in qs[-4:]))
EOF_MARKER = None
