'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''


def voto(ano):
    from datetime import datetime

    idade = datetime.today().year - ano

    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA, VOTO NEGADO'
    elif 16 >= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    #elif 18 >= idade <= 65:
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'



anoNascimento = int(input('Em que ano você nasceu: '))
print(voto(anoNascimento))