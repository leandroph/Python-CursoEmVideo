def aumentar(valor=0, taxa=0, formato=False):
    '''
    -> Função para aumentar o preco de um produto informado
    :param valor: recebe um valor
    :param taxa: recebe o valor da taxa
    :param formato: valor opcional, que faz a formação em reais (R$)
    :return: retorna um valor já com o seu percetual de aumento
    '''
    aumento = valor + (valor * (taxa / 100))
    return aumento if formato is False else moeda(aumento)


def diminuir(valor=0, taxa=0, formato=False):
    '''
    -> Função para diminuir o preço de um produto informado
    :param valor: recebe um valor a ser calculado
    :param taxa: recebe o valor da taxa
    :param formato: valor opcional, que faz a formação em reais (R$)
    :return: retorna um valor ja com seu percetual de diminuição
    '''
    dim = valor - (valor * (taxa / 100))
    return dim if formato is False else moeda(dim)


def dobro(valor=0, formato=False):
    '''
    -> Função para calcular o dobro de número
    :param valor: recebe um valor a ser calculado
    :param formato: valor opcional, que faz a formação em reais (R$)
    :return: returna o dobro de um número formato ou não formado
    '''
    dobro = valor * 2
    return dobro if formato is False else moeda(dobro)


def metade(valor=0, formato=False):
    '''
    -> Função para calcular a metade de um número
    :param valor: recebe um valor a ser calculado
    :param formato: valor opcional, que faz a formação em reais (R$)
    :return: returna a metade de um número formato ou não formado
    '''
    metade = valor / 2
    return metade if formato is False else moeda(metade)


def moeda(valor=0, moeda='R$'):
    '''
    -> Função que realiza a formatação de um valor em reais (R$)
    :param valor: recebe um valor
    :param moeda: String formatada com o cifrão de reias (R$)
    :return: retorna uma string de um valor formatado para o valor de reias (R$)
    '''
    return f'{moeda} {valor:.2f}'.replace('.', ',')