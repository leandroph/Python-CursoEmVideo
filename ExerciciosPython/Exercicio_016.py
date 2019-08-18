''''Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção Inteira.'''

from math import trunc

num = float(input("Digite um valor real: "))
#o método trunc() pega apenas a parte inteira do número flutuante.
print("A porção inteira de {:.2f} é {}".format(num, trunc(num)))