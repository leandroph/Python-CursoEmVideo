'''
Faça um programa que leia 5 valores númericos e guarde-os em
uma lista. No final, mostre qual foi o maior valor e o menor valor digitado e as
suas respectivas posições na lista.
'''

listanum = [] #cria a lista para armazenar os numeros
maior = menor = 0

for c in range(0,5):
    #adicionando os numeros a lista
    listanum.append(int(input(f'Digite um valor para a posicao {c}: ')))

    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print('=-'*30)
print(f'Voce digitou os valores {listanum}')

print(f'O maior valor digitado foi {maior} nas posicoes', end="")
for indice, valor in enumerate(listanum):
    if valor == maior:
        print(f'{indice}...', end="")

print(f'O maior valor digitado foi {menor}', end="")
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f'{indice}...', end="")