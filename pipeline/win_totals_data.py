#!/usr/bin/env python3
"""Data layer for the win-totals engine: resolves teams across the three sources
(ASSEMBLY ratings, CFBD schedules, market file), attaches FCS ratings, and builds each
team's games list (opponent rating/band, site, conference flag) for both the 'ours'
(final) and 'consensus' (anchor_blend) rating sets."""
import json, glob, csv, re, os, unicodedata


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


MKT_ALIAS = {'Appalachian State': 'App State', 'Connecticut': 'UConn',
             'FIU': 'Florida International', 'Hawaii': "Hawai'i", 'Miami Florida': 'Miami',
             'Miami Ohio': 'Miami (OH)', 'North Carolina State': 'NC State',
             'Sam Houston State': 'Sam Houston', 'San Jose State': 'San José State'}


def load(fcs_path='data/fcs_ratings_2026.csv', root='.'):
    def p(rel):
        return os.path.join(root, rel)
    n2c = {}
    for r in csv.DictReader(open(p('data/anchors/team_name_map.csv'))):
        n2c[r['norm_key']] = r['cfbd_school']
    c2n = {v: k for k, v in n2c.items()}

    teams = {}       # norm_key -> {name, final, band, anchor, conf}
    name2nk = {}
    for r in csv.DictReader(open(p('outputs/final_pass/ASSEMBLY.csv'))):
        nk = c2n.get(r['team']) or (norm(r['team']) if norm(r['team']) in n2c else norm(r['team']))
        teams[nk] = {'nk': nk, 'name': r['team'], 'final': float(r['final']),
                     'band': float(r['band']), 'anchor': float(r['anchor_blend']),
                     'conf': r['conference']}
        name2nk[r['team']] = nk

    # FCS ratings: name (cfbd) -> {rating, band, tier, note}
    fcs = {}
    if os.path.exists(p(fcs_path)):
        for r in csv.DictReader(open(p(fcs_path))):
            fcs[r['team']] = {'rating': float(r['rating']), 'band': float(r.get('band', 9)),
                              'tier': r.get('tier', ''), 'note': r.get('note', '')}
    FCS_DEFAULT = {'rating': -40.0, 'band': 10.0, 'tier': 'default', 'note': 'unrated default'}

    def resolve(cfbd_name, classification):
        nk = c2n.get(cfbd_name) or (norm(cfbd_name) if norm(cfbd_name) in n2c else None)
        if classification == 'fbs' and nk in teams:
            return ('fbs', nk)
        return ('fcs', cfbd_name)

    # per-team schedule -> games
    schedules = {}
    for gp in glob.glob(p('snapshots/*/pulls/schedule_2026.json')):
        games = json.load(open(gp))
        # identify which of the 138 this file belongs to (the team appearing in every game)
        # use directory name via reverse of team dir; simpler: infer from games' common team
        from collections import Counter
        cnt = Counter()
        for g in games:
            cnt[g['homeTeam']] += 1
            cnt[g['awayTeam']] += 1
        subj_name = cnt.most_common(1)[0][0]
        kind, subj_nk = resolve(subj_name, 'fbs')
        if subj_nk not in teams:
            continue
        glist = []
        for g in games:
            if g['seasonType'] != 'regular':
                continue
            home = g['homeTeam'] == subj_name
            opp_name = g['awayTeam'] if home else g['homeTeam']
            opp_class = g['awayClassification'] if home else g['homeClassification']
            site = 0 if g['neutralSite'] else (1 if home else -1)
            okind, okey = resolve(opp_name, opp_class)
            if okind == 'fbs':
                o = teams[okey]
                opp = {'kind': 'fbs', 'nk': okey, 'name': o['name'],
                       'mu_our': o['final'], 'mu_anchor': o['anchor'], 'band': o['band']}
            else:
                fr = fcs.get(opp_name, FCS_DEFAULT)
                opp = {'kind': 'fcs', 'nk': None, 'name': opp_name,
                       'mu_our': fr['rating'], 'mu_anchor': fr['rating'], 'band': fr['band'],
                       'tier': fr.get('tier', ''), 'fcs_note': fr.get('note', '')}
            is_conf = bool(g['conferenceGame'])
            # CFBD flag correction (media-days triage 2026-07-21): the 2026 NDSU-SJSU game is a
            # NON-conference matchup between MW members (SJSU's 13th game via the Hawai'i
            # exemption). The MW plays a balanced 8-game slate (CBS Sports); NDSU's composition
            # is 8 MW + 3 non-conf FBS + 1 FCS (ESPN/Sportico/NDSU). CFBD marks it
            # conferenceGame=True, which gave both teams 9 conf games — census outlier.
            if {subj_name, opp_name} == {'North Dakota State', 'San José State'} or \
               {subj_name, opp_name} == {'North Dakota State', 'San Jose State'}:
                is_conf = False
            glist.append({'week': g['week'], 'opp': opp, 'site': site,
                          'is_conf': is_conf,
                          'date': g.get('startDate', '')})
        glist.sort(key=lambda x: (x['week'], x['date']))
        schedules[subj_nk] = glist

    # Pac-12 Week-13 FLEX games (audit fix 2026-07-20): CFBD's 2026 pull has no entry for the
    # conference's flex week (opponent officially TBD until Nov 22), leaving all 8 Pac-12 teams
    # with 11 games while the market prices 12 — which manufactured phantom Under edges. Append
    # the projected pairings (CBS/FBSchedules, Feb 2026 release) as non-conference games,
    # flagged flex=True so the UI can label them projected.
    fp = p('data/pac12_flex_2026.csv')
    if os.path.exists(fp):
        for r in csv.DictReader(open(fp)):
            wk = int(r['week'])
            for subj, oppn, site in ((r['away'], r['home'], -1), (r['home'], r['away'], 1)):
                snk, onk = name2nk.get(subj), name2nk.get(oppn)
                if snk not in schedules or onk not in teams:
                    continue
                if any(g.get('flex') for g in schedules[snk]):
                    continue                          # already appended
                o = teams[onk]
                schedules[snk].append({
                    'week': wk, 'site': site, 'is_conf': False, 'date': '2026-11-28',
                    'flex': True,
                    'opp': {'kind': 'fbs', 'nk': onk, 'name': o['name'],
                            'mu_our': o['final'], 'mu_anchor': o['anchor'], 'band': o['band']}})
    return {'teams': teams, 'schedules': schedules, 'fcs': fcs, 'name2nk': name2nk}
