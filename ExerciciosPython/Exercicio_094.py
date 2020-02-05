'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média.
'''

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Deseja continuar: [S/N]')).upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break

#exibindo os  dados
print(f'Ao total temos {len(galera)} pessoas cadastradas')

media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')

print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in'Ff':
        print(f'{p["nome"]}', end='')
print()

print('Lista das pessoas que estão acima da média')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()