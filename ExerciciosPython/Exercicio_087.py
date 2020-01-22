'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares = somaColuna = mqior = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}][{coluna}]"))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{matriz[linha][coluna]:^5}', end='')
    print()

#soma dos valores pares da matriz
for linha in range(0,3):
    for coluna in range(0,3):
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]

#A soma dos valores da terceira coluna.
for linha in range(0,3):
    somaColuna += matriz[linha][2]

for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print(f'A soma dos valores pares da matriz é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaColuna}.')
print(f'O maior valor da segunda linha é {maior}.')