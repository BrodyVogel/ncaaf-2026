#!/usr/bin/env python3
"""B4 Amendment 2: proforma-bridge injection of S17 curve grades.
Replicates proforma_v2's v2 arm exactly, runs it twice (without/with FCS
entrants), diffs unit percentiles, transmits via standard blend weights.
WRITE_ROWS=1 -> append adjudication rows post-sanity."""
import csv, glob, json, os, re, unicodedata
from collections import defaultdict
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
WRITE = os.environ.get('WRITE_ROWS') == '1'


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
BLEND = {'DB': 1 / 3, 'LB': 0.40}
POS2UNIT = {'QB': 'QB', 'HB': 'RB', 'FB': 'RB', 'WR': 'WRTE', 'TE': 'WRTE',
            'T': 'OL', 'G': 'OL', 'C': 'OL', 'DI': 'DL', 'ED': 'DL',
            'LB': 'LB', 'CB': 'DB', 'S': 'DB'}


def w_of(n, g):
    return min(n / (n + K[g]), WCAP.get(g, 1.0))


S = list(csv.DictReader(open('data/research/spine.csv')))
sp = {2024: defaultdict(list), 2025: defaultdict(list)}
for r in S:
    y = int(r['season'])
    if y in (2024, 2025):
        sp[y][norm(r['name'])].append(r)
rec26 = {}
for e in json.load(open('data/cfbd/recruiting_players/recruits_2026.json')):
    if e.get('rating'):
        rec26[norm(e.get('name', ''))] = float(e['rating'])

P4_26 = {'SEC', 'Big Ten', 'Big 12', 'ACC'}
meta = {}
for gpath in glob.glob('snapshots/*/grades.json'):
    tdir = gpath.split('/')[1]
    g = json.load(open(gpath)); m = json.load(open(f'snapshots/{tdir}/META.json'))
    meta[tdir] = dict(name=m['team'], conf=m.get('conference', '?'),
                      p4=(m.get('conference') in P4_26 or m['team'] == 'Notre Dame'),
                      grades={u: g['units'][u]['grade'] for u in g['units']})

# curve projections keyed (team_dir, norm name)
proj = {}
for p in csv.DictReader(open('data/research/s17_projections_2026.csv')):
    proj[(p['team'], norm(p['player']))] = dict(curve=float(p['proj_fbs']), pos=p['pos'],
                                                slot=p['slot'], player=p['player'])


def find_row(nm, team_nk, origin):
    for y in (2025, 2024):
        cands = sp[y].get(nm, [])
        if not cands:
            continue
        if len(cands) == 1:
            return cands[0], y
        onk = norm(origin.split(':', 1)[1]) if origin.startswith('transfer:') else team_nk
        exact = [c for c in cands if c['team'] == onk or c['team'] == team_nk]
        if len(exact) >= 1:
            return exact[0], y
    return None, None


