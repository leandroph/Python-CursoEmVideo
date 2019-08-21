'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print("Suas opções:\n"
      "[ 0 ] PEDRA\n"
      "[ 1 ] PAPEL\n"
      "[ 2 ] TESOURA")
jogador = int(input("Qual a sua jogada? "))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print("-=" * 11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-=" * 11)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("jOGADA INVÁLIDA")
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("jOGADA INVÁLIDA")
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print("EMPATE")
    else:
        print("jOGADA INVÁLIDA")