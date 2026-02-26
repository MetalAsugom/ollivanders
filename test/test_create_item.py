from src import items

def test_normal_item():
    dexterity_vest = items.NormalItem("Dexteriy Vest", 50, 20)
    assert dexterity_vest.quality == 20 and dexterity_vest.sell_in == 50