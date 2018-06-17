'''Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome "SANTO".'''

cidade = str(input("Cidade de seu nascimento")).strip()
print(cidade[:5].upper() == "SANTO")