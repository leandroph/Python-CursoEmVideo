'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date


anoNascimento = int(input("Informe seu ano de nascimento: "))
#pegando o ano atual do sistema
anoAtual = date.today().year

idade = anoAtual - anoNascimento

if (idade < 18):
    print("Quem nasceu em {} tem {} em {}".format(anoNascimento, idade, anoAtual))
    print("Ainda faltam {} anos para o alistamento\n"
          "Seu alistamento será em {}".format(18 - idade, anoNascimento + 18))
elif (idade > 18):
    print("Quem nasceu em {} tem {} em {}".format(anoNascimento, idade, anoAtual))
    print("Você já deveria ter se alistado há {} anos\n"
          "Seu alistamento foi em {}".format(idade - 18, anoNascimento + 18))
elif (idade == 18):
    print("Quem nasceu em {} tem {} anos em {}".format(anoNascimento, idade, anoAtual))
    print("Você tem que se alistar IMEDIATAMENTE")