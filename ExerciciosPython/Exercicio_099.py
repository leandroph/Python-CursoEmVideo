'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''


def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados: ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print()


#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()