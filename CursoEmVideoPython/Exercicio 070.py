'''Crie um programa que leia o nome e o preço de vários produtos.
 programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
total = 0
totmil = 0
menor = 0
cont = 0
barato = " "
while True:
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço R$: "))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

print("------------------------------------------------")
print("--------------COMPRAS ENCERRADAS----------------")
print("Total da compra R$: {:.2f}".format(total))
print("{} produtos custam mais de R$ 1000,00".format(totmil))
print("O produto mais barato é uma {} custando R$: {:.2f}".format(nome, menor))
