from collections import namedtuple
from random import choice

Card = namedtuple("Card", ["rank", "suit"])


class Frenchdeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds hearts club".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = Frenchdeck()

print(len(deck))
print(deck[-1])
print(choice(deck))
