#!/usr/bin/env python3
"""Shared PFF machinery: unit spec, player-file team-name resolution, table loaders.

Used by: step4_conversion_calibration.py (k/cap), grading/build_exemplars.py (scale
anchors), snapshot_build.py (per-team evidence packs). One definition, everywhere.
"""
import csv, os, re, unicodedata

UNITS = {  # unit: (table, positions, vol_col, grade_col, min_player_vol, min_unit_vol)
    "QB":   ("passing_summary",  {"QB"},         "dropbacks",            "grades_offense", 100, 100),
    "RB":   ("rushing_summary",  {"HB", "FB"},   "attempts",             "grades_offense",  60, 100),
    "WRTE": ("receiving_summary",{"WR", "TE"},   "routes",               "grades_offense", 150, 300),
    "OL":   ("offense_blocking", {"T", "G", "C"},"snap_counts_offense",  "grades_offense", 200, 600),
    "DL":   ("defense_summary",  {"DI", "ED"},   "snap_counts_defense",  "grades_defense", 200, 400),
    "LB":   ("defense_summary",  {"LB"},         "snap_counts_defense",  "grades_defense", 200, 400),
    "DB":   ("defense_summary",  {"CB", "S"},    "snap_counts_defense",  "grades_defense", 200, 400),
}
OFF_UNITS, DEF_UNITS = ["QB", "RB", "WRTE", "OL"], ["DL", "LB", "DB"]

ALIAS = {  # PFF player-file team_name -> norm_key (hand-verified); None = not a panel team
    "CAL": "california", "GA STATE": "georgiastate", "GA TECH": "georgiatech",
    "LA MONROE": "louisianamonroe", "LA TECH": "louisianatech", "VA TECH": "virginiatech",
    "ARK STATE": "arkansasstate", "BOSTON COL": "bostoncollege", "BOWL GREEN": "bowlinggreen",
    "C MICHIGAN": "centralmichigan", "COAST CAR": "coastalcarolina", "DOMINION": "olddominion",
    "E CAROLINA": "eastcarolina", "E MICHIGAN": "easternmichigan", "FAU": "floridaatlantic",
    "FIU": "floridainternational", "GA SOUTHRN": "georgiasouthern", "JAMES MAD": "jamesmadison",
    "JVILLE ST": "jacksonvillestate", "KENNESAW": "kennesawstate", "LA LAFAYET": "louisiana",
    "MIDDLE TN": "middletennessee", "MO STATE": "missouristate", "N CAROLINA": "northcarolina",
    "N ILLINOIS": "northernillinois", "N TEXAS": "northtexas", "NEW MEX ST": "newmexicostate",
    "NWESTERN": "northwestern", "S ALABAMA": "southalabama", "S CAROLINA": "southcarolina",
    "S DIEGO ST": "sandiegostate", "S JOSE ST": "sanjosestate", "SM HOUSTON": "samhouston",
    "SO MISS": "southernmiss", "UCONN": "connecticut", "UMASS": "massachusetts",
    "USF": "southflorida", "W KENTUCKY": "westernkentucky", "W MICHIGAN": "westernmichigan",
    "W VIRGINIA": "westvirginia", "WAKE": "wakeforest", "W GEORGIA": None,
}
EXP = {"st": "state", "okla": "oklahoma", "colo": "colorado", "app": "appalachian",
       "miss": "mississippi", "tenn": "tennessee", "wash": "washington", "mich": "michigan",
       "fla": "florida", "ill": "illinois", "wis": "wisconsin", "minn": "minnesota",
       "ariz": "arizona", "ore": "oregon", "neb": "nebraska", "tex": "texas", "wyo": "wyoming"}

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)

def player_norm(s):
    """Normalize a player name for CFBD<->PFF matching: fold accents, drop punctuation,
    strip TRAILING generational suffixes only (initial-style names like 'JR Rosenberg'
    keep their letters), squash spaces. 'D.J. McKinney' == 'DJ McKinney'; 'Dwight
    Bootle II' == 'Dwight Bootle'; 'J.R. Rosenberg' == 'JR Rosenberg'. Collision risk
    is bounded by the name+origin match in the builder."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    toks = s.split()
    while len(toks) > 2 and toks[-1] in ("jr", "sr", "ii", "iii", "iv", "v"):
        toks.pop()
    return "".join(toks)

def build_team_lookup(map_path="data/anchors/team_name_map.csv",
                      nonfbs_path="data/anchors/pff_nonfbs_map.csv"):
    """Returns (norm_key->cfbd dict, player-file-team-name->cfbd resolver).

    Resolution order: non-FBS overlay (exact PFF name -> CFBD school string; lets FCS/D2
    arrival origins match) -> hand-verified FBS ALIAS -> abbreviation expansion -> norm.
    The overlay is a separate file so the 138-row FBS map (anchor-pipeline canon) is
    untouched. Added 2026-07-15 after the arrival-row drop bug (see repair_pff_arrivals.py).
    """
    n2c = {r["norm_key"]: r["cfbd_school"] for r in csv.DictReader(open(map_path))}
    nonfbs = {}
    if os.path.exists(nonfbs_path):
        nonfbs = {r["pff_name"]: r["cfbd_school"] for r in csv.DictReader(open(nonfbs_path))}
    def lookup(team_name):
        if team_name in nonfbs:
            return nonfbs[team_name]
        if team_name in ALIAS:
            k = ALIAS[team_name]
            return n2c.get(k) if k else None
        k = norm("".join(EXP.get(w, w) for w in team_name.lower().split()))
        return n2c.get(k) or n2c.get(norm(team_name))
    return n2c, lookup

def table_path(table, y):
    return f"data/pff_history/{y}/{table}_{y}.csv" if y < 2025 else f"data/pff/PFF_{table}.csv"

def load_unit_year(table, y, positions, vol_col, grade_col):
    """player_id -> (team_name, vol, grade) for one unit-table-year."""
    out = {}
    for r in csv.DictReader(open(table_path(table, y))):
        if r["position"] not in positions:
            continue
        try:
            vol, grade = float(r[vol_col] or 0), float(r[grade_col])
        except ValueError:
            continue
        out[r["player_id"]] = (r["team_name"], vol, grade)
    return out

def load_unit_rows(table, y, positions):
    """Full rows (dict) for one unit-table-year, position-filtered. For evidence packs."""
    return [r for r in csv.DictReader(open(table_path(table, y))) if r["position"] in positions]

def team_unit_grades_asplayed(y, lookup, scale=1.0):
    """(cfbd_team, unit) -> (snapweighted grade, total vol) for season y AS PLAYED
    (membership and quality both from year y). Used for exemplars, NOT for projections."""
    out = {}
    for unit, (table, positions, vol_col, grade_col, min_pv, min_uv) in UNITS.items():
        acc = {}
        for pid, (tn, vol, grade) in load_unit_year(table, y, positions, vol_col, grade_col).items():
            team = lookup(tn)
            if team is None or vol < min_pv * scale:
                continue
            a = acc.setdefault(team, [0.0, 0.0])
            a[0] += grade * vol; a[1] += vol
        for team, (num, den) in acc.items():
            if den >= min_uv * scale:
                out[(team, unit)] = (num / den, den)
    return out
