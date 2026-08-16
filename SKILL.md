---
name: public-apis-lookup
description: Search and lookup free public APIs for web development, prototyping, and data ingestion by category, authentication method, CORS support, and HTTPS.
---

# Public APIs Lookup Skill

This skill provides an offline, verified index of 1,500+ public and free APIs from the curated `public-apis/public-apis` directory. Use this skill to recommend, discover, or integrate verified public APIs into client-side apps, backend services, or demo prototypes without hallucinating fake endpoints or needing to scrape the web.

---

## When to Use

- Looking for public or free data sources for web apps (e.g. Weather, Cryptocurrency, Geocoding, Dictionaries, Anime, Animals, Finance, Sports, Open Data).
- Finding **No-Auth (Keyless)** or **CORS-enabled** APIs suitable for pure client-side vanilla JavaScript / React / Vite frontends without backend proxies or API key exposure.
- Verifying endpoint documentation URLs and authentication requirements (`No`, `apiKey`, `OAuth`).

---

## Tool Usage (`query_apis.py`)

Run the zero-dependency lookup tool via terminal:

```bash
python3 ~/.agents/skills/public-apis-lookup/scripts/query_apis.py [OPTIONS]
```

### Options & Flags

| Flag | Argument | Description | Example |
|:---|:---|:---|:---|
| `-q`, `--query` | string / regex | Search keyword or regex across names and descriptions | `--query "crypto"` |
| `-c`, `--category` | string / regex | Filter by category name | `--category "Weather"` |
| `--auth` | `no` \| `apiKey` \| `OAuth` | Filter by authentication requirement | `--auth no` |
| `--cors` | `yes` \| `no` \| `unknown` | Filter by CORS support | `--cors yes` |
| `--https` | none | Require HTTPS support | `--https` |
| `--limit` | int | Maximum results to return (default: 20) | `--limit 10` |
| `--categories` | none | List all available categories and API counts | `--categories` |
| `--json` | none | Output raw JSON instead of markdown table | `--json` |

---

## Common Query Patterns

### 1. Keyless & CORS-friendly Frontend APIs
When building client-side apps (where API keys cannot be safely stored and browser CORS is required):
```bash
python3 ~/.agents/skills/public-apis-lookup/scripts/query_apis.py -c "Finance" --auth no --cors yes
```

### 2. Search by Keyword Across All Categories
```bash
python3 ~/.agents/skills/public-apis-lookup/scripts/query_apis.py -q "dictionary" --https
```

### 3. List All Categories
```bash
python3 ~/.agents/skills/public-apis-lookup/scripts/query_apis.py --categories
```

---

## Invariants & Rules

1. **Client-Side vs Backend**:
   - For client-side single-page applications, always verify `--cors yes` and prefer `--auth no`.
   - If an API requires an `apiKey` or `OAuth`, remind the user or route requests through a backend server / edge proxy to avoid leaking secrets in client-side bundles.
2. **Deterministic Links**: Always use the exact documentation URLs returned by `query_apis.py` rather than making up endpoints.
