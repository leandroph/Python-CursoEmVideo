'''
Crie um programa que leia uma frase qualquer e diga se ela
é um palíndromo, desconsiderando os espaços.
'''

frase = str(input("Escreva uma frase: ")).strip().upper()

palavras = frase.split()
junto = "".join(palavras)
inverso =""
print(junto)

for letra in range(len(junto)-1, -1 , -1):#vai inverter a palavra
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))

if inverso == junto:
    print("É um palindromo")
else:
    print("Não é um palindromo")