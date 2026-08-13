def get_net_price(sell):
    if sell <= 100:
        return sell * (1 - 0.15)
    elif sell <= 200:
        return sell * (1 - 0.12)
    else:
        return sell * (1 - 0.05)


def profit(buy,sell_net):
    return sell_net - buy




def get_profit(buy,sell_net):
    return profit(buy,sell_net)/buy *100
