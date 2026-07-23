#!/usr/bin/env python3
"""False-agreement screen over every sweep ACCEPT (units not blended, not hand-done).
For each: dg_full (as swept), dg_rank (within-cell rank disagreement — immune to
ceiling-squeeze and offset-axis artifacts), dg_starter, info, plus flags:
  UNMSTAR   an UNMATCHED roster row whose notes cite a PFF grade >= 73 (missing star)
  DUALQB    QB unit whose dossier notes cite rush/dual-threat value (passing-facet blind)
  RANKDIS   |dg_rank| >= 30 cell-percentile points while the swept |dg_full| <= 8
  STARTDIS  starter-view |dg| > 12 while full <= 8 (composition-masked)
Queue = any flag. Also emits the 4<|dg|<=8 near-trigger band and a seeded random-40
sample of clean deep accepts (|dg|<=4, no flags). Nothing is changed by this script."""
import csv, json, os, re, glob, unicodedata, random
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
    tdir = gpath.split('/')[1]; m = json.load(open(gpath))
    meta[tdir] = dict(name=m['team'], conf=m.get('conference', '?'),
                      p4=(m.get('conference') in P4_26 or m['team'] == 'Notre Dame'))
# v1 dossier grades from git-preserved v1_grade
dossier = {}
for gpath in glob.glob('snapshots/*/grades.json'):
    tdir = gpath.split('/')[1]; g = json.load(open(gpath))
    for u, d in g['units'].items():
        dossier[(meta[tdir]['name'], u)] = d.get('v1_grade', d['grade'])

units = {}
GRADE_RE = re.compile(r'(\d\d\.\d)')
for tdir, mt in sorted(meta.items()):
    tnk = norm(mt['name']); is_ind = mt['conf'] == 'FBS Independents'
    ag = defaultdict(lambda: dict(fv=[], fw=[], sv=[], sw=[], info=0.0, allw=0.0,
                                  unmstar=False, notes=[]))
    for r in csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')):
        u = r['unit'].strip().upper()
        if u not in GRPS: continue
        s1 = str(r.get('slot', '1')).strip() == '1'
        wt = 1.0 if s1 else 0.33
        a = ag[u]; a['allw'] += wt
        nm = norm(r['player']); cls = (r.get('class') or '').strip().upper()
        origin = (r.get('origin') or '').strip(); note = (r.get('notes') or '')
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
        else:
            gs = [float(x) for x in GRADE_RE.findall(note)]
            if any(x >= 73 for x in gs): a['unmstar'] = True
        a['notes'].append(note)
        if val is not None:
            a['fv'].append(val); a['fw'].append(wt)
            if s1: a['sv'].append(val); a['sw'].append(wt)
    for u, a in ag.items():
        if not a['fw']: continue
        units[(mt['name'], u)] = dict(
            conf=mt['conf'],
            full=float(np.average(a['fv'], weights=a['fw'])),
            starter=float(np.average(a['sv'], weights=a['sw'])) if a['sw'] else None,
            info=a['info'] / a['allw'] if a['allw'] else 0.0,
            unmstar=a['unmstar'],
            dualqb=(u == 'QB' and any(('rush' in n.lower() or 'dual' in n.lower() or 'legs' in n.lower())
                                      for n in a['notes'])))
def pctile(key):
    for u in GRPS:
        sub = [(k, v) for k, v in units.items() if k[1] == u and v.get(key) is not None]
        vals = np.array([v[key] for _, v in sub]); order = vals.argsort().argsort()
        for (k, v), p in zip(sub, 100.0 * order / (len(sub) - 1)): v[key + '_pct'] = p
pctile('full'); pctile('starter')
def cellkey(conf, u): return ('MWC+P12' if conf in ('Pac-12', 'Mountain West') else conf, u)
cm = {'full': defaultdict(list), 'starter': defaultdict(list)}
cells = defaultdict(list)
for (tm, u), v in units.items():
    d = dossier.get((tm, u))
    if d is None or v['conf'] == 'FBS Independents': continue
    ck = cellkey(v['conf'], u)
    cells[ck].append((tm, d, v.get('full_pct'), v.get('starter_pct')))
    if v.get('full_pct') is not None: cm['full'][ck].append(v['full_pct'] - d)
    if v.get('starter_pct') is not None: cm['starter'][ck].append(v['starter_pct'] - d)
