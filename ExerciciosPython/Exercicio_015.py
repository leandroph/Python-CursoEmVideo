'''Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por Km rodado.'''

print("##### ALUGUEL DE CARROS #####")

km = float(input("Informe a KM percorrida com o carro: "))
dias = int(input("Informe quantos dias o carro foi alugado: "))

preco = (km * 0.15) + (dias * 60)

print("o preço do aluguel do carro é de R$:{}".format(preco))
