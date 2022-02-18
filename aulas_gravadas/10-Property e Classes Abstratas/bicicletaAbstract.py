import abc


class Bicicleta(abc.ABC):
    _marca = 'Caloi'

    def __init__(self):
        self._velocidade = 0

    @classmethod
    def marca(cls):
        return cls._marca

    @staticmethod
    def rodas():
        return 2

    @property
    def velocidade(self):
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        if valor >= 0:
            self._velocidade = valor
        else:
            self._velocidade = 0

    @abc.abstractmethod
    def pedalar(self):
        """Cada classe concreta deve definir o método pedalar com seu incremento na velocidade"""

    @abc.abstractmethod
    def frear(self):
        """Cada classe concreta deve definir o método frear com seu decremento na velocidade"""


class Monark(Bicicleta):
    _marca = 'Monark'

    def pedalar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 3


if __name__ == '__main__':
    bicicleta = Monark()
    bicicleta.pedalar()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.frear()
    print(bicicleta.velocidade)
    print(Bicicleta.marca())
    print(bicicleta.rodas())
    print(Monark.marca())
