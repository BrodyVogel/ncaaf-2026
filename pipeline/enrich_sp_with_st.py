#!/usr/bin/env python3
"""Verify the prep-session SP+ capture against the user's browser ground truth (join on
rank, which is identical across both since it's the same ranking), then enrich the capture
with the special-teams column (§3: "handle ST simply") + component ranks.

Fails loud if any rank's overall/off/def disagree — that would mean the WebFetch capture
was stale (§14) and the blend input needs rebuilding.
"""
import csv, re, sys

def parse_paste(path):
    out = {}
    for line in open(path):
        m = re.match(r"^\s*(\d+)\.\s+(.+?)\t([\-\d.]+)\t([\-\d.]+) \((\d+)\)\t([\-\d.]+) \((\d+)\)\t([\-\d.]+) \((\d+)\)", line)
        if not m:
            continue
        rank, team, ov, off, offr, dfn, defr, st, str_ = m.groups()
        out[int(rank)] = dict(team_paste=team, overall=float(ov), off=float(off),
                              off_rank=int(offr), def_=float(dfn), def_rank=int(defr),
                              st=float(st), st_rank=int(str_))
    return out

def main(paste_path, cap_path):
    paste = parse_paste(paste_path)
    cap = list(csv.DictReader(open(cap_path)))
    assert len(paste) == 138 and len(cap) == 138, f"paste={len(paste)} cap={len(cap)}"

    mismatches = []
    for r in cap:
        rk = int(r["rank"]); p = paste[rk]
        for cap_k, paste_k in [("sp_plus_overall", "overall"), ("sp_plus_off", "off"), ("sp_plus_def", "def_")]:
            if abs(float(r[cap_k]) - p[paste_k]) > 1e-9:
                mismatches.append((rk, r["norm_key"], cap_k, r[cap_k], p[paste_k]))

    if mismatches:
        print(f"FAIL: {len(mismatches)} value mismatches (capture may be stale):")
        for m in mismatches[:20]:
            print("  rank", m[0], m[1], m[2], "capture=", m[3], "paste=", m[4])
        return 1

    # Verified. Enrich with ST + component ranks.
    fieldnames = list(cap[0].keys()) + ["sp_plus_st", "sp_plus_off_rank", "sp_plus_def_rank", "sp_plus_st_rank"]
    for r in cap:
        p = paste[int(r["rank"])]
        r["sp_plus_st"] = p["st"]; r["sp_plus_off_rank"] = p["off_rank"]
        r["sp_plus_def_rank"] = p["def_rank"]; r["sp_plus_st_rank"] = p["st_rank"]
    with open(cap_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames); w.writeheader(); w.writerows(cap)

    # Sanity: overall ≈ off - def + st (rounded to 0.1)
    bad = [r["norm_key"] for r in cap
           if abs(float(r["sp_plus_overall"]) - (float(r["sp_plus_off"]) - float(r["sp_plus_def"]) + float(r["sp_plus_st"]))) > 0.15]
    print(f"OK: 138/138 overall/off/def match the browser capture; ST + component ranks added.")
    print(f"decomposition check (overall≈off-def+st within 0.15): {138-len(bad)}/138 clean" + (f"; off: {bad}" if bad else ""))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
