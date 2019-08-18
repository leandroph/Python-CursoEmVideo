'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = float(input('informe a velocidade do veículo: '))

if velocidade > 80:
    print('Você está acima da velocidade permitida '
          'será multado')
    multa = (velocidade - 80) * 7
    print('Valor da multa R$: {:.2f}'.format(multa))