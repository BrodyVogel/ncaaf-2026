#!/usr/bin/env python3
"""S8 shadow-arm engine: build the FORMULA arm mechanically (no hand curation)
for any season 2022-2026, then aggregate to unit percentiles and team scores.

Two membership modes:
  B "roster"  (2022-2025): CFBD season roster = who is on the team. Each rostered
               player matched to PFF tape in y-1 (full) or y-2 (vol x0.5).
  A "portal"  (2026, no CFBD roster posted): y-1 tape at team, minus portal-out,
               minus draft picks, minus class-year>=SR heuristic, plus portal-in,
               plus y-2-only players still on the y-1 roster.
Both modes: true-FR priors from recruiting composites fill remaining depth slots.

Arithmetic is the shipped v2 formula (identical constants to proforma_v2.py):
  v2 = posmean + w(vol)*(grade-posmean) + jump + dest-conf offset,  w=min(n/(n+k),cap)
  FR: prior = b0 + slope*(composite-0.861) + dest-conf offset
Depth: within (team,unit) rank tape players by evidence volume; top N_u at weight
1.0, next 2 at 0.33 (QB: 1). FR fills at 0.33, never displacing tape from slot 1
unless the unit has fewer tape players than N_u. JUCO/D2/FCS/no-tape: silent
(mirrors the curated info-share guard).

Usage: imported by s8_phase1_fidelity.py / s8_run_panel.py. Direct run: smoke test.
"""
import csv, json, os, re, sys, unicodedata
from collections import defaultdict

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(R, 'data/cfbd/2026-07-12')

GRPS = ['QB', 'RB', 'WRTE', 'OL', 'DL', 'LB', 'DB']
POSMEAN = {'QB': 69.7, 'RB': 73.5, 'WRTE': 62.6, 'OL': 62.0, 'DL': 64.9, 'LB': 62.3, 'DB': 65.2}
K = {'QB': 230, 'RB': 110, 'WRTE': 190, 'OL': 595, 'DL': 290, 'LB': 630, 'DB': 1180}
WCAP = {'QB': 0.55, 'LB': 0.50}
FRB = {'QB': (58.1, 92.4), 'RB': (73.0, 12.0), 'WRTE': (61.0, 32.5), 'OL': (56.5, 76.6),
       'DL': (60.5, 50.3), 'LB': (58.8, 31.1), 'DB': (62.7, 46.8)}
JUMP_G5P4, JUMP_P4G5 = -3.54, 1.45
UW = {'QB': 1.2, 'RB': 0.8, 'WRTE': 0.8, 'OL': 1.0, 'DL': 1.0, 'LB': 0.8, 'DB': 1.0}
NSLOT1 = {'QB': 1, 'RB': 2, 'WRTE': 5, 'OL': 5, 'DL': 5, 'LB': 3, 'DB': 5}
NSLOT2 = {'QB': 1, 'RB': 2, 'WRTE': 2, 'OL': 2, 'DL': 2, 'LB': 2, 'DB': 2}
C2G = {'SEC': 'SEC', 'American Athletic': 'AAC', 'ACC': 'ACC', 'Big Ten': 'B10', 'Big 12': 'B12',
       'Conference USA': 'CUSA', 'FBS Independents': 'IND', 'Mid-American': 'MAC',
       'Mountain West': 'MWC', 'Pac-12': 'PAC', 'Sun Belt': 'SBC'}
REC_POS = {'QB': 'QB', 'RB': 'RB', 'APB': 'RB', 'FB': 'RB', 'WR': 'WRTE', 'TE': 'WRTE',
           'OT': 'OL', 'IOL': 'OL', 'OG': 'OL', 'OC': 'OL', 'OL': 'OL',
           'DT': 'DL', 'SDE': 'DL', 'WDE': 'DL', 'DL': 'DL', 'EDGE': 'DL',
           'ILB': 'LB', 'OLB': 'LB', 'LB': 'LB', 'CB': 'DB', 'S': 'DB', 'DB': 'DB'}
OFF = json.load(open(f'{R}/data/backtest/conf_offsets_2021_2025.json'))['offsets']


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


def pnorm(s):
    """Player-name key: fold accents/punct, strip trailing generational suffixes."""
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    toks = s.split()
    while len(toks) > 2 and toks[-1] in ('jr', 'sr', 'ii', 'iii', 'iv', 'v'):
        toks.pop()
    return ''.join(toks)


def load_spine():
    sp = defaultdict(list)
    for r in csv.DictReader(open(f'{R}/data/research/spine.csv')):
        r['season'] = int(r['season'])
        r['grade'] = float(r['grade']); r['vol'] = float(r['vol']); r['p4'] = int(r['p4'])
        sp[r['season']].append(r)
    return sp


