from decorator import getfullargspec, decorator
from time import sleep, strftime


@decorator
def logar(f, fmt='%H:%M:%S', *args, **kwargs):
    print(strftime(fmt))
    return f(*args, **kwargs)


@logar  # Decorator com Parâmetros
def mochileiro():
    return 42


@logar(fmt='%d/%m/%y %H:%M:%S')  # Decorator com Parâmetros
def ola(nome):
    return f'Olá {nome}'


if __name__ == '__main__':
    print(getfullargspec(ola))
    print(mochileiro())
    print(mochileiro.__name__)  # Wraps
    print(ola('Mateus'))
    print(ola.__name__)  # Wraps
    sleep(1)
    print(mochileiro())
    print(ola('Rafael'))
