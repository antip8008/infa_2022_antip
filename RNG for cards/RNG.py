import random


class Deck:
    N = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
    S = ['S', 'C', 'D', 'H']

    def __init__(self):
        self.__cards = []

    def shuffle(self):
        for n in self.__class__.N:
            for s in self.__class__.S:
                self.__cards.append(f'{n}{s}')
        random.shuffle(self.__cards)

    @property
    def next(self):
        if len(self):
            return self.__cards.pop()

    def nexts(self, n):
        res = []
        for i in range(0, n):
            res.append(self.next)
        return res

    def __len__(self):
        return len(self.__cards)


class Holdem(Deck):

    def flop(self):
        return self.nexts(3)

    def turn(self):
        return self.next

    def river(self):
        return self.next

d = Holdem()
d.shuffle()

print('p1', d.nexts(2))
print('p2', d.nexts(2))
print('flop', d.flop())
print('turn', d.turn())
print('river', d.river())

