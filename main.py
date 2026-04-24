#!/usr/bin/env python3
"""
Digital Infrastructure Insider — Web Publishing Platform
FastAPI + Jinja2 + SQLite, deployable on Railway
"""

import json
import os
import re
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import Optional

import markdown as md
from markupsafe import Markup
import resend
from fastapi import Depends, FastAPI, HTTPException, Request, Header
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# ── Config ────────────────────────────────────────────────────────────────────

DB_PATH = os.environ.get("DB_PATH", "dii.db")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "change-me-in-production")
RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
EMAIL_TO = os.environ.get("EMAIL_TO", "")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "DII Briefing <briefing@dii.news>")

app = FastAPI(title="Digital Infrastructure Insider")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
templates.env.filters["markdown"] = lambda text: Markup(
    md.markdown(text or "", extensions=["nl2br", "sane_lists"])
)

BEATS = [
    "Data Infrastructure",
    "European Telecom",
    "Connectivity",
    "Energy & Power",
    "Capital & Deals",
    "Nordics",
    "UK & Ireland",
    "Western Europe",
]

# ── Database ──────────────────────────────────────────────────────────────────

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS editions (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                num         INTEGER UNIQUE NOT NULL,
                date        TEXT NOT NULL,
                published   INTEGER DEFAULT 1,
                created_at  TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS articles (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                edition_id  INTEGER NOT NULL,
                slug        TEXT UNIQUE NOT NULL,
                beat        TEXT NOT NULL,
                title       TEXT NOT NULL,
                subtitle    TEXT,
                body_md     TEXT NOT NULL,
                summary     TEXT,
                bullets     TEXT,   -- JSON array of strings
                sources     TEXT,   -- JSON array of {title, url}
                thread_tags TEXT,   -- JSON array of thread IDs
                created_at  TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (edition_id) REFERENCES editions(id)
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

# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return re.sub(r"^-+|-+$", "", text)

def row_to_dict(row) -> dict:
    d = dict(row)
    for field in ("bullets", "sources", "thread_tags"):
        if field in d and d[field]:
            d[field] = json.loads(d[field])
        else:
            d[field] = [] if field != "sources" else []
    return d

# ── Models ────────────────────────────────────────────────────────────────────

class ArticlePayload(BaseModel):
    beat: str
    title: str
    subtitle: Optional[str] = None
    body_md: str
    summary: Optional[str] = None
    bullets: Optional[list[str]] = None
    sources: Optional[list[dict]] = None   # [{title, url}]
    thread_tags: Optional[list[str]] = None

class PublishPayload(BaseModel):
    edition_num: int
    date: str                              # YYYY-MM-DD
    articles: list[ArticlePayload]

# ── Auth ──────────────────────────────────────────────────────────────────────

def verify_webhook(x_webhook_secret: str = Header(None)):
    if x_webhook_secret != WEBHOOK_SECRET:
        raise HTTPException(status_code=401, detail="Invalid webhook secret")

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    with get_db() as db:
        edition = db.execute(
            "SELECT * FROM editions WHERE published=1 ORDER BY num DESC LIMIT 1"
        ).fetchone()
        if not edition:
            return templates.TemplateResponse(request, "index.html", {
                "edition": None, "articles": [], "beats": BEATS,
            })
        articles = [
            row_to_dict(r) for r in db.execute(
                "SELECT * FROM articles WHERE edition_id=? ORDER BY id",
                (edition["id"],)
            ).fetchall()
        ]
    return templates.TemplateResponse(request, "index.html", {
        "edition": dict(edition),
        "articles": articles,
        "beats": BEATS,
    })


@app.get("/edition/{num}", response_class=HTMLResponse)
async def edition_page(request: Request, num: int):
    with get_db() as db:
        edition = db.execute(
            "SELECT * FROM editions WHERE num=? AND published=1", (num,)
        ).fetchone()
        if not edition:
            raise HTTPException(status_code=404, detail="Edition not found")
        articles = [
            row_to_dict(r) for r in db.execute(
                "SELECT * FROM articles WHERE edition_id=? ORDER BY id",
                (edition["id"],)
            ).fetchall()
        ]
        archive = db.execute(
            "SELECT num, date FROM editions WHERE published=1 ORDER BY num DESC"
        ).fetchall()
    return templates.TemplateResponse(request, "edition.html", {
        "edition": dict(edition),
        "articles": articles,
        "beats": BEATS,
        "archive": [dict(r) for r in archive],
    })


@app.get("/article/{slug}", response_class=HTMLResponse)
async def article_page(request: Request, slug: str):
    with get_db() as db:
        article = db.execute(
            "SELECT a.*, e.num as edition_num, e.date as edition_date "
            "FROM articles a JOIN editions e ON a.edition_id=e.id WHERE a.slug=?",
            (slug,)
        ).fetchone()
        if not article:
            raise HTTPException(status_code=404, detail="Article not found")
        # Sibling articles in same edition for next/prev nav
        siblings = db.execute(
            "SELECT slug, title, beat FROM articles WHERE edition_id=? ORDER BY id",
            (article["edition_id"],)
        ).fetchall()
    art = row_to_dict(article)
    sibling_list = [dict(s) for s in siblings]
    idx = next((i for i, s in enumerate(sibling_list) if s["slug"] == slug), 0)
    return templates.TemplateResponse(request, "article.html", {
        "article": art,
        "prev_article": sibling_list[idx - 1] if idx > 0 else None,
        "next_article": sibling_list[idx + 1] if idx < len(sibling_list) - 1 else None,
    })


@app.get("/archive", response_class=HTMLResponse)
async def archive(request: Request):
    with get_db() as db:
        editions = db.execute(
            "SELECT e.*, COUNT(a.id) as article_count "
            "FROM editions e LEFT JOIN articles a ON e.id=a.edition_id "
            "WHERE e.published=1 GROUP BY e.id ORDER BY e.num DESC"
        ).fetchall()
    return templates.TemplateResponse(request, "archive.html", {
        "editions": [dict(e) for e in editions],
    })


# ── Webhooks ──────────────────────────────────────────────────────────────────

@app.post("/webhook/publish")
async def publish_edition(payload: PublishPayload, _=Depends(verify_webhook)):
    with get_db() as db:
        existing = db.execute(
            "SELECT id FROM editions WHERE num=?", (payload.edition_num,)
        ).fetchone()

        if existing:
            edition_id = existing["id"]
            db.execute(
                "UPDATE editions SET date=? WHERE id=?",
                (payload.date, edition_id)
            )
            db.execute("DELETE FROM articles WHERE edition_id=?", (edition_id,))
        else:
            cur = db.execute(
                "INSERT INTO editions (num, date) VALUES (?,?)",
                (payload.edition_num, payload.date)
            )
            edition_id = cur.lastrowid

        slugs = []
        for art in payload.articles:
            base_slug = f"ep{payload.edition_num}-{slugify(art.title)}"
            slug = base_slug
            counter = 2
            while slug in slugs:
                slug = f"{base_slug}-{counter}"
                counter += 1
            slugs.append(slug)

            db.execute("""
                INSERT INTO articles
                  (edition_id, slug, beat, title, subtitle, body_md,
                   summary, bullets, sources, thread_tags)
                VALUES (?,?,?,?,?,?,?,?,?,?)
            """, (
                edition_id, slug, art.beat, art.title, art.subtitle,
                art.body_md, art.summary,
                json.dumps(art.bullets or []),
                json.dumps(art.sources or []),
                json.dumps(art.thread_tags or []),
            ))

    return {
        "status": "published",
        "edition_num": payload.edition_num,
        "article_count": len(payload.articles),
        "url": f"/edition/{payload.edition_num}",
    }


@app.delete("/webhook/edition/{num}")
async def delete_edition(num: int, _=Depends(verify_webhook)):
    with get_db() as db:
        edition = db.execute("SELECT id FROM editions WHERE num=?", (num,)).fetchone()
        if not edition:
            raise HTTPException(status_code=404, detail="Edition not found")
        db.execute("DELETE FROM articles WHERE edition_id=?", (edition["id"],))
        db.execute("DELETE FROM editions WHERE num=?", (num,))
    return {"status": "deleted", "edition_num": num}


@app.post("/webhook/send-email")
async def send_email(_=Depends(verify_webhook)):
    if not RESEND_API_KEY:
        raise HTTPException(status_code=503, detail="RESEND_API_KEY not configured")
    if not EMAIL_TO:
        raise HTTPException(status_code=503, detail="EMAIL_TO not configured")

    with get_db() as db:
        edition = db.execute(
            "SELECT * FROM editions WHERE published=1 ORDER BY num DESC LIMIT 1"
        ).fetchone()
        if not edition:
            raise HTTPException(status_code=404, detail="No published editions")
        articles = [
            row_to_dict(r) for r in db.execute(
                "SELECT * FROM articles WHERE edition_id=? ORDER BY id",
                (edition["id"],)
            ).fetchall()
        ]

    base_url = "https://agile-hope-production.up.railway.app"
    web_url = f"{base_url}/edition/{edition['num']}"
    html = templates.get_template("email_briefing.html").render(
        edition=dict(edition),
        articles=articles,
        web_url=web_url,
        base_url=base_url,
    )

    resend.api_key = RESEND_API_KEY
    result = resend.Emails.send({
        "from": EMAIL_FROM,
        "to": [EMAIL_TO],
        "subject": f"DII Edition {edition['num']} — {edition['date']}",
        "html": html,
    })

    return {"status": "sent", "email_id": result.get("id"), "edition_num": edition["num"]}


@app.get("/health")
async def health():
    return {"status": "ok"}
