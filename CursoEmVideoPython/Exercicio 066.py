'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é
a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre elas (desconsiderando o flag).'''

num = 0
total = 0
cont = 0
while num != 999:
    num = int(input("Qual o  valor: "))
    if num == 999:
        break
    total += num
    cont += 1

print("Você informou {} e a  soma dos valores é {}".format(cont, total))