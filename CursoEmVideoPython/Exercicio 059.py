'''Exercício Python 059: Crie um programa que leia dois
valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo  valor: "))
escolha = 0
while escolha != 5:
    print("[1] somar\n"
          "[2] multiplicar\n"
          "[3] maior\n"
          "[4] novos números\n"
          "[5] sair do programa")
    escolha = int(input("Informe sua escolha:"))

    if escolha == 1:
        print("{} + {} = {}".format(num1, num2,num1 + num2))
    elif escolha == 2:
        print("{} + {} = {}".format(num1, num2, num1 * num2))
    elif escolha == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print("O maior número é {}".format(maior))
    elif escolha == 4:
        print("Trocar os valores informados")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo  valor: "))
    elif escolha == 5:
        print("Finalizando programa")
    else:
        print("Escolha inválida")