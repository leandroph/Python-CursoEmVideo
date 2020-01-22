'''
Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

listaNumeros = [[],[]]
valor = 0

for c in range(1,8):
    valor = int(input("Digite o valor: "))
    if valor % 2 == 0:
        listaNumeros[0].append(valor)
    else:
        listaNumeros[1].append(valor)

listaNumeros[0].sort()#ordena a lista de pares
listaNumeros[1].sort()#ordena a lista de ímpares
print(f'Os valores pares são: {listaNumeros[0]}')
print(f'Os valores ímpares são: {listaNumeros[1]}')