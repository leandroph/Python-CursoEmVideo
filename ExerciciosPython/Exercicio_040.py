'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Primeira nota: "))

media = (nota1 + nota2) / 2

print("Sua média foi {:.2f}".format(media))
if (media < 5):
    print("Você está REPROVADO")
elif (media < 6.9):
    print("Você está em RECUPERAÇÂO")
elif (media >= 7):
    print("Parabéns você está APROVADO")