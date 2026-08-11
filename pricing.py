def get_price(item):
    for period in ("last_24_hours", "last_7_days", "last_30_days", "last_90_days"):
        median = item[period]["median"]
        if median is not None:
            return median
    return None


def net_price(price):
    if price <= 100:
        return price * (1 - 0.15)  # suka оставляем что получилось
    elif price <= 200:
        return price * (1 - 0.12)
    else:
        return price * (1 - 0.05)
