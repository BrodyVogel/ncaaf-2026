#!/usr/bin/env python3
"""Reconciliation of the 256 sweep blends via dual-aggregation robustness.
For every FBS team x unit, compute v2 value two ways:
  FULL     the sweep's aggregation (all two-deep rows, slot-1 = 1.0, others 0.33)
  STARTER  slot-1 rows only (strips FR-prior/backup drag and depth-parse blindness)
Percentile + conference-demeaned gap under each; dg_robust = sign-preserving min
magnitude (0 if the two views disagree in sign). Re-derive each blend's move with the
same policy (DB 1/3, LB .40, else .50; info<0.20 halved; academy halved; cap +/-8).
The 5 pinned manual overrides are kept. Outputs an amendment list; appends AMENDED
rows to data/research/adjudication_v2.csv (last-write-wins for the regen script)."""
import csv, json, os, re, glob, unicodedata
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
P4G = ['SEC', 'B10', 'B12', 'ACC']; G5G = ['AAC', 'CUSA', 'MAC', 'MWC', 'SBC']
P4MEAN = {u: sum(OFF[u].get(c, 0) for c in P4G) / 4 for u in GRPS}
G5MEAN = {u: sum(OFF[u].get(c, 0) for c in G5G) / 5 for u in GRPS}
ACADEMY = {'Army', 'Navy', 'Air Force'}
BLENDW = {'DB': 1/3, 'LB': 0.40}
PINNED = {('Duke', 'QB'), ('Michigan', 'QB'), ('Wisconsin', 'QB'),
          ('Louisiana Tech', 'WRTE'), ('Tulane', 'RB')}
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
meta = {}
for gpath in glob.glob('snapshots/*/META.json'):
    tdir = gpath.split('/')[1]
    m = json.load(open(gpath))
    meta[tdir] = dict(name=m['team'], conf=m.get('conference', '?'),
                      p4=(m.get('conference') in P4_26 or m['team'] == 'Notre Dame'))

# v1 dossier grades = pre-adjudication values (from git-preserved v1_grade or current)
dossier = {}
for gpath in glob.glob('snapshots/*/grades.json'):
    tdir = gpath.split('/')[1]; g = json.load(open(gpath))
    for u, d in g['units'].items():
        dossier[(meta[tdir]['name'], u)] = d.get('v1_grade', d['grade'])

units = {}
for tdir, mt in sorted(meta.items()):
    tnk = norm(mt['name'])
    is_ind = mt['conf'] == 'FBS Independents'
    ag = defaultdict(lambda: dict(fv=[], fw=[], sv=[], sw=[], info=0.0, allw=0.0))
    for r in csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')):
        u = r['unit'].strip().upper()
        if u not in GRPS: continue
        s1 = str(r.get('slot', '1')).strip() == '1'
        wt = 1.0 if s1 else 0.33
        a = ag[u]; a['allw'] += wt
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
            val = POSMEAN[u] + w_of(v, u) * (g - POSMEAN[u]) + jump + dterm
            a['info'] += wt * w_of(v, u)
        elif cls == 'FR' and not origin.startswith('transfer:') and nm in rec26:
            b0, sl = FRB[u]
            val = b0 + sl * (rec26[nm] - 0.861) + dterm
            a['info'] += wt * 0.25
        if val is not None:
            a['fv'].append(val); a['fw'].append(wt)
            if s1: a['sv'].append(val); a['sw'].append(wt)
    for u, a in ag.items():
        if not a['fw']: continue
        units[(mt['name'], u)] = dict(
            conf=mt['conf'],
            full=float(np.average(a['fv'], weights=a['fw'])),
            starter=float(np.average(a['sv'], weights=a['sw'])) if a['sw'] else None,
            info=a['info'] / a['allw'] if a['allw'] else 0.0)

def pctile(field, key):
    for u in GRPS:
        sub = [(k, v) for k, v in units.items() if k[1] == u and v.get(key) is not None]
        vals = np.array([v[key] for _, v in sub]); order = vals.argsort().argsort()
        for (k, v), p in zip(sub, 100.0 * order / (len(sub) - 1)): v[key + '_pct'] = p
pctile(units, 'full'); pctile(units, 'starter')

def cellkey(conf, u): return ('MWC+P12' if conf in ('Pac-12', 'Mountain West') else conf, u)
cm = {'full': defaultdict(list), 'starter': defaultdict(list)}
for (tm, u), v in units.items():
    if v['conf'] == 'FBS Independents': continue
    d = dossier.get((tm, u))
    if d is None: continue
    if v.get('full_pct') is not None: cm['full'][cellkey(v['conf'], u)].append(v['full_pct'] - d)
    if v.get('starter_pct') is not None: cm['starter'][cellkey(v['conf'], u)].append(v['starter_pct'] - d)
cm = {k: {c: float(np.mean(x)) for c, x in d.items()} for k, d in cm.items()}

blends = [r for r in csv.DictReader(open('/tmp/sweep_proposals.csv'))
          if r['dg'] != '' and r['final'] != r['dossier'] and r['unit'] in GRPS]
amend, keep, no_starter = [], [], []
for b in blends:
    key = (b['team'], b['unit'])
    if key in PINNED:
        keep.append((b, 'pinned manual override')); continue
    v = units[key]; d = int(b['dossier'])
    dg_f = (v['full_pct'] - d) - cm['full'][cellkey(v['conf'], b['unit'])]
    if v.get('starter_pct') is None:
        no_starter.append(b); dg_r = dg_f; tag = 'no starter matched — full-agg only'
    else:
        dg_s = (v['starter_pct'] - d) - cm['starter'][cellkey(v['conf'], b['unit'])]
        if np.sign(dg_f) != np.sign(dg_s): dg_r, tag = 0.0, f'views disagree (full {dg_f:+.1f} / starter {dg_s:+.1f}) — no move'
        elif abs(dg_s) < abs(dg_f): dg_r, tag = dg_s, f'starter view smaller ({dg_s:+.1f} vs full {dg_f:+.1f})'
        else: dg_r, tag = dg_f, f'full view smaller-or-equal ({dg_f:+.1f} vs starter {dg_s:+.1f})'
    w = BLENDW.get(b['unit'], 0.50)
    if v['info'] < 0.20: w *= 0.5
    if b['team'] in ACADEMY: w *= 0.5
    move = int(np.clip(round(w * dg_r), -8, 8))
    new_final = int(np.clip(d + move, 1, 99))
    old_final = int(b['final'])
    if new_final != old_final:
        amend.append(dict(team=b['team'], unit=b['unit'], dossier=d, old=old_final,
                          final=new_final, tag=tag, dg_full=round(dg_f, 1)))
    else:
        keep.append((b, tag))

print(f'blends {len(blends)} | unchanged {len(keep)} | AMENDED {len(amend)} | no-starter fallback {len(no_starter)}')
mag = [abs(a['old'] - a['final']) for a in amend]
if amend: print(f'amendment sizes: mean {np.mean(mag):.1f}, max {max(mag)} | toward dossier: {sum(1 for a in amend if abs(a["final"]-a["dossier"])<abs(a["old"]-a["dossier"]))}/{len(amend)}')
print('\n=== AMENDMENTS ===')
for a in sorted(amend, key=lambda x: -abs(x['old'] - x['final'])):
    print(f"{a['team']:22s} {a['unit']:4s} dossier {a['dossier']:3d}: {a['old']:3d} -> {a['final']:3d}  [{a['tag']}]")
with open('/tmp/amendments.json', 'w') as f: json.dump(amend, f, indent=1)
