'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print("Suas opções:")
print("[0] Pedra\n[1] Papel\n[2] Tesoura")
jogador = int(input("Qual a sua escolha: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
print(20*"=")
print("O computador jogou {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
print(20*"=")

if computador == 0: #computador jogou PEDRA
    if jogador == 0:#jogador jogou PEDRA
        print("EMPATE")
    elif jogador == 1: #jogador jogou PAPEL
        print("JOGADOR VENCE")
    elif jogador == 2:#jogador jogou TESOURA
        print("COMPUTADOR VENCE")
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:#jogador jogou PEDRA
        print("COMPUTADOR VENCE ")
    elif jogador == 1: #jogador jogou PAPEL
        print("EMPATE")
    elif jogador == 2:#jogador jogou TESOURA
        print("JOGADOR VENCE")
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:#jogador jogou PEDRA
        print("JOGADOR VENCE")
    elif jogador == 1: #jogador jogou PAPEL
        print("COMPUTADOR VENCE")
    elif jogador == 2:#jogador jogou TESOURA
        print("EMPATE")