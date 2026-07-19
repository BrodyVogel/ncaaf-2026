#!/usr/bin/env python3
"""Roster reconciliation — catch the 'Butler' failure mode.

Motivation (2026-07-19): Oregon State's grade missed Aaron Butler, a 4-star Texas WR
transfer + projected starter. Post-mortem: Butler appeared ONLY in the Athlon magazine
depth-chart line ("WR Hampton*/Butler*"); he was absent from the CFBD portal pull (which
had Hampton/Noland) and from the empty CFBD roster pull, so the grader — reading a dense
depth-chart line — picked up Hampton and dropped Butler, with no data backstop to flag it.

This script diffs each team's Athlon depth-chart names against (a) the team's grade
write-up (grades.json rationale + unit_dossiers.md) and (b) the CFBD portal_in pull, and
flags depth-chart players the GRADE never mentions — prioritising the Butler profile
(a transfer in neither the write-up nor the portal data).

Coverage: only the 21 teams that carry a parseable '[Athlon] DEPTH CHART' block. Teams
without one are listed as uncovered (would need prose-level parsing). roster_2026.json is
empty across the field (a pull gap), so it is not used.

Usage: python3 pipeline/roster_reconcile.py            # all covered teams
       python3 pipeline/roster_reconcile.py <Team_Dir> # one team
Output: outputs/staleness/ROSTER_RECONCILE.md  (+ prints a summary)
Deterministic; reads only frozen snapshot inputs.
"""
import os, re, sys, json, glob

POS = {"WR","TE","QB","RB","FB","LT","LG","C","RG","RT","OL","OT","OG","T","G",
       "DE","DT","NT","DL","EDGE","OLB","MLB","WLB","ILB","LB","SAM","MIKE","WILL",
       "CB","NB","S","FS","SS","DB","NICKEL","STAR","K","P","LS","KR","PR","ATH","H"}
CLASS_RE = re.compile(r"\((?:Sr|Jr|So|Fr|RS|GR|R-?Fr|R-?So)[^)]*\)", re.I)


def depth_chart_block(mag_path):
    if not os.path.exists(mag_path):
        return None
    lines = open(mag_path, errors="ignore").read().splitlines()
    start = None
    for i, ln in enumerate(lines):
        if "DEPTH CHART" in ln:
            start = i
            break
    if start is None:
        return None
    buf = [lines[start]]
    for ln in lines[start + 1:]:
        s = ln.strip()
        if s.startswith("## ") or re.match(r"^-\s*20\d\d", s) or s.startswith("## Phil"):
            break
        buf.append(ln)
    return " ".join(buf)


def parse_names(block):
    """Return list of dicts: {surname, raw, transfer, bold, slot} for each dc name."""
    # drop the header + group labels
    block = re.sub(r".*?DEPTH CHART[^:]*:", "", block, count=1)
    block = re.sub(r"(OFFENSE|DEFENSE|SPEC(?:IAL)?(?: TEAMS)?)\s*\(?\d*\)?\s*:", ";", block)
    SUFFIX = {"ii", "iii", "iv", "v", "jr", "sr", "jr.", "sr."}
    out = []
    # entries are separated by ';' and by ' - ' (BC-style "POS: Name - POS: Name")
    segs = re.split(r";| - (?=[A-Z]{1,5}[:/ ])", block)
    for seg in segs:
        seg = seg.strip().strip(".")
        # drop a leading 'POS:' or 'POS ' label
        seg = re.sub(r"^[A-Z]{1,5}(?:/[A-Z]{1,3})?\s*:?\s*", "", seg)
        if not seg:
            continue
        toks = seg.split()
        while toks and re.sub(r"[^A-Za-z]", "", toks[0]).upper() in POS:
            toks.pop(0)
        if not toks:
            continue
        namestr = " ".join(toks)
        for slot, part in enumerate(namestr.split("/")):
            raw = part.strip()
            if not raw:
                continue
            transfer = "*" in raw
            bold = "**" in raw
            clean = re.sub(r"\([^)]*\)", " ", raw)          # strip ALL parentheticals
            clean = clean.replace("*", " ").replace("`", " ").replace("**", " ")
            clean = re.sub(r"[^A-Za-z.'\- ]", " ", clean).strip()
            words = [w for w in clean.split() if w]
            # drop trailing generational suffix, take last real token as the name
            while len(words) > 1 and words[-1].lower().strip(".") in SUFFIX:
                words.pop()
            if not words:
                continue
            nametok = words[-1]
            surname = nametok.split(".")[-1].strip("'-")
            # artifact filter: real surname starts uppercase, >=3 letters, not a pos/class code
            if not re.match(r"^[A-Z][A-Za-z'\-]{2,}$", surname):
                continue
            if surname.upper() in POS or surname.lower() in SUFFIX:
                continue
            bold = bold or surname.isupper()
            out.append({"surname": surname, "raw": raw[:40],
                        "transfer": transfer, "bold": bold,
                        "slot": "S" if slot == 0 else "B"})
    return out


