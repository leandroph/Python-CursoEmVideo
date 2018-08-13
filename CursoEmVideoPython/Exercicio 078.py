'''Faça um programa que leia 5 valores númericos e guarde-os em
uma lista. No final, mostre qual foi o maior valor e o menor valor digitado e as
suas respectivas posições na lista.'''

lista = []
for c in range(0,5):
    lista.append(int(input("digite o {} valor: ".format(c + 1))))

    if c == 0:
        maior = lista[c]
        menor = lista[c]
        posicao1 = posicao2 = c
    if lista[c] > maior:
        maior = lista[c]
        posicao1 = c
    if lista[c] < menor:
        menor = lista[c]
        posicao2 = c

print("Lista completa {}".format(lista))
print(f"Maior valor da lista {maior} e está na posição {posicao1}")
print(f"Menor valor da lista {menor} e está na posição {posicao2}")


