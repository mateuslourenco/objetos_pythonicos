from time import sleep, strftime


def logar(f):
    def executar_com_tempo(*args, **kwargs):
        print(strftime('%H:%M:%S'))
        return f(*args, **kwargs)

    return executar_com_tempo


@logar
def mochileiro():
    return 42


@logar
def ola(nome):
    return f'Olá {nome}'


if __name__ == '__main__':
    print(mochileiro())
    print(ola('Mateus'))
    sleep(1)
    print(mochileiro())
    print(ola('Rafael'))
