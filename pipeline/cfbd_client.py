#!/usr/bin/env python3
"""Thin CFBD v2 client. Bearer auth, retries, raw-JSON saves, pull manifest.

Key comes from the file named by env CFBD_KEY_FILE (never printed, never committed).
Every pull() writes <outdir>/<name>.json and appends an entry to <outdir>/MANIFEST.json:
endpoint, params, UTC timestamp, HTTP status, record count. Machine-read beats web search.
"""
import json, os, time, datetime
import requests

BASE = "https://api.collegefootballdata.com"

class CFBD:
    def __init__(self, outdir: str):
        key_file = os.environ["CFBD_KEY_FILE"]
        self._headers = {"Authorization": "Bearer " + open(key_file).read().strip()}
        self.outdir = outdir
        os.makedirs(outdir, exist_ok=True)
        self.manifest_path = os.path.join(outdir, "MANIFEST.json")
        self.manifest = (json.load(open(self.manifest_path))
                         if os.path.exists(self.manifest_path) else [])

    def get(self, endpoint: str, params: dict | None = None, retries: int = 3):
        last = None
        for attempt in range(retries):
            r = requests.get(BASE + endpoint, params=params or {},
                             headers=self._headers, timeout=60)
            if r.status_code == 200:
                return r
            last = r
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt)
                continue
            break
        raise RuntimeError(f"CFBD {endpoint} {params} -> HTTP {last.status_code}: {last.text[:200]}")

    def pull(self, name: str, endpoint: str, params: dict | None = None) -> list | dict:
        """GET endpoint, save raw JSON as <name>.json, log to manifest, return parsed."""
        r = self.get(endpoint, params)
        data = r.json()
        path = os.path.join(self.outdir, name + ".json")
        with open(path, "w") as f:
            json.dump(data, f)
        self.manifest = [m for m in self.manifest if m["name"] != name]  # re-pull replaces
        self.manifest.append({
            "name": name, "endpoint": endpoint, "params": params or {},
            "pulled_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
            "http_status": r.status_code,
            "n_records": len(data) if isinstance(data, list) else 1,
            "calllimit_remaining": r.headers.get("x-calllimit-remaining"),
        })
        with open(self.manifest_path, "w") as f:
            json.dump(self.manifest, f, indent=1)
        return data
