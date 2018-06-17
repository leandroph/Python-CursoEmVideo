'''Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores.'''

from datetime import date

anoAtual = date.today().year
contMaior = 0
contMenor = 0

for c in range(1,8):# pega as 7 pessoas
    anoNasc = int(input("Informe ano de nascimento da {} pessoa: ".format(c)))
    idade = anoAtual - anoNasc
    if idade < 21:
        contMenor += 1
    else:
        contMaior += 1
print("{} pessoas são maior de idade\n"
      "{} pessoas ainda não atingiram a maior idade".format(contMaior, contMenor))
