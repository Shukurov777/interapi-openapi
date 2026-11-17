# Changelog

All notable changes to the InterAPI OpenAPI specification are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-11-17

### Added
- OpenAPI 3.1 specification of the public InterAPI endpoints (API version 2.0.0, `https://api.interapi.dev`).
- Download endpoints: `/api/v1/auto`, `/api/v1/instagram`, `/api/v1/tiktok`, `/api/v1/youtube`, `/api/v1/x`,
  `/api/v1/facebook`, `/api/v1/pinterest`, `/api/v1/rutube`, `/api/v1/likee`.
- `/api/v1/youtube/search` and `/api/v1/shazam` (GET by URL, POST by file upload).
- File proxies `/api/v1/media/file`, `/api/v1/media/thumb`, `/api/v1/youtube/file`.
- `/api/v1/account`, `/api/v1/catalog`, `/api/status`, `/api/health`.
- Authentication schemes (`X-API-Key` header, Bearer token, `api` query parameter), credit prices (`x-credits`),
  error responses and real example responses.
- Postman collection, curl / Python / Node.js examples, Redoc and Swagger UI pages, validation workflow.
