class Arvore:
    '''
        >>> for no in Arvore(9, Arvore(-2, Arvore(-4), Arvore(-1)), Arvore(19)):
        ...     print(no)
        -4
        -1
        -2
        0
        10
    '''

    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


#           0
#      -2      -10
# -4        -1
