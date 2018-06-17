'''Faça um programa que jogue par ou ímpar com o computador. O jogo só
será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo. '''
from random import randint

print("VAMOS JOGAR PAR OU ÍMPAR")
cont = 0
while True:
    computador = randint(1,11)
    jogador = int(input("Diga um valor"))
    total = computador + jogador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("PAR OU IMPAR? [P/I]")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}")

    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU")
            cont += 1
        else:
            print("Você PERDEU")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU")
            cont += 1
        else:
            print("Você PERDEU")
            break
print(f"Você venceu {cont} vezes")