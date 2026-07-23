#!/usr/bin/env python3
"""Reconciliation screen over every sweep blend (final != dossier).
Flags the five artifact signatures the |dg|>20 review surfaced:
  SOLO       exactly one matched contributor drives the unit
  STALE24    >=50% of matched info-weight comes from 2024 (look-through) rows
  UNM_HEAVY  unmatched share of total slot-weight >= 0.25 (a slot-1 miss = 1.0/1.66)
  INFO_EDGE  unit info in [0.10, 0.25) — barely cleared the uninformative bar
  PARSE      roster anomalies: combined names ('/'), missing slot, empty class
Plus BET flag for the 14 bet teams. Prints per-player detail for every flagged case."""
import csv, json, os, re, glob, unicodedata
from collections import defaultdict

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())
GRPS = ['QB', 'RB', 'WRTE', 'OL', 'DL', 'LB', 'DB']
POSMEAN = {'QB': 69.7, 'RB': 73.5, 'WRTE': 62.6, 'OL': 62.0, 'DL': 64.9, 'LB': 62.3, 'DB': 65.2}
K = {'QB': 230, 'RB': 110, 'WRTE': 190, 'OL': 595, 'DL': 290, 'LB': 630, 'DB': 1180}
WCAP = {'QB': 0.55, 'LB': 0.50}
BETS = {'UConn', 'Tulsa', 'Oregon State', 'Bowling Green', 'Liberty', 'Arizona State',
        'Kennesaw State', 'Illinois', 'West Virginia', 'East Carolina', "Hawai'i",
        'Florida', 'UCF', 'Pittsburgh'}
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
t2d = {}
for gpath in glob.glob('snapshots/*/META.json'):
    m = json.load(open(gpath)); t2d[m['team']] = gpath.split('/')[1]

blends = [r for r in csv.DictReader(open('/tmp/sweep_proposals.csv'))
          if r['dg'] != '' and r['final'] != r['dossier'] and r['unit'] in GRPS]
print(f'{len(blends)} sweep blends to screen')
flagged, clean = [], []
for b in blends:
    tdir = t2d[b['team']]; tnk = norm(b['team'])
    detail, mi = [], []
    slotw_m = slotw_u = 0.0; info_m = info24 = 0.0; parse = False
    for r in csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')):
        if r['unit'].strip().upper() != b['unit']: continue
        wt = 1.0 if str(r.get('slot', '1')).strip() == '1' else 0.33
        pl = r['player']; cls = (r.get('class') or '').strip().upper()
        if '/' in pl or not r.get('slot') or not cls: parse = True
        nm = norm(pl); origin = (r.get('origin') or '').strip()
        row, yy = find_row(nm, tnk, origin)
        if row is not None:
            g = float(row['grade']); v = float(row['vol']); ve = v * 0.5 if yy == 2024 else v
            wv = w_of(ve, b['unit'])
            slotw_m += wt; info_m += wt * wv
            if yy == 2024: info24 += wt * wv
            detail.append(f"{pl} {g:.1f}/{v:.0f}({yy}) w={wv:.2f}")
        elif cls == 'FR' and not origin.startswith('transfer:') and nm in rec26:
            slotw_m += wt; info_m += wt * 0.25
            detail.append(f"{pl} FR{rec26[nm]:.3f}")
        else:
            slotw_u += wt
            detail.append(f"{pl} UNMATCHED")
    tot = slotw_m + slotw_u
    info = info_m / tot if tot else 0
    n_real = sum(1 for d in detail if 'UNMATCHED' not in d)
    flags = []
    if n_real == 1: flags.append('SOLO')
    if info_m > 0 and info24 / info_m >= 0.5: flags.append('STALE24')
    if tot and slotw_u / tot >= 0.25: flags.append('UNM_HEAVY')
    if 0.10 <= info < 0.25: flags.append('INFO_EDGE')
    if parse: flags.append('PARSE')
    if b['team'] in BETS: flags.append('BET')
    rec = dict(b, flags='+'.join(flags), info=round(info, 2), detail=' | '.join(detail))
    (flagged if flags else clean).append(rec)

print(f'flagged {len(flagged)} | clean {len(clean)}')
from collections import Counter
fc = Counter(f for r in flagged for f in r['flags'].split('+'))
print('flag counts:', dict(fc))
print('\n=== FLAGGED (for hand review) ===')
for r in sorted(flagged, key=lambda x: -abs(float(x['dg']))):
    print(f"[{r['flags']:>24s}] {r['team']:20s} {r['unit']:4s} {r['dossier']:>3s}->{r['final']:>3s} dg{float(r['dg']):+6.1f} info{r['info']:.2f}")
    print(f"     {r['detail'][:150]}")
with open('/tmp/reconcile_flagged.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(flagged[0].keys()))
    w.writeheader()
    for r in flagged: w.writerow(r)
# clean sample for QC: every 9th
import itertools
print('\n=== CLEAN SAMPLE (QC, every 9th) ===')
for r in clean[::9]:
    print(f"{r['team']:20s} {r['unit']:4s} {r['dossier']:>3s}->{r['final']:>3s} dg{float(r['dg']):+6.1f} info{r['info']:.2f} | {r['detail'][:110]}")
