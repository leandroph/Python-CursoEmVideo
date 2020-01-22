'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais  pesadas
C) Uma listagem com as pessoas mais leves
'''

listaPessoas = list() #lista para armazenar todos os dados
listaPessoa = list() # lista para armazenar nome e peso de uma pessoa
maior = menor = 0

while True:
    listaPessoa.append(str(input("Nome: ")))
    listaPessoa.append(float(input("Peso: ")))

    if len(listaPessoas) == 0:
        maior = menor = listaPessoa[1]
    else:
        if listaPessoa[1] > maior:
            maior = listaPessoa[1]
        if listaPessoa[1] < menor:
            menor = listaPessoa[1]

    listaPessoas.append(listaPessoa[:])
    listaPessoa.clear()#limpa a lista de pessoa
    resp = str(input("Quer Continuar: [S/N]"))
    if resp in "Nn":
        break
print(f"Os dados foram {listaPessoas}")
print(f"Ao todo você cadastrou {len(listaPessoas)} pessoas")
print(f"O maior peso foi de {maior} KG. Peso de ", end='')
for pessoa in listaPessoas:
    if pessoa[1] == maior:
        print(pessoa[0], end='')

print(f"O menor peso foi de {menor} KG. Peso de", end='')
for pessoa in listaPessoas:
    if pessoa[1] == menor:
        print(pessoa[0], end='')
