from random import shuffle


class Tombola:
    def __init__(self):
        self.itens = []

    def carregar(self, lista):
        # Bug sutil. Ao atribuir a lista para self.itens, ambos passam a referenciar o mesmo objeto "lista"
        # self.itens = lista

        self.itens.extend(lista)  # Deste modo, self.itens não referencia para o mesmo objeto "lista"
        # Há outras opções ex: itens.copy() e etc...

    def carregada(self):
        return bool(self.itens)

    def misturar(self):
        shuffle(self.itens)

    def sortear(self):
        return self.itens.pop()
