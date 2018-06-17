'''Crie um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

print("##### COMPRA DE DÓLAR #####")

real = float(input("Informe quanto você tem em reais R$: "))
dolar = real / 3.27 #digamos que este seja o valor do dolar

print("Com R$ {} você compra U$$ {}" .format(real, dolar))