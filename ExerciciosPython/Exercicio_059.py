'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
opcao = 0

while (opcao != 5):
    print("[ 1 ] somar\n"
          "[ 2 ] multiplicar\n"
          "[ 3 ] maior\n"
          "[ 4 ] novos números\n"
          "[ 5 ] sair do programa")
    opcao = int(input("Informe a operação que deseja realizar: "))

    if (opcao == 1):
        soma = num1 + num2
        print("A soma entre {} e {} é {}".format(num1, num2, soma))
    elif (opcao == 2):
        multi = num1 * num2
        print("A multiplicação entre {} e {} é {}".format(num1, num2, multi))
    elif (opcao == 3):
        if (num1 > num2):
            maior = num1
        else:
            maior = num2
        print("O maior número entre {} e {} é {}".format(num1, num2, maior))
    elif (opcao == 4):
        print('Digite novos valores:')
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif (opcao == 5):
        print("Finalizando")
    else:
        print("Opção inválida")
print("Fim do programa. Volte Sempre")