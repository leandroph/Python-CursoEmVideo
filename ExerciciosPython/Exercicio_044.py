'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

preco = float(input("Informe o preço normal do produto: "))
print("FORMAS DE PAGAMENTO\n"
      "1 - À VISTA EM DINHEIRO/CHEQUE\n"
      "2 - À VISTA NO CARTÃO\n"
      "3 - 2x NO CARTÃO\n"
      "4 - 3x OU MAIS NO CARTÃO")
opcao = int(input("Digite a forma de pagamento (1, 2, 3, 4): "))

if (opcao == 1):
    novoPreco = preco - ((preco * 10) / 100)
    print("Pagamento em dinheiro/cheque tem 10% de desconto")
elif (opcao == 2):
    novoPreco = preco - ((preco * 5) / 100)
    print("Pagamento à vista no cartão tem 5% de desconto")
elif (opcao == 3):
    print("Pagamento em 2x no cartão não possui desconto")
elif (opcao == 4):
    novoPreco = preco + ((preco * 20) / 100)
    print("Pagamento em 3x ou mais no cartão possui 20% de juros")

if (opcao == 3):
    print("O seu produto custa R$ {}".format(preco))
else:
    print("seu produto custa R$ {:.2f} com o desconto fica R$ {:.2f}".format(preco, novoPreco))