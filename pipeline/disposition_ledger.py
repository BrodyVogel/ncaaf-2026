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
    nfl_declares, research_gone, yr4_returns = set(), set(), set()
    if os.path.exists(mp):
        meta = json.load(open(mp))
        overrides = {player_norm(n) for n in meta.get("portal_withdrawal_overrides", [])}
        confirmed_gone = {player_norm(n) for n in meta.get("portal_departure_confirmed", [])}
        # early NFL declares are invisible to feeds (not portal, not yr-4); research
        # documents them in META nfl_declare_confirmed + news.md (Utah Fano/Lomu case)
        nfl_declares = {player_norm(n) for n in meta.get("nfl_declare_confirmed", [])}
        # research-confirmed departures the feeds miss for other reasons (feed year-field
        # wrong, short-surname portal name-form, academy grads) - 2026-07-15 league audit
        research_gone = {player_norm(n) for n in meta.get("departure_confirmed_research", [])}
        # yr-4 players whose RETURN is magazine-evidenced (bonus/medical year, May prints)
        yr4_returns = {player_norm(n) for n in meta.get("yr4_return_overrides_documented", [])}
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
            elif nm in nfl_declares:
                status = "NFL-DECLARE (research)"
            elif nm in research_gone:
                status = "GONE (research)"
            elif nm in yr4_returns:
                status = "RETURNS (yr4 override, May-print)"
            elif roster.get(nm) == 4:
                status = "EXPIRED(yr4)*"  # * unless magazine override recorded in news.md
            else:
                status = "RETURNS"
            rows.append((u, r["player"], grade, vol, status))
    return rows


# ---- HANDOFF HARDENING (2026-07-17, items 4b/4c) ----------------------------
GONE_CLASS = ("EXPIRED(yr4)", "PORTAL->", "PORTAL(none)", "GONE (research)",
              "NFL-DECLARE")


def validate_overrides(root):
    """4b: every META override key must be a BARE PLAYER NAME that matches its
    universe (roster for yr4/nfl/research entries; out-feed for portal entries).
    Born from the Stuhlsatz slip: a sentence-form key silently matched nothing
    and the override never applied."""
    errors = []
    mp = f"{root}/META.json"
    if not os.path.exists(mp):
        return errors
    meta = json.load(open(mp))
    outs, roster = set(), set()
    op = f"{root}/pulls/portal_2026_out.json"
    if os.path.exists(op):
        outs = {player_norm(r["firstName"] + " " + r["lastName"])
                for r in json.load(open(op))}
    rp = f"{root}/pulls/roster_2025.json"
    if os.path.exists(rp):
        roster = {player_norm(p.get("firstName", "") + " " + p.get("lastName", ""))
                  for p in json.load(open(rp))}
    # pff tape-row names: research/nfl/yr4 entries may legitimately match the
    # tape name form rather than the CFBD roster form (ECU Poku case)
    pff_names = set()
    for u in ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB"]:
        f = f"{root}/pff/unit_{u}.csv"
        if os.path.exists(f):
            for r in csv.DictReader(open(f)):
                pff_names.add(player_norm(r.get("player", "")))
    wide = roster | outs | pff_names
    fields = [("portal_withdrawal_overrides", outs, "out-feed"),
              ("portal_departure_confirmed", outs, "out-feed"),
              ("yr4_return_overrides_documented", wide, "roster/tape"),
              ("nfl_declare_confirmed", wide, "roster/tape"),
              ("departure_confirmed_research", wide, "roster/tape/out-feed")]
    for field, universe, uname in fields:
        for entry in meta.get(field, []):
            if not universe:
                continue  # no pull to validate against (rare; newcomer edge)
            nm = player_norm(entry)
            if nm in universe:
                continue
            # near match ONLY for name-like keys (<=4 tokens): suffix variants
            # such as 'Anthony Beavers Jr.' vs roster 'Anthony Beavers'.
            # Sentence-form keys must NEVER near-match (they contain the name
            # but the ledger's exact-match set ignores them - Stuhlsatz slip).
            if len(entry.split()) <= 4 and any(
                    nm and len(nm) > 8 and (nm in u or u in nm) for u in universe):
                continue
            hint = (" (sentence-form key: use the BARE player name; put the "
                    "rationale in known_name_exceptions/news.md)"
                    if len(entry.split()) > 4 else "")
            errors.append(f"OVERRIDE-KEY ERROR [{field}] '{entry[:60]}' matches no "
                          f"{uname} name{hint} - the override is NOT applying")
    return errors


