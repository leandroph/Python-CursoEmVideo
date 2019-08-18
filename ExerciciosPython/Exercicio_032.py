'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

from datetime import date
ano = int(input("Digite um ano qualquer (para pegar o ano atual digite 0): "))
if ano == 0:
    ano = date.today().year #pega o ano atual
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print("O {} ano é BISSEXTO".format(ano))
else:
    print("O {} ano não é BISSEXTO".format(ano))