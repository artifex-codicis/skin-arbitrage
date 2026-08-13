import requests
URL = "https://lis-skins.com/market_export_json/api_csgo_full.json"
def lis_skins(names):
    cheapest = {}
    response = requests.get(URL)
    data = response.json()
    for item in data["items"]:
        name = item["name"]
        price = item["price"]
        if name not in names:
            continue
        if name not in cheapest or price < cheapest[name]:
            cheapest[name] = price
    return cheapest