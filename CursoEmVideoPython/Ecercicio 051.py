'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

termo = int(input("Informe o primeiro termo da PA"))
razao = int(input("Informe a razao da PA"))

decimoTermo = (termo + (10 - 1) * razao) + razao

for c in range(termo,decimoTermo,razao):
    print("{}".format(c), end = " ")