def reconcile_twodeep(root, rows):
    """4c: any ledger name with a GONE-class status that appears in the 2026
    roster_two_deep.csv player column is a HARD ERROR. This automates the
    manual prints-vs-ledger reconciliation that caught Stuhlsatz (Wyoming) and
    McCoy (Hawai'i) - both two-print 2026 starters rendered EXPIRED until the
    yr4 override was set. Allowed in the two-deep: RETURNS* and WITHDREW."""
    errors = []
    tdp = f"{root}/roster_two_deep.csv"
    if not os.path.exists(tdp):
        return errors
    try:
        rdr = csv.DictReader(open(tdp))
        pcol = next((c for c in (rdr.fieldnames or []) if c.lower() == "player"), None)
        if not pcol:
            return [f"reconcile: no 'player' column in {tdp} (header: {rdr.fieldnames})"]
        two_deep = set()
        for r in rdr:
            for name in (r.get(pcol) or "").split("/"):
                nm = player_norm(name.strip())
                if nm:
                    two_deep.add(nm)
    except Exception as e:  # malformed csv must fail loud, not silent
        return [f"reconcile: cannot parse {tdp}: {e}"]
    for u, player, g, v, status in rows:
        if any(status.startswith(s) for s in GONE_CLASS):
            if player_norm(player) in two_deep:
                errors.append(
                    f"LEDGER-vs-TWO-DEEP CONFLICT [{u}] {player} ({g}/{v:.0f}): "
                    f"ledger says '{status}' but the player is IN the 2026 "
                    f"two-deep. Either the two-deep is wrong, or an override is "
                    f"missing (yr4_return_overrides / portal_withdrawal_overrides "
                    f"- bare-name key). Stuhlsatz/McCoy class.")
    return errors
# -----------------------------------------------------------------------------


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
    args = [a for a in sys.argv[1:] if a not in ("--write", "--check")]
    write = "--write" in sys.argv
    check_only = "--check" in sys.argv   # validation + reconcile only, no ledger text
    dirs = [f"snapshots/{d}" for d in args] or sorted(
        d for d in __import__("glob").glob("snapshots/*") if os.path.isdir(d))
    total_errors = 0
    for d in dirs:
        team = os.path.basename(d)
        if not os.path.isdir(d):
            print(f"{team}: snapshot dir MISSING ({d}) - check Team_Dir spelling")
            total_errors += 1
            continue
        rows = ledger(d)
        text = render(team, rows)
        flags = [r for r in rows if "ADJUDICATE" in r[4]]
        errors = validate_overrides(d) + reconcile_twodeep(d, rows)
        if write and os.path.exists(f"{d}/unit_dossiers.md"):
            t = open(f"{d}/unit_dossiers.md").read()
            marker = "## DISPOSITION LEDGER"
            if marker in t:
                t = t[:t.index(marker)].rstrip() + "\n"
            open(f"{d}/unit_dossiers.md", "w").write(t + text)
            print(f"{team}: ledger written ({len(rows)} rows, {len(flags)} to adjudicate)")
        elif check_only:
            print(f"{team}: {len(rows)} rows, {len(flags)} to adjudicate, "
                  f"{len(errors)} error(s)")
        else:
            print(f"=== {team}{text}")
        for e in errors:
            print(f"  !! {team}: {e}")
        total_errors += len(errors)
    if total_errors:
        sys.exit(f"DISPOSITION GATE FAILED: {total_errors} error(s)")
