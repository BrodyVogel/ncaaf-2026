#!/usr/bin/env python3
"""Per-player formula detail for TEAM UNIT pairs given on argv: 'Team:UNIT' ..."""
import csv, json, os, re, sys, glob, unicodedata
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
for arg in sys.argv[1:]:
    team, unit = arg.rsplit(':', 1)
    tdir = t2d[team]; tnk = norm(team)
    print(f"--- {team} {unit} ---")
    for r in csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')):
        if r['unit'].strip().upper() != unit: continue
        sl_ = r.get('slot', '?')
        nm = norm(r['player']); origin = (r.get('origin') or '').strip()
        row, yy = find_row(nm, tnk, origin)
        cls = (r.get('class') or '').strip().upper()
        if row is not None:
            g = float(row['grade']); v = float(row['vol'])
            ve = v * 0.5 if yy == 2024 else v
            print(f"  s{sl_} {r['player']:24s} {cls:3s} {origin[:28]:28s} tape {g:5.1f}/{v:4.0f} ({yy}, conf {row['conf'][:12]}) w={w_of(ve,unit):.2f} shrunk={POSMEAN[unit]+w_of(ve,unit)*(g-POSMEAN[unit]):.1f}")
        elif cls == 'FR' and nm in rec26:
            b0, sl = FRB[unit]
            print(f"  s{sl_} {r['player']:24s} FR  comp {rec26[nm]:.4f} -> prior {b0+sl*(rec26[nm]-0.861):.1f}")
        else:
            print(f"  s{sl_} {r['player']:24s} {cls:3s} {origin[:28]:28s} UNMATCHED")
        note = (r.get('notes') or '')[:150]
        print(f"      note: {note}")
