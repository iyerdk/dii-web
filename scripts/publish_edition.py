#!/usr/bin/env python3
"""Parse a DII research markdown file and publish it via the webhook.

Usage:
    python scripts/publish_edition.py [path/to/research/YYYY-WW.md]

If no file is given, defaults to the current ISO week's research file.

Required env vars:
    DII_WEBHOOK_URL     Full URL of the publish webhook
    DII_WEBHOOK_SECRET  Value for the x-webhook-secret header
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


def _clean(val: str) -> str:
    """Strip whitespace and any surrounding angle brackets or quotes."""
    return re.sub(r'^[\s<\'"]+|[\s>\'"]+$', '', val)

WEBHOOK_URL = _clean(os.environ.get("DII_WEBHOOK_URL", ""))
WEBHOOK_SECRET = _clean(os.environ.get("DII_WEBHOOK_SECRET", ""))


# ── File resolution ────────────────────────────────────────────────────────────

def resolve_file(arg: str | None) -> Path:
    if arg:
        return Path(arg)
    today = date.today().isocalendar()
    return Path(f"research/{today.year}-{today.week:02d}.md")


# ── Parsing ────────────────────────────────────────────────────────────────────

def _extract(pattern: str, text: str, flags: int = 0) -> str | None:
    m = re.search(pattern, text, flags)
    return m.group(1).strip() if m else None


def _url_title(url: str) -> str:
    try:
        return urlparse(url).netloc.removeprefix("www.")
    except Exception:
        return url


def parse_research(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    # ── Header fields ──
    edition_num_str = _extract(r"^Edition:\s*(\d+)", text, re.M)
    if not edition_num_str:
        sys.exit(f"ERROR: 'Edition: N' line missing in {path}")
    edition_num = int(edition_num_str)

    edition_date = _extract(r"^Generated:\s*(\d{4}-\d{2}-\d{2})", text, re.M) \
                   or date.today().isoformat()

    # ── Article sections (split on horizontal rules, skip the header block) ──
    raw_sections = re.split(r"\n---\n", text)
    articles = []

    for section in raw_sections:
        section = section.strip()
        m = re.match(r"###\s+([^:\n]+):\s+(.+)", section)
        if not m:
            continue

        beat = m.group(1).strip()
        title = m.group(2).strip()
        subtitle = _extract(r"^Subtitle:\s*(.+)", section, re.M)

        # Thread tags (comma-separated; "new" means the thread is unnamed yet)
        thread_raw = _extract(r"^Thread:\s*(.+)", section, re.M) or ""
        thread_tags = [
            t.strip() for t in thread_raw.split(",")
            if t.strip() and t.strip().lower() != "new"
        ]

        # Sources block → [{title, url}]
        sources_block = re.search(r"^Sources:\n((?:- .+\n?)+)", section, re.M)
        sources = []
        if sources_block:
            for line in sources_block.group(1).splitlines():
                url = line.lstrip("- ").strip()
                if url:
                    sources.append({"title": _url_title(url), "url": url})

        # Bullets
        bullets_block = re.search(
            r"\*\*Key facts.*?\*\*\n((?:- .+\n?)+)", section
        )
        bullets = []
        if bullets_block:
            for line in bullets_block.group(1).splitlines():
                b = line.lstrip("- ").strip()
                if b:
                    bullets.append(b)

        # Narrative → body_md; first sentence → summary
        narrative = _extract(r"\*\*Research narrative.*?\*\*\n(.+)", section, re.S)
        body_md = narrative.strip() if narrative else ""
        summary_m = re.match(r"([^.!?]+[.!?])", body_md.replace("\n", " "))
        summary = summary_m.group(1).strip() if summary_m else None

        articles.append({
            "beat": beat,
            "title": title,
            "subtitle": subtitle,
            "body_md": body_md,
            "summary": summary,
            "bullets": bullets,
            "sources": sources,
            "thread_tags": thread_tags,
        })

    return {"edition_num": edition_num, "date": edition_date, "articles": articles}


# ── API helpers ────────────────────────────────────────────────────────────────

def post_webhook(payload: dict) -> dict:
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-webhook-secret": WEBHOOK_SECRET,
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    if not WEBHOOK_URL or not WEBHOOK_SECRET:
        sys.exit("ERROR: DII_WEBHOOK_URL and DII_WEBHOOK_SECRET must be set")

    path = resolve_file(sys.argv[1] if len(sys.argv) > 1 else None)

    if not path.exists():
        sys.exit(f"Research file not found: {path} — skipping")

    print(f"Parsing: {path}")
    parsed = parse_research(path)
    edition_num = parsed["edition_num"]

    payload = {
        "edition_num": edition_num,
        "date": parsed["date"],
        "articles": parsed["articles"],
    }

    print(f"Publishing edition {edition_num} ({len(parsed['articles'])} articles, date {parsed['date']})...")
    result = post_webhook(payload)
    print(f"Published: {result.get('url')} | email_id={result.get('email_id')}")

    if result.get("email_error"):
        print(f"WARNING: email not sent — {result['email_error']}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
