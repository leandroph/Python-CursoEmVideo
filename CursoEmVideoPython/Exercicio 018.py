'''Faça um programa que leia um ângulo qualquer e mostre na tela o
valor do seno, cosseno e tangente desse ângulo.'''
import math
angulo = float(input("Digite o valor do angulo"))
anRad = math.radians(angulo)#tranforma o angulo para radianos

cos = math.cos(anRad)
sen = math.sin(anRad)
tan = math.tan(anRad)

print("O angulo de {} tem o SENO de {:.2f}".format(angulo, sen))
print("O angulo de {} tem o COSSENO de {:.2f}".format(angulo, cos))
print("O angulo de {} tem o TANGENTE de {:.2f}".format(angulo, tan))