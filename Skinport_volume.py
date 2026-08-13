import requests

URL = "https://api.skinport.com/v1/sales/history"
def get_watchlist():
    params = {"app_id":730,"currency":"USD",}
    response = requests.get(URL,params = params,headers = {"Accept-Encoding":"br"})
    data = response.json()
    watchlist= {item["market_hash_name"]:item["last_7_days"]["min"]
                 for item in data
                 if item["last_7_days"]["volume"] >= 100 and (item["last_7_days"]["min"] or 0 )>= 10
                 }
    return watchlist
