#!/usr/bin/env python3
"""Produce the PRODUCTION conference-offset table (full-sample 2021-2025).

The exemplar ruler and grading-time evidence discounts use FULL-sample offsets (a scale
definition, not a prediction test - LOYO belongs to the calibration in step4b, where it
guards against outcome leakage). Writes:
  data/backtest/conf_offsets_2021_2025.json   (machine-readable, unit x conference group)
Offsets are grade-point adjustments, FBS-observation-mean-centered per unit; add to a
raw PFF unit aggregate (or a player's grade, by the conference where it was EARNED)
to place it on the competition-adjusted scale.
"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step4b_calibration_conf_adjusted import fit_offsets
from pff_common import build_team_lookup

def main():
    _, lookup = build_team_lookup()
    off = fit_offsets(exclude_year=None, lookup=lookup)
    out = {u: {g: round(v, 2) for g, v in d.items()} for u, d in off.items()}
    path = "data/backtest/conf_offsets_2021_2025.json"
    with open(path, "w") as f:
        json.dump({"_meta": {"fitted": "2021-2025 as-played unit grades vs same-year final SP+, "
                             "conference-group dummies (ND treated power); FBS-mean-centered",
                             "usage": "adjusted = raw + offset[unit][group where grade was earned]"},
                   "offsets": out}, f, indent=1)
    print(f"wrote {path}")
    for u, d in out.items():
        print(f"  {u:5s} " + " ".join(f"{g}:{v:+.0f}" for g, v in sorted(d.items())))

if __name__ == "__main__":
    main()
