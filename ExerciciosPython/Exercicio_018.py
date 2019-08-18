'''Faça um programa que leia um ângulo qualquer e mostre na tela o
valor do seno, cosseno e tangente desse ângulo.'''
from math import radians, sin, cos, tan

angulo = float(input("Informe um ângulo: "))

seno = sin(radians(angulo))
print("O seno do ângulo {} é {:.2f}".format(angulo, seno))

cosseno = cos(radians(angulo))
print("O cosseno do ângulo {} é {:.2f}".format(angulo, cosseno))

tangente = tan(radians(angulo))
print("A tangente do ângulo {} é {:.2f}".format(angulo, tangente))