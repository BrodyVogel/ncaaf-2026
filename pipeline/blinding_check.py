#!/usr/bin/env python3
"""Blinding lint (brief §4): scan snapshot text for consensus/market leakage.

Run before every snapshot freeze: python3 blinding_check.py snapshots/Kansas_State
Flags forbidden tokens for manual review (warn-list, human judgment on context —
e.g. a coach quote saying "we were ranked" is fine; a copied SP+ number is not).
Exits 1 if anything is flagged so a freeze script can gate on it.
"""
import os, re, sys

TOKENS = [
    r"\bsp\+", r"\bspplus", r"\bfpi\b", r"\bfei\b", r"\bmassey", r"team\s*rankings",
    r"\bkford", r"game\s*grader", r"win\s+total", r"over/under", r"\bo/u\b",
    r"\bodds\b", r"\bvegas\b", r"\bfuture[s]?\s+price", r"power\s+rating",
    r"power\s+ranking", r"predicted\s+order", r"picked\s+to\s+finish",
    r"preseason\s+(no\.|rank|top.?25|#)", r"\bconsensus\b",
]
SCAN_EXT = (".md", ".csv", ".json", ".txt")

SKIP_DIRS = {"pulls", "pff"}  # machine-staged raw CFBD/PFF data: surnames like "Massey"
                              # and hometowns like "Las Vegas" are not leakage. The lint
                              # targets HUMAN-AUTHORED research files.

def main(root):
    pat = re.compile("|".join(TOKENS), re.IGNORECASE)
    hits = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if not fn.endswith(SCAN_EXT):
                continue
            path = os.path.join(dirpath, fn)
            for i, line in enumerate(open(path, errors="replace"), 1):
                m = pat.search(line)
                if m:
                    hits.append((path, i, m.group(0), line.strip()[:100]))
    if hits:
        print(f"BLINDING REVIEW NEEDED - {len(hits)} flagged line(s):")
        for path, i, tok, ctx in hits:
            print(f"  {path}:{i} [{tok}] {ctx}")
        return 1
    print(f"clean: no consensus/market tokens under {root}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
