#!/usr/bin/env python3
"""AUDIT QA #3: test-retest re-grade harness (measures run-to-run grade wobble).

sample mode: seeded random ~5% of (team, unit) pairs from completed grades ->
  worklist CSV. Re-grades are performed in-session against the SAME frozen snapshot,
  saved as snapshots/<team>/grades_retest.json (same schema, only sampled units).
compare mode: joins original vs retest, reports |delta| distribution.
  Acceptance gate: median |delta| <= 5 and p90 |delta| <= 8 percentile points;
  otherwise tighten the template before finalizing ratings (audit round 1, item 3).

Usage:
  python3 qa_regrade_sample.py sample <snapshots_dir> <out_csv> [--frac 0.05] [--seed 26]
  python3 qa_regrade_sample.py compare <snapshots_dir>
"""
import csv, json, os, random, sys

def units_of(gj):
    return list(gj.get("units", {}).keys())

def main():
    mode, snaps = sys.argv[1], sys.argv[2]
    if mode == "sample":
        out = sys.argv[3]
        frac = float(sys.argv[sys.argv.index("--frac") + 1]) if "--frac" in sys.argv else 0.05
        seed = int(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else 26
        pairs = []
        for d in sorted(os.listdir(snaps)):
            p = os.path.join(snaps, d, "grades.json")
            if os.path.exists(p):
                gj = json.load(open(p))
                pairs += [(gj["team"], u) for u in units_of(gj)]
        rng = random.Random(seed)
        k = max(1, round(frac * len(pairs)))
        sample = rng.sample(sorted(pairs), k)
        with open(out, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["team", "unit"]); w.writerows(sorted(sample))
        print(f"sampled {k} of {len(pairs)} graded units (seed {seed}) -> {out}")
    elif mode == "compare":
        deltas = []
        for d in sorted(os.listdir(snaps)):
            p0 = os.path.join(snaps, d, "grades.json")
            p1 = os.path.join(snaps, d, "grades_retest.json")
            if os.path.exists(p0) and os.path.exists(p1):
                g0, g1 = json.load(open(p0)), json.load(open(p1))
                for u, v in g1.get("units", {}).items():
                    if u in g0.get("units", {}):
                        deltas.append((g0["team"], u, abs(g0["units"][u]["grade"] - v["grade"])))
        if not deltas:
            sys.exit("no retest files found")
        ds = sorted(x[2] for x in deltas)
        med = ds[len(ds)//2]; p90 = ds[int(0.9 * (len(ds)-1))]
        ok = med <= 5 and p90 <= 8
        print(f"retest n={len(deltas)}: median |Δ|={med}, p90 |Δ|={p90} -> "
              f"{'PASS' if ok else 'FAIL - tighten template before finalizing'}")
        for t, u, d in sorted(deltas, key=lambda x: -x[2])[:10]:
            print(f"  {t} {u}: Δ={d}")

if __name__ == "__main__":
    main()
