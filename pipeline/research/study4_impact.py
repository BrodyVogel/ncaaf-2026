#!/usr/bin/env python3
"""Study 4 pro-forma: does the validated global retention correction (w' = w + 0.0591,
matched-tape arm only) change the 2026 board? The adjudication machinery consumed formula
values through WITHIN-GROUP RANK percentiles (full_pct) and cell-demeaned gaps (dg), so a
near-monotone recalibration should be nearly invisible. This measures exactly how nearly.
NO grades are changed."""
import csv, json, os, re, glob, unicodedata
import numpy as np
from collections import defaultdict

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BETA = 0.0591
def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())
GRPS = ['QB', 'RB', 'WRTE', 'OL', 'DL', 'LB', 'DB']
POSMEAN = {'QB': 69.7, 'RB': 73.5, 'WRTE': 62.6, 'OL': 62.0, 'DL': 64.9, 'LB': 62.3, 'DB': 65.2}
K = {'QB': 230, 'RB': 110, 'WRTE': 190, 'OL': 595, 'DL': 290, 'LB': 630, 'DB': 1180}
WCAP = {'QB': 0.55, 'LB': 0.50}
FRB = {'QB': (58.1, 92.4), 'RB': (73.0, 12.0), 'WRTE': (61.0, 32.5), 'OL': (56.5, 76.6),
       'DL': (60.5, 50.3), 'LB': (58.8, 31.1), 'DB': (62.7, 46.8)}
C2G = {'SEC': 'SEC', 'American Athletic': 'AAC', 'ACC': 'ACC', 'Big Ten': 'B10', 'Big 12': 'B12',
       'Conference USA': 'CUSA', 'FBS Independents': 'IND', 'Mid-American': 'MAC',
       'Mountain West': 'MWC', 'Pac-12': 'PAC', 'Sun Belt': 'SBC'}
OFF = json.load(open('data/backtest/conf_offsets_2021_2025.json'))['offsets']
P4G = ['SEC', 'B10', 'B12', 'ACC']; G5G = ['AAC', 'CUSA', 'MAC', 'MWC', 'SBC']
P4MEAN = {u: sum(OFF[u].get(c, 0) for c in P4G) / 4 for u in GRPS}
G5MEAN = {u: sum(OFF[u].get(c, 0) for c in G5G) / 5 for u in GRPS}
def w_of(n, g): return min(n / (n + K[g]), WCAP.get(g, 1.0))

S = list(csv.DictReader(open('data/research/spine.csv')))
sp = {2024: defaultdict(list), 2025: defaultdict(list)}
for r in S:
    y = int(r['season'])
    if y in (2024, 2025): sp[y][norm(r['name'])].append(r)
rec26 = {}
for e in json.load(open('data/cfbd/recruiting_players/recruits_2026.json')):
    if e.get('rating'): rec26[norm(e.get('name', ''))] = float(e['rating'])
def find_row(nm, team_nk, origin):
    for y in (2025, 2024):
        cands = sp[y].get(nm, [])
        if not cands: continue
        if len(cands) == 1: return cands[0], y
        onk = norm(origin.split(':', 1)[1]) if origin.startswith('transfer:') else team_nk
        exact = [c for c in cands if c['team'] == onk or c['team'] == team_nk]
        if len(exact) >= 1: return exact[0], y
    return None, None

P4_26 = {'SEC', 'Big Ten', 'Big 12', 'ACC'}
meta, dossier = {}, {}
for gpath in glob.glob('snapshots/*/META.json'):
    tdir = gpath.split('/')[1]; m = json.load(open(gpath))
    meta[tdir] = dict(name=m['team'], conf=m.get('conference', '?'),
                      p4=(m.get('conference') in P4_26 or m['team'] == 'Notre Dame'))
for gpath in glob.glob('snapshots/*/grades.json'):
    tdir = gpath.split('/')[1]; g = json.load(open(gpath))
    for u, d in g['units'].items():
        dossier[(meta[tdir]['name'], u)] = d.get('v1_grade', d['grade'])

