'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
'''

nome = str(input('Digite seu nome: '))

print(nome.lower())#deixa a string em letra minuscula
print(nome.upper())#deixa a string com letra maiuscula

#pega o tamanho da string e subtrai pelo total de espaços que a string contem
totalCaracteres = len(nome) - nome.count(" ")

print("Seu nome tem um total de {} caracteres".format(totalCaracteres))