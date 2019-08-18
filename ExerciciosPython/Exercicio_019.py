'''Um professor quer sortear um dos seus quatro alunos para apagar o
quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo
na tela o nome do escolhido.'''

import random

nome1 = str(input("Primeiro aluno: "))
nome2 = str(input("Segundo aluno: "))
nome3 = str(input("Terceiro aluno: "))
nome4 = str(input("Quarto aluno: "))

alunos = [nome1, nome2, nome3, nome4]

sorteio = random.choice(alunos)
print("O aluno sorteado foi {}".format(sorteio))