def fabrica_de_multiplicadores(multiplicador):
    def multiplicar(n):
        return n * multiplicador

    return multiplicar


def fabrica_de_multiplicadores_e_divisores(multiplicador, divisor):
    def multiplicar_dividir(n):
        return n * multiplicador / divisor

    return multiplicar_dividir


dobro = fabrica_de_multiplicadores(2)
triplo = fabrica_de_multiplicadores(3)
print(dobro(3))
print(triplo(4))

teste = fabrica_de_multiplicadores_e_divisores(10, 5)
print(teste(1))
