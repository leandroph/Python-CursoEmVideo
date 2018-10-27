'''Crie um programa onde 4 jogadores jogem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6),
}

print("Valores Sorteados")
for k, v in jogo.items():
    print(f'O jogador {k} tirou {v}')
    sleep(1)

ranking = list()#vai ser considerado uma lista e tratado como uma
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("RANKING DE VITÓRIA")

for i,v in enumerate(ranking):
    print(f' {i+1} lugar : {v[0]} com {v[1]}')