units = {}
flagged_identity = []
injected_players = defaultdict(list)
for tdir, mt in sorted(meta.items()):
    team_nk = norm(mt['name'])
    rows = list(csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')))
    agg = defaultdict(lambda: {'v2': [], 'v2i': [], 'w': []})
    for r in rows:
        u = (r.get('unit') or '').strip().upper()
        if u not in GRPS:
            continue
        slot = r.get('slot') or r.get('depth') or '1'
        wt = 1.0 if str(slot).strip() == '1' else 0.33
        nm = norm(r['player'] or '')
        cls = (r.get('class') or '').strip().upper()
        origin = (r.get('origin') or '').strip()
        row, yy = find_row(nm, team_nk, origin)
        inj = proj.get((tdir, nm))
        v2 = None
        if row is not None:
            g = float(row['grade']); v = float(row['vol'])
            if yy == 2024:
                v *= 0.5
            p4_from = bool(int(row['p4'])); p4_to = mt['p4']
            jump = -3.54 if (not p4_from and p4_to) else (1.45 if (p4_from and not p4_to) else 0.0)
            pm = POSMEAN[u]
            dconf = 'MWC' if mt['conf'] == 'Pac-12' else C2G.get(mt['conf'], 'IND')
            v2 = pm + w_of(v, u) * (g - pm) + jump + OFF[u].get(dconf, 0)
            if inj:
                flagged_identity.append((tdir, r['player']))  # spine already matched: skip injection
                inj = None
        elif cls == 'FR' and not origin.startswith('transfer:') and nm in rec26:
            dconf = 'MWC' if mt['conf'] == 'Pac-12' else C2G.get(mt['conf'], 'IND')
            b0, sl = FRB[u]
            v2 = b0 + sl * (rec26[nm] - 0.861) + OFF[u].get(dconf, 0)
        if v2 is not None:
            agg[u]['v2'].append(v2); agg[u]['v2i'].append(v2); agg[u]['w'].append(wt)
        elif inj:
            dconf = 'MWC' if mt['conf'] == 'Pac-12' else C2G.get(mt['conf'], 'IND')
            v2i = inj['curve'] + OFF[u].get(dconf, 0)
            agg[u]['v2i'].append(v2i); agg[u]['w'].append(wt)
            agg[u]['v2'].append(None)   # invisible in baseline arm
            injected_players[(tdir, u)].append((inj['player'], inj['curve'], wt))
    for u, a in agg.items():
        w = np.array(a['w'])
        base_vals = [(x, ww) for x, ww in zip(a['v2'], w) if x is not None]
        if not base_vals:
            continue
        bv = np.average([x for x, _ in base_vals], weights=[ww for _, ww in base_vals])
        iv = np.average(a['v2i'], weights=w)
        units[(tdir, u)] = dict(team=mt['name'], base=float(bv), inj=float(iv),
                                shipped=mt['grades'].get(u))

# percentile both arms within unit type across the field
keys = list(units.keys())
for u in GRPS:
    sub = [k for k in keys if k[1] == u]
    for arm in ('base', 'inj'):
        vals = np.array([units[k][arm] for k in sub])
        order = vals.argsort().argsort()
        for k, pct in zip(sub, 100.0 * order / max(len(sub) - 1, 1)):
            units[k][arm + '_pct'] = pct

results = []
for (tdir, u), d in units.items():
    if (tdir, u) not in injected_players:
        continue
    dp = d['inj_pct'] - d['base_pct']
    bw = BLEND.get(u, 0.5)
    tr = bw * dp
    results.append(dict(team=tdir, unit=u, dpct=round(dp, 1), blended=round(tr, 2),
                        shipped=d['shipped'], players=injected_players[(tdir, u)]))

D = np.array([r['blended'] for r in results])
print(f'affected units: {len(results)} | identity-guard skips: {len(flagged_identity)}')
print(f'post-blend delta: mean {D.mean():+.2f} | SD {D.std():.2f} | P5 {np.percentile(D,5):+.2f} | P95 {np.percentile(D,95):+.2f}')
print(f'|delta|>=2: {int((np.abs(D)>=2).sum())} | >8 pre-cap: {int((np.abs(D)>8).sum())} ({100*(np.abs(D)>8).mean():.1f}% — gate <10%)')
up, dn = int((D > 0.5).sum()), int((D < -0.5).sum())
print(f'direction: up {up} / flat {len(D)-up-dn} / down {dn}  (one-direction gate <90%: {100*max(up,dn)/max(len(D),1):.0f}%)')
HELD = {'UConn','Tulsa','Oregon_State','Bowling_Green','Liberty','Arizona_State','Kennesaw_State','Illinois','West_Virginia','East_Carolina',"Hawai'i",'Florida','UCF','Pittsburgh','Wisconsin','Buffalo','Nevada','Wake_Forest','Rutgers'}
rows_to_write = [r for r in results if abs(r['blended']) >= 2.0]
print(f'\nunits crossing the row threshold (|blend x dpct| >= 2): {len(rows_to_write)}')
for r in sorted(rows_to_write, key=lambda x: -abs(x['blended'])):
    tag = 'HELD' if r['team'] in HELD else '    '
    ents = '; '.join(f'{p} {c:.0f}' for p, c, _ in r['players'])
    print(f"  {tag} {r['team']:18s} {r['unit']:4s} shipped {r['shipped']:3d} dpct {r['dpct']:+.1f} -> {r['blended']:+.1f}  [{ents[:80]}]")

if WRITE:
    n = 0
    with open('data/research/adjudication_v2.csv', 'a', newline='') as f:
        w = csv.writer(f)
        for r in sorted(rows_to_write, key=lambda x: -abs(x['blended'])):
            g = r['shipped']
            newg = int(round(g + max(-8.0, min(8.0, r['blended']))))
            if newg == g:
                continue
            ents = '; '.join(f'{p} curve {c:.0f}' for p, c, _ in r['players'])
            w.writerow([meta[r['team']]['name'], r['unit'], g,
                        f"S17 curve via proforma bridge: {ents}; formula dpct {r['dpct']:+.1f}",
                        newg, '-',
                        f"B4-A2 FCS-curve integration 2026-08-02 — systematic per registration; blend {BLEND.get(r['unit'], 0.5)} x dpct, capped"])
            n += 1
    print(f'\nwrote {n} adjudication rows')
