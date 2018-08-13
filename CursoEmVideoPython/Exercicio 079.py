'''Crie um programa onde o usuário possa digitar vários valores
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No
final, serão exibidos todos os valores únicos digitados, em ordem crescente'''

lista = []
while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Número já inserido na lista")
    resp = str(input("Deseja continuar [S/N]: "))
    if resp in "Nn":
        break

print(f"Lista em ordem crescente {sorted(lista)}")