'''
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

soma = 0
total = 0

for cont in range(1, 501, 2):
    if cont % 3 == 0:
        soma += cont
        total += 1
print("a soma de todos os {} valores solicitados é {}".format(total, soma))