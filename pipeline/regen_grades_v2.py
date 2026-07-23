#!/usr/bin/env python3
"""Regenerate snapshots/*/grades.json as v2 vintage from data/research/adjudication_v2.csv.
Last-write-wins per (team,unit); 'ALL' = hold all units; 'FLAG' rows skipped.
Changed units get v1_grade preserved + an adjudication note; _meta.vintage set on every file."""
import csv, json, glob

fin = {}
for r in csv.DictReader(open('data/research/adjudication_v2.csv')):
    if r['unit'] in ('ALL', 'FLAG'): continue
    try: f = int(r['final'])
    except ValueError: continue          # 'reopen'/'hold' placeholders superseded by later rows
    fin[(r['team'], r['unit'])] = (f, r['conf'], r['reason'], r['formula_note'])

n_changed = n_units = 0
for gpath in sorted(glob.glob('snapshots/*/grades.json')):
    tdir = gpath.split('/')[1]
    m = json.load(open(f'snapshots/{tdir}/META.json'))
    g = json.load(open(gpath))
    team = m['team']
    for u, d in g['units'].items():
        n_units += 1
        key = (team, u)
        if key not in fin: continue      # Kennesaw ALL-hold etc.
        f, conf, reason, note = fin[key]
        if f != d['grade']:
            d['v1_grade'] = d['grade']
            d['grade'] = f
            if conf and conf != '-': d['confidence'] = conf
            d['adjudication'] = f"{reason}: {note[:160]}"
            n_changed += 1
    g.setdefault('_meta', {})['vintage'] = 'v2 2026-07'
    g['_meta']['adjudication_log'] = 'data/research/adjudication_v2.csv'
    json.dump(g, open(gpath, 'w'), indent=1)
print(f'{n_changed} unit grades changed of {n_units} across 138 teams')