def conf_map(year):
    """team norm-key -> conference name, for FBS teams of that season."""
    out = {}
    if year >= 2026:
        for t in json.load(open(f'{D}/teams_fbs_2026.json')):
            out[norm(t['school'])] = t.get('conference') or '?'
    else:
        for r in json.load(open(f'{D}/records_{year}.json')):
            if r.get('classification') == 'fbs':
                out[norm(r['team'])] = r.get('conference') or '?'
    return out


def off_group(conf, year):
    """Offset group for a destination conference. Post-2023 Pac-12 (2-team, then
    rebuilt-with-MWC) plays as MWC; 2021-23 Pac-12 is PAC."""
    if conf == 'Pac-12' and year >= 2024:
        return 'MWC'
    return C2G.get(conf, 'IND')


def is_p4(conf, year):
    base = {'SEC', 'Big Ten', 'Big 12', 'ACC', 'FBS Independents'}
    return conf in (base | ({'Pac-12'} if year <= 2023 else set()))


class TapeIndex:
    """Spine lookback for a target season: y-1 full, y-2 at half volume."""

    def __init__(self, spine, year):
        self.year = year
        self.by_name = {y: defaultdict(list) for y in (year - 1, year - 2)}
        self.by_team_name = {}
        for y in (year - 1, year - 2):
            for r in spine.get(y, []):
                self.by_name[y][pnorm(r['name'])].append(r)
                self.by_team_name[(y, r['team'], pnorm(r['name']))] = r

    def find(self, nm, team_nk, origin_nk=None):
        """-> (row, eff_vol, from_year) | (None, 0, None).
        Preference: same-team y-1; origin-team y-1; unique y-1; then y-2 (vol*0.5)."""
        for y, mult in ((self.year - 1, 1.0), (self.year - 2, 0.5)):
            r = self.by_team_name.get((y, team_nk, nm))
            if r is not None:
                return r, r['vol'] * mult, y
            if origin_nk:
                r = self.by_team_name.get((y, origin_nk, nm))
                if r is not None:
                    return r, r['vol'] * mult, y
            cands = self.by_name[y].get(nm, [])
            if len(cands) == 1:
                return cands[0], cands[0]['vol'] * mult, y
        return None, 0.0, None


def recruits_for(year):
    """(team_nk, unit) -> [composite ratings, desc]. HS recruits of that class."""
    out = defaultdict(list)
    for e in json.load(open(f'{R}/data/cfbd/recruiting_players/recruits_{year}.json')):
        u = REC_POS.get((e.get('position') or '').upper())
        if u and e.get('committedTo') and e.get('rating'):
            out[(norm(e['committedTo']), u)].append(float(e['rating']))
    for k in out:
        out[k].sort(reverse=True)
    return out


def membership_roster(year, confs):
    """Mode B: CFBD season roster. -> {team_nk: [(pnorm_name, class_year), ...]}"""
    out = defaultdict(list)
    for p in json.load(open(f'{D}/roster_{year}.json')):
        tk = norm(p.get('team'))
        if tk in confs:
            out[tk].append((pnorm((p.get('firstName') or '') + ' ' + (p.get('lastName') or '')),
                            p.get('year')))
    return out


def membership_portal(year, confs, spine):
    """Mode A (2026-style): reconstruct membership without a season roster.
    -> {team_nk: [(pnorm_name, class_year_or_None), ...]}, using y-1 tape residence,
    portal moves, draft picks, and the SR class heuristic."""
    prev = year - 1
    portal_out, portal_in = defaultdict(set), defaultdict(set)
    for e in json.load(open(f'{D}/portal_{year}.json')):
        nm = pnorm((e.get('firstName') or '') + ' ' + (e.get('lastName') or ''))
        if e.get('origin'):
            portal_out[norm(e['origin'])].add(nm)
        if e.get('destination'):
            portal_in[norm(e['destination'])].add(nm)
    drafted = set()
    for p in json.load(open(f'{R}/data/cfbd/draft_{year}.json')):
        drafted.add(pnorm(p.get('name') or ''))
    cls = {}
    rospath = f'{D}/roster_{prev}.json'
    if os.path.exists(rospath):
        for p in json.load(open(rospath)):
            cls[(norm(p.get('team')), pnorm((p.get('firstName') or '') + ' ' + (p.get('lastName') or '')))] = p.get('year')
    out = defaultdict(list)
    seen = defaultdict(set)
    for y in (prev, prev - 1):
        for r in spine.get(y, []):
            tk, nm = r['team'], pnorm(r['name'])
            if tk not in confs or nm in seen[tk]:
                continue
            if y == prev - 1 and (tk, nm) not in cls:
                continue                      # y-2-only must still be on the y-1 roster
            if nm in portal_out[tk] or nm in drafted:
                continue
            c = cls.get((tk, nm))
            if isinstance(c, int) and c >= 4:
                continue                      # SR heuristic (known-noisy: 5th-years lost)
            seen[tk].add(nm)
            out[tk].append((nm, c))
    for tk, names in portal_in.items():
        if tk in confs:
            for nm in names:
                if nm not in seen[tk]:
                    seen[tk].add(nm)
                    out[tk].append((nm, None))
    return out


