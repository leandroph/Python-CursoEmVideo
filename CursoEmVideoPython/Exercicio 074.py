'''Crie um programa que vai gerar cinco números
aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão
na tupla.'''

from random import randint

tupla = ((randint(1,10)), (randint(1,10)), (randint(1,10)),
         (randint(1, 10)), (randint(1,10)))

for num in tupla:
  print(num, end=' ')

print("\no maior número da tupla é {}".format(max(tupla)))#pega o maior numero
print("o menor número da tupla é {}".format(min(tupla))) #pega o menor numero