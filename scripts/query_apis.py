#!/usr/bin/env python3
"""
CLI tool to query and filter the local Public APIs database.
Zero external dependencies (Python standard library only).
"""

import argparse
import json
import os
import re
import sys

# Use realpath to properly resolve symlinks when invoked via ~/.local/bin/public-apis
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), "resources", "public_apis.json")

def load_data():
    if not os.path.exists(DATA_PATH):
        sys.stderr.write(f"Error: Dataset not found at {DATA_PATH}\n")
        sys.exit(1)
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def search_apis(apis, query=None, category=None, auth=None, cors=None, https_only=False, limit=20):
    results = []
    
    q_re = re.compile(query, re.IGNORECASE) if query else None
    cat_re = re.compile(category, re.IGNORECASE) if category else None
    
    for item in apis:
        if cat_re and not cat_re.search(item.get("category", "")):
            continue
            
        if q_re:
            text = f"{item.get('api', '')} {item.get('description', '')} {item.get('category', '')}"
            if not q_re.search(text):
                continue
                
        if auth is not None:
            item_auth = item.get("auth", "No").strip()
            if auth.lower() in ("no", "none", "false"):
                if item_auth.lower() not in ("no", "none", ""):
                    continue
            elif auth.lower() in ("key", "apikey"):
                if "apikey" not in item_auth.lower():
                    continue
            elif auth.lower() in ("oauth",):
                if "oauth" not in item_auth.lower():
                    continue
                    
        if cors is not None:
            item_cors = item.get("cors", "unknown").lower()
            if cors.lower() == "yes" and item_cors != "yes":
                continue
            elif cors.lower() == "no" and item_cors != "no":
                continue
                
        if https_only and not item.get("https", False):
            continue
            
        results.append(item)
        if len(results) >= limit:
            break
            
    return results

def format_markdown_table(results):
    if not results:
        return "No matching APIs found."
        
    lines = [
        "| API | Category | Description | Auth | CORS | Link |",
        "|:---|:---|:---|:---:|:---:|:---|"
    ]
    for r in results:
        api_name = r.get("api", "")
        cat = r.get("category", "")
        desc = r.get("description", "").replace("|", "/")
        auth = r.get("auth", "No")
        cors = r.get("cors", "unknown")
        url = r.get("url", "")
        link = f"[{api_name}]({url})" if url else api_name
        lines.append(f"| {link} | {cat} | {desc} | `{auth}` | {cors} | [Docs]({url}) |")
        
    return "\n".join(lines)

def list_categories(apis):
    cats = {}
    for a in apis:
        cat = a.get("category", "Uncategorized")
        cats[cat] = cats.get(cat, 0) + 1
    sorted_cats = sorted(cats.items(), key=lambda x: x[0])
    lines = ["| Category | API Count |", "|:---|:---:|"]
    for cat, count in sorted_cats:
        lines.append(f"| {cat} | {count} |")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Query public APIs repository index")
    parser.add_argument("-q", "--query", help="Regex or keyword query to search API names and descriptions")
    parser.add_argument("-c", "--category", help="Filter by category regex (e.g. Weather, Finance, Animals)")
    parser.add_argument("--auth", choices=["no", "apiKey", "OAuth"], help="Filter by auth requirement")
    parser.add_argument("--cors", choices=["yes", "no", "unknown"], help="Filter by CORS support")
    parser.add_argument("--https", action="store_true", help="Require HTTPS support")
    parser.add_argument("--limit", type=int, default=20, help="Maximum number of results (default: 20)")
    parser.add_argument("--categories", action="store_true", help="List all available categories and count")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format instead of Markdown table")
    
    args = parser.parse_args()
    apis = load_data()
    
    if args.categories:
        print(list_categories(apis))
        return
        
    results = search_apis(
        apis=apis,
        query=args.query,
        category=args.category,
        auth=args.auth,
        cors=args.cors,
        https_only=args.https,
        limit=args.limit
    )
    
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(format_markdown_table(results))

if __name__ == "__main__":
    main()
