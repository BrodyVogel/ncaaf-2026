#!/usr/bin/env python3
"""Pro forma v2 board: reuse each snapshot's roster_two_deep, swap arithmetic only.
Arm v1 = raw grade + origin-conference offset (no shrink). Arm v2 = validated formula.
Same matched players both arms; unit aggregate -> national percentile; delta = v2 - v1.
Outputs: outputs/proforma_v2_2026.csv (unit rows) + outputs/PROFORMA_V2_2026.md (all teams)."""
import csv, json, os, re, unicodedata, glob
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
def w_of(n, g): return min(n / (n + K[g]), WCAP.get(g, 1.0))

# spine rows by name for 2025 and 2024
S = list(csv.DictReader(open('data/research/spine.csv')))
sp = {2024: defaultdict(list), 2025: defaultdict(list)}
for r in S:
    y = int(r['season'])
    if y in (2024, 2025): sp[y][norm(r['name'])].append(r)

# recruits 2026 (true-FR composites)
rec26 = {}
p26 = 'data/cfbd/recruiting_players/recruits_2026.json'
if not os.path.exists(p26):
    import urllib.request
    key = open('/root/.cfb_secrets/cfbd_api_key.txt').read().strip()
    req = urllib.request.Request('https://api.collegefootballdata.com/recruiting/players?year=2026&classification=HighSchool',
                                 headers={'Authorization': 'Bearer ' + key})
    json.dump(json.load(urllib.request.urlopen(req, timeout=60)), open(p26, 'w'))
for e in json.load(open(p26)):
    if e.get('rating'): rec26[norm(e.get('name', ''))] = float(e['rating'])

# team meta: 2026 conference/class + dossier planned grades
P = json.load(open('outputs/win_totals_payload.json'))
P4_26 = {'SEC', 'Big Ten', 'Big 12', 'ACC'}
BETS = {'UConn', 'Tulsa', 'Oregon State', 'Bowling Green', 'Liberty', 'Arizona State',
        'Kennesaw State', 'Illinois', 'West Virginia', 'East Carolina', "Hawai'i",
        'Florida', 'UCF', 'Pittsburgh'}
meta = {}
for gpath in glob.glob('snapshots/*/grades.json'):
    tdir = gpath.split('/')[1]
    g = json.load(open(gpath)); m = json.load(open(f'snapshots/{tdir}/META.json'))
    meta[tdir] = dict(name=m['team'], conf=m.get('conference', '?'),
                      p4=(m.get('conference') in P4_26 or m['team'] == 'Notre Dame'),
                      grades={u: g['units'][u]['grade'] for u in g['units']})

def find_row(nm, team_nk, origin):
    for y in (2025, 2024):
        cands = sp[y].get(nm, [])
        if not cands: continue
        if len(cands) == 1: return cands[0], y
        onk = norm(origin.split(':', 1)[1]) if origin.startswith('transfer:') else team_nk
        exact = [c for c in cands if c['team'] == onk or c['team'] == team_nk]
        if len(exact) >= 1: return exact[0], y
    return None, None

units = []; match_stats = [0, 0]
for tdir, mt in sorted(meta.items()):
    team_nk = norm(mt['name'])
    rows = list(csv.DictReader(open(f'snapshots/{tdir}/roster_two_deep.csv')))
    agg = defaultdict(lambda: {'v1': [], 'v2': [], 'w': [], 'cov': [0, 0]})
    for r in rows:
        u = r['unit'].strip().upper()
        if u not in GRPS: continue
        slot = r.get('slot', '1')
        wt = 1.0 if str(slot).strip() == '1' else 0.33
        a = agg[u]; a['cov'][1] += 1
        nm = norm(r['player']); cls = (r.get('class') or '').strip().upper()
        origin = (r.get('origin') or '').strip()
        row, yy = find_row(nm, team_nk, origin)
        if row is not None:
            match_stats[0] += 1
            g = float(row['grade']); v = float(row['vol'])
            if yy == 2024: v *= 0.5                      # look-through (v2); v1 gets same evidence
            p4_from = bool(int(row['p4'])); p4_to = mt['p4']
            jump = -3.54 if (not p4_from and p4_to) else (1.45 if (p4_from and not p4_to) else 0.0)
            pm = POSMEAN[u]
            # v2 = validated FORECAST of next-year grade, then the dest-conference SCALE
            # term to convert predicted grade -> national quality (offsets keep their
            # legitimate scale job; they only lose the forecasting job).
            dconf = 'MWC' if mt['conf'] == 'Pac-12' else C2G.get(mt['conf'], 'IND')
            v2 = pm + w_of(v, u) * (g - pm) + jump + OFF[u].get(dconf, 0)
            v1 = g + OFF[u].get(C2G.get(row['conf'], 'IND'), 0)
            a['v1'].append(v1); a['v2'].append(v2); a['w'].append(wt); a['cov'][0] += 1
        elif cls == 'FR' and not origin.startswith('transfer:') and nm in rec26:
            b0, sl = FRB[u]
            dconf = 'MWC' if mt['conf'] == 'Pac-12' else C2G.get(mt['conf'], 'IND')
            v2 = b0 + sl * (rec26[nm] - 0.861) + OFF[u].get(dconf, 0)
            a['v1'].append(POSMEAN[u]); a['v2'].append(v2); a['w'].append(wt); a['cov'][0] += 1
            match_stats[0] += 1
        else:
            match_stats[1] += 1
    for u, a in agg.items():
        if not a['w']: continue
        w = np.array(a['w'])
        units.append(dict(team=mt['name'], tdir=tdir, unit=u, conf=mt['conf'],
                          v1=float(np.average(a['v1'], weights=w)), v2=float(np.average(a['v2'], weights=w)),
                          cov=a['cov'][0] / max(a['cov'][1], 1), dossier=mt['grades'].get(u)))

