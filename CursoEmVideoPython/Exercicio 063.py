'''Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. '''
print("------ SEQUÊNCIA DE FIBONACCI -----")
num = int(input("Informe o número de elementos que deseja: "))
cont = 2
n1 = 0
n2 = 1

print("Sequencia: ", end="")
print("{} {} ".format(n1, n2), end="")
while cont <= num:
    n3 = n1 + n2
    print("{} ".format(n3), end="")
    n1 = n2
    n2 = n3
    cont += 1
print("\nFIM")