'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag).'''

num = 0
total = 0
cont = 0
while num != 999:
    num = int(input("Qual o  valor: "))
    total += num
    cont += 1
    if num == 999:
        total -= 999
        cont -= 1
print("Você informou {} e a  soma dos valores é {}".format(cont, total))