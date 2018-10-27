'''Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = dict()#cria um dicionário

aluno["nome"] = str(input("Nome aluno: "))
aluno["media"] = float(input(f'Média do {aluno["nome"]}: '))

if aluno["media"] < 5:
    aluno["situacao"] = "REPROVADO"
elif aluno["media"] < 7:
    aluno["situacao"] = 'RECUPERAÇÃO'
else:
    aluno["situacao"] = "APROVADO"

for k, v in aluno.items():
    print(f'{k} é igual {v}')