'''Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.'''

nome = str(input("Informe o nome")).strip()
print("Seu nome contem SILVA? {}".format("silva" in nome.lower()))