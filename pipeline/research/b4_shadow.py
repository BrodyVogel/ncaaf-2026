#!/usr/bin/env python3
"""B4 shadow: unit-level deltas from swapping dossier numbers for S17 curve
grades on matched FCS entrants. Per REGISTRATION_B4_FCS_INTEGRATION.
WRITE_ROWS=1 -> append adjudication rows for |delta| >= 2 (post-sanity)."""
import csv, glob, json, os, re, unicodedata
from collections import defaultdict
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
WRITE = os.environ.get('WRITE_ROWS') == '1'


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


K_TABLE = {'QB': 230, 'RB': 110, 'WRTE': 190, 'OL': 595, 'DL': 290, 'LB': 630, 'DB': 1180}
POS2UNIT = {'QB': 'QB', 'HB': 'RB', 'FB': 'RB', 'WR': 'WRTE', 'TE': 'WRTE',
            'T': 'OL', 'G': 'OL', 'C': 'OL', 'DI': 'DL', 'ED': 'DL',
            'LB': 'LB', 'CB': 'DB', 'S': 'DB'}
DOSS_RE = re.compile(r'([A-Z][\w\'.\- ]+?)\s*\((\d+\.?\d*)/(\d+)\)')
SEC_RE = re.compile(r'^- (QB|RB|WRTE|OL|DL|LB|DB|ST)\b|^## (QB|RB|WRTE|OL|DL|LB|DB|ST)\b')


def fcs_snaps():
    """best snap count per player from FCS 2025 files."""
    out = {}
    cols = ('snap_counts_defense', 'snap_counts_offense', 'snap_counts_block',
            'passing_snaps', 'snap_counts_pass_play', 'total_snaps')
    for fn in glob.glob('data/pff_history/fcs/*_2025.csv'):
        if 'special_teams' in fn:
            continue
        for r in csv.DictReader(open(fn)):
            nm = norm(r.get('player') or '')
            sn = 0
            for c in cols:
                try:
                    sn = max(sn, float(r.get(c) or 0))
                except ValueError:
                    pass
            if not sn:
                try:
                    sn = float(r.get('player_game_count') or 0) * 60
                except ValueError:
                    sn = 0
            if nm and sn > out.get(nm, 0):
                out[nm] = sn
    return out


SNAPS = fcs_snaps()
proj = list(csv.DictReader(open('data/research/s17_projections_2026.csv')))
print(f'projections loaded: {len(proj)}')

results, manual = [], []
for p in proj:
    tdir, pl, pos = p['team'], p['player'], p['pos']
    unit = POS2UNIT.get(pos)
    if unit is None:
        continue
    dpath = f'snapshots/{tdir}/unit_dossiers.md'
    gpath = f'snapshots/{tdir}/grades.json'
    if not (os.path.exists(dpath) and os.path.exists(gpath)):
        continue
    txt = open(dpath).read()
    # find the entrant's dossier number anywhere in the doc (surname+number pattern)
    dnum = None
    for m in DOSS_RE.finditer(txt):
        if norm(m.group(1)).endswith(norm(pl.split()[-1])) and norm(pl) in norm(m.group(1)) + norm(pl.split()[-1]) or norm(m.group(1)) == norm(pl):
            dnum = float(m.group(2))
            break
    if dnum is None:
        # looser: surname match on the entrant's full line
        for m in DOSS_RE.finditer(txt):
            if norm(m.group(1)).split and norm(pl.split()[-1]) in norm(m.group(1)):
                dnum = float(m.group(2))
                break
    curve = float(p['proj_fbs'])
    # unit volume mass: all grade/vol pairs in the unit's section
    lines = txt.split('\n')
    sec_players = []
    in_sec = False
    for ln in lines:
        mm = SEC_RE.match(ln)
        if mm:
            in_sec = (mm.group(1) or mm.group(2)) == unit
        if in_sec:
            for m2 in DOSS_RE.finditer(ln):
                sec_players.append((norm(m2.group(1)), float(m2.group(2)), int(m2.group(3))))
    k = K_TABLE[unit]
    mass = sum(v / (v + k) for _, _, v in sec_players)
    ent_sn = SNAPS.get(norm(pl), 300)
    w_ent = ent_sn / (ent_sn + k)
    g = json.load(open(gpath))['units'][unit]['grade']
    if dnum is not None:
        # original mechanism (18 numeric cases)
        share = w_ent / max(mass, w_ent * 1.5) if mass > 0 else 1 / 1.5
        delta = share * (curve - dnum)
        mech = 'numeric'
    elif sec_players and mass > 0:
        # AMENDMENT 1: recompute unit = listed tape players + entrant at curve
        listed_mean = sum((v / (v + k)) * gg for _, gg, v in sec_players) / mass
        recomputed = (mass * listed_mean + w_ent * curve) / (mass + w_ent)
        # shipped grade is the human all-things-considered number; compare
        delta = recomputed - g
        share = w_ent / (mass + w_ent)
        dnum = g  # for display: entrant priced vs the shipped unit level
        mech = 'recompute'
    else:
        share = w_ent / (w_ent + 1.0)
        delta = share * (curve - g)
        dnum = g
        mech = 'fallback'
    results.append(dict(team=tdir, unit=unit, player=pl, pos=pos, slot=p['slot'],
                        curve=curve, dossier=dnum, share=round(share, 3),
                        delta=round(delta, 2), shipped=g, mech=mech))

