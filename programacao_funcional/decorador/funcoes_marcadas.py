from programacao_funcional.decorador.registrador import get_marcadas, marcar


def primeira():
    pass


primeira = marcar(primeira)


# Açúcar sintático do python
@marcar  # Decorator
def segunda():
    pass


if __name__ == '__main__':
    for f in (get_marcadas()):
        print(f.__name__)
    primeira()
    segunda()
