'''Faça um programa que leia o sexo de uma pessoa, mas
só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto.'''

sexo = str(input("Informe o seu sexo [M/F]: ")).upper()
while sexo not in "MF":
    print("Dados Inválidos")
    sexo = str(input("Informe o seu sexo [M/F]: ")).upper()
print("Dado lido com sucessso")