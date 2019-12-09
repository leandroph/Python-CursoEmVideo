'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie
duas listas extras que vão contar apenas  os valores pares e os valores impares digitados, respectivamente. Ao
final mostre o conteúdo das três listas geradas.
'''

lista = []
listaPares = []
listaImpares = []

while True:
    n = int(input('Digite um valor : '))
    lista.append(n)

    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        listaPares.append(v)
    elif v % 2 == 1:
        listaImpares.append(v)

print(f'Os valores da lista sao {lista}')
print(f'Os valores da lista pares sao {listaPares}')
print(f'Os valores da lista impares sao {listaImpares}')