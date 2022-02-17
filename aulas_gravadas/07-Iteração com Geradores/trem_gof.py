class Trem:
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __iter__(self):
        return IteratorTrem(self.num_vagoes)


class IteratorTrem:
    def __init__(self, num_vagoes):
        self.atual = 0
        self.ultimo_vagao = num_vagoes - 1

    def __next__(self):
        if self.atual <= self.ultimo_vagao:
            self.atual += 1
            return f'Vagao {self.atual}'
        else:
            raise StopIteration()


if __name__ == '__main__':
    for vagao in Trem(4):
        print(vagao)
