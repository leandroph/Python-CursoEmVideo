'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

termo = int(input("Informe o primeiro termo da PA"))
razao = int(input("Informe a razao da PA"))

cont = 1
while cont <= 10:
    print("{}".format(termo), end = " ")
    termo += razao
    cont += 1