'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao total (sem considerar espaços).'''

nome = str(input("Informe seu nome: ")).strip()#separa as palavras da string
print("Nome com letras Maiusculas: {}".format(nome.upper()))
print("Nome com letras Minusculas: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))#o nome com  os espaços menos os espaços
#assim se tem o total de letras do nome sem os espaços

