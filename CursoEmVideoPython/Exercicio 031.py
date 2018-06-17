'''Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

km = float(input("Qual a distância da sua viagem em Km: "))

if(km <= 200):
    preco = km * 0.50
    print("O valor da passagem para uma de {} Km é R$: {}".format(km, preco))
else:
    preco = km * 0.45
    print("O valor da passagem para uma de {} Km é R$: {}".format(km, preco))