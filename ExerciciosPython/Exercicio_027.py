'''
Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.
'''

nome = str(input('Digite o seu nome: ')).strip().split()

print('Primeiro nome {}'.format(nome[0]))
print('Último nome {}'.format(nome[len(nome)-1]))