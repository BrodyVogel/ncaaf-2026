#!/usr/bin/env python3
"""Disposition ledger: every 2025 producer (>=100 unit volume) with a verified status.

Born 2026-07-15 from the density review: distilled dossiers hid a systematic gap (the
Hopper error). The ledger makes every returns/leaves call EXPLICIT and mechanical:

  PORTAL->dest   in portal_2026_out with a destination
  PORTAL(none)   in portal_2026_out, no destination  -> needs adjudication (magazine
                 chart / beat note); WITHDREW if in META portal_withdrawal_overrides
  EXPIRED(yr4)   CFBD year==4 and not in portal_out (unless magazine override)
  OVERRIDE-RET   yr-4 but magazine-explicit 2026 return (listed in META known context)
  RETURNS        none of the above

Draft/expulsion cases the feeds can't see must still come from research (news.md), but
every OTHER disposition is now machine-derived. Appends a ledger section to
unit_dossiers.md with --write; prints to stdout otherwise.

Usage: python3 pipeline/disposition_ledger.py <Team_Dir> [...] [--write]
"""
import csv, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pff_common import player_norm

VOL_KEYS = ("passing_snaps", "run_plays", "routes", "snap_counts_offense", "snap_counts_defense")
GRADE_KEYS = ("grades_offense", "grades_defense")


def ledger(root):
    outs, roster, overrides, confirmed_gone = {}, {}, set(), set()
    op = f"{root}/pulls/portal_2026_out.json"
    if os.path.exists(op):
        for r in json.load(open(op)):
            outs[player_norm(r["firstName"] + " " + r["lastName"])] = r.get("destination")
    rp = f"{root}/pulls/roster_2025.json"
    if os.path.exists(rp):
        for p in json.load(open(rp)):
            roster[player_norm(p.get("firstName", "") + " " + p.get("lastName", ""))] = p.get("year")
    mp = f"{root}/META.json"
    if os.path.exists(mp):
        meta = json.load(open(mp))
        overrides = {player_norm(n) for n in meta.get("portal_withdrawal_overrides", [])}
        confirmed_gone = {player_norm(n) for n in meta.get("portal_departure_confirmed", [])}
    rows = []
    for u in ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB"]:
        f = f"{root}/pff/unit_{u}.csv"
        if not os.path.exists(f):
            continue
        for r in csv.DictReader(open(f)):
            if r["_provenance"] != "2025_this_team":
                continue
            vol = 0.0
            for k in VOL_KEYS:
                if r.get(k):
                    try:
                        vol = float(r[k])
                        break
                    except ValueError:
                        continue
            if vol < 100:
                continue
            grade = next((r[k] for k in GRADE_KEYS if r.get(k)), "?")
            nm = player_norm(r["player"])
            if nm not in outs:
                # variant match: unique surname in outs AND compatible first name
                # (Drew vs Andrew Cunningham = same person, first name is a prefix/suffix
                # variant). Surname alone is NOT enough: Max Carroll (LB, returns) must not
                # match Derrick Carroll (RB, portal) - the 2026-07-15 TCU false positive.
                toks = r["player"].split()
                sur = player_norm(toks[-1]) if toks else nm
                first = player_norm(toks[0]) if toks else ""
                hits = []
                for o in outs:
                    if not (o.endswith(sur) and len(sur) > 6):
                        continue
                    o_first = o[: len(o) - len(sur)].strip()
                    if len(first) >= 3 and len(o_first) >= 3 and (
                            o_first.startswith(first) or o_first.endswith(first)
                            or first.startswith(o_first) or first.endswith(o_first)):
                        hits.append(o)
                if len(hits) == 1:
                    nm = hits[0]
            if nm in outs:
                dest = outs[nm]
                if dest:
                    status = f"PORTAL->{dest}"
                elif nm in overrides:
                    status = "WITHDREW (override)"
                elif nm in confirmed_gone:
                    status = "PORTAL(none)-GONE (adjudicated)"
                else:
                    status = "PORTAL(none)-ADJUDICATE"
            elif roster.get(nm) == 4:
                status = "EXPIRED(yr4)*"  # * unless magazine override recorded in news.md
            else:
                status = "RETURNS"
            rows.append((u, r["player"], grade, vol, status))
    return rows


def render(team, rows):
    out = [f"\n## DISPOSITION LEDGER (auto-generated; >=100-vol 2025 producers; * = check news.md overrides)"]
    for u in ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB"]:
        urows = [r for r in rows if r[0] == u]
        if not urows:
            continue
        urows.sort(key=lambda x: -x[3])
        out.append(f"- {u}: " + "; ".join(f"{p} ({g}/{v:.0f}) {s}" for _, p, g, v, s in urows))
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--write"]
    write = "--write" in sys.argv
    dirs = [f"snapshots/{d}" for d in args] or sorted(
        d for d in __import__("glob").glob("snapshots/*") if os.path.isdir(d))
    for d in dirs:
        team = os.path.basename(d)
        rows = ledger(d)
        text = render(team, rows)
        flags = [r for r in rows if "ADJUDICATE" in r[4]]
        if write and os.path.exists(f"{d}/unit_dossiers.md"):
            t = open(f"{d}/unit_dossiers.md").read()
            marker = "## DISPOSITION LEDGER"
            if marker in t:
                t = t[:t.index(marker)].rstrip() + "\n"
            open(f"{d}/unit_dossiers.md", "w").write(t + text)
            print(f"{team}: ledger written ({len(rows)} rows, {len(flags)} to adjudicate)")
        else:
            print(f"=== {team}{text}")
