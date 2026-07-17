#!/usr/bin/env python3
"""FORWARD FLAGS checker (handoff item 5).

outputs/FORWARD_FLAGS.csv is the single cross-build verification ledger:
every departure/arrival whose OTHER side lands at a not-yet-built team gets
a row when it is discovered; the row is closed when that team's build
verifies it.

Columns: dest_team_dir, player, from_team, note, status(open|closed),
         added, closed_by

Operator workflow (documented in OPERATOR_HANDOFF.md):
  BUILD START:  python3 pipeline/forward_flags.py <Team_Dir>
                -> lists the open flags pointing at this team; verify each
                   against the feed/prints during the build.
  BUILD END:    edit the CSV - set status=closed + closed_by=<Team_Dir>
                for the verified rows; APPEND new rows for every departure
                to a still-unbuilt team surfaced by this build.
  SWEEP:        python3 pipeline/forward_flags.py --open
                -> all open flags grouped by destination.

Exit 1 (from the per-team mode) when open flags exist for that team - this
is a REMINDER gate, not a failure: run it, verify the flags, close them.
"""
import csv, os, sys

PATH = "outputs/FORWARD_FLAGS.csv"


def rows():
    if not os.path.exists(PATH):
        sys.exit(f"{PATH} missing")
    return list(csv.DictReader(open(PATH)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--open":
        from collections import defaultdict
        by = defaultdict(list)
        for r in rows():
            if r["status"] == "open":
                by[r["dest_team_dir"]].append(r)
        for dest in sorted(by):
            print(f"{dest}:")
            for r in by[dest]:
                print(f"  {r['player']} (from {r['from_team']}) - {r['note']}")
        print(f"\n{sum(len(v) for v in by.values())} open flag(s) across {len(by)} team(s)")
    else:
        team = sys.argv[1]
        hits = [r for r in rows() if r["dest_team_dir"] == team and r["status"] == "open"]
        if not hits:
            print(f"{team}: no open forward flags")
        else:
            print(f"{team}: {len(hits)} OPEN flag(s) to verify during this build:")
            for r in hits:
                print(f"  - {r['player']} (from {r['from_team']}): {r['note']}")
            print("Close them in outputs/FORWARD_FLAGS.csv (status=closed, "
                  f"closed_by={team}) once verified.")
            sys.exit(1)
