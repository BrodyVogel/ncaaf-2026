#!/usr/bin/env python3
"""Grades gate (handoff item 4d, 2026-07-17): one command that runs every
check previously done inline at grading time.

  1. grades.json parses; exactly 8 units; every grades_detail entry validates
     against pipeline/grading/grading_schema.json
  2. The dossier's 'PLANNED GRADES:' line matches grades.json (grade AND
     L-confidence per unit). A mismatch is allowed ONLY if the unit is named
     in _meta.planned_vs_final_deviations - silent drift between the written
     rationale and the shipped number is exactly what this blocks.
  3. _meta.snapshot_rev present (grades must reference the frozen commit).

Legacy note: builds before the PLANNED-GRADES line convention warn (not fail)
on check 2. All new builds MUST carry the line.

Usage: python3 pipeline/grades_check.py <Team_Dir> [...]   (or no args = sweep)
Exit 1 on any error.
"""
import glob, json, os, re, sys

try:
    import jsonschema
except ImportError:
    sys.exit("jsonschema not installed")

UNITS = ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB", "ST"]
LINE_RE = re.compile(r"PLANNED GRADES:\s*(.+)$", re.M)
SEG_RE = re.compile(r"^([A-Z]+)\s+(\d+)\s*(L)?$")


def parse_planned(dossier_text):
    m = LINE_RE.search(dossier_text)
    if not m:
        return None
    planned = {}
    for seg in m.group(1).split("|"):
        sm = SEG_RE.match(seg.strip())
        if sm:
            planned[sm.group(1)] = (int(sm.group(2)), bool(sm.group(3)))
    return planned


def check(root, schema):
    team = os.path.basename(root)
    errors, warns = [], []
    gp = f"{root}/grades.json"
    if not os.path.exists(gp):
        return [f"{team}: grades.json missing"], []
    try:
        g = json.load(open(gp))
    except Exception as e:
        return [f"{team}: grades.json unparseable: {e}"], []

    units = g.get("units", {})
    if sorted(units.keys()) != sorted(UNITS):
        errors.append(f"{team}: units keys wrong: {sorted(units.keys())}")
    details = g.get("grades_detail", [])
    if len(details) != 8:
        errors.append(f"{team}: grades_detail has {len(details)} entries (want 8)")
    for d in details:
        try:
            jsonschema.validate(d, schema)
        except jsonschema.ValidationError as e:
            errors.append(f"{team}: schema fail [{d.get('unit')}]: {e.message[:80]}")
        if d.get("unit") in units and d.get("grade") != units[d["unit"]]["grade"]:
            errors.append(f"{team}: grades_detail[{d.get('unit')}] grade "
                          f"{d.get('grade')} != units {units[d['unit']]['grade']}")

    if not g.get("_meta", {}).get("snapshot_rev"):
        errors.append(f"{team}: _meta.snapshot_rev missing (grades must cite the frozen commit)")

    dp = f"{root}/unit_dossiers.md"
    planned = parse_planned(open(dp).read()) if os.path.exists(dp) else None
    if planned is None:
        warns.append(f"{team}: no PLANNED GRADES line (legacy format) - planned-vs-final not checkable")
    else:
        deviations = json.dumps(g.get("_meta", {}).get("planned_vs_final_deviations", {}))
        for u in UNITS:
            if u not in planned:
                errors.append(f"{team}: PLANNED GRADES line missing unit {u}")
                continue
            pg, pl = planned[u]
            fg = units.get(u, {}).get("grade")
            fl = units.get(u, {}).get("confidence") == "L"
            if (pg, pl) != (fg, fl):
                if re.search(rf"\b{u}\b", deviations):
                    warns.append(f"{team}: {u} planned {pg}{'L' if pl else ''} -> "
                                 f"final {fg}{'L' if fl else ''} (declared deviation)")
                else:
                    errors.append(f"{team}: {u} planned {pg}{'L' if pl else ''} != "
                                  f"final {fg}{'L' if fl else ''} and NOT declared in "
                                  f"_meta.planned_vs_final_deviations")
    return errors, warns


if __name__ == "__main__":
    schema = json.load(open("pipeline/grading/grading_schema.json"))
    args = sys.argv[1:]
    dirs = [f"snapshots/{d}" for d in args] or sorted(
        d for d in glob.glob("snapshots/*") if os.path.isdir(d))
    total = 0
    for d in dirs:
        if not os.path.isdir(d):
            print(f"  !! {os.path.basename(d)}: snapshot dir MISSING - check spelling")
            total += 1
            continue
        errors, warns = check(d, schema)
        for w in warns:
            print(f"  ~  {w}")
        for e in errors:
            print(f"  !! {e}")
        if not errors:
            g = json.load(open(f"{d}/grades.json"))
            s = sum(u["grade"] for u in g["units"].values())
            L = sum(1 for u in g["units"].values() if u["confidence"] == "L")
            print(f"{os.path.basename(d)}: OK (sum {s}, {L} L)")
        total += len(errors)
    if total:
        sys.exit(f"GRADES CHECK FAILED: {total} error(s)")
    print("\ngrades check: all clean")
