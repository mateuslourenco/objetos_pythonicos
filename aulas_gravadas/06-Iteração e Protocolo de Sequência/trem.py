class Trem:
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __len__(self):
        return self.num_vagoes

    def __getitem__(self, pos):
        indice = pos if pos >= 0 else self.num_vagoes + pos
        if 0 <= indice < self.num_vagoes:
            # indice 2 -> vagao #3
            return f'vagao #{indice + 1}'
        raise IndexError(f'Vagao inexistente {pos}')


if __name__ == '__main__':
    for vagao in Trem(4):
        print(vagao)
