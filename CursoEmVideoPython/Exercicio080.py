'''Crie um programa onde o usuário possa digitar cinco valores númericos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final,
mostre a lista ordenada na tela.'''

lista = []

for c in range(0,5):
    num = int(input("Digite um valor: "))
    #primeiro valor
    if c == 0:
        lista.append(num)
    elif num > lista[len(lista)-1]:#se o número for maior que o ultimo elemento da lista
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print(f"Os valores digitados foram {lista}")