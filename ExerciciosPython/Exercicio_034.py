'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%.
'''

print("##### AUMENTO DE SALÁRIO #####")

salario = float(input('Informe o salário do funcionário: '))

if salario > 1250:
    aumento = salario + ((salario * 10)/100)
else:
    aumento = salario + ((salario * 15)/100)

print("Seu salário era R$:{} com o aumento passa a ser\n"
      "R$:{}".format(salario, aumento))
