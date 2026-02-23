MAX_QUALITY = 50

class Inventario():

    def __init__(self):
        self.items = [
        Item("+5 Dexterity Vest", 10, 20),
        ["Aged Brie", 2, 0],
        ["Elixir of the Mongoose", 5, 7],
        ["Sulfuras, Hand of Ragnaros", 0, 80],
        ["Sulfuras, Hand of Ragnaros", -1, 80],
        ["Backstage passes to a TAFKAL80ETC concert", 15, 20],
        ["Backstage passes to a TAFKAL80ETC concert", 10, 49],
        ["Backstage passes to a TAFKAL80ETC concert", 5, 49]
        ]

    def add_item(self):
        pass

    def update_quality(self):
        pass


    def update_sell_in(self):
        pass
    
class Item():

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
 
class NormalItem(Item):
    
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2

class AgedBrie():

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_quality(self):
        while self.quailty < MAX_QUALITY:
            if self.sell_in > 0:
                self.quality += 1
            else:
                self.quality += 2
        if self.quality > MAX_QUALITY:
            self.quality = MAX_QUALITY


class Sulfuras(NormalItem):
    
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)
    
    def update_quality(self):
        pass
        


class Backstage_passes():
    
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)
    
    def update_quality(self):
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in <= 10:
            self.quality += 2
        elif self.seell_in <=5:
            self.quality += 3
        else:
            self.quality = 0
