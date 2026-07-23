#!/usr/bin/env python3
"""Research spine: player-season panel 2021-2025 + season-pair links + portal-stars join.
Writes data/research/spine.csv and data/research/pairs.csv. Summary prints only."""
import csv, json, os, re, sys, unicodedata
from collections import defaultdict

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(R)

FILES = {  # file-stem -> (positions it is primary for, volume-column candidates)
    'passing_summary':   ({'QB'}, ['dropbacks', 'attempts']),
    'rushing_summary':   ({'HB', 'RB', 'FB'}, ['attempts']),
    'receiving_summary': ({'WR', 'TE'}, ['routes', 'targets']),
    'offense_blocking':  ({'T', 'G', 'C', 'OL'}, ['snap_counts_offense', 'snap_counts_pass_block', 'declined_penalties']),
    'defense_summary':   ({'DI', 'DT', 'DE', 'ED', 'EDGE', 'DL', 'LB', 'ILB', 'OLB', 'CB', 'S', 'DB'}, ['snap_counts_defense', 'snap_counts_total', 'tackles']),
}
GROUP = {'QB': 'QB', 'HB': 'RB', 'RB': 'RB', 'FB': 'RB', 'WR': 'WRTE', 'TE': 'WRTE',
         'T': 'OL', 'G': 'OL', 'C': 'OL', 'OL': 'OL', 'DI': 'DL', 'DT': 'DL', 'DE': 'DL',
         'ED': 'DL', 'EDGE': 'DL', 'DL': 'DL', 'LB': 'LB', 'ILB': 'LB', 'OLB': 'LB',
         'CB': 'DB', 'S': 'DB', 'DB': 'DB'}

def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())

# ---- conference map per (team, season) from CFBD records ----
conf_by = {}
for y in range(2021, 2026):
    for r in json.load(open(f'data/cfbd/2026-07-12/records_{y}.json')):
        conf_by[(norm(r['team']), y)] = r.get('conference') or '?'
# alias fixes for PFF->CFBD naming (from the full unmatched census)
ALIAS = {'olemiss': 'olemiss', 'centralflorida': 'ucf', 'miamifl': 'miami', 'miamioh': 'miamioh',
         'southerncal': 'usc', 'texasam': 'texasam', 'louisianalafayette': 'louisiana',
         'ulmonroe': 'louisianamonroe', 'umass': 'massachusetts', 'uconn': 'connecticut',
         'pitt': 'pittsburgh', 'sanjosest': 'sanjosestate',
         'arkstate': 'arkansasstate', 'bostoncol': 'bostoncollege', 'bowlgreen': 'bowlinggreen',
         'cmichigan': 'centralmichigan', 'cal': 'california', 'coastcar': 'coastalcarolina',
         'colostate': 'coloradostate', 'dominion': 'olddominion', 'ecarolina': 'eastcarolina',
         'emichigan': 'easternmichigan', 'fau': 'floridaatlantic', 'fiu': 'floridainternational',
         'gasouthrn': 'georgiasouthern', 'gastate': 'georgiastate', 'gatech': 'georgiatech',
         'jamesmad': 'jamesmadison', 'jvillestate': 'jacksonvillestate', 'kennesaw': 'kennesawstate',
         'lalafayet': 'louisiana', 'lamonroe': 'louisianamonroe', 'latech': 'louisianatech',
         'michstate': 'michiganstate', 'middletn': 'middletennessee', 'missstate': 'mississippistate',
         'mostate': 'missouristate', 'ncarolina': 'northcarolina', 'nillinois': 'northernillinois',
         'ntexas': 'northtexas', 'newmexstate': 'newmexicostate', 'nwestern': 'northwestern',
         'oklastate': 'oklahomastate', 'salabama': 'southalabama', 'scarolina': 'southcarolina',
         'sdiegostate': 'sandiegostate', 'sjosestate': 'sanjosestate', 'smhouston': 'samhoustonstate',
         'somiss': 'southernmiss', 'usf': 'southflorida', 'vatech': 'virginiatech',
         'wgeorgia': 'westgeorgia', 'wkentucky': 'westernkentucky', 'wmichigan': 'westernmichigan',
         'wvirginia': 'westvirginia', 'wake': 'wakeforest', 'washstate': 'washingtonstate'}
CFBD_KEYS = defaultdict(dict)
for (tk, y) in conf_by: CFBD_KEYS[y][tk] = tk

def team_conf(team, year):
    tk = norm(team)
    tk = re.sub(r'st$', 'state', tk)  # PFF 'OHIO ST' -> ohiostate
    for cand in (tk, ALIAS.get(tk, tk)):
        if (cand, year) in conf_by: return conf_by[(cand, year)], cand
    return None, tk

