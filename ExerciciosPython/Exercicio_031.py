'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

print("##### ALUGUEL DE CARROS #####")

km = float(input('Informe a kilometragem percorrida: '))

if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45

print("Você rodou {} km valor toral R$: {}".format(km, valor))