import requests

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
    "market_hash_name":"," .join(WATCHLIST),
}
headers = {"Accept-Encoding":"br"}


response = requests.get(URL, params=params,headers = headers)
print(response.status_code)

data = response.json()
print(data)

item = data[0]

def get_price(item):
   for period in ("last_24_hours","last_7_days","last_30_days"):
       median = item[period]["median"]
       if median is not None:
           return median
   return None

def net_price(price):
    if price <= 100 :
     return price * (1 - 0.15) #suka оставляем что получилось
    elif price <= 200 :
        return price * (1-0.12)
    else:
        return price * (1-0.05)

for item in data:
    name = item["market_hash_name"]
    price = get_price(item)
    if price is None:
        print(f"{name} has no price")
        continue
    net= net_price(price)
    print(f"{name}, {price} EUR, net {net:.2f} EUR")