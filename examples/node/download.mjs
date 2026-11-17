#!/usr/bin/env node
// Download the media of any supported link with InterAPI (Node.js 18+, no dependencies).
//
//   export INTERAPI_KEY=ia_live_...       // https://interapi.dev - 1,000 free credits
//   node download.mjs "https://vt.tiktok.com/ZSQrfS4U7/" [outDir]
//
// Works with Instagram, TikTok, Pinterest, X (Twitter), Facebook, Likee, YouTube and RuTube links.
// Optional: INTERAPI_BASE_URL (default https://api.interapi.dev).
import { createWriteStream } from "node:fs";
import { mkdir } from "node:fs/promises";
import { join } from "node:path";
import { Readable } from "node:stream";
import { pipeline } from "node:stream/promises";

const BASE = (process.env.INTERAPI_BASE_URL ?? "https://api.interapi.dev").replace(/\/$/, "");
const KEY = process.env.INTERAPI_KEY;
const [link, outDir = "."] = process.argv.slice(2);

if (!KEY) {
  console.error("Set INTERAPI_KEY first - get a key at https://interapi.dev");
  process.exit(1);
}
if (!link) {
  console.error('Usage: node download.mjs "<post-or-video-url>" [outDir]');
  process.exit(1);
}

// One call for every platform: the platform is detected from the link.
const res = await fetch(`${BASE}/api/v1/auto?${new URLSearchParams({ url: link })}`, {
  headers: { "X-API-Key": KEY },
});
if (!res.ok) {
  const body = await res.json().catch(() => ({}));
  console.error(`HTTP ${res.status}: ${body.detail ?? res.statusText}`);
  process.exit(1);
}
const data = await res.json();
console.log(`${data.source}: ${JSON.stringify(data.title.slice(0, 70))}`);
console.log(
  `cost: ${res.headers.get("x-request-cost") ?? "?"} credits, balance left: ${res.headers.get("x-balance-remaining") ?? "?"}`,
);

// Best file: HD video, else any video, else photo, else audio.
const media = data.media.filter((m) => m.quality !== "cover");
const best = (type) => media.filter((m) => m.type === type).sort((a, b) => (b.height ?? 0) - (a.height ?? 0))[0];
const item =
  media.find((m) => m.url === data.video_hd_url) ??
  (data.video_hd_url || data.video_url ? { url: data.video_hd_url || data.video_url, type: "video", ext: "mp4" } : null) ??
  best("video") ?? best("photo") ?? best("audio");
if (!item) {
  console.error("No downloadable media in the answer");
  process.exit(1);
}
if (item.ext === "m3u8") {
  console.error(`HLS playlist - save it with: ffmpeg -i "${item.url}" -c copy video.mp4`);
  process.exit(1);
}

const ext = item.ext ?? { video: "mp4", photo: "jpg", audio: "mp3" }[item.type];
const name = data.title.replace(/[^\p{L}\p{N}._-]+/gu, "_").slice(0, 40).replace(/^_+|_+$/g, "") || data.source;
await mkdir(outDir, { recursive: true });
const path = join(outDir, `${name}.${ext}`);

const file = await fetch(item.url);
if (!file.ok) {
  console.error(`Download failed: HTTP ${file.status}`);
  process.exit(1);
}
await pipeline(Readable.fromWeb(file.body), createWriteStream(path));
console.log(`saved ${path}`);
