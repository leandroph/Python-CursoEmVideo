'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo. '''
print("TABUADA")

while True:
    num = int(input("Digite a taduada desejada: "))
    if num < 0:
        break
    for cont in range(1,11):
        print("{} x {} = {}".format(cont, num, cont*num))