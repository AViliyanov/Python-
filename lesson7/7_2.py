from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, h, n):
        self.h = h
        self.n = n

    @abstractmethod
    def coat(self):
        return float(self.n) / 6.5 + 0.5

    @abstractmethod
    def suit(self):
        return 2*float(self.h) + 0.3

    @property
    def total(self):
        total_all = self.coat() + self.suit()
        return total_all

class Num(Clothes):
    def coat(self):
        return float(self.n) / 6.5 + 0.5
    def suit(self):
        return 2*float(self.h) + 0.3




total = Num(2,6.5)
print(f"Coat: {total.coat()}")
print(f"Suit: {total.suit()}")
print(f"Total: {total.total}")






