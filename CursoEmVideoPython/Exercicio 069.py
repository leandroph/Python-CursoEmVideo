'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

contIdade, contH, contM =0

while True:
    idade = int(input("Informe a idade:"))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]")).strip().upper()[0]

    if idade >  18:
        contIdade += 1
    if sexo == "M":
        contH += 1
    if sexo == "F" and idade < 20:
        contM += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

print("Pessoas maiores de 18 anos {}".format(contIdade))
print("Total de Homens cadastrados {}".format(contH))
print("Total de mulheres com menos de 20 anos {}".format(contM))
print("ACABOU")