'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
while True:

    lista.append(int(input("Digite um valor: ")))

    resp = str(input("Deseja continuar [S/N]: "))
    if resp in "Nn":
        break

lista.sort(reverse=True)
print(f"Quantidade de números digitados {len(lista)}")
print(f"Lista em ordem decrescente {lista}")

if 5 in lista:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")