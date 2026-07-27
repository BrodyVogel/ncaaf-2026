#!/usr/bin/env python3
"""Price posted Week 0/1/GOTY spreads under the S5-validated identity translation.
fair = final_diff + 2.3*site; cover probs sigma=16.09 w/ push handling; lenses:
honest (b=1) and market-discount (b=0.895, h=3.16); conviction = min-lens.
Inputs: /tmp/lines2026.json, /tmp/g2026w{1,2}.json (CFBD pulls), current payload.
See FINDINGS_S5_2026-07-27.md. Betting gated on owner sign-off items."""
