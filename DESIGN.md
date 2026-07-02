# Digital Infrastructure Insider — Project Design

## What It Is

A weekly executive briefing on global digital infrastructure for investors and operators.
Editorial focus: Nordics, UK, and Western Europe.

Delivered as a website and email newsletter. Content is researched and written by a
scheduled Claude Code agent and published via webhook to a Railway-hosted web app.

---

## Repository Structure

```
dii-web/                        # Web app + editorial state
├── main.py                     # FastAPI app (all routes and webhooks)
├── railway.json                # Railway deployment config
├── Procfile                    # Start command: uvicorn main:app
├── requirements.txt
├── beat_depth.json             # Last edition number per beat (agent reads/writes)
├── THREADS.md                  # Live story thread tracker (agent reads/writes)
├── DESIGN.md                   # This file
├── research/
│   ├── YYYY-WW.md              # Weekly research notes (written by Monday agent)
│   └── YYYY-WW-articles.json  # Publish payload (saved on failure as fallback)
├── scripts/
│   └── publish_edition.py     # Manual publish helper script
└── templates/                  # Jinja2 HTML templates
    ├── base.html
    ├── index.html
    ├── edition.html
    ├── article.html
    ├── archive.html
    └── email_briefing.html

dii-podcast/                    # Podcast companion (separate repo)
├── context/
│   └── DIGEST.md              # Editorial standards and voice guide
└── ...
```

---

## System Architecture

```
Claude Code Agent (scheduled)
        │
        │  Monday: research run → writes research/YYYY-WW.md
        │  Thursday: write + publish run (this file documents that flow)
        │
        ▼
Railway App  (agile-hope-production.up.railway.app)
  ├── FastAPI (main.py)
  ├── SQLite  (dii.db — persisted on Railway volume)
  └── Resend  (email delivery API)
```

---

## Data Flow

### Monday (Research Run)
1. Agent researches stories across beats
2. Writes `research/YYYY-WW.md` with key facts and narrative notes
3. Commits to `dii-web` repo

### Thursday (Write + Publish Run)
1. Agent reads `THREADS.md`, `beat_depth.json`, `dii-podcast/context/DIGEST.md`
2. Reads `research/YYYY-WW.md`
3. Queries `/archive` to get highest published edition number → new edition = max + 1
4. Writes 5–6 HBR-style articles (350–500 words each)
5. POSTs to `/webhook/publish` → SQLite insert + Resend email
6. Updates `THREADS.md` (append-only changelogs) and `beat_depth.json`
7. Commits and pushes to `dii-web` repo

---

## Railway App (main.py)

**Stack:** Python · FastAPI · SQLite · Jinja2 · Resend

**Environment variables:**
| Variable | Purpose |
|---|---|
| `DB_PATH` | SQLite file path (default: `dii.db`) |
| `WEBHOOK_SECRET` | Shared secret for all `/webhook/*` routes |
| `RESEND_API_KEY` | Resend API key for email delivery |
| `EMAIL_TO` | Subscriber email address |
| `EMAIL_FROM` | Sender address (default: `DII Briefing <briefing@dii.news>`) |

**Public routes:**
| Route | Description |
|---|---|
| `GET /` | Latest edition |
| `GET /edition/{num}` | Specific edition |
| `GET /article/{slug}` | Single article |
| `GET /archive` | All editions |
| `GET /health` | Health check |
| `GET /api/next-edition-num` | Returns `max(edition.num) + 1` |

**Webhook routes** (require `x-webhook-secret` header):
| Route | Description |
|---|---|
| `POST /webhook/publish` | Insert edition + articles into SQLite, send email |
| `POST /webhook/send-email` | Re-send email for latest published edition |
| `POST /webhook/notify` | Send an operational notification email |
| `DELETE /webhook/edition/{num}` | Delete an edition and its articles |

---

## Database Schema (SQLite)

```sql
editions (
  id          INTEGER PRIMARY KEY,
  num         INTEGER UNIQUE,   -- edition number (1, 2, 3 ...)
  date        TEXT,             -- YYYY-MM-DD
  published   INTEGER,          -- 1 = live
  created_at  TEXT
)

articles (
  id          INTEGER PRIMARY KEY,
  edition_id  INTEGER,          -- FK → editions
  slug        TEXT UNIQUE,      -- ep{N}-{title-slug}
  beat        TEXT,
  title       TEXT,
  subtitle    TEXT,
  body_md     TEXT,             -- Markdown, rendered to HTML at serve time
  summary     TEXT,             -- 2-sentence email preview
  bullets     TEXT,             -- JSON array of strings
  sources     TEXT,             -- JSON array of {title, url}
  thread_tags TEXT,             -- JSON array of thread IDs
  created_at  TEXT
)
```

---

## Editorial State Files

### beat_depth.json
Tracks the last edition number each beat appeared in. Agent warns if a beat has been
absent for 3+ editions.

```json
{
  "Data Infrastructure": 18,
  "Connectivity": 19,
  "Energy & Power": 19,
  "Capital & Deals": 19,
  "Nordics": 19,
  "UK & Ireland": 18,
  "Western Europe": 19,
  "European Telecom": 18
}
```

### THREADS.md
Compact state file tracking active story threads across editions. One entry per thread.
Changelogs are append-only — existing lines are never edited or deleted.

```
## thread-id: kebab-case-id
Beat: [beat name]
Status: active | dormant | closed
Summary: [current state with key figures]
Changelog:
- Edition N (YYYY-MM-DD): [what changed]
```

Status rules: active → dormant after 3+ editions with no development;
dormant → closed after 5+ editions with no development.

---

## Article Format

Each article in the publish payload:

```json
{
  "beat": "Nordics",
  "title": "Max 90 chars — lead with the insight",
  "subtitle": "One sentence that earns the read, max 120 chars",
  "body_md": "350–500 words Markdown",
  "summary": "2 plain-text sentences for email preview",
  "bullets": ["5 strings, each with a specific number or named entity"],
  "sources": [{"title": "...", "url": "..."}],
  "thread_tags": ["thread-id-1"]
}
```

Body structure: opening fact → 2–3 body paragraphs (context, mechanism, implications)
→ closing "what to watch in the next 6–18 months".

---

## Publish Payload (POST /webhook/publish)

```json
{
  "edition_num": 19,
  "date": "2026-07-02",
  "articles": [ ... ]
}
```

On success the response contains `"status": "published"` and `"email_error"` (null if
email sent, error string if not).

Fallback: if publish fails twice, the payload is saved as `research/YYYY-WW-articles.json`
and committed to the repo for manual re-publish.

---

## Voice and Editorial Standards

Defined in `dii-podcast/context/DIGEST.md`.

- **Data-first:** every claim needs a number, company name, or deal size
- **Executive lens:** frame for infrastructure investors and operators
- **Regional specificity:** Nordics, UK, Western Europe
- **Forward-looking:** end every topic with what to watch in the next 6–18 months
- **Tone:** authoritative but conversational; lead with the insight, not the context
