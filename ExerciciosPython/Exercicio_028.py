'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre
0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint

sorteio = (randint(0,5))
print('O computador pensou em um número de 0 a 5\n'
      'tente adivinhar')

num = int(input('Qual seu palpite: '))

if num == sorteio:
    print('Parabéns você acertou')
else:
    print('OHHHH, você errou\n'
          'o computador pensou no número {}'.format(sorteio))