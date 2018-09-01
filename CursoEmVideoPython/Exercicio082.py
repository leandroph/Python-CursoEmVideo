''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar apenas  os valores pares e os valores
impares digitados, respectivamente. Ao final mostre o conteúdo das três listas geradas.'''

lista = []
listapares = []
listaimpares = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)

    if num % 2 == 0:
        listapares.append(num)
    else:
        listaimpares.append(num)

    resp = str(input("Deseja continuar [S/N]: "))
    if resp in "Nn":
        break

print("Lista original {}".format(lista))
print("Lista com números pares{}".format(listapares))
print("Lista com números ímpares {}".format(listaimpares))
