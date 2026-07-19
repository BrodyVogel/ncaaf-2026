#!/usr/bin/env python3
"""Portal reconciliation (all 138 teams) — the complement to roster_reconcile.py.

roster_reconcile catches players the MAGAZINE had that the grade dropped (e.g. Butler,
who was magazine-only). This catches the other direction: incoming transfers the CFBD
PORTAL pull had that never made it into the roster model OR the grade write-up.

The two-deep CSV (snapshots/<T>/roster_two_deep.csv) is the structured roster the grade
was built from (the OurLads/magazine cross-reference artifact — present for all 138 teams).
So a portal-in transfer whose surname is in NEITHER the two-deep NOR the write-up
(grades.json + unit_dossiers.md) was FULLY DROPPED — captured nowhere. Those are the
candidates.

Relevance tiers (owner: irrelevant transfers the grade rightly ignored should not be
chased; moderate+ ones should be web-verified before trusting the flag):
  HIGH  rating >= 0.90 or stars >= 4      -> web-verify each
  MOD   0.86 <= rating < 0.90             -> web-verify each
  LOW   rating < 0.86 / unrated           -> likely irrelevant depth; list, don't chase
Also reported: 'seen not detailed' = in the two-deep but not the write-up (the assembler
captured them; the grader chose not to discuss — usually a correct omission of depth).

The CFBD portal pull is not blindly trusted: HIGH/MOD flags are for human/web
confirmation that the player actually transferred there and is correctly placed.

Usage: python3 pipeline/portal_reconcile.py            # all teams
       python3 pipeline/portal_reconcile.py <Team_Dir>
Output: outputs/staleness/PORTAL_RECONCILE.md. Deterministic.
"""
import os, re, sys, json, csv, glob

PREMIUM = {"QB", "EDGE", "CB", "WR", "OT", "DL", "RB"}
SUFFIX = {"jr", "sr", "ii", "iii", "iv", "v"}


def match_surname(fullname_or_last):
    """Last real token of a name, stripping generational suffixes. CFBD stores the suffix
    IN lastName ('Moore Jr.'), so 'Moore Jr.' -> 'moore'; 'Van Dorselaer' -> 'dorselaer'."""
    words = [w.strip("'-.") for w in str(fullname_or_last).split() if w.strip("'-.")]
    while len(words) > 1 and words[-1].lower() in SUFFIX:
        words.pop()
    return words[-1].lower() if words else ""


def twodeep_surnames(team_dir):
    p = f"snapshots/{team_dir}/roster_two_deep.csv"
    out = set()
    if not os.path.exists(p):
        return out
    for r in csv.DictReader(open(p)):
        nm = (r.get("player") or "").strip()
        if nm:
            out.add(match_surname(nm))
    return out


def writeup_text(team_dir):
    t = ""
    gp = f"snapshots/{team_dir}/grades.json"
    if os.path.exists(gp):
        d = json.load(open(gp))
        for det in d.get("grades_detail", []):
            t += " ".join(det.get("rationale_bullets") or [])
            t += " " + " ".join(k.get("name", "") for k in (det.get("key_players") or []))
            t += " " + " ".join(det.get("data_gaps") or [])
            t += " " + (det.get("g5_guard_note") or "")
    ud = f"snapshots/{team_dir}/unit_dossiers.md"
    if os.path.exists(ud):
        t += " " + open(ud, errors="ignore").read()
    return t.lower()


def tier(rating, stars, pos):
    r = rating or 0
    s = stars or 0
    if r >= 0.90 or s >= 4:
        return "HIGH"
    if r >= 0.86 or (s >= 3 and pos in PREMIUM and r >= 0.85):
        return "MOD"
    return "LOW"


