'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
aposentar. (35 anos de contribuição para se aposentar)'''

from datetime import datetime
dados = dict()

dados['nome'] = str(input('Informe o seu nome: '))
nasc = int(input('Informe o ano de nascimento: '))
anoAtual = datetime.now().year
dados['idade'] =  anoAtual - nasc
dados['CTPS'] = int(input("N° Carteira de Trabalho (0 não possui CTPS): "))

if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário R$: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - anoAtual)

print('='*30)
for k, v in dados.items():
    print(f' {k} tem o valor {v}')