from functools import wraps
from time import sleep, strftime


def logar(fn=None, *, fmt='%H:%M:%S'):  # Decorator com Parâmetro Opcional
    if fn is not None:
        return logar(fmt=fmt)(fn)

    def decorator(f):  # Decorator com Parâmetros
        @wraps(f)  # Wraps
        def executar_com_tempo(*args, **kwargs):
            print(strftime(fmt))  # Decorator com Parâmetros
            return f(*args, **kwargs)

        return executar_com_tempo
    return decorator


@logar  # Decorator com Parâmetros
def mochileiro():
    return 42


@logar(fmt='%d/%m/%y %H:%M:%S')  # Decorator com Parâmetros
def ola(nome):
    return f'Olá {nome}'


if __name__ == '__main__':
    print(mochileiro())
    print(mochileiro.__name__)  # Wraps
    print(ola('Mateus'))
    print(ola.__name__)  # Wraps
    sleep(1)
    print(mochileiro())
    print(ola('Rafael'))
