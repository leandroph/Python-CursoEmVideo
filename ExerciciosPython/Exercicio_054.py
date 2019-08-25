'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date

anoAtual = date.today().year
totMaior = 0
totMenor = 0

for cont in range(1, 8):
    anoNascimento = int(input("Em que ano a {} pessoa nasceu: ".format(cont)))
    idade = anoAtual - anoNascimento

    if (idade >= 21):
        totMaior += 1
    else:
        totMenor += 1

print("Ao total tivemos {} pessoas maiores de idade".format(totMaior))
print("E também tivemos {} pessoas menores de idade".format(totMenor))