def p4(conf, year):
    base = {'SEC', 'Big Ten', 'Big 12', 'ACC', 'FBS Independents'}
    return conf in (base | ({'Pac-12'} if year <= 2023 else set()))

# ---- load panel ----
rows, unmatched = [], defaultdict(int)
for y in range(2021, 2026):
    for stem, (poss, volcands) in FILES.items():
        if y < 2025:
            path = f'data/pff_history/{y}/{stem}_{y}.csv'
        else:
            path = f'data/pff/PFF_{stem}.csv'
        if not os.path.exists(path): print(f'MISSING {path}'); continue
        with open(path) as f:
            for r in csv.DictReader(f):
                pos = (r.get('position') or '').upper()
                if pos not in poss: continue
                g = r.get('grades_offense') if stem != 'defense_summary' else r.get('grades_defense')
                if not g: continue
                vol = next((float(r[c]) for c in volcands if r.get(c) not in (None, '')), 0.0)
                conf, tk = team_conf(r['team_name'], y)
                if conf is None:
                    unmatched[(r['team_name'], y)] += 1; continue
                rows.append(dict(player_id=r['player_id'], name=r.get('player', ''), season=y,
                                 pos=pos, grp=GROUP[pos], team=tk, conf=conf, p4=int(p4(conf, y)),
                                 grade=float(g), vol=vol, games=float(r.get('player_game_count') or 0)))
# dedup: keep max-volume row per (player, season)
best = {}
for r in rows:
    k = (r['player_id'], r['season'])
    if k not in best or r['vol'] > best[k]['vol']: best[k] = r
rows = list(best.values())

os.makedirs('data/research', exist_ok=True)
with open('data/research/spine.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# ---- pairs ----
by_ps = {(r['player_id'], r['season']): r for r in rows}
pairs = []
for r in rows:
    n = by_ps.get((r['player_id'], r['season'] + 1))
    if not n: continue
    moved = int(r['team'] != n['team'])
    jump = 'stay' if not moved else ('P4>G5' if r['p4'] and not n['p4'] else ('G5>P4' if not r['p4'] and n['p4'] else 'within'))
    pairs.append(dict(player_id=r['player_id'], name=r['name'], grp=r['grp'], season_t=r['season'],
                      team_t=r['team'], conf_t=r['conf'], p4_t=r['p4'], grade_t=r['grade'], vol_t=r['vol'],
                      team_t1=n['team'], conf_t1=n['conf'], p4_t1=n['p4'], grade_t1=n['grade'], vol_t1=n['vol'],
                      moved=moved, jump=jump, stars=''))

# ---- portal stars join (transfer year = season_t+1) ----
portal = defaultdict(dict)
for y in range(2022, 2026):
    for e in json.load(open(f'data/cfbd/2026-07-12/portal_{y}.json')):
        nm = norm((e.get('firstName') or '') + (e.get('lastName') or ''))
        org = norm(e.get('origin') or '')
        if e.get('stars'): portal[y][(nm, org)] = e['stars']
hit = 0
for p in pairs:
    if not p['moved']: continue
    s = portal.get(p['season_t'] + 1, {}).get((norm(p['name']), p['team_t']))
    if s is None:  # origin normalization may differ (e.g. 'ohiostate' vs 'ohiost')
        s = next((v for (nm, org), v in portal.get(p['season_t'] + 1, {}).items() if nm == norm(p['name'])), None)
    if s is not None: p['stars'] = s; hit += 1

with open('data/research/pairs.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(pairs[0].keys())); w.writeheader(); w.writerows(pairs)

# ---- summary ----
from statistics import mean
print(f"spine: {len(rows)} player-seasons | by year: " +
      str({y: sum(1 for r in rows if r['season'] == y) for y in range(2021, 2026)}))
print(f"unmatched team-season rows dropped: {sum(unmatched.values())} across {len(unmatched)} teams "
      f"(top: {sorted(unmatched.items(), key=lambda x: -x[1])[:4]})")
mv = [p for p in pairs if p['moved']]
print(f"pairs: {len(pairs)} | movers: {len(mv)} ({100*len(mv)/len(pairs):.0f}%) | jumps: " +
      str({j: sum(1 for p in mv if p['jump'] == j) for j in ('within', 'P4>G5', 'G5>P4')}))
print(f"portal-stars matched: {hit}/{len(mv)} movers ({100*hit/len(mv):.0f}%)")
print(f"groups: " + str({g: sum(1 for p in pairs if p['grp'] == g) for g in ('QB','RB','WRTE','OL','DL','LB','DB')}))