def dossier_text(team_dir):
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


def portal_surnames(team_dir):
    p = f"snapshots/{team_dir}/pulls/portal_2026_in.json"
    if not os.path.exists(p):
        return set()
    try:
        rows = json.load(open(p))
    except Exception:
        return set()
    return {str(r.get("lastName", "")).lower() for r in rows if r.get("lastName")}


def in_text(surname, text):
    return re.search(r"\b" + re.escape(surname.lower()) + r"\b", text) is not None


def reconcile(team_dir):
    block = depth_chart_block(f"snapshots/{team_dir}/magazines.md")
    if not block:
        return None
    names = parse_names(block)
    dtext = dossier_text(team_dir)
    portal = portal_surnames(team_dir)
    flags = []
    for n in names:
        in_doss = in_text(n["surname"], dtext)
        if in_doss:
            continue
        in_portal = n["surname"].lower() in portal
        # priority
        if n["transfer"] and not in_portal:
            pri = 1                      # Butler profile
        elif n["transfer"]:
            pri = 2                      # transfer dropped from write-up (but in portal data)
        elif n["slot"] == "S":
            pri = 3                      # starter (returner) not mentioned
        else:
            pri = 4                      # backup not mentioned (expected; low value)
        flags.append({**n, "in_portal": in_portal, "priority": pri})
    return {"team": team_dir, "n_names": len(names), "flags": flags}


def main():
    teams = sys.argv[1:] or [os.path.basename(os.path.dirname(p))
                             for p in sorted(glob.glob("snapshots/*/magazines.md"))]
    covered, results = [], []
    for t in teams:
        r = reconcile(t)
        if r is None:
            continue
        covered.append(t)
        results.append(r)
    write_report(results, covered)
    p1 = sum(1 for r in results for f in r["flags"] if f["priority"] == 1)
    p2 = sum(1 for r in results for f in r["flags"] if f["priority"] == 2)
    p3 = sum(1 for r in results for f in r["flags"] if f["priority"] == 3)
    print(f"RECONCILE | {len(covered)} teams w/ depth chart | "
          f"P1(transfer, no data backstop, dropped)={p1} | P2(transfer dropped)={p2} | "
          f"P3(starter unmentioned)={p3} -> outputs/staleness/ROSTER_RECONCILE.md")


def write_report(results, covered):
    L = ["# Roster reconciliation — depth-chart names the grade never mentions\n",
         "_pipeline/roster_reconcile.py. Flags Athlon depth-chart players absent from the "
         "team's grade write-up. P1 = the Butler profile (a transfer in NEITHER the "
         "write-up NOR the CFBD portal pull — magazine-only, no data backstop). Review P1/P2 "
         "by hand; P3 is often a legit omission. roster_2026.json is empty field-wide and "
         "unused; coverage is the 21 teams with a parseable depth chart._\n"]
    order = {1: "P1 transfer/no-backstop", 2: "P2 transfer dropped",
             3: "P3 starter unmentioned", 4: "P4 backup unmentioned"}
    for pri in (1, 2, 3):
        rows = [(r["team"], f) for r in results for f in r["flags"] if f["priority"] == pri]
        L.append(f"\n## {order[pri]} — {len(rows)} flag(s)\n")
        if not rows:
            L.append("_none_\n")
            continue
        L.append("| team | depth-chart entry | slot | in portal data? |")
        L.append("|---|---|---|---|")
        for team, f in sorted(rows, key=lambda x: x[0]):
            L.append(f"| {team} | `{f['raw']}` (→ {f['surname']}) | "
                     f"{'starter' if f['slot']=='S' else 'backup'} | "
                     f"{'yes' if f['in_portal'] else 'NO'} |")
    # coverage
    allteams = [os.path.basename(os.path.dirname(p))
                for p in sorted(glob.glob("snapshots/*/magazines.md"))]
    uncovered = [t for t in allteams if t not in covered]
    L.append(f"\n## Coverage\n\nCovered ({len(covered)} teams w/ Athlon depth chart): "
             + ", ".join(covered) + ".\n")
    L.append(f"\nNot covered ({len(uncovered)} teams — no parseable depth chart; would need "
             f"prose parsing): " + ", ".join(uncovered) + ".\n")
    os.makedirs("outputs/staleness", exist_ok=True)
    open("outputs/staleness/ROSTER_RECONCILE.md", "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
