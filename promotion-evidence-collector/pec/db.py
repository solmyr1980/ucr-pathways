"""SQLite storage for documents, passages, candidate classifications,
evidence records, review decisions and duplicate relationships."""

from __future__ import annotations

import json
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT
);

CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    sha256 TEXT NOT NULL UNIQUE,
    filename TEXT NOT NULL,
    ext TEXT NOT NULL,
    size INTEGER NOT NULL,
    stored_path TEXT NOT NULL,
    uploaded_at TEXT NOT NULL,
    genre TEXT DEFAULT '',
    metadata_author TEXT DEFAULT '',
    metadata_title TEXT DEFAULT '',
    doc_date TEXT DEFAULT '',
    doc_date_source TEXT DEFAULT '',
    page_label TEXT DEFAULT 'page',
    paged INTEGER DEFAULT 1,
    page_count INTEGER DEFAULT 0,
    char_count INTEGER DEFAULT 0,
    text_status TEXT DEFAULT 'pending',
    status_detail TEXT DEFAULT '',
    sketch TEXT DEFAULT '[]',
    analyzed INTEGER DEFAULT 0,
    engine TEXT DEFAULT '',
    excluded INTEGER DEFAULT 0,
    manual_text INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS document_copies (
    id INTEGER PRIMARY KEY,
    document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    filename TEXT NOT NULL,
    uploaded_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pages (
    document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    page_no INTEGER NOT NULL,
    text TEXT NOT NULL,
    PRIMARY KEY (document_id, page_no)
);

CREATE TABLE IF NOT EXISTS passages (
    id INTEGER PRIMARY KEY,
    document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    page_no INTEGER NOT NULL,
    text TEXT NOT NULL,
    norm_hash TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_passages_doc ON passages(document_id);

CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY,
    passage_id INTEGER NOT NULL REFERENCES passages(id) ON DELETE CASCADE,
    engine TEXT NOT NULL,
    draft TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_candidates_passage ON candidates(passage_id);

CREATE TABLE IF NOT EXISTS document_relations (
    id INTEGER PRIMARY KEY,
    doc_a INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    doc_b INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    relation TEXT NOT NULL,
    similarity REAL NOT NULL,
    UNIQUE (doc_a, doc_b, relation)
);

CREATE TABLE IF NOT EXISTS evidence (
    id INTEGER PRIMARY KEY,
    fingerprint TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    claim TEXT NOT NULL,
    domains TEXT NOT NULL,
    level TEXT NOT NULL,
    level_reason TEXT NOT NULL,
    evidence_types TEXT NOT NULL,
    status TEXT NOT NULL,
    confidence TEXT NOT NULL,
    date_start TEXT DEFAULT '',
    date_end TEXT DEFAULT '',
    needs_more_evidence INTEGER DEFAULT 0,
    missing_evidence TEXT DEFAULT '',
    notes TEXT DEFAULT '',
    review_reasons TEXT DEFAULT '[]',
    review_state TEXT DEFAULT 'none',
    include_in_dossier INTEGER DEFAULT 0,
    auto_classification TEXT DEFAULT '{}',
    suggested_links TEXT DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS evidence_sources (
    evidence_id INTEGER NOT NULL REFERENCES evidence(id) ON DELETE CASCADE,
    passage_id INTEGER NOT NULL REFERENCES passages(id) ON DELETE CASCADE,
    role TEXT NOT NULL,
    self_description INTEGER DEFAULT 0,
    PRIMARY KEY (evidence_id, passage_id)
);

CREATE TABLE IF NOT EXISTS decisions (
    id INTEGER PRIMARY KEY,
    target_type TEXT NOT NULL,
    target_key TEXT NOT NULL,
    decision TEXT NOT NULL,
    payload TEXT DEFAULT '{}',
    decided_at TEXT NOT NULL,
    UNIQUE (target_type, target_key)
);
"""


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def data_dir() -> Path:
    path = Path(os.environ.get("PEC_DATA_DIR", Path(__file__).resolve().parent.parent / "pec_data"))
    path.mkdir(parents=True, exist_ok=True)
    (path / "originals").mkdir(exist_ok=True)
    return path


class Store:
    def __init__(self, path: str | Path | None = None):
        self.path = str(path or data_dir() / "evidence.sqlite3")
        self.conn = sqlite3.connect(self.path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.execute("PRAGMA journal_mode = WAL")
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    @property
    def originals_dir(self) -> Path:
        path = Path(self.path).parent / "originals"
        path.mkdir(parents=True, exist_ok=True)
        return path

    @contextmanager
    def tx(self):
        try:
            yield self.conn
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

    def q(self, sql: str, params=()) -> list[sqlite3.Row]:
        return self.conn.execute(sql, params).fetchall()

    def one(self, sql: str, params=()):
        return self.conn.execute(sql, params).fetchone()

    # Settings -------------------------------------------------------------
    def get_setting(self, key: str, default: str = "") -> str:
        row = self.one("SELECT value FROM settings WHERE key = ?", (key,))
        return row["value"] if row else default

    def set_setting(self, key: str, value: str) -> None:
        with self.tx() as c:
            c.execute(
                "INSERT INTO settings(key, value) VALUES (?, ?) "
                "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
                (key, value),
            )

    # Decisions ------------------------------------------------------------
    def record_decision(self, target_type: str, target_key: str, decision: str, payload: dict | None = None):
        with self.tx() as c:
            c.execute(
                "INSERT INTO decisions(target_type, target_key, decision, payload, decided_at) "
                "VALUES (?, ?, ?, ?, ?) ON CONFLICT(target_type, target_key) DO UPDATE SET "
                "decision = excluded.decision, payload = excluded.payload, decided_at = excluded.decided_at",
                (target_type, target_key, decision, json.dumps(payload or {}), now()),
            )

    def decisions(self, target_type: str) -> dict[str, sqlite3.Row]:
        return {r["target_key"]: r for r in self.q("SELECT * FROM decisions WHERE target_type = ?", (target_type,))}

    def reset(self) -> None:
        with self.tx() as c:
            for table in (
                "evidence_sources", "evidence", "candidates", "passages", "pages",
                "document_relations", "document_copies", "decisions", "documents",
            ):
                c.execute(f"DELETE FROM {table}")
        for f in self.originals_dir.glob("*"):
            f.unlink()

    def close(self):
        self.conn.close()
