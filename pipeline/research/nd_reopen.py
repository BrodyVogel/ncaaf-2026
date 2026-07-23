#!/usr/bin/env python3
"""Notre Dame re-open: recompute both pro forma arms with the Independents fix
(dest scale term = P4 pool mean, matching the dossier's own 'IND cell NOT applied' call).
Per-player detail + re-percentile vs existing field + P4-pooled demeaned gap."""
import csv, json, os, re, unicodedata
import numpy as np
from collections import defaultdict

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
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
P4G = ['SEC', 'B10', 'B12', 'ACC']
P4MEAN = {u: sum(OFF[u].get(c, 0) for c in P4G) / 4 for u in GRPS}
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

team_nk = norm('Notre Dame')
rows = list(csv.DictReader(open('snapshots/Notre_Dame/roster_two_deep.csv')))
agg = defaultdict(lambda: {'v1': [], 'v2': [], 'w': [], 'cov': [0, 0]})
print('=== per-player (v2 fixed = shrink + jump + P4-pool scale) ===')
for r in rows:
    u = r['unit'].strip().upper()
    if u not in GRPS: continue
    wt = 1.0 if str(r.get('slot', '1')).strip() == '1' else 0.33
    a = agg[u]; a['cov'][1] += 1
    nm = norm(r['player']); cls = (r.get('class') or '').strip().upper()
    origin = (r.get('origin') or '').strip()
    row, yy = find_row(nm, team_nk, origin)
    if row is not None:
        g = float(row['grade']); v = float(row['vol'])
        if yy == 2024: v *= 0.5
        p4_from = bool(int(row['p4']))
        jump = -3.54 if not p4_from else 0.0     # ND counts as P4 dest
        pm = POSMEAN[u]
        v2 = pm + w_of(v, u) * (g - pm) + jump + P4MEAN[u]
        v1 = g + P4MEAN[u] if row['conf'] == 'FBS Independents' else g + OFF[u].get(C2G.get(row['conf'], 'IND'), 0)
        a['v1'].append(v1); a['v2'].append(v2); a['w'].append(wt); a['cov'][0] += 1
        print(f"{u:5s} s{r['slot']} {r['player']:24s} {g:5.1f}/{v:4.0f}({yy}) w={w_of(v,u):.2f} jump={jump:+.1f} -> v2 {v2:.1f} (v1 {v1:.1f})")
    elif cls == 'FR' and not origin.startswith('transfer:') and nm in rec26:
        b0, sl = FRB[u]
        v2 = b0 + sl * (rec26[nm] - 0.861) + P4MEAN[u]
        a['v1'].append(POSMEAN[u]); a['v2'].append(v2); a['w'].append(wt); a['cov'][0] += 1
        print(f"{u:5s} s{r['slot']} {r['player']:24s} FR comp={rec26[nm]:.3f} -> v2 {v2:.1f}")
    else:
        print(f"{u:5s} s{r['slot']} {r['player']:24s} UNMATCHED ({cls}, {origin})")

# unit aggregates + re-percentile against the existing field
units_field = list(csv.DictReader(open('outputs/proforma_v2_2026.csv')))
print('\n=== ND unit aggregates, re-percentiled vs field ===')
print('unit  v2raw   v2_pct(old->new)  dossier  raw_gap  P4mean_gap  demeaned_gap')
# rebuild the underlying v2 raw values per unit from the proforma script would be needed;
# instead percentile ND's fixed value against OTHER teams' v2 raw distribution recomputed:
# cheaper: rank vs stored v2_pct is impossible from pct alone -> recompute whole field quickly? No:
# use the stored per-unit percentile of OTHER teams as an empirical CDF anchored by their v2 raw...
# Simplest correct: re-run the proforma aggregation for ALL teams with ND fixed. Do that.
import glob
P = json.load(open('outputs/win_totals_payload.json'))
P4_26 = {'SEC', 'Big Ten', 'Big 12', 'ACC'}
meta = {}
for gpath in glob.glob('snapshots/*/grades.json'):
    tdir = gpath.split('/')[1]
    g = json.load(open(gpath)); m = json.load(open(f'snapshots/{tdir}/META.json'))
    meta[tdir] = dict(name=m['team'], conf=m.get('conference', '?'),
                      p4=(m.get('conference') in P4_26 or m['team'] == 'Notre Dame'),
                      grades={u: g['units'][u]['grade'] for u in g['units']})
units = []
for tdir, mt in sorted(meta.items()):
    tnk = norm(mt['name'])
    rws = list(csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')))
    ag = defaultdict(lambda: {'v2': [], 'w': []})
    is_ind = mt['conf'] == 'FBS Independents'
    for r in rws:
        u = r['unit'].strip().upper()
        if u not in GRPS: continue
        wt = 1.0 if str(r.get('slot', '1')).strip() == '1' else 0.33
        nm = norm(r['player']); cls = (r.get('class') or '').strip().upper()
        origin = (r.get('origin') or '').strip()
        row, yy = find_row(nm, tnk, origin)
        if is_ind:
            dterm = {u2: (P4MEAN[u2] if mt['p4'] else sum(OFF[u2].get(c, 0) for c in ['AAC','CUSA','MAC','MWC','SBC'])/5) for u2 in GRPS}[u]
        else:
            dconf = 'MWC' if mt['conf'] == 'Pac-12' else C2G.get(mt['conf'], 'IND')
            dterm = OFF[u].get(dconf, 0)
        if row is not None:
            g = float(row['grade']); v = float(row['vol'])
            if yy == 2024: v *= 0.5
            p4_from = bool(int(row['p4'])); p4_to = mt['p4']
            jump = -3.54 if (not p4_from and p4_to) else (1.45 if (p4_from and not p4_to) else 0.0)
            pm = POSMEAN[u]
            ag[u]['v2'].append(pm + w_of(v, u) * (g - pm) + jump + dterm); ag[u]['w'].append(wt)
        elif cls == 'FR' and not origin.startswith('transfer:') and nm in rec26:
            b0, sl = FRB[u]
            ag[u]['v2'].append(b0 + sl * (rec26[nm] - 0.861) + dterm); ag[u]['w'].append(wt)
    for u, a in ag.items():
        if a['w']:
            units.append(dict(team=mt['name'], conf=mt['conf'], unit=u,
                              v2=float(np.average(a['v2'], weights=np.array(a['w']))),
                              dossier=mt['grades'].get(u)))
for u in GRPS:
    sub = [r for r in units if r['unit'] == u]
    vals = np.array([r['v2'] for r in sub]); order = vals.argsort().argsort()
    for r, pct in zip(sub, 100.0 * order / (len(sub) - 1)): r['v2_pct'] = pct
# gaps: g = v2_pct - dossier; P4 pooled mean per unit
for u in GRPS:
    p4gaps = [r['v2_pct'] - r['dossier'] for r in units
              if r['unit'] == u and r['dossier'] is not None and
              (r['conf'] in P4_26 or r['team'] == 'Notre Dame')]
    m = np.mean(p4gaps)
    nd = [r for r in units if r['unit'] == u and r['team'] == 'Notre Dame'][0]
    old = {'QB': 47.2, 'RB': 6.6, 'WRTE': 50.0, 'OL': 1.5, 'DL': 61.9, 'LB': 48.1, 'DB': 80.3}[u]
    gap = nd['v2_pct'] - nd['dossier']
    print(f"{u:5s} {nd['v2']:5.1f}   {old:5.1f} -> {nd['v2_pct']:5.1f}   {nd['dossier']:3d}     "
          f"{gap:+6.1f}   {m:+6.1f}      {gap - m:+6.1f}")
