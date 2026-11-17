#!/usr/bin/env bash
# InterAPI quick tour with curl.
#
#   export INTERAPI_KEY=ia_live_...        # get a key (1,000 free credits): https://interapi.dev
#   ./examples/curl.sh [video-or-post-url]
#
# Optional: INTERAPI_BASE_URL (default https://api.interapi.dev)
set -euo pipefail

: "${INTERAPI_KEY:?Set INTERAPI_KEY first - get a key at https://interapi.dev}"
BASE="${INTERAPI_BASE_URL:-https://api.interapi.dev}"
LINK="${1:-https://vt.tiktok.com/ZSQrfS4U7/}"

pp() { if command -v jq >/dev/null 2>&1; then jq "$@"; else cat; fi; }

echo "== 1. Balance, plan and prices (free) =="
curl -sS "$BASE/api/v1/account" -H "X-API-Key: $INTERAPI_KEY" | pp '{balance, plan: .plan.name, costs}'

echo
echo "== 2. Any supported link -> direct media URLs: GET /api/v1/auto =="
curl -sS -G "$BASE/api/v1/auto" \
  --data-urlencode "url=$LINK" \
  -H "X-API-Key: $INTERAPI_KEY" | pp '{source, title, video_hd_url, music_url, thumbnail}'

echo
echo "== 3. Response headers show the price of the request =="
curl -sS -G -o /dev/null -D - "$BASE/api/v1/auto" \
  --data-urlencode "url=$LINK" \
  -H "X-API-Key: $INTERAPI_KEY" | grep -i -E '^(HTTP|x-request-cost|x-balance-remaining|x-ratelimit)' || true

echo
echo "== 4. YouTube Music search: GET /api/v1/youtube/search =="
curl -sS -G "$BASE/api/v1/youtube/search" \
  --data-urlencode "q=macan" \
  --data-urlencode "filter=music" \
  --data-urlencode "limit=3" \
  -H "X-API-Key: $INTERAPI_KEY" | pp '.results[] | {title, author, url}'

echo
echo "== 5. Save the file through the free file proxy (key in ?api=) =="
curl -sS -L -G "$BASE/api/v1/media/file" \
  --data-urlencode "source=tiktok" \
  --data-urlencode "url=$LINK" \
  --data-urlencode "api=$INTERAPI_KEY" \
  -o video.mp4 -w "saved video.mp4 (%{size_download} bytes, HTTP %{http_code})\n"
