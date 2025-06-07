import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path("storage/tasks.db")

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self._init_db()
    
    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            deadline TEXT,
            created_at TEXT NOT NULL,
            is_completed INTEGER DEFAULT 0
        )
        """)
        self.conn.commit()
    
    def add_task(self, user_id: int, title: str, category: str, deadline: str = None):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (user_id, title, category, deadline, created_at) VALUES (?, ?, ?, ?, ?)",
            (user_id, title, category, deadline, datetime.now().isoformat())
        )
        self.conn.commit()
        return cursor.lastrowid
    
    # Другие методы: get_tasks, complete_task, delete_task и т.д.
