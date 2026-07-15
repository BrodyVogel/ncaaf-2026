#!/usr/bin/env python3
"""Standing DEPARTURE cross-check (permanent gate; approved 2026-07-15).

Mirror of the arrival cross-check, born from the Hopper error: Tulane's dossier claimed
its best DL as returning while the team's own portal-out feed showed him at Colorado.

Rule set (adjudication order):
  1. A player in portal_2026_out WITH a destination school is GONE. A research doc or
     grades.json citing them as a returner is an ERROR - full stop.
  2. A player in portal_2026_out with destination None entered the portal but may have
     withdrawn. They count as RETURNING only with dated later evidence: presence on a
     May-printed magazine depth chart (Athlon bolding is strongest), or a dated beat
     note. Otherwise treat as GONE.
  3. Names checked: every grades.json key_player whose role isn't a transfer/add, plus
     any name on a dossier line containing a RETURN-claim token.

Usage:
  python3 pipeline/departure_check.py <Team_Dir> [...]    # gate specific snapshots
  python3 pipeline/departure_check.py                     # sweep all snapshots
Exit 1 if any un-adjudicated violation is found (grade-blocking, like blinding_check).
Adjudicated destination-None returns are declared in META.json under
"portal_withdrawal_overrides": ["Player Name", ...] with the evidence recorded in news.md.
"""
import csv, glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pff_common import player_norm

RETURN_TOKENS = ("return", "back", "anchor", "retain")


def check(root):
    team = os.path.basename(root)
    op = f"{root}/pulls/portal_2026_out.json"
    if not os.path.exists(op):
        print(f"{team}: no portal_out pull - SKIP")
        return []
    outs = {}
    for r in json.load(open(op)):
        outs[player_norm(r["firstName"] + " " + r["lastName"])] = r.get("destination")
    meta = json.load(open(f"{root}/META.json")) if os.path.exists(f"{root}/META.json") else {}
    overrides = {player_norm(n) for n in meta.get("portal_withdrawal_overrides", [])}
    name_exceptions = {player_norm(n) for n in meta.get("known_name_exceptions", [])}
    # early NFL declares: research-confirmed GONE (META nfl_declare_confirmed); citing one
    # as a returner is a violation exactly like a portal departure (Utah Fano/Lomu case)
    nfl_declares = {player_norm(n) for n in meta.get("nfl_declare_confirmed", [])}
    violations = []

    roster_names = set()
    rp = f"{root}/pulls/roster_2025.json"
    if os.path.exists(rp):
        for pl in json.load(open(rp)):
            roster_names.add(player_norm(pl.get("firstName", "") + " " + pl.get("lastName", "")))
    ip = f"{root}/pulls/portal_2026_in.json"
    if os.path.exists(ip):
        for pl in json.load(open(ip)):
            roster_names.add(player_norm(pl.get("firstName", "") + " " + pl.get("lastName", "")))

    # 1) grades.json key_players
    gp = f"{root}/grades.json"
    if os.path.exists(gp):
        for d in json.load(open(gp))["grades_detail"]:
            for kp in d.get("key_players", []):
                nm = player_norm(kp["name"])
                role = kp.get("role", "").lower()
                variant_known = any((r.startswith(nm) or nm.startswith(r))
                                    for r in roster_names if len(nm) > 8 and len(r) > 8)
                if nm in name_exceptions or any(w in role for w in ("signee", "prospect", "recruit", "fr,", "battle")):
                    pass
                elif nm not in roster_names and nm not in outs and not variant_known:
                    # unknown name = possible mis-citation (the McAlpine lesson): match by surname
                    sur = nm  # squashed; use last capitalized token of original
                    toks = kp["name"].split()
                    sur = player_norm(toks[-1]) if toks else nm
                    sur_hits = [o for o in outs if o.endswith(sur) and len(sur) > 6]
                    if sur_hits:
                        violations.append((d["unit"], kp["name"], f"UNKNOWN NAME; surname matches portal-out {sur_hits}", "key_player-misnamed"))
                    else:
                        violations.append((d["unit"], kp["name"], "UNKNOWN NAME (not in roster/arrivals/outs)", "key_player-unknown"))
                    continue
                if nm in outs and not any(w in role for w in ("transfer", "add", "signee")):
                    dest = outs[nm]
                    if dest:
                        violations.append((d["unit"], kp["name"], f"-> {dest}", "key_player"))
                    elif nm not in overrides:
                        violations.append((d["unit"], kp["name"], "portal (no dest), no override", "key_player"))
                if nm in nfl_declares:
                    violations.append((d["unit"], kp["name"], "NFL declare (research-confirmed GONE)", "key_player"))

    # 2) dossier RETURN-claim lines
    dp = f"{root}/unit_dossiers.md"
    if os.path.exists(dp):
        for line in open(dp):
            low = line.lower()
            if not any(t in low for t in RETURN_TOKENS):
                continue
            if "->" in line or "gone" in low or "departed" in low:
                continue  # line already states a departure; not a return claim
            for nm, dest in outs.items():
                if len(nm) > 5 and nm in player_norm(line):
                    if dest:
                        violations.append(("dossier", nm, f"-> {dest}", line.strip()[:70]))
                    elif nm not in overrides:
                        violations.append(("dossier", nm, "portal (no dest), no override", line.strip()[:70]))

    seen = set()
    uniq = []
    for v in violations:
        k = (v[0], v[1])
        if k not in seen:
            seen.add(k)
            uniq.append(v)
    for unit, name, status, ctx in uniq:
        print(f"  {team} [{unit}] {name}: {status}  ({ctx})")
    if not uniq:
        print(f"{team}: clean")
    return uniq


if __name__ == "__main__":
    dirs = [f"snapshots/{d}" for d in sys.argv[1:]] or sorted(
        d for d in glob.glob("snapshots/*") if os.path.isdir(d))
    total = 0
    for d in dirs:
        total += len(check(d))
    if total:
        sys.exit(f"DEPARTURE CHECK FAILED: {total} violation(s)")
    print("\ndeparture check: all clean")
