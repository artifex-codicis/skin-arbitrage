import requests
import sqlite3
from datetime import datetime
import time
from pircing import get_price, net_price
conn = sqlite3.connect("prices.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS prices(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL,
        net REAL,
        volume INTEGER,
        checked_at TEXT NOT NULL
)
""")
conn.commit()
#requests
URL = "https://api.skinport.com/v1/sales/history"

WATCHLIST = [
    "Frost Avalanche",
    "The Resurrection of Shen - Wings",
    "Manifold Paradox",
    "The Devotions of Dragonus - Wings",
    "Fractal Horns of Inner Abysm"
]

params = {
    "app_id":570,
    "currency":"EUR",
    "market_hash_name":",".join(WATCHLIST),
}
headers = {"Accept-Encoding":"br"}


while True:
    try:
        response = requests.get(URL, params=params,headers = headers)
        data = response.json()
    except Exception as e:
       print(f"Error: {e}")
       time.sleep(1800)
       continue
    for item in data:
        name = item["market_hash_name"]
        price = get_price(item)
        if price is None:
            print(f"{name} has no price")
            continue
        net= net_price(price)
        volume = item["last_24_hours"]["volume"]
        print(f"{name}, {price} EUR, net {net:.2f} EUR")

        cur.execute("INSERT INTO prices(name,price,net,volume,checked_at) VALUES (?,?,?,?,?)",
                (name,price,net,volume,datetime.now().isoformat())
    )

    conn.commit()
    print(f"SAVED:{datetime.now():%H:%M:%S},pause for 30 minutes")
    time.sleep(1800)
