'''Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.'''

print("##### AUMENTO DE SALÁRIO #####")

salario = float(input("Qual o salário do funcionario R$: "))

novoSalario = salario + ((salario * 15) / 100)
print("Um funcionário que ganhava R${:.2f} com 15% de aumento "
      "Passa a receber um salário de R$: {:.2f}" .format(salario, novoSalario))
