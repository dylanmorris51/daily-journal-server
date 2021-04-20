import sqlite3
import json
from models import Entry, Mood

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
                e.date,
                m.label
            FROM entries e
            JOIN mood m
                ON m.id = e.mood_id
        """)

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['mood_id'], row['date'])

            mood = Mood(row['mood_id'], row['label'])

            entry.mood = mood.__dict__

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

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM entries
            WHERE id = ?
        """, (id,))

def get_entries_by_search(searchTerms):
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
            WHERE e.concept LIKE ? OR e.entry LIKE ? 
        """, (f"%{searchTerms}%", f"%{searchTerms}%"))

        dataset = db_cursor.fetchall()

        entries = []

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['mood_id'], row['date'])

            entries.append(entry.__dict__)

        return json.dumps(entries)

def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Entries
                ( concept, entry, mood_id, date)
            VALUES
                ( ?, ?, ?, ?)
        """, (
            new_entry['concept'],
            new_entry['entry'],
            new_entry['moodId'],
            new_entry['date']
        ))

        id = db_cursor.lastrowid

        new_entry['id'] = id
    return json.dumps(new_entry)