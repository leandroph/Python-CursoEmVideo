'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
nasc = int(input("Ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - nasc

if(idade == 18):
    print("Você tem que se alistar IMEDIATAMENTE")
elif(idade < 18):
    saldo = 18 - idade
    print("Ainda faltam {} anos para você se alistar".format(saldo))
    ano = anoAtual + saldo
    print("Seu alistamento será no ano de {}".format(ano))
elif(idade > 18):
    saldo = idade - 18
    print("Você já devia ter se alistado à {} anos".format(saldo))
    ano = anoAtual - saldo
    print("Você devia ter se alistado no ano de {}".format(ano))