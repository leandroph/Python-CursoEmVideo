'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cálculo do fatorial.
'''


def fatorial(num, show = False):
    """
    -> Função que retorna a fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: fat que é a fatorial do número informado
    """

    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat


print(fatorial(5, True))