print(f'computable deltas: {len(results)} | manual (no dossier number): {len(manual)}')
D = np.array([r['delta'] for r in results])
print(f'delta distribution: mean {D.mean():+.2f} | SD {D.std():.2f} | P5 {np.percentile(D,5):+.2f} | P95 {np.percentile(D,95):+.2f}')
print(f'|delta|>=2: {int((np.abs(D)>=2).sum())} | >=8: {int((np.abs(D)>=8).sum())} ({100*(np.abs(D)>=8).mean():.1f}% - sanity gate <10%)')
print(f'direction: up {int((D>0.5).sum())} / flat {int((np.abs(D)<=0.5).sum())} / down {int((D<-0.5).sum())}')

# aggregate per unit (multiple entrants can hit the same unit)
unit_agg = defaultdict(float)
unit_bits = defaultdict(list)
for r in results:
    unit_agg[(r['team'], r['unit'])] += r['delta']
    unit_bits[(r['team'], r['unit'])].append(r)
flags = {k: v for k, v in unit_agg.items() if abs(v) >= 2.0}
print(f'\nunits with |aggregate delta| >= 2: {len(flags)}')
HELD = {'UConn','Tulsa','Oregon_State','Bowling_Green','Liberty','Arizona_State','Kennesaw_State','Illinois','West_Virginia','East_Carolina',"Hawai'i",'Florida','UCF','Pittsburgh','Wisconsin','Buffalo','Nevada','Wake_Forest','Rutgers'}
for (t, u), d in sorted(flags.items(), key=lambda x: -abs(x[1])):
    tag = 'HELD' if t in HELD else '    '
    ents = '; '.join(f"{b['player']} curve {b['curve']:.0f} vs doss {b['dossier']:.0f} (sh {b['share']})" for b in unit_bits[(t, u)])
    print(f'  {tag} {t:18s} {u:4s} {d:+.1f}  [{ents[:110]}]')
print('\nmanual-read queue (no dossier number):')
for t, u, pl, pos, c, slot in manual[:15]:
    print(f'  {t:18s} {u:4s} {pl:24s} curve {c:.0f} slot{slot}')
if len(manual) > 15:
    print(f'  ... +{len(manual)-15} more')

if WRITE:
    n_rows = 0
    with open('data/research/adjudication_v2.csv', 'a', newline='') as f:
        w = csv.writer(f)
        for (t, u), d in sorted(flags.items(), key=lambda x: -abs(x[1])):
            bits = unit_bits[(t, u)]
            g = bits[0]['shipped']
            newg = int(round(g + max(-8.0, min(8.0, d))))
            if newg == g:
                continue
            meta = json.load(open(f'snapshots/{t}/META.json'))
            ents = '; '.join(f"{b['player']} curve {b['curve']:.0f} vs dossier {b['dossier']:.0f} share {b['share']}" for b in bits)
            w.writerow([meta['team'], u, g, f'S17 curve integration: {ents}', newg, '-',
                        f'B4 FCS-curve integration 2026-08-02 — systematic per REGISTRATION_B4; delta {d:+.1f} capped'])
            n_rows += 1
    print(f'\nwrote {n_rows} adjudication rows')
