class Memifero:
    """vertabrados dotados de glândulas mamárias"""


class Cao(Memifero):
    qt_patas = 4
    carnivoro = True
    nervoso = False

    def __init__(self, nome):
        self.nome = nome

    def latir(self, vezes=1):
        # quando nervoso, late o dobro
        vezes = vezes + (self.nervoso * vezes)
        print(f'{self.nome}:' + ' Au!' * vezes)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Cão(%r)' % self.nome

    def __eq__(self, outro):
        return (isinstance(outro, Cao) and
                self.__dict__ == outro.__dict__)


cana = Cao('Cana')
cana.latir()
cana.nervoso = True
cana.latir()
