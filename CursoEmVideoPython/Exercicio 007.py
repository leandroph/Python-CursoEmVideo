'''Desenvolva um programa que leia as
duas notas de um aluno, calcule e mostre a sua média.'''

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2
print("A média do aluno foi de {:.2f}".format(media))