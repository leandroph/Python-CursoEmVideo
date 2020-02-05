'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
aposentar. (35 anos de contribuição para se aposentar)
'''

from datetime import datetime
dados =dict()

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem)'))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) -  datetime.now().year)

print('-='*30)

for key, valor in dados.items():
    print(f' - {key} tem o valor {valor}')