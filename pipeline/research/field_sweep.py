#!/usr/bin/env python3
"""Tier-3 field sweep. Recomputes the pro forma field WITH the Independents fix,
computes within-conference demeaned gaps (Pac-12 pooled with MWC; IND teams excluded
— both already fully adjudicated), and proposes a verdict for every (team,unit) not
already in data/research/adjudication_v2.csv:
  |dg| <= 4              -> Tier-3 verified accept (hold)
  |dg| > 4               -> blend toward formula: DB 1/3, LB 0.40, others 0.50,
                            halved if coverage < 0.5, hold if no matched players;
                            move capped +/-8, grades clamped [1,99]
  ST                     -> hold (no formula arm; news/media-days already integrated)
Writes PROPOSALS to /tmp/sweep_proposals.csv + a review ledger of big cases to stdout.
Nothing is appended to the adjudication log by this script."""
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
for gpath in glob.glob('snapshots/*/grades.json'):
    tdir = gpath.split('/')[1]
    g = json.load(open(gpath)); m = json.load(open(f'snapshots/{tdir}/META.json'))
    meta[tdir] = dict(name=m['team'], conf=m.get('conference', '?'),
                      p4=(m.get('conference') in P4_26 or m['team'] == 'Notre Dame'),
                      grades={u: g['units'][u]['grade'] for u in g['units']},
                      confs={u: g['units'][u].get('confidence', 'M') for u in g['units']})

