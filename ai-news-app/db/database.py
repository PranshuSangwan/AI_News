import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "news.db")
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS news")
cursor.execute("""
CREATE TABLE news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()


def init_db():
    # Database is initialized on import.
    return


def save_news_summary(topic, summary):
    cursor.execute(
        "INSERT INTO news (topic, summary) VALUES (?, ?)",
        (topic, summary)
    )
    conn.commit()
