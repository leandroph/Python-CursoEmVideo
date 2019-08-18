'''Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto.'''

preco = float(input("Informe o preço do produto R$: "))
novo = preco - ((preco * 5) / 100)

print("O produto custa R$ {} com 5% de desconto \n"
      "O valor fica R$ {:.2f}" .format(novo))