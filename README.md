
# Skin arbitrage

## What it does
Compares CS2 prices on Skinport and LisSkins, calculates the margin after factoring in the commission.



## How
Skinport shows how much the seller will receive, but only for one item at a time and only if the price is entered manually.
The tracker calculates this automatically based on the list of items and compares it to the purchase prices on LisSkins

## How to run
```
pip install -r requirements.txt
python main.py
python -m pytest
```
## Conclusion 
The margin is **generally, but not always**, negative; the commission eats into the difference between the platforms.


## Structure
- `main.py` - entry point, runs the collection loop 
- `Skinport_volume.py` - Fetches names and prices from Skinport, which has sales of more than 100 per week
- `lis.py`- Fetches the cheapest listing price from LisSkins for the given item names
- `net_price.py`- Calculates the margin, the percentage of sales on Skinport, and the net profit
- `storage.py` - The SQL database where we store **profitable deals**
- `test_s.py`- Calculation Test and Database SQL Test 