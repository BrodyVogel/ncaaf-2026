#!/usr/bin/env python3
"""Canonical team-name bridge. EVERY cross-source name join routes through to_nk().

Canonical key = data/anchors/team_name_map.csv norm_key (the anchor/payload
convention, 138 teams). Folded-in source spellings: all seven columns of
team_name_map (SP+/FEI/Massey/FPI/TeamRankings/PFF-full/CFBD) plus the
PFF CSV-file team abbreviations (hand-verified against the summary-file
universes 2021-2025) and legacy alias spellings.

to_nk(s) -> canonical norm_key or None (caller decides how to treat unknowns;
None almost always means a non-FBS team, which most joins should skip —
but SKIPPING MUST BE COUNTED AND REPORTED, never silent).

Added 2026-08-02 after the join-coverage sweep: bare norm()-vs-norm() joins
silently dropped App State / UConn / UL Monroe / Miami-FL rows in S16/S17/S18,
and S16's local PFF_AL mapped 13 majors to nonexistent keys (USC, Ole Miss,
NC State, SMU, TCU, UCF, UTSA, UTEP, BYU, LSU, UNLV, UAB, Miami-OH) plus two
misspelled entries (sanjosest/sandiegost vs actual sjosest/sdiegost).
"""
import csv
import os
import re
import unicodedata

_MAP = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', '..', 'data', 'anchors', 'team_name_map.csv')


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


# PFF summary-file team_name values (normed) -> canonical norm_key.
# Verified against the actual distinct-value universes of
# data/pff_history/{2021..2024}/*_summary*.csv and data/pff/PFF_*_summary/blocking.
PFF_ABBREV = {
    'arkstate': 'arkansasstate', 'bostoncol': 'bostoncollege',
    'bowlgreen': 'bowlinggreen', 'cal': 'california',
    'coastcar': 'coastalcarolina', 'colostate': 'coloradostate',
    'dominion': 'olddominion', 'ecu': 'eastcarolina',
    'fau': 'floridaatlantic', 'gasouthrn': 'georgiasouthern',
    'gastate': 'georgiastate', 'gatech': 'georgiatech',
    'jamesmad': 'jamesmadison', 'jvillest': 'jacksonvillestate',
    'lalafayet': 'louisiana', 'ull': 'louisiana',
    'lamonroe': 'louisianamonroe', 'latech': 'louisianatech',
    'michstate': 'michiganstate', 'middletn': 'middletennessee',
    'missstate': 'mississippistate', 'ncarolina': 'northcarolina',
    'newmexst': 'newmexicostate', 'nwestern': 'northwestern',
    'oklastate': 'oklahomastate', 'scarolina': 'southcarolina',
    'sdiegost': 'sandiegostate', 'sandiegost': 'sandiegostate',
    'sjosest': 'sanjosestate', 'sanjosest': 'sanjosestate',
    'smhouston': 'samhouston', 'somiss': 'southernmiss',
    'vatech': 'virginiatech', 'wake': 'wakeforest',
    'washstate': 'washingtonstate', 'wvirginia': 'westvirginia',
    'ndakst': 'northdakotastate', 'sacramento': 'sacramentostate',
}

_ANY = {}
NK = frozenset()


def _build():
    global NK
    rows = list(csv.DictReader(open(_MAP)))
    canon = {r['norm_key'] for r in rows}
    for r in rows:
        for c in r:
            v = norm(r[c])
            if not v:
                continue
            prev = _ANY.get(v)
            assert prev in (None, r['norm_key']), \
                f'alias collision: {v} -> {prev} / {r["norm_key"]}'
            _ANY[v] = r['norm_key']
    for k, v in PFF_ABBREV.items():
        assert v in canon, f'PFF alias target not canonical: {v}'
        prev = _ANY.get(k)
        assert prev in (None, v), f'PFF alias collision: {k} -> {prev} / {v}'
        _ANY[k] = v
    NK = frozenset(canon)


_build()


def to_nk(s):
    """Any team string / abbreviation / foreign key -> canonical norm_key, else None."""
    return _ANY.get(norm(s))


def coverage(values, label=''):
    """Join-coverage report helper: (n_resolved, unresolved_list)."""
    vals = list(values)
    un = sorted({str(v) for v in vals if to_nk(v) is None})
    if label:
        print(f'[alias] {label}: {len(vals) - len(un)}/{len(vals)} resolved'
              + (f' | unresolved: {un[:12]}{"..." if len(un) > 12 else ""}' if un else ''))
    return len(vals) - len(un), un
