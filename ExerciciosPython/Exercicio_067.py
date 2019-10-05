'''
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
'''

while True:
    print('Informe um numero negativo para sair')
    num = int(input('Qual a tabuada desejada:'))
    if num < 0:
        break
    print('-'*30)
    for c in range(1,11):
        print(f'{c} x {num} = {c * num}')
    print('-' * 30)

    print('Programa Tabuada Encerrado')