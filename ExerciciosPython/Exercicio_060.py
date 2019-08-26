'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

#from math import factorial

print("Digite um número para")
num = int(input("Calcular o seu Fatorial: "))

#fatorial = factorial(num)
#print("O fatorial de {} é {}".format(num, fatorial))

c = num
fatorial = 1
print("Calculando {}! = ".format(num), end='')
while (c > 0):
    print('{}'.format(c), end='')
    print(" x " if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print("{}".format(fatorial))