units = []
for tdir, mt in sorted(meta.items()):
    tnk = norm(mt['name'])
    rws = list(csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')))
    ag = defaultdict(lambda: {'v2': [], 'w': [], 'cov': [0, 0]})
    is_ind = mt['conf'] == 'FBS Independents'
    for r in rws:
        u = r['unit'].strip().upper()
        if u not in GRPS: continue
        wt = 1.0 if str(r.get('slot', '1')).strip() == '1' else 0.33
        a = ag[u]; a['cov'][1] += 1
        nm = norm(r['player']); cls = (r.get('class') or '').strip().upper()
        origin = (r.get('origin') or '').strip()
        row, yy = find_row(nm, tnk, origin)
        if is_ind:
            dterm = P4MEAN[u] if mt['p4'] else G5MEAN[u]
        else:
            dconf = 'MWC' if mt['conf'] == 'Pac-12' else C2G.get(mt['conf'], 'IND')
            dterm = OFF[u].get(dconf, 0)
        if row is not None:
            g = float(row['grade']); v = float(row['vol'])
            if yy == 2024: v *= 0.5
            p4_from = bool(int(row['p4'])); p4_to = mt['p4']
            jump = -3.54 if (not p4_from and p4_to) else (1.45 if (p4_from and not p4_to) else 0.0)
            pm = POSMEAN[u]
            a['v2'].append(pm + w_of(v, u) * (g - pm) + jump + dterm); a['w'].append(wt); a['cov'][0] += 1
            a.setdefault('info', []).append(wt * w_of(v, u))
        elif cls == 'FR' and not origin.startswith('transfer:') and nm in rec26:
            b0, sl = FRB[u]
            a['v2'].append(b0 + sl * (rec26[nm] - 0.861) + dterm); a['w'].append(wt); a['cov'][0] += 1
            a.setdefault('info', []).append(wt * 0.25)   # S2b freshman-prior partial 0.266 ~ quarter-season trust
        else:
            a.setdefault('slotw_un', []).append(wt)
    for u in GRPS:
        a = ag.get(u)
        row = dict(team=mt['name'], conf=mt['conf'], unit=u,
                   dossier=mt['grades'].get(u), dconf_letter=mt['confs'].get(u, 'M'))
        if a and a['w']:
            row['v2'] = float(np.average(a['v2'], weights=np.array(a['w'])))
            row['cov'] = a['cov'][0] / max(a['cov'][1], 1)
            # unit information = matched volume-weight share over ALL slot weight (unmatched contribute 0)
            allw = sum(a['w']) + sum(a.get('slotw_un', []))
            row['info'] = sum(a.get('info', [])) / allw if allw else 0.0
        else:
            row['v2'] = None; row['cov'] = 0.0; row['info'] = 0.0
        units.append(row)

for u in GRPS:
    sub = [r for r in units if r['unit'] == u and r['v2'] is not None]
    vals = np.array([r['v2'] for r in sub]); order = vals.argsort().argsort()
    for r, pct in zip(sub, 100.0 * order / (len(sub) - 1)): r['v2_pct'] = pct

# demeaning cells: conf x unit; Pac-12 pooled with MWC; IND excluded
def cell(r): return ('MWC+P12' if r['conf'] in ('Pac-12', 'Mountain West') else r['conf'], r['unit'])
cellmean = defaultdict(list)
for r in units:
    if r['conf'] == 'FBS Independents' or r.get('v2_pct') is None or r['dossier'] is None: continue
    cellmean[cell(r)].append(r['v2_pct'] - r['dossier'])
cellmean = {k: float(np.mean(v)) for k, v in cellmean.items()}

# skip set from the log
done = set()
for r in csv.DictReader(open('data/research/adjudication_v2.csv')):
    if r['unit'] == 'ALL':
        for u in GRPS + ['ST']: done.add((r['team'], u))
    elif r['unit'] not in ('FLAG',):
        done.add((r['team'], r['unit']))

BLEND = {'DB': 1/3, 'LB': 0.40}
TRIGGER = 8.0        # ~1 SD of the demeaned gap (8.49 empirically); matches the manual
                     # rounds' de facto floor (smallest hand-blended |dg| was 8)
ACADEMY = {'Army', 'Navy', 'Air Force'}   # triple-option: PFF individual grades scheme-distorted
proposals = []
for tdir, mt in sorted(meta.items()):
    for u in GRPS + ['ST']:
        if (mt['name'], u) in done: continue
        dossier = mt['grades'].get(u); letter = mt['confs'].get(u, 'M')
        if u == 'ST':
            proposals.append(dict(team=mt['name'], unit=u, dossier=dossier,
                                  formula_note='no formula arm', final=dossier, conf=letter,
                                  reason='T3 hold; news/media-days integrated', dg=''))
            continue
        r = next(x for x in units if x['team'] == mt['name'] and x['unit'] == u)
        if r['v2'] is None or r['conf'] == 'FBS Independents':
            proposals.append(dict(team=mt['name'], unit=u, dossier=dossier,
                                  formula_note='no matched players — formula uninformative',
                                  final=dossier, conf=letter, reason='T3 hold; no formula info', dg=''))
            continue
        dg = (r['v2_pct'] - dossier) - cellmean[cell(r)]
        if abs(dg) <= TRIGGER:
            proposals.append(dict(team=mt['name'], unit=u, dossier=dossier,
                                  formula_note=f'dg{dg:+.1f}', final=dossier, conf=letter,
                                  reason='T3 verified accept' + ('' if abs(dg) <= 4 else ' (within 1SD noise band)'),
                                  dg=round(dg, 1)))
        elif r['info'] < 0.10:
            proposals.append(dict(team=mt['name'], unit=u, dossier=dossier,
                                  formula_note=f'dg{dg:+.1f} but unit info {r["info"]:.2f} — formula is prior-noise',
                                  final=dossier, conf=letter, reason='T3 hold; formula uninformative', dg=round(dg, 1)))
        else:
            w = BLEND.get(u, 0.50)
            covnote = ''
            if r['info'] < 0.20:
                w *= 0.5; covnote = f'; info {r["info"]:.2f} — blend halved'
            if mt['name'] in ACADEMY:
                w *= 0.5; covnote += '; option-scheme blind spot — blend halved'
            move = int(np.clip(round(w * dg), -8, 8))
            final = int(np.clip(dossier + move, 1, 99))
            proposals.append(dict(team=mt['name'], unit=u, dossier=dossier,
                                  formula_note=f'dg{dg:+.1f}{covnote}',
                                  final=final, conf=('M' if abs(move) >= 4 else letter),
                                  reason=('DB policy 1/3 blend' if u == 'DB' else
                                          'LB 0.4 blend' if u == 'LB' else '50/50 blend') if move else 'blend rounds to 0; hold',
                                  dg=round(dg, 1)))

with open('/tmp/sweep_proposals.csv', 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=['team', 'unit', 'dossier', 'formula_note', 'final', 'conf', 'reason', 'dg'])
    wr.writeheader()
    for p in proposals: wr.writerow(p)

nz = [p for p in proposals if p['dg'] != '' and p['final'] != p['dossier']]
big = [p for p in proposals if p['dg'] != '' and abs(p['dg']) > 10]
print(f"proposals {len(proposals)} | accepts/holds {len(proposals)-len(nz)} | blends {len(nz)} | |dg|>10 review cases {len(big)}")
print(f"\n=== |dg|>10 REVIEW LEDGER (sorted) ===")
for p in sorted(big, key=lambda x: -abs(x['dg'])):
    print(f"{p['team']:22s} {p['unit']:4s} {p['dossier']:3d} -> {p['final']:3d}  dg{p['dg']:+6.1f}  {p['formula_note']}")
print("\n=== blend count by unit ===")
bc = defaultdict(int)
for p in nz: bc[p['unit']] += 1
print(dict(bc))
print("\n=== cell means (formula-vs-dossier inflation by conf) ===")
for (c, u), m in sorted(cellmean.items()):
    if u == 'QB': print(f"{c:20s} QB {m:+6.1f}")
