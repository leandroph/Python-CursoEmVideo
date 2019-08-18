'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte
o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder
30% do salário ou então o empréstimo será negado.
'''

print('##### EMPRÉSTIMO BANCÁRIO #####')

casa = float(input("Digite o valor do Empréstimo: "))
salario = float(input("Informe seu  salário: "))
anos = int(input("Em quantos anos deseja pagar"))

prestacao = casa / (anos * 12)
minino = (salario * 30) / 100

print("O valor da parcela será de R$:{:.2f} ".format(prestacao))

if prestacao < minino:
    print("Emprestimo APROVADO")
else:
    print("Empréstimo RECUSADO")