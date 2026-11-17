# InterAPI — Social Media Downloader API (OpenAPI 3.1)

**OpenAPI 3.1 specification of [InterAPI](https://interapi.dev): a REST API that turns Instagram, TikTok, YouTube, X (Twitter), Facebook, Pinterest, RuTube and Likee links into direct video, photo and audio URLs, plus YouTube search and Shazam music recognition.**

[![OpenAPI 3.1](https://img.shields.io/badge/OpenAPI-3.1-6BA539?logo=openapiinitiative&logoColor=white)](openapi.yaml)
[![validate](https://github.com/Shukurov777/interapi-openapi/actions/workflows/validate.yml/badge.svg)](https://github.com/Shukurov777/interapi-openapi/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![API docs](https://img.shields.io/badge/docs-Redoc-8A2BE2)](https://shukurov777.github.io/interapi-openapi/)
[![API status](https://img.shields.io/website?url=https%3A%2F%2Fapi.interapi.dev%2Fapi%2Fhealth&up_message=online&down_message=offline&label=API)](https://interapi.dev/en/status/)

Русская версия: [README.ru.md](README.ru.md)

- Base URL: `https://api.interapi.dev`
- Auth: `X-API-Key` header
- Pay per request in credits (5-15 per request), 1,000 free credits on sign-up, credits never expire, no subscription
- Spec: [`openapi.yaml`](openapi.yaml) / [`openapi.json`](openapi.json) | Interactive docs: [Redoc](https://shukurov777.github.io/interapi-openapi/) / [Swagger UI](https://shukurov777.github.io/interapi-openapi/swagger.html)

## Supported platforms

| Platform | What you get |
|----------|--------------|
| **Instagram** | Reels, videos, photos and carousels from public posts |
| **TikTok** | Videos without watermark (SD / HD) and the MP3 track, Douyin links |
| **YouTube** | Video and audio formats (MP4, WebM, M4A, Opus), Shorts, YouTube Music |
| **X (Twitter)** | Videos in every quality, GIFs and photos |
| **Facebook** | Public videos and Reels in HD and SD, `fb.watch` links |
| **Pinterest** | Video pins, images and GIFs, `pin.it` links |
| **RuTube** | Videos and Shorts up to 1080p (HLS) |
| **Likee** | Short videos |
| **YouTube Search** | Videos, music, playlists, channels, live streams, Shorts |
| **Shazam** | Identify a song from an audio/video URL or an uploaded file |

One universal endpoint, `GET /api/v1/auto`, detects the platform from any supported link.

## Endpoints

| Endpoint | What it does | Credits | Docs |
|----------|--------------|---------|------|
| `GET /api/v1/auto` | Any supported link, platform auto-detected | 5-15 (as the detected platform) | [Docs](https://interapi.dev/en/docs/) |
| `GET /api/v1/instagram` | Instagram Reels, posts, photos, carousels | 6 | [Docs](https://interapi.dev/en/docs/instagram/) |
| `GET /api/v1/tiktok` | TikTok video without watermark + MP3 | 6 | [Docs](https://interapi.dev/en/docs/tiktok/) |
| `GET /api/v1/youtube` | YouTube video and audio formats | 15 | [Docs](https://interapi.dev/en/docs/youtube/) |
| `GET /api/v1/x` | X (Twitter) videos, GIFs, photos | 5 | [Docs](https://interapi.dev/en/docs/x/) |
| `GET /api/v1/facebook` | Facebook videos and Reels, HD / SD | 5 | [Docs](https://interapi.dev/en/docs/facebook/) |
| `GET /api/v1/pinterest` | Pinterest video, images, GIFs | 5 | [Docs](https://interapi.dev/en/docs/pinterest/) |
| `GET /api/v1/rutube` | RuTube videos and Shorts (HLS) | 5 | [Docs](https://interapi.dev/en/docs/rutube/) |
| `GET /api/v1/likee` | Likee videos | 5 | [Docs](https://interapi.dev/en/docs/likee/) |
| `GET /api/v1/youtube/search` | Search YouTube and YouTube Music | 6 | [Docs](https://interapi.dev/en/docs/youtube-search/) |
| `GET /api/v1/shazam` | Recognize a song from a URL | 5 | [Docs](https://interapi.dev/en/docs/shazam/) |
| `POST /api/v1/shazam` | Recognize a song from an uploaded file (max 50 MB) | 5 | [Docs](https://interapi.dev/en/docs/shazam/) |
| `GET /api/v1/youtube/file` | Download a YouTube audio/video file (redirect or stream) | free | [Docs](https://interapi.dev/en/docs/#files) |
| `GET /api/v1/media/file` | Download the file of an Instagram, TikTok, Pinterest, Likee, X, Facebook or RuTube post | free | [Docs](https://interapi.dev/en/docs/#files) |
| `GET /api/v1/media/thumb` | Thumbnail image of a post | free | [Docs](https://interapi.dev/en/docs/#files) |
| `GET /api/v1/account` | Balance, plan, prices and usage of your key | free | [Docs](https://interapi.dev/en/docs/#auth) |
| `GET /api/v1/catalog` | Machine-readable list of APIs and prices (no key) | free | [Docs](https://interapi.dev/en/docs/) |
| `GET /api/status` | Per-endpoint status for the last 24 hours (no key) | free | [Status](https://interapi.dev/en/status/) |
| `GET /api/health` | Health check (no key) | free | [Status](https://interapi.dev/en/status/) |

## Quick start

1. Create an account at [interapi.dev](https://interapi.dev) and copy your API key (1,000 free credits are added on sign-up).
2. Send a request. Replace `YOUR_API_KEY`.

**curl**

```bash
curl -G "https://api.interapi.dev/api/v1/auto" \
  --data-urlencode "url=https://vt.tiktok.com/ZSQrfS4U7/" \
  -H "X-API-Key: YOUR_API_KEY"
```

**Python**

```python
import requests

r = requests.get(
    "https://api.interapi.dev/api/v1/auto",
    params={"url": "https://vt.tiktok.com/ZSQrfS4U7/"},
    headers={"X-API-Key": "YOUR_API_KEY"},
    timeout=60,
)
r.raise_for_status()
data = r.json()
print(data["source"], data["video_hd_url"])
```

**JavaScript (Node.js 18+ / browser)**

```js
const params = new URLSearchParams({ url: "https://vt.tiktok.com/ZSQrfS4U7/" });
const res = await fetch(`https://api.interapi.dev/api/v1/auto?${params}`, {
  headers: { "X-API-Key": "YOUR_API_KEY" },
});
const data = await res.json();
console.log(data.source, data.video_hd_url);
```

Example response (shortened):

```json
{
  "status": "success",
  "platform": "InterAPI",
  "source": "tiktok",
  "title": "Любите маринад с уксусом? #рецепты #рецептынановыйгод",
  "media": [
    { "type": "video", "quality": "SD", "url": "https://v16m.tiktokcdn-us.com/video/tos/alisg/…" },
    { "type": "video", "quality": "HD", "url": "https://v16.tiktokcdn-us.com/video/tos/alisg/…/7044457969840295169_original.mp4" },
    { "type": "audio", "quality": "MP3", "url": "https://v16-ies-music.tiktokcdn-us.com/video/tos/alisg/…" }
  ],
  "video_hd_url": "https://v16.tiktokcdn-us.com/video/tos/alisg/…/7044457969840295169_original.mp4",
  "music_url": "https://v16-ies-music.tiktokcdn-us.com/video/tos/alisg/…",
  "thumbnail": "https://p19-common-sign.tiktokcdn-us.com/tos-alisg-p-0037/…",
  "duration_ms": 2791
}
```

Ready-to-run scripts that read the key from `INTERAPI_KEY`: [`examples/curl.sh`](examples/curl.sh), [`examples/python/download.py`](examples/python/download.py), [`examples/node/download.mjs`](examples/node/download.mjs).

## Authentication

Send your key in the `X-API-Key` header:

```
X-API-Key: ia_live_...
```

`Authorization: Bearer ia_live_...` and the `?api=ia_live_...` query parameter are accepted as well. Use the query parameter when a third-party client such as Telegram downloads a file by URL and cannot send headers. Never put your key into public front-end code. `/api/v1/catalog`, `/api/status` and `/api/health` need no key.

## Credits, pricing and response codes

- Every successful request costs **5 to 15 credits** depending on the API (see the table above). `/api/v1/auto` costs as much as the platform it detects.
- **`5xx` answers are free. `4xx` answers cost at most 1 credit.** Authentication errors and validation errors (`422`) are not charged.
- File proxies (`/api/v1/media/file`, `/api/v1/media/thumb`, `/api/v1/youtube/file`) and `/api/v1/account` are free.
- **1,000 free credits** on sign-up (limited to 30 requests per hour until the first top-up). Credits **never expire**, there is **no subscription**. Packages and payment methods: [interapi.dev/en/pricing](https://interapi.dev/en/pricing/).
- Every metered response carries `X-Request-Cost` and `X-Balance-Remaining` headers.

| Code | Meaning |
|------|---------|
| `200` | Success, the price is charged |
| `400` | Invalid or unsupported link |
| `401` | API key missing or invalid |
| `402` | Out of credits |
| `403` | Private content or disabled account |
| `404` | Post not found |
| `422` | Missing or invalid query parameter |
| `429` | Rate limit exceeded, see `Retry-After` |
| `502`, `5xx` | Source platform or server problem, not charged |

Errors share one shape: `{"detail": "Invalid TikTok URL", "request_id": "..."}`.

## Use the spec

**Browse and try it**

- Redoc reference: <https://shukurov777.github.io/interapi-openapi/>
- Swagger UI: <https://shukurov777.github.io/interapi-openapi/swagger.html>
- Swagger Editor: <https://editor.swagger.io/?url=https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/openapi.yaml>

**Raw files**

- YAML: <https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/openapi.yaml>
- JSON: <https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/openapi.json>
- Postman collection: <https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/postman/InterAPI.postman_collection.json>

**Postman** - *Import* -> *Link*, paste the Postman collection URL above (or import `openapi.yaml` to let Postman build the collection), then set the collection variable `apiKey`.

**Insomnia / Bruno / Hoppscotch** - import `openapi.yaml` from the raw URL.

**Generate an SDK**

```bash
# openapi-generator (https://openapi-generator.tech)
npx @openapitools/openapi-generator-cli generate \
  -i https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/openapi.yaml \
  -g python -o ./interapi-python

# Python client with full OpenAPI 3.1 support
pipx run openapi-python-client generate \
  --url https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/openapi.yaml

# TypeScript types
npx openapi-typescript https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/openapi.yaml -o interapi.d.ts
```

Other generators for Go, Java, PHP, Rust, C# and Kotlin work the same way: pass `openapi.yaml` and a `-g <language>` option.

**Validate locally**

```bash
npx @redocly/cli lint openapi.yaml
```

## Links

- Website: <https://interapi.dev>
- API documentation: <https://interapi.dev/en/docs/>
- Pricing: <https://interapi.dev/en/pricing/>
- Status: <https://interapi.dev/en/status/>
- Guides (Telegram bots in Python and PHP, downloader examples): <https://interapi.dev/en/guides/>

## Disclaimer

InterAPI is an independent service and is not affiliated with Instagram, TikTok, YouTube, X, Facebook, Pinterest, RuTube, Likee or Shazam. Names and logos belong to their owners. Use the API only with content you have the right to download.

## License

The specification and examples in this repository are released under the [MIT License](LICENSE). Using the API itself requires an account at [interapi.dev](https://interapi.dev).
