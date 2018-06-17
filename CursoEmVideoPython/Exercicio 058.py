'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.'''

from random import randint
print(10*"---")
print("Vou pensar em um numero de 0 a 10")
print(10*"---")
cont = 1
computador = randint(0,10)
num = int(input("Tente adivinhar qual o número o computador escolheu: "))

while (num != computador):
    if num < computador:
        print("Pensei em um valor maior")
    else:
        print("Pensei em um valor menor")
    num = int(input("Tente adivinhar qual o número o computador escolheu: "))
    cont += 1

print("PARABÉNS você acertou o número que escolhi")
print("Você levou {} tentativas para acertar".format(cont))
