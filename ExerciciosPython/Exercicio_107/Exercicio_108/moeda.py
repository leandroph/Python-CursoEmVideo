def aumentar(valor=0, taxa=0):
    aumento = valor + (valor * (taxa / 100))
    return aumento


def diminuir(valor=0, taxa=0):
    dim = valor - (valor * (taxa / 100))
    return dim


def dobro(valor=0):
    dobro = valor * 2
    return dobro


def metade(valor=0):
    metade = valor / 2
    return metade


def moeda(valor=0, moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')