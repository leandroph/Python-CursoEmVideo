'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

km = float(input("Digite a velocidade atual do carro: "))

if (km > 80):
    print("Você ultrapassou o limite de velocidade")
    multa = (km - 80) * 7
    print("Você estava a uma velocidade de {} km/h\n"
          "Deverá pagar multa de R$: {}".format(km, multa))
else:
    print("Você esta no limite de velocidade permitido de 80 km/h\n"
          "sua velocidade foi de {}".format(km))