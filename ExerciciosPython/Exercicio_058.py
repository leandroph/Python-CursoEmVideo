'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint

sorteio = (randint(0,5))
print('O computador pensou em um número de 0 a 5\n'
      'tente adivinhar')

acertou = False
palpite = 0

while not acertou:
    num = int(input('Qual seu palpite: '))
    palpite += 1
    if (num == sorteio):
        acertou = True
    else:
        if (num < sorteio):
            print("Mais... Tente mais uma vez.")
        elif (num > sorteio):
            print("Menos... Tente mais uma vez.")

print("Acertou com {} palpites".format(palpite
                                       ))