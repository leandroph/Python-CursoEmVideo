'''Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
número escolhido pelo computador. O programa deverá escrever na tela se
o usuário venceu ou perdeu.'''
from random import randint
print(10*"---")
print("Vou pensar em um numero de 0 a 5")
print(10*"---")
computador = randint(0,5)
num = int(input("Tente adivinhar qual o número o computador escolheu: "))

if (num == computador):
    print("PARABÉNS você acertou o número escolhido foi {}".format(computador))
else:
    print("Você errou o número escolhido foi {}".format(computador))