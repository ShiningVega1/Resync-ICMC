#!/usr/bin/env python3
"""Build static site and CMS content feed for GitHub Pages (stdlib only)."""
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
for path in ROOT.iterdir():
    if path.name in {".git", ".github", "_site", "scripts", "content", "README.md", ".pages.yml", "wrangler.toml", "_redirects"}:
        continue
    if path.is_dir():
        shutil.copytree(path, OUT / path.name)
    elif path.is_file():
        shutil.copy2(path, OUT / path.name)

feed = {}
for kind in ("announcements", "posts", "events"):
    feed[kind] = []
    for path in sorted((ROOT / "content" / kind).glob("*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(item, dict):
            raise ValueError(f"{path}: expected object")
        if not isinstance(item.get("title"), str) or not isinstance(item.get("date"), str):
            raise ValueError(f"{path}: title/date required")
        item["slug"] = path.stem
        feed[kind].append(item)
    feed[kind].sort(key=lambda x: x["date"], reverse=True)

(OUT / "content").mkdir(exist_ok=True)
(OUT / "content" / "feed.json").write_text(json.dumps(feed, ensure_ascii=False, indent=2), encoding="utf-8")
print("Built _site and content/feed.json")
