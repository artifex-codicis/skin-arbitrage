from Skinport_tracker import get_price,net_price

def test_24h():
    item = {
        "last_24_hours": {"median": 25.04, "volume": 6},
        "last_7_days": {"median": 26.94, "volume": 62},
    }
    assert get_price(item) == 25.04

    def test_falls_back_to_7d():
        item = {
            "last_24_hours": {"median": None, "volume": 0},
            "last_7_days": {"median": 26.94, "volume": 62},
            "last_30_days": {"median": 27.69, "volume": 308},
            "last_90_days": {"median": 28.52, "volume": 1114},
        }
        assert get_price(item) == 26.94
def test_na_yebana():
    assert net_price(50) == 42.5
def test_na_yebana2():
    assert net_price(150) == 132
def test_na_yebana3():
    assert net_price(500) == 475
