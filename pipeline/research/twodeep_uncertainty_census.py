#!/usr/bin/env python3
"""Diagnostic (not a study): among players ON our 2026 two-deeps, how many have
eligibility/presence evidence we should call uncertain?

Classes for RETURNING two-deep players (origin contains 'return'):
  SAFE      roster_2025 class <= 3  (machine-confirmed eligible)
  FLAGGED   class >=4/None BUT dossier carries 'RETURNS (yr4 override, May-print)'
            (explicit human override, dated source)
  SILENT    class >=4/None (or name absent from roster_2025) and NO override tag
            (assumed returning without an explicit eligibility flag)
Arrivals: checked only for presence in portal_2026 feed (news-only adds counted).
"""
import csv, json, os, re, unicodedata
from collections import defaultdict

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


# roster_2025 index: (team_norm, name_norm) -> year;  also name-only per team set
roster = defaultdict(dict)
for p in json.load(open('data/cfbd/2026-07-12/roster_2025.json')):
    t = norm(p['team'])
    t = {'connecticut': 'uconn'}.get(t, t)
    nm = norm((p.get('firstName') or '') + (p.get('lastName') or ''))
    roster[t][nm] = p.get('year')

portal26 = set()
for e in json.load(open('data/cfbd/2026-07-12/portal_2026.json')):
    nm = norm((e.get('firstName') or '') + (e.get('lastName') or ''))
    portal26.add(nm)

HELD = {'UConn', 'Tulsa', 'Oregon_State', 'Bowling_Green', 'Liberty',
        'Arizona_State', 'Kennesaw_State', 'Illinois', 'West_Virginia',
        'East_Carolina', "Hawai'i", 'Florida', 'UCF', 'Pittsburgh',
        'Wisconsin', 'Buffalo', 'Nevada', 'Wake_Forest', 'Rutgers'}

DOSS_RE = re.compile(r'([A-Z][\w\'.\- ]+?)\s*\((\d+\.?\d*)/(\d+)\)\s*([A-Z]+[^;]*)')

tot = defaultdict(int)
held_rows, silent_rows = [], []
arr_tot = arr_nofeed = 0
missing_dirs = sorted(d for d in HELD if not os.path.isdir(f'snapshots/{d}'))

for d in sorted(os.listdir('snapshots')):
    td = f'snapshots/{d}'
    if not os.path.isdir(td) or not os.path.exists(f'{td}/roster_two_deep.csv'):
        continue
    tkey = norm(d)
    # dossier: name -> (vol, disposition)
    doss = {}
    override_names, expired_names = set(), set()
    if os.path.exists(f'{td}/unit_dossiers.md'):
        for line in open(f'{td}/unit_dossiers.md'):
            for m in DOSS_RE.finditer(line):
                nm, g, vol, disp = m.groups()
                doss[norm(nm)] = (float(g), int(vol), disp.strip()[:40])
                if 'yr4 override' in disp:
                    override_names.add(norm(nm))
                if 'EXPIRED(yr4)' in disp:
                    expired_names.add(norm(nm))
    for r in csv.DictReader(open(f'{td}/roster_two_deep.csv')):
        pl, orig = r.get('player') or '', (r.get('origin') or '').lower()
        r['slot'] = r.get('slot') or r.get('depth') or '?'
        if not pl or pl.lower() in ('player', ''):
            continue
        nk = norm(pl)
        if 'return' in orig:
            tot['returning'] += 1
            yr = roster.get(tkey, {}).get(nk, 'ABSENT')
            if yr is not None and yr != 'ABSENT' and yr <= 3:
                tot['safe'] += 1
            elif nk in override_names:
                tot['flagged_override'] += 1
                if d in HELD:
                    held_rows.append((d, r['unit'], r['slot'], pl, doss.get(nk, (0, 0, ''))[1], 'FLAGGED', yr))
            else:
                tot['silent'] += 1
                v = doss.get(nk, (0, 0, ''))[1]
                silent_rows.append((d, r['unit'], r['slot'], pl, v, yr))
                if d in HELD:
                    held_rows.append((d, r['unit'], r['slot'], pl, v, 'SILENT', yr))
        elif 'arrival' in orig or 'transfer' in orig or 'portal' in orig:
            arr_tot += 1
            if nk not in portal26:
                arr_nofeed += 1
        else:
            tot['other_origin'] += 1

print(f"missing held dirs: {missing_dirs}")
print(f"two-deep RETURNING players field-wide: {tot['returning']}")
print(f"  SAFE (class<=3 in roster_2025):      {tot['safe']}  ({100*tot['safe']/max(tot['returning'],1):.0f}%)")
print(f"  FLAGGED (May-print yr4 override):    {tot['flagged_override']}")
print(f"  SILENT (ambiguous, no override tag): {tot['silent']}")
print(f"non-returning two-deep rows: arrivals/transfers {arr_tot} (no portal-feed record: {arr_nofeed}), other-origin {tot['other_origin']}")

print(f"\nHELD-team uncertain returning two-deep players (n={len(held_rows)}):")
for d, u, s, pl, v, cls, yr in sorted(held_rows, key=lambda x: -x[4]):
    print(f"  {d:15s} {u:5s} slot{s:>2s}  {pl:26s} vol {v:4d}  {cls}  class={yr}")

silent_rows.sort(key=lambda x: -x[4])
print(f"\nTop-20 SILENT field-wide by tape volume:")
for d, u, s, pl, v, yr in silent_rows[:20]:
    print(f"  {d:18s} {u:5s} slot{s:>2s} {pl:26s} vol {v:4d} class={yr}")
sil_hi = sum(1 for r in silent_rows if r[4] >= 150)
print(f"\nSILENT with vol>=150 (real 2025 tape, so presumably yr4-adjacent): {sil_hi}")
print(f"SILENT with vol<150 or no dossier line (walk-on/depth/name-mismatch): {len(silent_rows)-sil_hi}")
