import sqlite3
from datetime import datetime


def connect(path = "arbitrage.db"):
    conn = sqlite3.connect(path)
    conn.execute("""
            CREATE TABLE IF NOT EXISTS arbitrage(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            buy REAL,
            sell REAL,
            profit REAL,
            percent REAL,
            checked_at TEXT NOT NULL
    )
    """)
    conn.commit()
    return conn

def save_arbitrage(conn,name,buy,sell,profit,percent):
    conn.execute("INSERT INTO arbitrage(name,buy,sell,profit,percent,checked_at) VALUES (?,?,?,?,?,?)",
                 (name,buy,sell,profit,percent,datetime.now().isoformat())
    )
