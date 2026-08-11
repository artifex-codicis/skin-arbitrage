import sqlite3
from datetime import datetime


def connect(path = "prices.db"):
    conn = sqlite3.connect(path)
    conn.execute("""
            CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL,
            net REAL,
            volume REAL,
            checked_at TEXT NOT NULL
    )
    """)
    conn.commit()
    return conn

def save_price(conn,name,price,net,volume):
    conn.execute("INSERT INTO prices(name,price,net,volume,checked_at) VALUES (?,?,?,?,?)",
                 (name,price,net,volume,datetime.now().isoformat())
    )
