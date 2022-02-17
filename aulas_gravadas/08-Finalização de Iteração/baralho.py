from collections import namedtuple

Carta = namedtuple('Carta', 'valor naipe')


class Baralho:
    valores = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    naipes = '♣ ♦ ♥ ♠'.split()

    def __init__(self):
        self.cartas = [Carta(v, n) for n in self.naipes for v in self.valores]

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, pos):
        return self.cartas[pos]


if __name__ == '__main__':
    baralho = Baralho()

    for carta in baralho:
        print(carta)
