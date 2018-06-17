'''Um professor quer sortear um dos seus quatro alunos para apagar o
quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo
na tela o nome do escolhido.'''
import random
n1 = str(input("Primeiro nome "))
n2 = str(input("Primeiro nome "))
n3 = str(input("Primeiro nome "))
n4 = str(input("Primeiro nome "))

nomes = [n1, n2, n3, n4]#coloca os nomes em uma lista
sorteio = random.choice(nomes)

print("O aluno sorteado foi {}".format(sorteio))