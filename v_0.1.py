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