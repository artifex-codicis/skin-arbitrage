from Skinport_volume import  get_watchlist
from net_price import get_net_price,profit,get_profit
from lis import lis_skins
from storage import connect,save_arbitrage
import time
from datetime import datetime

conn = connect()

while True:
  # stores
  WATCHLIST = get_watchlist()
  cheapest = lis_skins(WATCHLIST)
  for name,sell in WATCHLIST.items():
    if name in cheapest:
      net_price = get_net_price(sell)
      buy = cheapest[name]
      p = profit(buy,net_price)
      percent = get_profit(buy,net_price)
      print(f"Name:{name},Buy Price:{buy},Net Price:{net_price},Percent:{percent:.2f},Profit:{p:.2f}")
      if percent > 0:
         save_arbitrage(conn,name,buy,net_price,p,percent)
  conn.commit()
  print(f"SAVED:{datetime.now():%H:%M:%S},pause for 30 minutes")
  time.sleep(1800)
