'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.'''
resposta = "N"
total, cont = 0
while resposta != "N":
    num = int("Digite um número: ")
    total += num
    cont += 1

    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input("Deseja continuar [S/N]")).upper()

media = total / cont
print("Você informou {} números e a média entre eles é {} ".format(cont, media))
print("O maior número informado foi {}".format(maior))
print("O menor número informado foi {}".format(menor))