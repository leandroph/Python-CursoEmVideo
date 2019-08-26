'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
resolvendo o exercício com laço for
'''

print("Digite um número para")
num = int(input("Calcular o seu Fatorial: "))

c = num
fatorial = 1
print("Calculando {}! = ".format(num), end='')
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(" x " if c > 1 else ' = ', end='')
    fatorial *= c

print("{}".format(fatorial))