# percentile each arm within unit-type across the field
for u in GRPS:
    sub = [r for r in units if r['unit'] == u]
    for arm in ('v1', 'v2'):
        vals = np.array([r[arm] for r in sub]); order = vals.argsort().argsort()
        for r, pct in zip(sub, 100.0 * order / (len(sub) - 1)): r[arm + '_pct'] = pct
for r in units: r['delta'] = r['v2_pct'] - r['v1_pct']

with open('outputs/proforma_v2_2026.csv', 'w', newline='') as f:
    wcsv = csv.DictWriter(f, fieldnames=['team', 'conf', 'unit', 'v1_pct', 'v2_pct', 'delta', 'dossier', 'cov'])
    wcsv.writeheader()
    for r in sorted(units, key=lambda x: (x['team'], x['unit'])):
        wcsv.writerow({k: (round(r[k], 1) if isinstance(r[k], float) else r[k]) for k in wcsv.fieldnames})

# team table: weighted mean unit delta (final_pass-style: all 7 near-equal; use |OLS|-ish weights)
UW = {'QB': 1.2, 'RB': 0.8, 'WRTE': 0.8, 'OL': 1.0, 'DL': 1.0, 'LB': 0.8, 'DB': 1.0}
teams = defaultdict(dict)
for r in units: teams[r['team']][r['unit']] = r
lines = []
for tm, uu in teams.items():
    ws = sum(UW[u] for u in uu); d = sum(UW[u] * uu[u]['delta'] for u in uu) / ws
    cov = np.mean([uu[u]['cov'] for u in uu])
    approx = 0.35 * d * 0.12   # percentile pts -> ~pts via conversion slope ~0.12, then K
    lines.append((tm, list(uu.values())[0]['conf'], d, approx, cov,
                  max(uu.values(), key=lambda r: abs(r['delta']))))
lines.sort(key=lambda x: -abs(x[2]))
md = ["# Pro forma v2 vs v1-mechanical — all FBS teams (2026-07-23)", "",
      "delta = v2 percentile − v1 percentile, unit-weighted team mean. approx_rating ≈ conversion×K×delta.",
      "cov = share of two-deep players matched. Positive = v2 likes the roster more than the offset arithmetic did.",
      "", "| team | conf | Δteam | ≈rating | cov | biggest unit move | bet |", "|---|---|---|---|---|---|---|"]
for tm, cf, d, ap, cov, big in lines:
    md.append(f"| {tm} | {cf} | {d:+.1f} | {ap:+.2f} | {cov:.0%} | {big['unit']} {big['delta']:+.0f} (v1 {big['v1_pct']:.0f}→v2 {big['v2_pct']:.0f}, dossier {big['dossier']}) | {'●' if tm in BETS else ''} |")
md += ["", "## Top-25 unit-level disagreements", "",
       "| team | unit | v1_pct | v2_pct | Δ | dossier | cov |", "|---|---|---|---|---|---|---|"]
for r in sorted(units, key=lambda x: -abs(x['delta']))[:25]:
    md.append(f"| {r['team']} | {r['unit']} | {r['v1_pct']:.0f} | {r['v2_pct']:.0f} | {r['delta']:+.0f} | {r['dossier']} | {r['cov']:.0%} |")
open('outputs/PROFORMA_V2_2026.md', 'w').write('\n'.join(md))
print(f"matched {match_stats[0]} two-deep players, unmatched {match_stats[1]} "
      f"({100*match_stats[0]/(sum(match_stats)):.0f}%) | units {len(units)} | teams {len(teams)}")
print(f"mean |team delta| {np.mean([abs(l[2]) for l in lines]):.1f} pctile pts | "
      f">|5|: {sum(1 for l in lines if abs(l[2])>5)} teams | top: " +
      ", ".join(f"{l[0]} {l[2]:+.0f}" for l in lines[:5]))
