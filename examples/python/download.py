#!/usr/bin/env python3
"""Download the media of any supported link with InterAPI.

    pip install requests
    export INTERAPI_KEY=ia_live_...       # https://interapi.dev - 1,000 free credits
    python download.py "https://vt.tiktok.com/ZSQrfS4U7/" --out downloads

Works with Instagram, TikTok, Pinterest, X (Twitter), Facebook, Likee, YouTube and RuTube links.
Optional: INTERAPI_BASE_URL (default https://api.interapi.dev).
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import requests

BASE = os.environ.get("INTERAPI_BASE_URL", "https://api.interapi.dev").rstrip("/")


def api_get(path: str, **params) -> requests.Response:
    key = os.environ.get("INTERAPI_KEY")
    if not key:
        sys.exit("Set INTERAPI_KEY first - get a key at https://interapi.dev")
    r = requests.get(f"{BASE}{path}", params=params, headers={"X-API-Key": key}, timeout=90)
    if not r.ok:
        try:
            detail = r.json().get("detail")
        except ValueError:
            detail = r.text[:200]
        sys.exit(f"HTTP {r.status_code}: {detail}")
    return r


def pick(data: dict) -> dict | None:
    """Best file of the answer: HD video, else any video, else photo, else audio."""
    media = data.get("media") or []
    by_url = {m["url"]: m for m in media}
    for field in ("video_hd_url", "video_url"):
        if data.get(field) in by_url:
            return by_url[data[field]]
        if data.get(field):
            return {"type": "video", "url": data[field], "ext": "mp4"}
    for kind in ("video", "photo", "audio"):
        items = [m for m in media if m["type"] == kind and m.get("quality") != "cover"]
        if items:
            return max(items, key=lambda m: m.get("height") or 0)
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", help="link to a post or video")
    ap.add_argument("--out", default=".", help="output directory (default: current)")
    args = ap.parse_args()

    resp = api_get("/api/v1/auto", url=args.url)  # platform is detected automatically
    data = resp.json()
    print(f"{data['source']}: {data['title'][:70]!r}")
    print(f"cost: {resp.headers.get('X-Request-Cost', '?')} credits, "
          f"balance left: {resp.headers.get('X-Balance-Remaining', '?')}")

    item = pick(data)
    if not item:
        sys.exit("No downloadable media in the answer")
    if item.get("ext") == "m3u8":  # RuTube streams over HLS
        sys.exit(f'HLS playlist - save it with: ffmpeg -i "{item["url"]}" -c copy video.mp4')

    ext = item.get("ext") or {"video": "mp4", "photo": "jpg", "audio": "mp3"}[item["type"]]
    name = re.sub(r"[^\w.-]+", "_", data["title"])[:40].strip("_") or data["source"]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{name}.{ext}"

    with requests.get(item["url"], stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(1 << 16):
                f.write(chunk)
    print(f"saved {path} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
