'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

valor = float(input("Qual o preço do produto: "))
print("Formas de pagamentos:")
print("[1] pagamento a vista dinheiro/cheque")
print("[2] pagamento a vista no cartão")
print("[3] pagamento em 2x no cartão")
print("[4] pagamento em 3x ou mais no cartão")
opcao = int(input("Qual a forma de pagamento: "))

if opcao == 1:
    desconto = valor - ((valor * 10)/100)
elif opcao == 2:
    desconto = valor - ((valor * 5)/100)
elif opcao == 3:
    desconto = valor
elif opcao == 4:
    desconto = valor + ((valor * 20)/100)
print("O valor do produto é de R$:{:.2f} com o desconto fica R$:{:.2f}".format(valor,desconto))