def build_units(beta):
    units = {}
    for tdir, mt in sorted(meta.items()):
        tnk = norm(mt['name']); is_ind = mt['conf'] == 'FBS Independents'
        ag = defaultdict(lambda: dict(fv=[], fw=[]))
        for r in csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')):
            u = r['unit'].strip().upper()
            if u not in GRPS: continue
            wt = 1.0 if str(r.get('slot', '1')).strip() == '1' else 0.33
            nm = norm(r['player']); cls = (r.get('class') or '').strip().upper()
            origin = (r.get('origin') or '').strip()
            row, yy = find_row(nm, tnk, origin)
            if is_ind: dterm = P4MEAN[u] if mt['p4'] else G5MEAN[u]
            else:
                dconf = 'MWC' if mt['conf'] == 'Pac-12' else C2G.get(mt['conf'], 'IND')
                dterm = OFF[u].get(dconf, 0)
            val = None
            if row is not None:
                g = float(row['grade']); v = float(row['vol'])
                if yy == 2024: v *= 0.5
                p4_from = bool(int(row['p4'])); p4_to = mt['p4']
                jump = -3.54 if (not p4_from and p4_to) else (1.45 if (p4_from and not p4_to) else 0.0)
                w = w_of(v, u) + beta                      # <-- the correction (matched-tape arm only)
                val = POSMEAN[u] + w * (g - POSMEAN[u]) + jump + dterm
            elif cls == 'FR' and not origin.startswith('transfer:') and nm in rec26:
                b0, sl = FRB[u]
                val = b0 + sl * (rec26[nm] - 0.861) + dterm
            if val is not None:
                ag[u]['fv'].append(val); ag[u]['fw'].append(wt)
        for u, a in ag.items():
            if a['fw']:
                units[(mt['name'], u)] = dict(conf=mt['conf'],
                                              full=float(np.average(a['fv'], weights=a['fw'])))
    # within-group rank percentiles
    for u in GRPS:
        sub = [(k, v) for k, v in units.items() if k[1] == u]
        vals = np.array([v['full'] for _, v in sub]); order = vals.argsort().argsort()
        for (k, v), p in zip(sub, 100.0 * order / (len(sub) - 1)): v['pct'] = p
    # cell-demeaned dg
    def cellkey(conf, u): return ('MWC+P12' if conf in ('Pac-12', 'Mountain West') else conf, u)
    cm = defaultdict(list)
    for (tm, u), v in units.items():
        d = dossier.get((tm, u))
        if d is None or v['conf'] == 'FBS Independents': continue
        cm[cellkey(v['conf'], u)].append(v['pct'] - d)
    cmm = {c: float(np.mean(x)) for c, x in cm.items()}
    dg = {}
    for (tm, u), v in units.items():
        d = dossier.get((tm, u))
        if d is None or v['conf'] == 'FBS Independents': continue
        dg[(tm, u)] = (v['pct'] - d) - cmm[cellkey(v['conf'], u)]
    return units, dg

base_u, base_dg = build_units(0.0)
corr_u, corr_dg = build_units(BETA)

keys = sorted(set(base_dg) & set(corr_dg))
dd = np.array([corr_dg[k] - base_dg[k] for k in keys])
print(f"units compared: {len(keys)} | mean |d(dg)| {np.abs(dd).mean():.3f} pctile pts | max {np.abs(dd).max():.2f}")
flips = [(k, base_dg[k], corr_dg[k]) for k in keys
         if (abs(base_dg[k]) > 8) != (abs(corr_dg[k]) > 8)]
print(f"trigger-status flips (|dg|>8 boundary): {len(flips)}")
for k, b, c in sorted(flips, key=lambda z: -abs(z[2] - z[1]))[:15]:
    print(f"   {k[0]:22s} {k[1]:4s} dg {b:+6.2f} -> {c:+6.2f}")
# rank movement
rk = np.array([corr_u[k]['pct'] - base_u[k]['pct'] for k in keys])
print(f"rank percentile movement: mean |d| {np.abs(rk).mean():.3f} | >2 pts: {(np.abs(rk) > 2).sum()} units | max {np.abs(rk).max():.2f}")
big = sorted(keys, key=lambda k: -abs(corr_u[k]['pct'] - base_u[k]['pct']))[:8]
for k in big:
    print(f"   {k[0]:22s} {k[1]:4s} pct {base_u[k]['pct']:5.1f} -> {corr_u[k]['pct']:5.1f}")
