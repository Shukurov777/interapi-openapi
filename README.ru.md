# InterAPI — API для скачивания видео из соцсетей (OpenAPI 3.1)

**Спецификация OpenAPI 3.1 для [InterAPI](https://interapi.dev): REST API, который превращает ссылки Instagram, TikTok, YouTube, X (Twitter), Facebook, Pinterest, RuTube и Likee в прямые ссылки на видео, фото и аудио. Есть поиск по YouTube и распознавание музыки (Shazam).**

[![OpenAPI 3.1](https://img.shields.io/badge/OpenAPI-3.1-6BA539?logo=openapiinitiative&logoColor=white)](openapi.yaml)
[![validate](https://github.com/Shukurov777/interapi-openapi/actions/workflows/validate.yml/badge.svg)](https://github.com/Shukurov777/interapi-openapi/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

English version: [README.md](README.md)

- Базовый URL: `https://api.interapi.dev`
- Авторизация: заголовок `X-API-Key`
- Оплата за запрос в кредитах (5–15 за запрос), 1000 бесплатных кредитов при регистрации, кредиты не сгорают, подписки нет
- Спецификация: [`openapi.yaml`](openapi.yaml) / [`openapi.json`](openapi.json) | Документация: [Redoc](https://shukurov777.github.io/interapi-openapi/) / [Swagger UI](https://shukurov777.github.io/interapi-openapi/swagger.html)

## Платформы

Instagram, TikTok (без водяного знака + MP3), YouTube (видео и аудио, Shorts, Music), X (Twitter), Facebook, Pinterest, RuTube, Likee, поиск по YouTube и YouTube Music, распознавание музыки Shazam по ссылке или файлу. Эндпоинт `GET /api/v1/auto` сам определяет платформу по ссылке.

## Эндпоинты и цены

| Эндпоинт | Что делает | Кредиты |
|----------|------------|---------|
| `GET /api/v1/auto` | Любая поддерживаемая ссылка, платформа определяется сама | 5–15 (как у платформы) |
| `GET /api/v1/instagram` | Reels, посты, фото, карусели | 6 |
| `GET /api/v1/tiktok` | Видео без водяного знака + MP3 | 6 |
| `GET /api/v1/youtube` | Видео и аудио YouTube | 15 |
| `GET /api/v1/x` | Видео, GIF и фото из X (Twitter) | 5 |
| `GET /api/v1/facebook` | Видео и Reels Facebook, HD / SD | 5 |
| `GET /api/v1/pinterest` | Видео, изображения, GIF Pinterest | 5 |
| `GET /api/v1/rutube` | Видео и Shorts RuTube (HLS) | 5 |
| `GET /api/v1/likee` | Видео Likee | 5 |
| `GET /api/v1/youtube/search` | Поиск по YouTube и YouTube Music | 6 |
| `GET` / `POST /api/v1/shazam` | Распознавание песни по ссылке / файлу (до 50 МБ) | 5 |
| `/api/v1/youtube/file`, `/api/v1/media/file`, `/api/v1/media/thumb` | Файловые прокси | бесплатно |
| `GET /api/v1/account` | Баланс, тариф, цены, лимиты ключа | бесплатно |
| `GET /api/v1/catalog`, `/api/status`, `/api/health` | Каталог, статус, health (без ключа) | бесплатно |

Ответы `5xx` бесплатны, ответы `4xx` стоят не больше 1 кредита.

## Быстрый старт

1. Зарегистрируйтесь на [interapi.dev](https://interapi.dev) и скопируйте API-ключ (1000 бесплатных кредитов).
2. Отправьте запрос:

```bash
curl -G "https://api.interapi.dev/api/v1/auto" \
  --data-urlencode "url=https://vt.tiktok.com/ZSQrfS4U7/" \
  -H "X-API-Key: YOUR_API_KEY"
```

```python
import requests

r = requests.get(
    "https://api.interapi.dev/api/v1/auto",
    params={"url": "https://vt.tiktok.com/ZSQrfS4U7/"},
    headers={"X-API-Key": "YOUR_API_KEY"},
    timeout=60,
)
print(r.json()["video_hd_url"])
```

Готовые скрипты (ключ берётся из переменной `INTERAPI_KEY`): [`examples/curl.sh`](examples/curl.sh), [`examples/python/download.py`](examples/python/download.py), [`examples/node/download.mjs`](examples/node/download.mjs).

## Как использовать спецификацию

- Redoc: <https://shukurov777.github.io/interapi-openapi/>
- Swagger UI: <https://shukurov777.github.io/interapi-openapi/swagger.html>
- Swagger Editor: <https://editor.swagger.io/?url=https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/openapi.yaml>
- Postman: *Import* -> *Link* -> <https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/postman/InterAPI.postman_collection.json>, затем задайте переменную коллекции `apiKey`
- Генерация SDK: `npx @openapitools/openapi-generator-cli generate -i https://raw.githubusercontent.com/Shukurov777/interapi-openapi/main/openapi.yaml -g python -o ./interapi-python`

## Ссылки

- Сайт: <https://interapi.dev>
- Документация: <https://interapi.dev/en/docs/> (на русском: <https://interapi.dev/docs/>)
- Цены: <https://interapi.dev/pricing/>
- Статус: <https://interapi.dev/status/>
- Гайды (боты для Telegram на Python и PHP): <https://interapi.dev/guides/>

InterAPI — независимый сервис и не связан с Instagram, TikTok, YouTube, X, Facebook, Pinterest, RuTube, Likee и Shazam. Названия и логотипы принадлежат их владельцам.

Лицензия спецификации и примеров: [MIT](LICENSE).
