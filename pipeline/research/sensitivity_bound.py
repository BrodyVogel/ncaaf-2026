#!/usr/bin/env python3
"""Sensitivity bound for the blend constants. The 251 rule-set blend pairs (256 sweep
blends minus the 5 pinned manual overrides) get their applied move scaled by 0x
(variant A: pure dossier for the rule-set layer) and 2x (variant B: cap ±16).
For each variant: rewrite snapshots grades in place -> final_pass -> win_totals_compute
-> stash payload. Caller restores git state afterward. Usage: sensitivity_bound.py A|B"""
import csv, json, glob, sys

VAR = sys.argv[1]
SCALE = {'A': 0.0, 'B': 2.0}[VAR]
PINNED = {('Duke', 'QB'), ('Michigan', 'QB'), ('Wisconsin', 'QB'),
          ('Louisiana Tech', 'WRTE'), ('Tulane', 'RB')}
ruleset = set()
for r in csv.DictReader(open('/tmp/sweep_proposals.csv')):
    if r['dg'] != '' and r['final'] != r['dossier'] and (r['team'], r['unit']) not in PINNED:
        ruleset.add((r['team'], r['unit']))

n = 0
for gpath in sorted(glob.glob('snapshots/*/grades.json')):
    tdir = gpath.split('/')[1]
    m = json.load(open(f'snapshots/{tdir}/META.json'))
    g = json.load(open(gpath))
    changed = False
    for u, d in g['units'].items():
        if (m['team'], u) in ruleset and 'v1_grade' in d:
            v1 = d['v1_grade']; move = d['grade'] - v1
            d['grade'] = int(max(1, min(99, round(v1 + SCALE * move))))
            changed = True; n += 1
    if changed: json.dump(g, open(gpath, 'w'), indent=1)
print(f'variant {VAR}: scaled {n} rule-set unit moves by {SCALE}x')
