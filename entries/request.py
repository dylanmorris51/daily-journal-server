import sqlite3
import json
from models import Entry

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                e.id,
                e.concept,
                e.entry,
                e.mood_id,
                e.date
            FROM entries e
        """)

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['mood_id'], row['date'])

            entries.append(entry.__dict__)

        return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                e.id,
                e.concept,
                e.entry,
                e.mood_id,
                e.date
            FROM entries e
            WHERE e.id = ?
        """, (id,))

        data = db_cursor.fetchone()

        entry = Entry(data['id'], data['concept'], data['entry'], data['mood_id'], data['date'])

        return json.dumps(entry.__dict__)
