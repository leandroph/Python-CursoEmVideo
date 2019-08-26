'''
Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
'''

print("SEQUÊNCIA DE FIBONACCI")
print("-----------------------")

num = int(input("Quantos termos deseja mostrar: "))

penultimo = 0
ultimo = 1

print("{} - {}".format(penultimo, ultimo),end='')
cont = 3
while cont <= num:
    novo = penultimo + ultimo
    print(" - {}".format(novo),end='')
    penultimo = ultimo
    ultimo = novo
    cont += 1
print(" - FIM")