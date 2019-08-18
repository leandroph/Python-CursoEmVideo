'''Faça um programa que leia o nome de uma
pessoa e mostre uma mensagem de boas-vindas.'''

nome = input("Digite o seu nome: ")
#possui três format para poder imprimir a cor do nome
print("Seja bem vindo ao Curso de Python\n{}{}".format('\033[31m', nome))