cmm = {k: {c: float(np.mean(x)) for c, x in dd.items()} for k, dd in cm.items()}
# within-cell rank pcts
rank_dg = {}
for ck, members in cells.items():
    n = len(members)
    if n < 4: continue
    ds = np.array([m[1] for m in members]); fs = np.array([m[2] if m[2] is not None else np.nan for m in members])
    dr = ds.argsort().argsort() * 100.0 / (n - 1)
    fr = np.argsort(np.argsort(np.nan_to_num(fs, nan=-1))) * 100.0 / (n - 1)
    for (tm, d, fp, sp_), dpct, fpct in zip(members, dr, fr):
        if fp is not None: rank_dg[(tm, ck[1])] = float(fpct - dpct)

# which pairs are DONE (hand rounds + blends + re-read)? -> anything already carrying a
# re-read/manual row. Build from log: pairs whose LAST row reason mentions re-read/manual/
# blend/split/reopen etc. Simpler: done = pairs in review_index (256) + hand set.
done = set()
for r in csv.DictReader(open('/tmp/review_index.csv')): done.add((r['team'], r['unit']))
HAND = set()
for r in csv.DictReader(open('data/research/adjudication_v2.csv')):
    if r['unit'] in ('ALL', 'FLAG'):
        if r['unit'] == 'ALL':
            for u in GRPS + ['ST']: HAND.add((r['team'], u))
        continue
    if 're-read' in r['reason'] or 'T3' in r['reason'] or 'blend' in r['reason'].lower(): continue
    HAND.add((r['team'], r['unit']))

accepts = []
for r in csv.DictReader(open('/tmp/sweep_proposals.csv')):
    if r['unit'] not in GRPS: continue
    if r['dg'] == '' or r['final'] != r['dossier']: continue   # accepts/holds only
    key = (r['team'], r['unit'])
    if key in done or key in HAND: continue
    v = units.get(key)
    if v is None: continue
    d = int(r['dossier']); dgf = float(r['dg'])
    dgr = rank_dg.get(key)
    dgs = None
    if v.get('starter_pct') is not None:
        dgs = (v['starter_pct'] - d) - cmm['starter'][cellkey(v['conf'], r['unit'])]
    flags = []
    if v['unmstar']: flags.append('UNMSTAR')
    if v['dualqb']: flags.append('DUALQB')
    if dgr is not None and abs(dgr) >= 30 and abs(dgf) <= 8: flags.append('RANKDIS')
    if dgs is not None and abs(dgs) > 12 and abs(dgf) <= 8: flags.append('STARTDIS')
    accepts.append(dict(team=r['team'], unit=r['unit'], dossier=d, dg=dgf,
                        dg_rank=round(dgr, 0) if dgr is not None else '',
                        dg_starter=round(dgs, 1) if dgs is not None else '',
                        info=round(v['info'], 2), flags='+'.join(flags),
                        reason=r['reason']))
flagged = [a for a in accepts if a['flags']]
band = [a for a in accepts if not a['flags'] and 4 < abs(a['dg']) <= 8]
deep = [a for a in accepts if not a['flags'] and abs(a['dg']) <= 4]
random.seed(20260723)
sample = random.sample(deep, min(40, len(deep)))
print(f"accepts screened {len(accepts)} | FLAGGED {len(flagged)} | near-band(4-8) {len(band)} | deep clean {len(deep)} (sample 40)")
from collections import Counter
print('flag mix:', dict(Counter(f for a in flagged for f in a['flags'].split('+'))))
json.dump(dict(flagged=flagged, band=band, sample=sample), open('/tmp/accept_queue.json', 'w'), indent=0)
print('queue written to /tmp/accept_queue.json')
