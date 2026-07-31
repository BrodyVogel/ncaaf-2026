#!/usr/bin/env python3
"""P0: reduced team-game fitting panel, 2016-2025 regular seasons.

One row per team-game (FBS teams only; FBS-vs-FCS games kept, flagged):
identifiers, site, result, garbage-filtered efficiency observations
(overall/pass/rush PPA, success rate, explosiveness, plays, drives),
turnovers, and QB-starter fields (de facto starter by attempts + season-modal
comparison -> qb_change flag per IN_SEASON_ANCHOR_DESIGN injury rule).

Output: data/research/insession_panel_2016_2025.csv + coverage report to stdout.
"""
import csv, json, os, re, unicodedata
from collections import defaultdict

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


def gpath(y):
    p = f'data/cfbd/insession/games_{y}_regular.json'
    return p if os.path.exists(p) else f'data/cfbd/2026-07-12/games_{y}_regular.json'


YEARS = range(2016, 2026)
rows_out = []
cov = defaultdict(lambda: defaultdict(int))

for y in YEARS:
    games = {g['id']: g for g in json.load(open(gpath(y)))}
    fbs = set()
    for g in games.values():
        for side in ('home', 'away'):
            cls = g.get(f'{side}Classification')
            if cls == 'fbs':
                fbs.add(norm(g[f'{side}Team']))

    # turnovers per (gameId, team)
    tos = {}
    for w in range(1, 16):
        p = f'data/cfbd/insession/teams/teams_{y}_w{w}.json'
        if not os.path.exists(p):
            continue
        try:
            wk = json.load(open(p))
        except json.JSONDecodeError:
            continue
        for g in wk:
            for t in g.get('teams', []):
                st = {s['category']: s['stat'] for s in t.get('stats', [])}
                try:
                    to = int(st.get('turnovers', 0) or 0)
                except ValueError:
                    to = 0
                tos[(g['id'], norm(t['team']))] = to

    # QB starter per (gameId, team) by max attempts; season-modal per team
    starters, qb_games = {}, defaultdict(list)
    for w in range(1, 16):
        p = f'data/cfbd/insession/qb/pass_{y}_w{w}.json'
        if not os.path.exists(p):
            continue
        try:
            wk = json.load(open(p))
        except json.JSONDecodeError:
            continue
        for g in wk:
            for t in g.get('teams', []):
                best, att_best = None, -1
                for cat in t.get('categories', []):
                    if cat['name'] != 'passing':
                        continue
                    for typ in cat['types']:
                        if typ['name'] != 'C/ATT':
                            continue
                        for a in typ['athletes']:
                            try:
                                att = int(a['stat'].split('/')[1])
                            except (IndexError, ValueError):
                                continue
                            if att > att_best:
                                best, att_best = a['name'], att
                if best:
                    k = (g['id'], norm(t['team']))
                    starters[k] = best
                    qb_games[norm(t['team'])].append(best)
    modal = {t: max(set(v), key=v.count) for t, v in qb_games.items()}

    # advanced rows
    adv = json.load(open(f'data/cfbd/insession/adv_{y}_nogarbage.json'))
    for r in adv:
        if r.get('seasonType') != 'regular':
            continue
        gid = r['gameId']
        g = games.get(gid)
        if g is None:
            continue
        tk, ok = norm(r['team']), norm(r['opponent'])
        if tk not in fbs:
            continue
        is_home = norm(g['homeTeam']) == tk
        pts = g['homePoints'] if is_home else g['awayPoints']
        opp_pts = g['awayPoints'] if is_home else g['homePoints']
        if pts is None:
            continue
        o, d = r.get('offense') or {}, r.get('defense') or {}
        po, ro = o.get('passingPlays') or {}, o.get('rushingPlays') or {}
        st_qb = starters.get((gid, tk))
        row = dict(
            year=y, week=r['week'], game_id=gid, team=tk, opp=ok,
            home=int(is_home), neutral=int(bool(g.get('neutralSite'))),
            fcs_opp=int(ok not in fbs), points=pts, opp_points=opp_pts,
            margin=pts - opp_pts,
            off_ppa=o.get('ppa'), off_sr=o.get('successRate'),
            off_expl=o.get('explosiveness'), off_plays=o.get('plays'),
            off_drives=o.get('drives'),
            off_pass_ppa=po.get('ppa'), off_rush_ppa=ro.get('ppa'),
            def_ppa=d.get('ppa'), def_sr=d.get('successRate'),
            turnovers=tos.get((gid, tk), ''),
            qb_starter=st_qb or '',
            qb_change=int(bool(st_qb) and st_qb != modal.get(tk, st_qb)),
        )
        rows_out.append(row)
        cov[y]['rows'] += 1
        cov[y]['with_to'] += int(row['turnovers'] != '')
        cov[y]['with_qb'] += int(bool(st_qb))
        cov[y]['qb_change'] += row['qb_change']
        cov[y]['fcs'] += row['fcs_opp']

os.makedirs('data/research', exist_ok=True)
out = 'data/research/insession_panel_2016_2025.csv'
with open(out, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
    w.writeheader()
    w.writerows(rows_out)
print(f'panel: {len(rows_out)} team-game rows -> {out}')
print(f'{"year":>5} {"rows":>6} {"turnov%":>8} {"qb%":>6} {"qbchg":>6} {"fcsopp":>7}')
for y in YEARS:
    c = cov[y]
    print(f'{y:>5} {c["rows"]:>6} {100*c["with_to"]/max(c["rows"],1):>7.1f}% '
          f'{100*c["with_qb"]/max(c["rows"],1):>5.1f}% {c["qb_change"]:>6} {c["fcs"]:>7}')
