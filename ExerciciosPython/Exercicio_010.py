'''Crie um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

print("##### COMPRA DE DÓLAR #####")

real = float(input("Informe quanto você tem em R$: "))

dolar = real / 3.82 #suponha-se que este seja o valor do dólar

print("Com R$: {:.2f} é possível comprar U$$: {:.2f}".format(real, dolar))