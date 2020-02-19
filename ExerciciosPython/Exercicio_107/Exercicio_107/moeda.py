def aumentar(valor, taxa):
    aumento = valor + (valor * (taxa / 100))
    return aumento


def diminuir(valor, taxa):
    dim = valor - (valor * (taxa / 100))
    return dim


def dobro(valor):
    dobro = valor * 2
    return dobro


def metade(valor):
    metade = valor / 2
    return metade