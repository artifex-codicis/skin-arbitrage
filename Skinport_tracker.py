import requests

URL = "https://api.skinport.com/v1/sales/history"

params = {
    "app_id":730,
    "currency":"EUR",
    "market_hash_name": "AK-47 | Redline (Field-Tested)",
}
headers = {"Accept-Encoding":"br"}


response = requests.get(URL, params=params,headers = headers)
print(response.status_code)

data = response.json()
print(data)

item = data[0]

def get_price(item):
    if item["last_24_hours"]["volume"] == 0:
        return item["last_7_days"]["median"]
    return item["last_24_hours"]["median"]

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
    net= net_price(price)
    print(f"{name}, {price} EUR, net {net} EUR")

