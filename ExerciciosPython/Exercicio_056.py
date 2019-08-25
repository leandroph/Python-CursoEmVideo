'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do
programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.
'''

somaIdade = 0
cont = 0
maioridade = 0
nomeVelho = ""
for pessoa in range(1,5):
    nome = str(input("Nome da {}° pessoa".format(pessoa))).upper()
    idade = int(input("Idade da {}° pessoa".format(pessoa)))
    sexo = str(input("Sexo: M - masculino e F - feminino")).upper()

    somaIdade += idade
    media = somaIdade / 4

    if sexo == "M" and pessoa == 1:
        maioridade = idade
        nomeVelho = nome

    if sexo == "M" and idade > maioridade:
        maioridade = idade
        nomeVelho = nome

    if sexo == "F" and idade < 20:
        cont += 1

print("A media de idade do grupo é {}".format(media))
print("O homem mais velho tem {} anos e seu nome é {}".format(maioridade, nomeVelho))
print("A quantidade de mulheres com menos de 20 anos é {}".format(cont))