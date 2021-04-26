from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def qty_clothes(self):
        pass

    def __add__(self, other):
        return self.qty_clothes + other.qty_clothes

class Coat(Clothes):

    @property
    def qty_clothes(self):
        return round(self.param/6.5 + 0.5, 2)


class Costume(Clothes):

    @property
    def qty_clothes(self):
        return round((2*self.param + 0.3) / 100, 2)

coat = Coat(3)
print(coat.qty_clothes)

cos = Costume(175)
print(cos.qty_clothes)

print(coat + cos)