'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []

while True:
    n = int(input('Digite um valor : '))
    lista.append(n)

    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

print(f'Ao total foram digitados {len(lista)} numeros')
print(f'Os valores da lista sao {lista}')

lista.sort(reverse=True)
print(f'Os valores da lista em ordem decrescente sao {lista}')

if 5 in lista:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 nao esta na lista')