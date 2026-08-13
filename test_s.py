from net_price import get_net_price,profit,get_profit
from storage import connect,save_arbitrage
from pytest import approx

#Net_price
def test_net_price1():
    assert get_net_price(50) == 42.5
def test_net_price2():
    assert get_net_price(150) == 132
def test_net_price3():
    assert get_net_price(500) == 475

def test_profit():
    assert profit(10,12.75) == 2.75
def test_percent():
    assert get_profit(10,12.75) == approx(27.5)

#SQL

def test_save_read():
    conn = connect(":memory:")

    save_arbitrage(conn,"Ak-47",12,10,-0.7,-8.10)
    conn.commit()


    rows = conn.execute("SELECT name,buy,sell,profit,percent FROM arbitrage ORDER BY id").fetchall()

    assert len(rows) == 1
    assert rows[0] == ("Ak-47",12,10,-0.7,-8.10)