def reconcile(team_dir):
    p = f"snapshots/{team_dir}/pulls/portal_2026_in.json"
    if not os.path.exists(p):
        return None
    try:
        rows = json.load(open(p))
    except Exception:
        return None
    td = twodeep_surnames(team_dir)
    wu = writeup_text(team_dir)
    dropped, seen_not_detailed = [], 0
    for r in rows:
        sn = match_surname(r.get("lastName", ""))
        if not sn or len(sn) < 3:
            continue
        in_td = sn in td
        in_wu = re.search(r"\b" + re.escape(sn) + r"\b", wu) is not None
        if in_td:
            if not in_wu:
                seen_not_detailed += 1
            continue
        if in_wu:
            continue
        # fully dropped
        dropped.append({
            "team": team_dir,
            "name": (str(r.get("firstName", "")) + " " + sn).strip(),
            "pos": r.get("position", "?"),
            "origin": r.get("origin", "?"),
            "rating": r.get("rating") or 0,
            "stars": r.get("stars") or 0,
            "elig": r.get("eligibility", "?"),
            "date": (r.get("transferDate") or "")[:10],
            "tier": tier(r.get("rating"), r.get("stars"), r.get("position", "?")),
        })
    return {"team": team_dir, "n_portal": len(rows), "dropped": dropped,
            "seen_not_detailed": seen_not_detailed}


def main():
    teams = sys.argv[1:] or sorted(
        os.path.basename(os.path.dirname(os.path.dirname(p)))
        for p in glob.glob("snapshots/*/pulls/portal_2026_in.json"))
    results = [reconcile(t) for t in teams]
    results = [r for r in results if r]
    write_report(results)
    allflags = [f for r in results for f in r["dropped"]]
    hi = [f for f in allflags if f["tier"] == "HIGH"]
    mod = [f for f in allflags if f["tier"] == "MOD"]
    low = [f for f in allflags if f["tier"] == "LOW"]
    snd = sum(r["seen_not_detailed"] for r in results)
    print(f"PORTAL RECONCILE | {len(results)} teams | fully-dropped transfers: "
          f"HIGH={len(hi)} MOD={len(mod)} LOW={len(low)} | "
          f"seen-not-detailed (captured, not discussed)={snd} -> "
          f"outputs/staleness/PORTAL_RECONCILE.md")


def write_report(results):
    allflags = [f for r in results for f in r["dropped"]]
    L = ["# Portal reconciliation — transfers the data had that the grade fully dropped\n",
         "_pipeline/portal_reconcile.py. A 'fully dropped' transfer is in the CFBD portal "
         "pull but in NEITHER the team's two-deep CSV NOR the grade write-up. HIGH/MOD tiers "
         "warrant one web source to confirm they actually transferred there + are correctly "
         "placed (the CFBD pull is not blindly trusted). LOW = likely irrelevant depth. "
         "'seen-not-detailed' (in the two-deep but not discussed) is usually a correct "
         "omission and is only counted, not listed._\n"]
    for tname in ("HIGH", "MOD"):
        fl = sorted([f for f in allflags if f["tier"] == tname],
                    key=lambda x: (-x["rating"], x["team"]))
        L.append(f"\n## {tname} leverage — {len(fl)} fully-dropped (web-verify)\n")
        if not fl:
            L.append("_none_\n")
            continue
        L.append("| team | player | pos | origin | rating | stars | elig | date | verified? |")
        L.append("|---|---|---|---|---|---|---|---|---|")
        for f in fl:
            L.append(f"| {f['team']} | {f['name']} | {f['pos']} | {f['origin']} | "
                     f"{f['rating']:.3f} | {f['stars']} | {f['elig']} | {f['date']} | |")
    # LOW: summarize by team count only (avoid a wall of irrelevant depth)
    low = [f for f in allflags if f["tier"] == "LOW"]
    L.append(f"\n## LOW leverage — {len(low)} fully-dropped (likely irrelevant depth; not listed)\n")
    from collections import Counter
    byteam = Counter(f["team"] for f in low)
    L.append("Top teams by LOW-flag count: " +
             ", ".join(f"{t} ({n})" for t, n in byteam.most_common(12)) + ".\n")
    snd = sum(r["seen_not_detailed"] for r in results)
    L.append(f"\n## Seen-not-detailed\n\n{snd} transfers are in the two-deep CSV but not "
             "discussed in the write-up — captured by the roster model, the grader chose "
             "not to detail them (usually correct: depth/camp bodies). Not flagged.\n")
    os.makedirs("outputs/staleness", exist_ok=True)
    open("outputs/staleness/PORTAL_RECONCILE.md", "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
