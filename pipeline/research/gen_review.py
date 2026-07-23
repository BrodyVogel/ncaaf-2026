#!/usr/bin/env python3
"""Generate the per-case review file for all 256 blended units.
Each case: metrics header, the unit's dossier section (last matching), per-player
formula detail. Output /tmp/review_cases.txt + /tmp/review_index.csv."""
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
S = list(csv.DictReader(open('data/research/spine.csv')))
sp = {2024: defaultdict(list), 2025: defaultdict(list)}
for r in S:
    y = int(r['season'])
    if y in (2024, 2025): sp[y][norm(r['name'])].append(r)
rec26 = {}
for e in json.load(open('data/cfbd/recruiting_players/recruits_2026.json')):
    if e.get('rating'): rec26[norm(e.get('name', ''))] = float(e['rating'])
def w_of(n, g): return min(n / (n + K[g]), WCAP.get(g, 1.0))
def find_row(nm, team_nk, origin):
    for y in (2025, 2024):
        cands = sp[y].get(nm, [])
        if not cands: continue
        if len(cands) == 1: return cands[0], y
        onk = norm(origin.split(':', 1)[1]) if origin.startswith('transfer:') else team_nk
        exact = [c for c in cands if c['team'] == onk or c['team'] == team_nk]
        if len(exact) >= 1: return exact[0], y
    return None, None
t2d = {}
for gpath in glob.glob('snapshots/*/META.json'):
    m = json.load(open(gpath)); t2d[m['team']] = gpath.split('/')[1]

PINNED = {('Duke', 'QB'), ('Michigan', 'QB'), ('Wisconsin', 'QB'),
          ('Louisiana Tech', 'WRTE'), ('Tulane', 'RB')}
amend = {(a['team'], a['unit']): a for a in json.load(open('/tmp/amendments.json'))}
cases = []
for r in csv.DictReader(open('/tmp/sweep_proposals.csv')):
    if r['dg'] == '' or r['final'] == r['dossier'] or r['unit'] not in GRPS: continue
    cases.append(r)
cases.sort(key=lambda x: (x['team'], x['unit']))

def dossier_section(tdir, unit):
    txt = open(f'snapshots/{tdir}/unit_dossiers.md').read().split('\n')
    pat = re.compile(rf'^## {re.escape(unit)}\s*[—-]')
    starts = [i for i, ln in enumerate(txt) if pat.match(ln)]
    if not starts: return ['(no dossier section found)']
    i = starts[-1]
    out = [txt[i]]
    for ln in txt[i+1:]:
        if ln.startswith('## ') or ln.startswith('---'): break
        out.append(ln)
    return out[:16]

out = []
idx = []
for n_, b in enumerate(cases, 1):
    team, unit = b['team'], b['unit']
    tdir = t2d[team]; tnk = norm(team)
    cur = json.load(open(f'snapshots/{tdir}/grades.json'))['units'][unit]
    status = 'PINNED-MANUAL' if (team, unit) in PINNED else ('AMENDED' if (team, unit) in amend else 'policy')
    am = amend.get((team, unit))
    hdr = (f"=== [{n_}/{len(cases)}] {team} {unit} | dossier {b['dossier']} -> current {cur['grade']} "
           f"| sweep dg{b['dg']} | {status}" + (f" (starter-view: {am['tag']})" if am else '') +
           f" | note: {b['formula_note'][:80]}")
    lines = [hdr, "FORMULA:"]
    for rr in csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')):
        if rr['unit'].strip().upper() != unit: continue
        nm = norm(rr['player']); origin = (rr.get('origin') or '').strip()
        row, yy = find_row(nm, tnk, origin)
        cls = (rr.get('class') or '').strip().upper()
        if row is not None:
            g = float(row['grade']); v = float(row['vol']); ve = v * 0.5 if yy == 2024 else v
            lines.append(f"  {rr['player'][:26]:26s} {cls:3s} {origin[:24]:24s} {g:5.1f}/{v:4.0f} ({yy}) w={w_of(ve,unit):.2f} -> {POSMEAN[unit]+w_of(ve,unit)*(g-POSMEAN[unit]):.1f}")
        elif cls == 'FR' and nm in rec26:
            lines.append(f"  {rr['player'][:26]:26s} FR  comp {rec26[nm]:.3f}")
        else:
            lines.append(f"  {rr['player'][:26]:26s} {cls:3s} {origin[:24]:24s} UNMATCHED")
    lines.append("DOSSIER:")
    lines += ['  ' + l for l in dossier_section(tdir, unit)]
    out.append('\n'.join(lines))
    idx.append(dict(n=n_, team=team, unit=unit, dossier=b['dossier'], current=cur['grade'], status=status))
open('/tmp/review_cases.txt', 'w').write('\n\n'.join(out))
with open('/tmp/review_index.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['n', 'team', 'unit', 'dossier', 'current', 'status'])
    w.writeheader()
    for i in idx: w.writerow(i)
print(f"{len(cases)} cases, {sum(len(o.splitlines()) for o in out)} lines -> /tmp/review_cases.txt")
