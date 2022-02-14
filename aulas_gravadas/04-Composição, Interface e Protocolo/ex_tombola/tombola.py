from random import shuffle


class Tombola:
    def __init__(self):
        self.itens = []

    def carregar(self, lista):
        self.itens = lista

    def carregada(self):
        return bool(self.itens)

    def misturar(self, embaralhador=shuffle):
        embaralhador(self.itens)

    def sortear(self):
        return self.itens.pop()
