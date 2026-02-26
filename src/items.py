class Inventory:
    def __init__(self, inventory):
        self.inventory = inventory


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


class Interfaz:
    def updateQuality(self):
        pass


class NormalItem(Item, Interfaz):
    def __init__(self, name, sell_in, quality):
        Item().__init__(name, sell_in, quality)

    def updateQuality(self):
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2

    def set_sell_in(self):
        self.sell_in -= 1


class BackstagePasses(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem().__init__(name, sell_in, quality)

    def updateQuality(self):
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in <= 10:
            self.quality += 2
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 0:
            self.quality = 0


class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem().__init__(name, sell_in, quality)

    def updateQuality(self):
        while self.quality != 50:
            if self.sell_in > 0:
                self.quality += 1
            elif self.sell_in < 0:
                self.quality += 2
        if self.quality > 50:
            self.quality = 50


class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem().__init__(name, sell_in, quality)

    def updateQuality(self):
        assert self.quality == 80
        pass


class Conjured(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem().__init__(name, sell_in, quality)

    def updateQuality(self):
        if self.sell_in > 0:
            self.quality -= 2
        else:
            self.quality -= 4
