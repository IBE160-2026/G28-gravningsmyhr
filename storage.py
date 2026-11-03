"""Transactional key/value persistence. SQLite locally; PostgreSQL in production."""
import json
import os
import sqlite3
from contextlib import contextmanager


@contextmanager
def transaction():
    url = os.environ.get('DATABASE_URL')
    if os.environ.get('VERCEL') and not url:
        raise RuntimeError('DATABASE_URL mangler. Produksjon krever PostgreSQL.')
    db = None
    try:
        if url:
            import psycopg
            db = psycopg.connect(url, connect_timeout=10)
            db.execute('CREATE TABLE IF NOT EXISTS app_state (id integer PRIMARY KEY, body text NOT NULL)')
            db.execute("INSERT INTO app_state VALUES (1, %s) ON CONFLICT DO NOTHING", (json.dumps(dict(users={}, sessions={}, games={}, classes={}, attempts={})),))
            raw = db.execute('SELECT body FROM app_state WHERE id=1 FOR UPDATE').fetchone()[0]
        else:
            db = sqlite3.connect(os.environ.get('BEER_DB', 'beergame.sqlite3'), timeout=20)
            db.execute('CREATE TABLE IF NOT EXISTS app_state (id integer PRIMARY KEY, body text NOT NULL)')
            db.commit()
            db.execute('BEGIN IMMEDIATE')
            db.execute('INSERT OR IGNORE INTO app_state VALUES (1, ?)', (json.dumps(dict(users={}, sessions={}, games={}, classes={}, attempts={})),))
            raw = db.execute('SELECT body FROM app_state WHERE id=1').fetchone()[0]
        state = json.loads(raw)
        yield state
        db.execute('UPDATE app_state SET body=' + ('%s' if url else '?') + ' WHERE id=1', (json.dumps(state),))
        db.commit()
    except BaseException:
        if db is not None:
            db.rollback()
        raise
    finally:
        if db is not None:
            db.close()
