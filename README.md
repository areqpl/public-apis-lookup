# 🌐 Public APIs Lookup Skill & CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Indexed APIs](https://img.shields.io/badge/APIs-1%2C500%2B-brightgreen.svg)](resources/public_apis.json)
[![Categories](https://img.shields.io/badge/Categories-51-orange.svg)](#-indexed-categories)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-success.svg)](#)

> **Lightning-fast, offline Public APIs discovery CLI & AI agent skill.**  
> Search over **1,500+ free, public REST APIs** across 51 categories by authentication type (`No Auth`, `API Key`, `OAuth`), browser CORS support, and HTTPS.

Compatible with **Antigravity CLI**, **Claude Code**, **Cursor**, **Windsurf**, **Aider**, and **standalone terminal environments**.

---

## 📑 Table of Contents
- [⚡ Quick Installation](#-quick-installation)
- [✨ Key Features](#-key-features)
- [🚀 CLI Usage](#-cli-usage)
- [🤖 AI Coding Agent Integration](#-ai-coding-agent-integration)
- [📂 Project Structure](#-project-structure)
- [📊 Indexed Categories](#-indexed-categories)
- [📜 License](#-license)

---

## ⚡ Quick Installation

### Option 1: 1-Liner Install (Curl)
```bash
curl -sSL https://raw.githubusercontent.com/areqpl/public-apis-lookup/main/install.sh | bash
```

### Option 2: Clone & Install Locally
```bash
git clone https://github.com/areqpl/public-apis-lookup.git
cd public-apis-lookup
./install.sh
```

---

## ✨ Key Features

- **⚡ Zero Latency / Offline**: Built-in, structured JSON database with 1,580 verified APIs. No web scraping or slow search latency.
- **🛡️ Frontend & CORS Filtering**: Immediately isolate browser-ready (`CORS: Yes`) and keyless (`Auth: No`) endpoints for client-side single-page applications.
- **📦 Zero Dependencies**: Pure Python standard library (`json`, `re`, `argparse`, `sys`). No `pip install` or virtual environments required.
- **🤖 Universal Agent Skill**: Pre-configured `SKILL.md` compliant with modern agent architectures (Antigravity, Claude Code, Cursor, Windsurf).
- **📋 Multiple Output Formats**: Human-readable Markdown tables or script-friendly JSON.

---

## 🚀 CLI Usage

The `public-apis` command is available globally in your shell after installation.

### Examples

```bash
# 1. Search by keyword across all API titles and descriptions
public-apis -q "crypto"

# 2. Find Keyless & CORS-ready APIs for frontend web apps (e.g. Weather)
public-apis -c "Weather" --auth no --cors yes

# 3. Search for dictionary APIs with HTTPS support
public-apis -q "dictionary" --https

# 4. List all 51 available categories and API counts
public-apis --categories

# 5. Output raw JSON for scripting or jq parsing
public-apis -q "pokemon" --json | jq .
```

### CLI Flags Reference

| Flag | Argument | Description | Example |
|:---|:---|:---|:---|
| `-q`, `--query` | string / regex | Search keyword or regex in names & descriptions | `-q "currency"` |
| `-c`, `--category` | string / regex | Filter by category name | `-c "Finance"` |
| `--auth` | `no` \| `apiKey` \| `OAuth` | Filter by authentication type | `--auth no` |
| `--cors` | `yes` \| `no` \| `unknown` | Filter by browser CORS support | `--cors yes` |
| `--https` | none | Restrict results to HTTPS endpoints only | `--https` |
| `--limit` | integer | Maximum number of results (default: `20`) | `--limit 5` |
| `--categories` | none | Output summary table of all categories | `--categories` |
| `--json` | none | Output results as structured JSON | `--json` |

---

## 🤖 AI Coding Agent Integration

### Antigravity / Gemini CLI
This repository installs directly into `~/.agents/skills/public-apis-lookup/SKILL.md`. Your agent will proactively discover and execute `public-apis` whenever you ask for API recommendations or external data sources during frontend / backend scaffolding.

### Cursor / Claude Code / Windsurf
Add the following instruction to your project's `.cursorrules` or system prompts:
```markdown
When designing applications requiring external APIs or demo data, use `public-apis` CLI
(e.g., `public-apis -c "<Category>" --auth no --cors yes`) to find verified public endpoints.
```

---

## 📂 Project Structure

```
public-apis-lookup/
├── SKILL.md                  # Agent skill specification (YAML frontmatter + runbook)
├── README.md                 # Documentation & SEO-rich guide
├── LICENSE                   # MIT License
├── install.sh                # Universal 1-click installer
├── scripts/
│   └── query_apis.py         # Standard library CLI query tool
└── resources/
    └── public_apis.json      # Structured database of 1,580 public APIs
```

---

## 📊 Indexed Categories

Includes 51 curated categories:
`Animals`, `Anime`, `Anti-Malware`, `Art & Design`, `Authentication & Authorization`, `Blockchain`, `Books`, `Business`, `Calendar`, `Cloud Storage & File Sharing`, `Continuous Integration`, `Cryptocurrency`, `Currency Exchange`, `Data Validation`, `Development`, `Dictionaries`, `Documents & Productivity`, `Email`, `Entertainment`, `Environment`, `Finance`, `Food & Drink`, `Games & Comics`, `Geocoding`, `Government`, `Health`, `Jobs`, `Machine Learning`, `Music`, `News`, `Open Data`, `Open Source Projects`, `Patent`, `Personality`, `Phone`, `Photography`, `Programming`, `Science & Math`, `Security`, `Shopping`, `Social`, `Sports & Fitness`, `Test Data`, `Text Analysis`, `Tracking`, `Transportation`, `URL Shorteners`, `Vehicle`, `Video`, `Weather`.

---

## 📜 License

Distributed under the [MIT License](LICENSE). Based on data curated by the open-source community at [public-apis/public-apis](https://github.com/public-apis/public-apis).
