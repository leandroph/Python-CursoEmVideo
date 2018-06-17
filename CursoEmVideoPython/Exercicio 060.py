'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

print("----- CÁLCULO FATORIAL -----")
num = int(input("Digite um número:"))
fatorial = 1
numfat = num

while numfat > 0:
    fatorial *= numfat
    numfat -= 1


print("O fatorial de {} é {}".format(num, fatorial))