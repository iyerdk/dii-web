#!/usr/bin/env python3
"""
Digital Infrastructure Insider — Weekly Research Web App
FastAPI + Jinja2 + SQLite, deployable on Railway
"""

import json
import os
import secrets
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Optional

import anthropic
from fastapi import Depends, FastAPI, HTTPException, Request, Header
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# ── Config ────────────────────────────────────────────────────────────────────

DB_PATH = os.environ.get("DB_PATH", "dii.db")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "change-me-in-production")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

app = FastAPI(title="Digital Infrastructure Insider")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ── Database ──────────────────────────────────────────────────────────────────

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS episodes (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                slug        TEXT UNIQUE NOT NULL,
                episode_num INTEGER NOT NULL,
                title       TEXT NOT NULL,
                subtitle    TEXT,
                date        TEXT NOT NULL,
                summary     TEXT,
                content_md  TEXT,
                shownotes   TEXT,       -- JSON blob
                mp3_url     TEXT,
                published   INTEGER DEFAULT 1,
                created_at  TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS research_context (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                episode_id  INTEGER NOT NULL,
                topic       TEXT NOT NULL,
                content     TEXT NOT NULL,
                sources     TEXT,       -- JSON array of URLs
                FOREIGN KEY (episode_id) REFERENCES episodes(id)
            );
        """)

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

init_db()

# ── Models ────────────────────────────────────────────────────────────────────

class PublishPayload(BaseModel):
    episode_num: int
    title: str
    subtitle: Optional[str] = None
    date: str                       # YYYY-MM-DD
    summary: Optional[str] = None
    content_md: str                 # full two-speaker markdown script
    shownotes: Optional[dict] = None
    mp3_url: Optional[str] = None
    research_topics: Optional[list[dict]] = None  # [{topic, content, sources}]

class ChatRequest(BaseModel):
    episode_slug: str
    section_context: str            # text of the section being asked about
    question: str

# ── Auth helper ───────────────────────────────────────────────────────────────

def verify_webhook(x_webhook_secret: str = Header(None)):
    if x_webhook_secret != WEBHOOK_SECRET:
        raise HTTPException(status_code=401, detail="Invalid webhook secret")

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    with get_db() as db:
        episodes = db.execute(
            "SELECT * FROM episodes WHERE published=1 ORDER BY episode_num DESC LIMIT 20"
        ).fetchall()
        latest = episodes[0] if episodes else None
        shownotes = json.loads(latest["shownotes"]) if latest and latest["shownotes"] else {}
    return templates.TemplateResponse(request, "index.html", {
        "latest": latest,
        "shownotes": shownotes,
        "archive": episodes[1:] if episodes else [],
    })


@app.get("/episode/{slug}", response_class=HTMLResponse)
async def episode(request: Request, slug: str):
    with get_db() as db:
        ep = db.execute(
            "SELECT * FROM episodes WHERE slug=? AND published=1", (slug,)
        ).fetchone()
        if not ep:
            raise HTTPException(status_code=404, detail="Episode not found")
        topics = db.execute(
            "SELECT * FROM research_context WHERE episode_id=?", (ep["id"],)
        ).fetchall()
        shownotes = json.loads(ep["shownotes"]) if ep["shownotes"] else {}
        archive = db.execute(
            "SELECT slug, title, date FROM episodes WHERE published=1 ORDER BY date DESC LIMIT 20"
        ).fetchall()
    return templates.TemplateResponse(request, "episode.html", {
        "ep": ep,
        "shownotes": shownotes,
        "topics": topics,
        "archive": archive,
    })


@app.post("/webhook/publish")
async def publish_episode(payload: PublishPayload, _=Depends(verify_webhook)):
    slug = f"ep{payload.episode_num}-{payload.date}"

    with get_db() as db:
        existing = db.execute("SELECT id FROM episodes WHERE slug=?", (slug,)).fetchone()
        if existing:
            db.execute("""
                UPDATE episodes SET title=?, subtitle=?, summary=?, content_md=?,
                shownotes=?, mp3_url=? WHERE slug=?
            """, (
                payload.title, payload.subtitle, payload.summary,
                payload.content_md, json.dumps(payload.shownotes or {}),
                payload.mp3_url, slug
            ))
            ep_id = existing["id"]
        else:
            cur = db.execute("""
                INSERT INTO episodes (slug, episode_num, title, subtitle, date, summary,
                content_md, shownotes, mp3_url)
                VALUES (?,?,?,?,?,?,?,?,?)
            """, (
                slug, payload.episode_num, payload.title, payload.subtitle,
                payload.date, payload.summary, payload.content_md,
                json.dumps(payload.shownotes or {}), payload.mp3_url
            ))
            ep_id = cur.lastrowid

        if payload.research_topics:
            db.execute("DELETE FROM research_context WHERE episode_id=?", (ep_id,))
            for t in payload.research_topics:
                db.execute(
                    "INSERT INTO research_context (episode_id, topic, content, sources) VALUES (?,?,?,?)",
                    (ep_id, t.get("topic"), t.get("content"), json.dumps(t.get("sources", [])))
                )

    return {"status": "published", "slug": slug, "url": f"/episode/{slug}"}


@app.delete("/webhook/episode/{slug}")
async def delete_episode(slug: str, _=Depends(verify_webhook)):
    with get_db() as db:
        ep = db.execute("SELECT id FROM episodes WHERE slug=?", (slug,)).fetchone()
        if not ep:
            raise HTTPException(status_code=404, detail="Episode not found")
        db.execute("DELETE FROM research_context WHERE episode_id=?", (ep["id"],))
        db.execute("DELETE FROM episodes WHERE slug=?", (slug,))
    return {"status": "deleted", "slug": slug}


@app.post("/api/chat")
async def chat(req: ChatRequest):
    if not ANTHROPIC_API_KEY:
        raise HTTPException(status_code=503, detail="AI chat not configured")

    with get_db() as db:
        ep = db.execute(
            "SELECT title, date, summary FROM episodes WHERE slug=?", (req.episode_slug,)
        ).fetchone()
        if not ep:
            raise HTTPException(status_code=404, detail="Episode not found")
        topics = db.execute(
            "SELECT topic, content FROM research_context WHERE episode_id="
            "(SELECT id FROM episodes WHERE slug=?)", (req.episode_slug,)
        ).fetchall()

    research_context = "\n\n".join(
        f"## {t['topic']}\n{t['content']}" for t in topics
    ) if topics else ""

    system = f"""You are the research assistant for "Digital Infrastructure Insider",
a weekly briefing on global digital infrastructure for executives and investors.

Episode: {ep['title']} ({ep['date']})
Summary: {ep['summary'] or ''}

The user is reading this section of the episode:
---
{req.section_context}
---

Full research context for this week:
---
{research_context}
---

Answer the user's question using the research above. Be concise and direct.
If the question goes beyond the week's research, say so and share what you do know."""

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=600,
        system=system,
        messages=[{"role": "user", "content": req.question}],
    )
    return {"answer": response.content[0].text}


@app.get("/health")
async def health():
    return {"status": "ok"}