def build_shadow(year, mode, spine=None):
    """-> units: {(team_nk, unit): dict(value, n_tape, n_fr, wsum)}, plus diagnostics."""
    spine = spine if spine is not None else load_spine()
    confs = conf_map(year)
    tape = TapeIndex(spine, year)
    recs = recruits_for(year)
    members = membership_roster(year, confs) if mode == 'roster' else membership_portal(year, confs, spine)
    diag = dict(teams=0, matched=0, ambiguous_dropped=0, fr_used=0)

    units = {}
    for tk, plist in members.items():
        diag['teams'] += 1
        pool = defaultdict(list)             # unit -> [(eff_vol, value, nm)]
        used = set()
        for nm, _cl in plist:
            if nm in used:
                continue
            row, ev, fy = tape.find(nm, tk)
            if row is None:
                continue
            used.add(nm)
            u = row['grp']
            pm = POSMEAN[u]
            w = min(ev / (ev + K[u]), WCAP.get(u, 1.0))
            p4_from = bool(row['p4'])
            p4_to = is_p4(confs[tk], year)
            jump = 0.0
            if row['team'] != tk:
                jump = JUMP_G5P4 if (not p4_from and p4_to) else (JUMP_P4G5 if (p4_from and not p4_to) else 0.0)
            v2 = pm + w * (row['grade'] - pm) + jump + OFF[u].get(off_group(confs[tk], year), 0.0)
            pool[u].append((ev, v2, nm))
            diag['matched'] += 1
        for u in GRPS:
            rows = sorted(pool.get(u, []), reverse=True)
            vals, wts = [], []
            for i, (ev, v2, nm) in enumerate(rows[:NSLOT1[u] + NSLOT2[u]]):
                vals.append(v2); wts.append(1.0 if i < NSLOT1[u] else 0.33)
            # FR fills: remaining depth budget from top recruiting composites
            n_fill = max(0, NSLOT1[u] + NSLOT2[u] - len(vals))
            for comp in recs.get((tk, u), [])[:n_fill]:
                b0, sl = FRB[u]
                vals.append(b0 + sl * (comp - 0.861) + OFF[u].get(off_group(confs[tk], year), 0.0))
                wts.append(1.0 if len(vals) <= NSLOT1[u] else 0.33)
                diag['fr_used'] += 1
            if vals:
                units[(tk, u)] = dict(
                    value=sum(v * w for v, w in zip(vals, wts)) / sum(wts),
                    n_tape=len(rows), n_fr=sum(1 for i in range(len(vals)) if i >= len(rows)),
                    wsum=sum(wts))
    return units, diag


def percentiles(units):
    """Within-unit-type percentile across the field. -> {(tk,u): pct}"""
    out = {}
    for u in GRPS:
        sub = sorted([(v['value'], tk) for (tk, uu), v in units.items() if uu == u])
        n = len(sub)
        for i, (val, tk) in enumerate(sub):
            out[(tk, u)] = 100.0 * i / (n - 1) if n > 1 else 50.0
    return out


def team_scores(units, pcts, impute=50.0):
    """UW-weighted mean unit percentile. Missing unit -> impute (flagged)."""
    teams = defaultdict(dict)
    for (tk, u) in units:
        teams[tk][u] = pcts[(tk, u)]
    out = {}
    for tk, uu in teams.items():
        num = den = 0.0
        for u in GRPS:
            num += UW[u] * uu.get(u, impute); den += UW[u]
        out[tk] = dict(score=num / den, n_units=len(uu))
    return out


if __name__ == '__main__':
    spine = load_spine()
    for year, mode in ((2025, 'roster'), (2025, 'portal'), (2026, 'portal')):
        units, diag = build_shadow(year, mode, spine)
        ts = team_scores(units, percentiles(units))
        print(f'{year} {mode}: {diag["teams"]} teams, {len(units)} units, '
              f'{diag["matched"]} tape players, {diag["fr_used"]} FR fills; '
              f'sample OhioState score={ts.get("ohiostate", {}).get("score", float("nan")):.1f}')
