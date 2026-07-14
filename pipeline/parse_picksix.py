#!/usr/bin/env python3
"""Extract Pick Six 2026 predictions (P4-only anchor input, brief §6/§11).

What Pick Six publishes for 2026: predicted conference orders + a per-team OVERALL rank
of the 68 P4 programs (top of each team page). The Game Grader tables in the General PDF
are 2025 RESULTS (retrospective, image-embedded) - not the 2026 projection - so the
anchor capture is the ordinal prediction: (conference rank, overall rank 1-68).
Rank -> points conversion happens in the anchor loader (order-statistic mapping onto the
P4 slice of the blended anchor distribution), not here.

Team pages: every 2nd page starting at page 3 (after cover + predicted order); line 1
carries "TEAM NAME ... #confrank ... #overallrank" (ties: "#6(TIE)"); Notre Dame PDF has
overall rank only. Usage: python3 parse_picksix.py "<staged dir>" <out_csv>
"""
import csv, re, subprocess, sys, unicodedata

CONFS = {"ACC": "ACC", "B10": "Big Ten", "B12": "Big 12", "SEC": "SEC"}

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)

# Pick Six team-page spellings -> norm_key overrides (fill after first run flags misses)
OVERRIDES = {"olemiss": "olemiss", "nwestern": "northwestern",
             "miami": "miamifl",            # P4 context: the ACC Miami
             "texaschristian": "tcu"}

def pdf_pages(path):
    txt = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True).stdout
    return txt.split("\f")

def parse_team_page(page):
    lines = [l for l in page.split("\n") if l.strip()][:3]
    if not lines:
        return None
    head = lines[0]
    ranks = re.findall(r"#(\d+)\s*(?:\(TIE\))?", " ".join(lines[:2]))
    name = re.split(r"#\d", head)[0].strip()
    if not name or not ranks or not name.isupper():
        return None
    return name.title(), [int(r) for r in ranks]

def main(staged_dir, out_csv):
    n2c = {r["norm_key"]: r["cfbd_school"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}
    rows, problems = [], []
    for tag, conf in CONFS.items():
        pages = pdf_pages(f"{staged_dir}/Pick Six 2026 - {tag}.pdf")
        for i in range(2, len(pages), 2):   # 0-indexed: team pages are 3,5,7,...
            parsed = parse_team_page(pages[i])
            if parsed is None:
                continue
            name, ranks = parsed
            if len(ranks) < 2:
                problems.append(f"{tag} p{i+1} '{name}': ranks={ranks}")
                continue
            k = OVERRIDES.get(norm(name), norm(name))
            cfbd = n2c.get(k)
            if cfbd is None:
                problems.append(f"{tag} p{i+1}: unmapped team '{name}' (norm={norm(name)})")
                continue
            rows.append(dict(team_raw=name, cfbd_school=cfbd, conference=conf,
                             conf_rank=ranks[0], overall_rank=ranks[1]))
    # Notre Dame: overall only
    nd = parse_team_page(pdf_pages(f"{staged_dir}/Pick Six 2026 - Notre Dame.pdf")[0])
    if nd:
        rows.append(dict(team_raw=nd[0], cfbd_school="Notre Dame", conference="FBS Independents",
                         conf_rank="", overall_rank=nd[1][0]))

    overall = sorted(r["overall_rank"] for r in rows)
    dup = {x for x in overall if overall.count(x) > 1}
    print(f"teams parsed: {len(rows)} (expect 68)")
    print(f"overall ranks: min={overall[0]} max={overall[-1]} ties(dup ranks)={sorted(dup) if dup else 'none'}")
    if problems:
        print("PROBLEMS:"); [print("  " + p) for p in problems]
    for conf in set(CONFS.values()):
        n = sum(1 for r in rows if r["conference"] == conf)
        print(f"  {conf}: {n} teams")
    rows.sort(key=lambda r: r["overall_rank"])
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["overall_rank", "conf_rank", "conference", "team_raw", "cfbd_school"])
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in w.fieldnames})
    print(f"wrote {out_csv}")
    return 0 if (len(rows) == 68 and not problems) else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
