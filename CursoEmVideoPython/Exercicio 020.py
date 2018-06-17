'''O mesmo professor do desafio 019 quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada.'''

import random
n1 = str(input("Primeiro nome "))
n2 = str(input("Primeiro nome "))
n3 = str(input("Primeiro nome "))
n4 = str(input("Primeiro nome "))

nomes = [n1, n2, n3, n4]#coloca os nomes em uma lista
ordem = random.sample(nomes, k=4)

print("A ordem sorteada para a ordem da apresentação foi")
print(ordem)