#!/usr/bin/env python3
"""refresh-stats.py — pull live public numbers, render honest stats SVGs.

Sources (all public APIs, no scraping, no counter services):
  GitHub REST   — stars across @Kayforkind's repos, merged PR count,
                  commits in the last year, reimagine-it release count
  npm registry  — reimagine-it downloads last week

Renders assets/stats-dark.svg and assets/stats-light.svg. Run locally or
from the weekly workflow (.github/workflows/refresh-stats.yml). Every
rendered number links its source so a reader can check it.
"""

import json
import os
import urllib.request
from datetime import date, timedelta
from pathlib import Path

GH = "https://api.github.com"
OWNER = "Kayforkind"
PKG = "reimagine-it"

def get(url, token=None):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "profile-stats-refresh",
    })
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def fmt(n):
    return f"{n:,}"

token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")

repos = get(f"{GH}/users/{OWNER}/repos?per_page=100&sort=pushed", token)
stars = sum(r["stargazers_count"] for r in repos)
n_repos = len(repos)

merged = get(f"{GH}/search/issues?q=type:pr+author:{OWNER}+is:merged&per_page=1", token)
n_prs = merged["total_count"]

since = (date.today() - timedelta(days=365)).isoformat()
commits = get(
    f"{GH}/search/commits?q=author:{OWNER}+committer-date:>{since}&per_page=1",
    token,
)
n_commits = commits["total_count"]

releases = get(f"{GH}/repos/{OWNER}/{PKG}/releases?per_page=100", token)
n_releases = len(releases)

dl = get(f"https://api.npmjs.org/downloads/point/last-week/{PKG}")
n_dl = dl["downloads"]

TODAY = date.today().isoformat()

TILES = [
    (fmt(stars), "stars across repos", f"https://github.com/{OWNER}?tab=repositories"),
    (fmt(n_prs), "PRs merged (all repos)", f"https://github.com/search?q=type%3Apr+author%3A{OWNER}+is%3Amerged"),
    (fmt(n_commits), "commits, past year", f"https://github.com/search?q=author%3A{OWNER}"),
    (fmt(n_releases), f"{PKG} releases", f"https://github.com/{OWNER}/{PKG}/releases"),
    (fmt(n_dl), "npm downloads / week", f"https://www.npmjs.com/package/{PKG}"),
    (fmt(n_repos), "public repos", f"https://github.com/{OWNER}?tab=repositories"),
]

def render(dark: bool) -> str:
    bg, panel, line = ("#0d1117", "#111823", "#1e2937") if dark else ("#ffffff", "#f6f8fa", "#d8dee4")
    ink, dim, accent = ("#e8eef5", "#8b98a9", "#2dd4bf") if dark else ("#1f2328", "#656d76", "#0e8f82")
    tiles, x = [], 24
    for value, label, href in TILES:
        tiles.append(f'''  <a href="{href}" target="_blank" rel="noopener">
    <rect x="{x}" y="86" width="192" height="128" rx="12" fill="{panel}" stroke="{line}"/>
    <text x="{x + 96}" y="146" text-anchor="middle" font-family="Consolas,'Cascadia Code',monospace" font-size="34" font-weight="700" fill="{accent}">{value}</text>
    <text x="{x + 96}" y="184" text-anchor="middle" font-family="'Segoe UI',system-ui,sans-serif" font-size="13" fill="{dim}">{label}</text>
  </a>''')
        x += 204
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1224" height="240" viewBox="0 0 1224 240" role="img" aria-label="Kazim Merchant — live shipping numbers">
  <rect width="1224" height="240" rx="14" fill="{bg}"/>
  <text x="24" y="42" font-family="'Segoe UI',system-ui,sans-serif" font-size="21" font-weight="700" fill="{ink}">Shipping in numbers</text>
  <text x="24" y="66" font-family="'Segoe UI',system-ui,sans-serif" font-size="12.5" fill="{dim}">pulled live from public APIs · refreshed weekly · every tile links its source</text>
{chr(10).join(tiles)}
  <text x="24" y="230" font-family="Consolas,monospace" font-size="10.5" fill="{dim}">generated {TODAY} by scripts/refresh-stats.py — no third-party counters, nothing fake</text>
</svg>
'''

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
(out / "stats-dark.svg").write_text(render(True), encoding="utf-8")
(out / "stats-light.svg").write_text(render(False), encoding="utf-8")

print(f"stars={stars} mergedPRs={n_prs} commits1y={n_commits} releases={n_releases} dl/week={n_dl} repos={n_repos}")
print(f"wrote {out/'stats-dark.svg'} and {out/'stats-light.svg'}")
